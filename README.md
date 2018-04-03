# Real-Time-Twitter-Stream
Stream live tweets across the world in real time on a world map.

This web app attaches to the [Twitter Streaming API ](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data) and extracts tweets with geo data using an open source python library 
[Tweepy](http://docs.tweepy.org/en/v3.5.0/getting_started.html#introduction) that act as a communicator to Twitter API.

## Installing and running
* Install [Flask](http://flask.pocoo.org/) a server side framework for Python.
```
pip install flask
```

* Clone the repo 
```
https://github.com/7saheelahmed/Real-Time-Twitter-Stream.git   
```

* Create a Twitter App account  on [Twitter Developer Platform](https://developer.twitter.com/) and use access tokens for api request authentication.

* Install [Tweepy](http://docs.tweepy.org/en/v3.5.0/getting_started.html#introduction)
```
pip install tweepy
```

* Go to your flask folder open scripts and run activate on terminal to start the server.
```
>>>cd flask\Scripts
>>>activate
```

* Now go to repository and run app.py on terminal to start the application
```
>>>cd Real-Time-Twitter-Stream
>>>python app.py
```

* Go to your [http://localhost:5000](http://localhost:8080) And that's it !!

## This is how it works >>>
![Backend](https://github.com/7saheelahmed/Real-Time-Twitter-Stream/blob/master/Results/Work.png)

## Results 
![App Results 1](https://github.com/7saheelahmed/Real-Time-Twitter-Stream/blob/master/Results/Tweets.png)
![App Results 2](https://github.com/7saheelahmed/Real-Time-Twitter-Stream/blob/master/Results/Tweets1.png)
![App Results 3](https://github.com/7saheelahmed/Real-Time-Twitter-Stream/blob/master/Results/Tweets3.png)

## Resources 
* [Flask](http://flask.pocoo.org/)
* [Twitter Streaming API](https://developer.twitter.com/en/docs/tutorials/consuming-streaming-data)
* [Tweepy](http://docs.tweepy.org/en/v3.5.0/)
* [Leaflet Js](http://leafletjs.com/)
* [AJAX/Jquery](https://jquery.com/)


