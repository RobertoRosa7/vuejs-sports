import Vue from 'vue';
import VueRouter from 'vue-router';

const Home = () => import('./components/Home.vue');
const CreateInsights = () => import('./components/CreateInsights.vue');

Vue.use(VueRouter);
const extractParamsId = route => ({ id: parseInt(route.params.id) });
const router = new VueRouter({
  mode: 'history',
  linkActiveClass: 'active',
  routes: [
    {
      path: '/',
      component: Home,
      alias: ['/home'],
      props: extractParamsId
    },
    {
      path: '/create',
      component: CreateInsights,
      alias: ['/create-insights', '/novo-insights', '/novo'],
      props: extractParamsId
    }
  ]
});

export default router;