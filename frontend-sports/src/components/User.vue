<template>
  <div class="section">
    <div class="image">
      <v-img class="profile-img" :src="image" />
    </div>
    <p class="name">Olá {{ user.name }}!</p>
    <small class="email">{{ user.email }}</small>
  </div>
</template>

<script>
export default {
  name: "User",
  data: () => ({
    image:
      "https://www.rd.com/wp-content/uploads/2017/09/01-shutterstock_476340928-Irina-Bg.jpg",
    user: {
      name: "Antônio",
      email: "antonio.pina@g.globo",
    },
  }),
};
</script>

<style scoped>
</style>
