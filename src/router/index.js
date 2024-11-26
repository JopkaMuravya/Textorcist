import { createRouter, createWebHistory } from 'vue-router';
import MainMenu from '../components/MainMenu.vue';
import GameComponent from '../components/GameComponent.vue';
import UserRegister from '../components/UserRegister.vue';
import GameOver from '../components/GameOver.vue';

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
  },
  {
    path: '/gameover',
    name: 'GameOver',
    component: GameOver,
    props: true
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;