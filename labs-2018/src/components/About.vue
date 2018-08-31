<template>
  <div id="about">
    <h1>Play, Learn, Create, Rock!</h1>
    <p>MAGLabs is a unique 3 day event, bringing maker content to the world of gaming. Explore our giant video game library, arcade, and concert hall. Learn to make your first game, create a cosplay, or solder your own electronic projects. All available to you 24 hours a day.</p>
    <Hotel/>
    <Register/>
    <v-btn
      to="/guests"
      color="secondary"
    >
      See Our Guests
    </v-btn>
    <v-btn
      to="/bands"
      color="secondary"
    >
      See Our Bands
    </v-btn>
  </div>
</template>

<script>
import Hotel from "./Hotel"
import Register from "./Register"

export default {
  components: {
    Hotel,
    Register
  }
}
</script>

<style>
#about  {
  text-align: left;
  padding: 30px;
}
</style>

