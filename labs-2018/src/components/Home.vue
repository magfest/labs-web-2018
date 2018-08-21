<template>
  <div>
    <Landing/>
    <About/>
    <v-layout 
      row 
      wrap 
    >
      <Play/>
      <Learn/>
      <Create/>
      <Rock/>
    </v-layout>
  </div>
</template>

<script>
import About from "./About"
import Play from "./Play"
import Create from "./Create"
import Learn from "./Learn"
import Rock from "./Rock"
import Landing from "./Landing"

export default {
  components: {
    About,
    Play,
    Learn,
    Create,
    Rock,
    Landing
  }
}
</script>

