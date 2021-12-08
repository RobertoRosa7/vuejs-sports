<template>
  <div class="section">
    <div class="image">
      <v-img class="profile-img" :src="user.photo" />
    </div>
    <p class="name">Olá {{ user.name }}!</p>
    <small class="email">{{ user.email }}</small>
  </div>
</template>

<script>
import api from '../../axios';

export default {
  name: "User",
  data: () => ({
    user: {}
  }),
  created() {
    api.get('/user?id=01').then(({ data }) => this.user = data.data);
  }
};
</script>

<style scoped>
</style>
