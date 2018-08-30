import Vue from 'vue'
import Vuex from 'vuex'
import faqs from "./modules/faq"
import guests from "./modules/guests"

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  modules: {
    faqs,
    guests
  },
  strict: debug
})