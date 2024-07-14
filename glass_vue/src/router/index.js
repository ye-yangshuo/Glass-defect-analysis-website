import Vue from 'vue';
import VueRouter from 'vue-router';
import Analyze from '@/components/DataAnalyze.vue';
import Images from '@/components/ImageView.vue';
import Login from '@/components/UserLogin.vue';
import Header from '@/components/HeaderTop.vue';
Vue.use(VueRouter);

const routes = [
  {
    path: '/Analyze',
    name: 'Analyze',
    component: Analyze,
  },
  {
    path: '/Images',
    name: 'Images',
    component: Images,
  },
  {
    path: '/',
    name: 'Login',
    component: Login,
  },
  {
    path: '/Header',
    name: 'Header',
    component: Header,
  },

  // 其他路由规则...
];

const router = new VueRouter({
  routes,
});

export default router;