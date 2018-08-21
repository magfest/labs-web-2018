<template>
  <v-flex 
    xs12 
    sm6 
    md3
  >
    <v-card
      height="100%"
      tile
      flat
      class="pad-card"
    >
      <v-card-media
        :src="require('../assets/rock.jpg')"
        :contain="true"
        height="25vh"
      ></v-card-media>
      <v-card-title>
        <h2>Rock</h2>
        <p>Each MAGFest event is a musical mecca, and this is no different. Come catch our awesome lineup of concerts, and find your new favorite VGM artist. You can also take your own musical skills to the next level with workshops in our Jam Clinic, and you can learn audio engineering and sound design with our concert hall workshops as well.</p>
      </v-card-title>
    </v-card>
  </v-flex>
</template>

<style>
.pad-card{
  padding:5px;
  text-align:left;
}
</style>


