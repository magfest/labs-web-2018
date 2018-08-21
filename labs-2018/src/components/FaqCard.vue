<template>
  <v-flex xs10 offset-xs1 class="card">
    <v-card>
      <v-card-title primary-title>
        <h3>{{ question }}</h3>
        <p v-html="answer"></p>
        <p class="note"> {{ note }}</p>
      </v-card-title>
    </v-card>
  </v-flex>
</template>

<script>
export default {
  props:  [
    'question',
    'answer',
    'note'
  ]
}
</script>

<style>
.note{
  background-color: #ffeeba
}
.center{
  text-align: center;
}
.card{
  padding-top:10px;
  text-align: left;
}
</style>

