<template>
  <v-flex xs12 md6>
    <v-container id="guestcard">
      <div class="contain" v-if="guest.bio.pic_url != ''">
        <img :src="'https://labs2018.uber.magfest.org' + guest.bio.pic_url">
      </div>
      <h2>{{ guest.group.name }}</h2>
      <p class="left">{{ guest.bio.desc }}</p>
      <v-container>
        <v-btn 
          :href="website"
          target="_blank"
          icon
          v-if="showWebsite"
        >
          <v-icon>web</v-icon>
        </v-btn>
        <v-btn
          :href="facebook"
          target="_blank"
          icon
          v-if="showFacebook"
        >
          <img id="facebook" :src="require('../assets/facebook.svg')">
        </v-btn>
        <v-btn
          :href="twitter"
          target="_blank"
          icon
          v-if="showTwitter"
        >
          <img id="facebook" :src="require('../assets/twitter.png')">
        </v-btn>
      </v-container>
    </v-container>
  </v-flex>
</template>

<script>
export default {
  props: [
    "guest"
  ],

  computed: {
    showWebsite(){
      if (this.guest.bio.website == ''){
        return false
      } else {
        return true
      }
    },
    website() {
      if (this.guest.bio.website.match(/http/) == 'http'){
        return this.guest.bio.website
      } else {
        return 'http://' + this.guest.bio.website
      }
    },
    showFacebook(){
      if (this.guest.bio.facebook == ''){
        return false
      } else {
        return true
      }
    },
    facebook(){
      if (this.guest.bio.facebook.match(/http/) == 'http'){
        return this.guest.bio.facebook
      } else {
        return 'http://' + this.guest.bio.facebook
      }
    },
    showTwitter(){
      if (this.guest.bio.twitter == ''){
        return false
      } else {
        return true
      }
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


