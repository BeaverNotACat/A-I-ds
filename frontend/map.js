import Map from 'ol/Map.js';
import View from 'ol/View.js';
import OSM from 'ol/source/OSM.js';
import TileLayer from 'ol/layer/Tile.js';

import { useGeographic } from 'ol/proj';

import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import GeoJSON from 'ol/format/GeoJSON';

import Icon from 'ol/style/Icon.js';
import {Circle, Fill, Text, Stroke, Style} from 'ol/style.js';


import getGeojson from './createGeojson';

useGeographic();


const stroke = new Stroke({
  color: 'rgba(0, 0, 0, 0.6)',
  width: 3,
});


const styleFunction = function(feature) {
  return new Style({
    stroke: stroke,
    text: new Text({
      text: feature.get('name')
    })
  })
};


function getLayer(){
  const data = new GeoJSON().readFeatures(getGeojson());
  const vectorSource = new VectorSource({
    features: data
  });


  return new VectorLayer({
    source: vectorSource,
    style: styleFunction,
  });
}




const map = new Map({
  layers: [
    new TileLayer({
      source: new OSM(),
    }),
    getLayer()
  ],
  target: 'map',
  view: new View({
    center: [37.619899588604255, 55.75221649261525], //координаты перевёрнуты
    zoom: 8,
    showFullExtent: true,
  }),
});

alert(getCookie("key"));