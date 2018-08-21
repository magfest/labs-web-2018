import '@babel/polyfill'
import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import Vuetify from 'vuetify'
import VueRouter from 'vue-router'


Vue.config.productionTip = false

Vue.use(Vuetify, {
  theme: {
    primary: '#94dfff',
    secondary: '#212121',
    accent: '#ED7E23'
  }
})
Vue.use(VueRouter)


import Home from './components/Home'
import Faq from "./components/Faq"
import store from './store'
const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes:[
    {
      path: '/', component: Home
    },
    {
      path: "/faq", component: Faq
    }
  ]
})



new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
