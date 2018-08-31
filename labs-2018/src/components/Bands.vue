<template>
  <v-container>
    <v-layout row wrap justify-space-between>
      <Guest
        v-for="band in bands"
        v-bind:key="band.id"
        v-bind:guest="band"
      />
    </v-layout>
  </v-container>
</template>

<script>
import { mapState } from "vuex"
import Guest from "./Guest"

export default {
  computed: mapState({
    bands: state => state.bands.bands.result
  }),

  components:{
    Guest
  }
}
</script>