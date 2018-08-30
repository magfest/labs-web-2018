<template>
  <div id="app">
    <v-app>
      <Nav/>
      <v-content  class="mainContent">
        <router-view></router-view>
      </v-content>
    </v-app>
  </div>
</template>

<script>
import Nav from "./components/Nav"

export default {
  name: 'app',
  components: {
    Nav
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background-color:#269;
  background-image: linear-gradient(rgba(127,127,127,.25) 2px, transparent 2px),
  linear-gradient(90deg, rgba(127,127,127,.25) 2px, transparent 2px),
  linear-gradient(rgba(127,127,127,.2) 1px, transparent 1px),
  linear-gradient(90deg, rgba(127,127,127,.2) 1px, transparent 1px);
  background-size:100px 100px, 100px 100px, 20px 20px, 20px 20px;
  background-position:-2px -2px, -2px -2px, -1px -1px, -1px -1px;
}

.mainContent{
  padding-top: 50px;
}
</style>
