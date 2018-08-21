import '@babel/polyfill'
import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import Vuetify from 'vuetify'
import VueRouter from 'vue-router'


Vue.config.productionTip = false

Vue.use(Vuetify)
Vue.use(VueRouter)



new Vue({
  render: h => h(App)
}).$mount('#app')
