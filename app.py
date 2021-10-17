from flask import Flask
from flask import render_template, jsonify
from info import data
from stream_code import main
import threading


class Thread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        main()


# create application
app = Flask(__name__)
prev_list = list()


@app.route('/')
def index():
    t = Thread()
    t.start()
    return render_template('index.html')


@app.route('/data')
def stream_data():
    '''
    GeoJSON Format
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [125.6, 10.1]
      },
      "properties": {
        "name": "Dinagat Islands"
      }
    }
    '''
    geo_data = []
    for item in data:
        geo_item = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": item['coordinates']['coordinates']
            },
            "properties": {
                "name": item["text"]
            },

        }
        geo_data.append(geo_item)
    
    global prev_list
    if prev_list == []:
        prev_list = geo_data[:]
        return jsonify(geo_data)
    else:
        d = []
        for item in geo_data:
            if item not in prev_list:
                d.append(item)
        prev_list = geo_data[:]
        return jsonify(d)

if __name__ == "__main__":
    app.run(debug=True, threaded=True, host="0.0.0.0")
