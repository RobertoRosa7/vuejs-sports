<template>
  <v-app class="app">
    <div class="background">
      <v-img class="image" :src="require('../assets/background.png')" />
    </div>
    <v-main>
      <div class="header">
        <div class="line">
          <div class="logo2">
            <span class="text-logo">Insights</span>
          </div>
          <div class="user">
            <div class="section">
              <div class="image">
                <v-img class="profile-img" :src="user.photo" />
              </div>
            </div>
          </div>
          <div class="more">
            <v-btn :to="'/create'" icon>
              <v-icon style="color: #ED4D77">add</v-icon>
            </v-btn>
          </div>
        </div>
        <div class="section">
          <p class="name">Olá {{ user.name }}!</p>
          <small class="email">{{ user.email }}</small>
        </div>
        <div class="section">
          <span class="feed">
            Feed de
            <strong>Insights</strong>
          </span>
        </div>
      </div>
      <div class="cads">
        <Card
          @delete="onDelete($event)"
          @detail="openDetail($event)"
          :card="card"
          v-for="card in cards"
          :key="card.id"
        />
      </div>
      <v-container v-if="cards.length > 0">
        <div class="more-cards">
          <v-btn icon>
            <v-icon>more_horiz</v-icon>
          </v-btn>
          <span>Toque para exibir mais insights</span>
        </div>
        <form @submit.prevent="search" @reset="resetar" class="card-search">
          <v-card class="search">
            <input
              v-model="searchTerms"
              type="text"
              name
              id
              placeholder="pesquise por termos ou categorias"
            />
            <v-btn type="submit" icon>
              <v-icon>search</v-icon>
            </v-btn>
          </v-card>
        </form>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import api from '../../axios';
import Card from './Card.vue';

export default {
  name: 'Home',
  components: {
    Card,
  },
  data: () => ({
    user: {
      name: "Antônia",
      email: "antonia.pina@g.globo",
      photo:
        "https://www.rd.com/wp-content/uploads/2017/09/01-shutterstock_476340928-Irina-Bg.jpg",
    },
    searchTerms: '',
    cards: [],
    filtered: []
  }),
  created() {
    api.get('/').then(({ data }) => {
      this.cards = data.data;
      this.filtered = data.data;
    });
    api.get('/user?id=01').then(({ data }) => this.user = data.data);
  },
  methods: {
    resetar() {
    },
    search() {
      if (this.searchTerms.length > 0) {
        const cards = this.cards.filter(value => value.category.toLowerCase() === this.searchTerms.toLowerCase());
        if (cards.length > 0) {
          this.cards = cards;
        }
      } else {
        this.cards = this.filtered;
      }
    },
    openDetail(event) {
      this.$router.push({ path: 'create', query: { id: event.id } });
    },
    onDelete(event) {
      api.delete(`/?id=${event.id}`).then(() => {
        alert('Feed excluído')
        api.get('/').then(({ data }) => {
          this.cards = data.data;
          this.filtered = data.data;
        });
      });

    }
  }
};
</script>

<style scoped>
.app {
  position: relative;
  overflow-x: hidden;
  background-color: #eee !important;
}
.header {
  height: calc(100vh - 640px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 16px;
  flex-direction: column;
}
.logo {
  max-width: 45px;
}

.text-logo {
  color: #ed4d77;
  font-family: "Exo 2";
  font-weight: bold;
  font-size: 0.8em;
}
.line {
  width: 100%;
  justify-content: space-between;
  align-items: center;
  flex-wrap: nowrap;
  display: flex;
  margin-top: 50px;
}
.background {
  position: absolute;
  top: 0;
  left: 0;
  max-height: calc(100vh - 550px);
  overflow: hidden;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.more {
  display: flex;
  justify-content: flex-end;
  min-width: 64px;
}
.logo {
  display: flex;
  justify-content: flex-start;
}
.logo2 {
  min-width: 64px;
}

.user {
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  min-width: 64px;
}
.section {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-top: 8px;
}
.section p {
  color: white;
  font-weight: 200;
  font-size: 1.5em;
  font-style: italic;
  margin: 0;
  line-height: 1em;
}
.section small {
  color: silver;
  letter-spacing: 0.08em;
  font-size: 0.7em;
}
.section .feed {
  color: #ed4d77;
  font-family: "Exo 2";
}
.profile-img {
  height: 64px;
  width: 64px;
  border: 2px solid #ed4d77;
  border-radius: 50%;
  overflow: hidden;
  margin-left: auto;
  margin-right: auto;
}
.more-cards {
  display: flex;
  flex-direction: column;
  width: 100%;
  justify-content: center;
  align-items: center;
}
.more-cards span {
  font-size: 0.8em;
  font-family: "Exo 2";
}
.card-search {
  margin-top: 60px;
}
.search {
  min-height: 52px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 8px;
}
.search span {
  font-size: 0.8em;
  font-family: "Exo 2";
  font-style: italic;
}
.search input {
  width: 100%;
}
.search input:focus,
.search input:active {
  border: none;
  outline: none;
}
.search input::placeholder {
  font-size: 0.8em;
  font-family: "Exo 2";
  font-style: italic;
}
</style>