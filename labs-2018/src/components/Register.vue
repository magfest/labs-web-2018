<template>
  <v-btn v-if="use=='nav'" flat href="https://labs2018.uber.magfest.org/uber/preregistration/form">
    Register Now
  </v-btn>
  <v-btn 
    v-else 
    href="hhttps://labs2018.uber.magfest.org/uber/preregistration/form"
    color="secondary"
  >
    Register Now
  </v-btn>
</template>

<script>
export default {
  props: [
    'use'
  ]
}
</script>