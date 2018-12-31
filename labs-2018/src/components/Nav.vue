<template>
  <v-toolbar  color="primary" dark>
    <v-toolbar-title><v-btn flat to="/" active-class="">MagLabs</v-btn></v-toolbar-title>
    <v-spacer></v-spacer>
      <span v-if="windowSize.x > 768">
      <v-btn
        flat
        :to="{path:'/schedule'}"
        >Schedule</v-btn>
        <v-btn
          flat
          :to="{path:'/faq'}"
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
            <v-list-tile :to="{path:'/schedule'}">Schedule</v-list-tile>
            <v-list-tile :to="{path:'/faq'}">FAQ</v-list-tile>
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
