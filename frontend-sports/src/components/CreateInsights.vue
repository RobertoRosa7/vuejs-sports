<template>
  <v-app class="create-insights">
    <div class="background">
      <v-img class="image" :src="require('../assets/background.png')" />
    </div>
    <v-main>
      <div class="header">
        <v-btn class="btn" :to="'/'" icon>
          <v-icon style="color: #ED4D77">arrow_back</v-icon>
        </v-btn>
        <p>
          <span>Criar</span>
          <strong>Insight</strong>
        </p>
      </div>
      <v-container class="container">
        <v-card class="input-text">
          <div class="form-group">
            <span>Insight</span>
            <textarea
              v-model="insights.description"
              class="form-control"
              placeholder="Escreva aqui seu insight..."
              name
              id
              cols="30"
              rows="10"
            ></textarea>
          </div>
          <v-divider></v-divider>
          <small>Limite de caracter 400</small>
          <div class="form-group">
            <span>Categoria</span>
            <input
              v-model="insights.category"
              type="text"
              class="form-control"
              placeholder="Adicione uma categoria (opcional)..."
            />
          </div>
          <v-divider></v-divider>
        </v-card>
      </v-container>
    </v-main>
    <div class="actions">
      <v-btn @click="create()" class="btn">
        <span>publicar</span>
      </v-btn>
    </div>
  </v-app>
</template> 
<script>
export default {
  name: "CreateInsights",
  data: () => ({
    insights: {}
  }),
  methods: {
    create() {
      const formSend = Object.assign({}, this.insights);
      console.log({ insights: formSend });
    }
  }
};
</script>

<style scoped>
.create-insights {
  position: relative;
}
.background {
  position: absolute;
  top: 0;
  left: 0;
  max-height: calc(100vh - 780px);
  overflow: hidden;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.header {
  display: flex;
  justify-content: space-between;
  z-index: 1;
  height: calc(100vh - 750px);
  align-items: center;
  color: #ed4d77;
}
.header p {
  flex: 1;
  text-align: center;
  display: flex;
  flex-direction: column;
  font-style: italic;
  margin-right: 30px;
}
.header p span {
  font-size: 1.2em;
  font-weight: 200;
  text-transform: uppercase;
  line-height: 1em;
  letter-spacing: 0.04em;
}
.header p strong {
  line-height: 1em;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}
.form-group {
  display: flex;
  flex-direction: column;
  margin: 25px 0;
}
.input-text {
  padding: 20px 16px;
}
.input-text small {
  display: block;
  text-align: right;
  font-family: "Exo 2";
  color: rgba(0, 0, 0, 0.4);
  font-style: italic;
}
.input-text span {
  font-family: "Exo 2";
  text-transform: uppercase;
  font-style: italic;
}
.form-control {
  padding: 8px;
}
.container {
  height: 100%;
}
.actions {
  position: fixed;
  bottom: 10px;
  width: 100%;
}
.actions .btn {
  width: 100% !important;
  background-color: #ed4d77 !important;
  color: white;
  font-family: "Exo 2";
  opacity: 0.5;
}
input::placeholder,
textarea::placeholder {
  font-size: 0.9em;
  color: rgba(0, 0, 0, 0.4);
  font-family: "Exo 2";
  font-style: italic;
}
</style>