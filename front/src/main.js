import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

//Vue material
import VueMaterial from 'vue-material';
import 'vue-material/dist/vue-material.css';
import VueRouter from 'vue-router';
import axios from 'axios';
import VueAxios from 'vue-axios';
import routes from './routes';
import VueMoment from 'vue-moment';
import moment from 'moment-timezone';
/*import VueLayers from 'vuelayers'
import { TileLayer, WmtsSource, WmsSource, OsmSource, PointGeom, StyleBox } from 'vuelayers';
import 'vuelayers/lib/style.css' // needs css-loader*/
import proj4 from 'proj4';
import {register} from 'ol/proj/proj4';

proj4.defs('EPSG:2056',
  '+proj=somerc +lat_0=46.95240555555556 +lon_0=7.439583333333333'
  + ' +k_0=1 +x_0=2600000 +y_0=1200000 +ellps=bessel '
  + '+towgs84=674.374,15.056,405.346,0,0,0,0 +units=m +no_defs');
register(proj4)

Vue.config.productionTip = false;

Vue.use(VueMaterial)
Vue.use(VueRouter)
Vue.use(VueAxios, axios)
//Vue.use(VueLayers)

Vue.use(VueMoment, {
  moment,
})

//Vue layers components
/* Vue.use(VueLayers, {
  dataProjection: 'EPSG:2056',
}) 
Vue.use(TileLayer)
Vue.use(WmtsSource)
Vue.use(WmsSource)
Vue.use(OsmSource)
Vue.use(PointGeom)
Vue.use(StyleBox)*/
const router = new VueRouter({
  mode: 'history',
  routes: routes
});

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
