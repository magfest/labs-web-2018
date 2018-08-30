<template>
  <v-container>
    <v-layout row wrap justify-space-between>
      <Guest
        v-for="guest in guests"
        v-bind:key="guest.id"
        v-bind:guest="guest"
      />
    </v-layout>
  </v-container>
</template>

<script>
import { mapState } from "vuex"
import Guest from "./Guest"

export default {
  computed: mapState({
    guests: state => state.guests.guests.result
  }),

  components:{
    Guest
  }
}
</script>

