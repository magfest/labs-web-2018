<template>
  <v-toolbar scroll-off-screen absolute color="primary" dark>
    <v-toolbar-title><v-btn flat to="/" active-class="">MagLabs 2018</v-btn></v-toolbar-title>
    <v-spacer></v-spacer>
      <span v-if="windowSize.x > 768">
        <v-btn 
          flat 
          :to="{path:'/faq'}"
          v-bind:class="{hidden:shouldHide}"
          >FAQ</v-btn>
        <Hotel :use="'nav'"/>
        <Register :use="'nav'"/>
      </span>
      <span v-else>
        <v-menu>
          <v-toolbar-title slot="activator">
            <span><v-icon>more_vert</v-icon></span>
          </v-toolbar-title>
          <v-list>
            <v-list-tile :to="{path:'/faq'}">FAQ</v-list-tile>
            <v-list-tile href="https://book.passkey.com/event/49604307/owner/10925932/landing">Book Now</v-list-tile>
            <v-list-tile href="https://labs2018.uber.magfest.org/uber/preregistration/form">Register</v-list-tile>
          </v-list>
        </v-menu>
      </span>
  </v-toolbar>
</template>

<script>
import Hotel from "./Hotel"
import Register from "./Register"

export default {
  components: {
    Hotel,
    Register
  },

  data() {
    return {
      windowSize: {
        x: 0,
        y: 0
      }
    }
  },

  mounted(){
    this.onResize()
  },

  methods: {
    onResize(){
      this.windowSize = {
        x: window.innerWidth,
        y: window.innerHeight
      }
    }
  }
}
</script>

<style>
@font-face {
    font-family: "Hello Blueprint";
    src: url(../assets/HelloBlueprint.ttf);
}

.title{
  font-family: "Hello Blueprint"
}

.hidden{
  display: true;
}
</style>


