<template>
  <v-container class="container">
    <v-row>
      <v-card class="card" elevation="2">
        <span class="text">{{ card.conteudo }}</span>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: ['card'],
  name: 'Card',
  data: () => ({})
}
</script>

<style scoped>
.container {
  padding: 20px;
}
.card {
  width: 100%;
  min-height: 64px;
  margin-bottom: 8px;
  margin-top: 8px;
  display: flex;
  flex-direction: column;
  padding: 8px;
}
.card span {
  font-size: 14px;
  font-family: "Exo 2";
  color: #000;
}
</style>
