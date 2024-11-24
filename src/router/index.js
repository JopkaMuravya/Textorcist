import { createRouter, createWebHistory } from 'vue-router';
import MainMenu from '../components/MainMenu.vue';
import GameComponent from '../components/GameComponent.vue';
import UserRegister from '../components/UserRegister.vue';

const routes = [
  {
    path: '/',
    name: 'MainMenu',
    component: MainMenu
  },
  {
    path: '/game',
    name: 'Game',
    component: GameComponent
  },
  {
    path: '/register',
    name: 'Register',
    component: UserRegister
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;