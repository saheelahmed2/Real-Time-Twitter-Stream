function getData(){

  $.ajax({
    type:'GET',
    url:'/data',
    success: function(data){
              L.geoJson(data).addTo(map);
              function onEachFeature(feature, layer) {
              // does this feature have a property named popupContent?
              if (feature.text) {
              layer.bindPopup(feature.text);
                }
              }
              // L.geoJson(geojsonFeature, {
              // onEachFeature: onEachFeature
              // }).addTo(map);
          }
        });
}

(function(){
  var counter = setInterval(getData, 10000);
})();