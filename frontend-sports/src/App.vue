<template>
  <transition name="slide" mode="out-in">
    <router-view></router-view>
  </transition>
</template>

<script>

export default {
  name: 'App',
  data: () => ({
  }),
};
</script>

<style scoped>
.slide-enter,
.slide-leave-to {
  transform: translateX(-100%);
  opacity: 0;
}
.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s;
}
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
  font-size: 1em;
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
</style>
