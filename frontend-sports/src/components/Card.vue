<template>
  <v-container class="container">
    <v-row>
      <v-card @click.stop="openDetail(card)" class="card" elevation="2">
        <span class="text">{{ card.text }}</span>
        <v-btn v-if="card.category" class="btn">
          <span>{{ card.category }}</span>
        </v-btn>
        <v-btn @click.stop="onDelete(card)" icon class="btn-delete">
          <v-icon>close</v-icon>
        </v-btn>
      </v-card>
    </v-row>
  </v-container>
</template>

<script>
export default {
  props: ['card'],
  name: 'Card',
  data: () => ({}),
  methods: {
    openDetail(card) {
      this.$emit('detail', card);
    },
    onDelete(card) {
      this.$emit('delete', card);
    }
  }
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
  padding: 26px 8px;
}
.card span {
  font-size: 14px;
  font-family: "Exo 2";
  color: #000;
  display: inline-block;
  text-align: center;
  position: relative;
}
.btn-delete {
  position: absolute;
  top: 0px;
  right: 5px;
}
.btn {
  background: white !important;
  border: 1px solid #ed4d77;
  min-width: 64px;
  margin: 16px auto;
  line-height: 1em;
  max-height: 30px;
  box-shadow: none;
}
.btn span {
  font-size: 0.7em;
  color: #ed4d77;
  font-weight: bold;
}
</style>
