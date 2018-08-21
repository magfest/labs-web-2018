<template>
  <v-btn v-if="use=='nav'" flat href="https://book.passkey.com/event/49604307/owner/10925932/landing">
    Book Hotel
  </v-btn>
  <v-btn 
    v-else 
    href="https://book.passkey.com/event/49604307/owner/10925932/landing"
    color="secondary"
  >
    Book Hotel
  </v-btn>
</template>

<script>
export default {
  props: [
    'use'
  ]
}
</script>
