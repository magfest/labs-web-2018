<template>
  <v-flex xs12 md6>
    <v-container id="guestcard">
      <div class="contain">
        <img :src="'https://labs2018.uber.magfest.org' + guest.bio.pic_url">
      </div>
      <h2>{{ guest.group.name }}</h2>
      <p class="left">{{ guest.bio.desc }}</p>
      <v-btn 
        :href="website"
        target="_blank"
        icon
      >
        <v-icon>web</v-icon>
      </v-btn>
      <v-btn
        :href="facebook"
        target="_blank"
        icon
      >
        <img id="facebook" :src="require('../assets/facebook.svg')">
      </v-btn>
      <v-btn
        :href="twitter"
        target="_blank"
        icon
      >
        <img id="facebook" :src="require('../assets/twitter.png')">
      </v-btn>
    </v-container>
  </v-flex>
</template>

<script>
export default {
  props: [
    "guest"
  ],

  computed: {
    website() {
      if (this.guest.bio.website.match(/http/) == 'http'){
        return this.guest.bio.website

      } else {
        return 'http://' + this.guest.bio.website
      }
    },
    facebook(){
      return 'https://' + this.guest.bio.facebook
    },
    twitter(){
      if (this.guest.bio.twitter.match(/twitter/) == 'twitter'){
        return this.guest.bio.twitter
      } else {
        return 'http://twitter.com/' + this.guest.bio.twitter
      }
    }
  }
}
</script>

<style>
#guestcard {
  background: white;
  color: black;
  margin: 5px;
  height: 100%;
  text-align: center;
}
.left{
  text-align: left;
}
#facebook {
  width: 20px;
}

.contain img{
  width: 100%;
  height: auto;
}
</style>


