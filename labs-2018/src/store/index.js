import Vue from 'vue'
import Vuex from 'vuex'
import faqs from "./modules/faq"
import guests from "./modules/guests"
import bands from "./modules/bands"

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    faqs,
    guests,
    bands
  },
  strict: debug
})