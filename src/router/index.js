import { createRouter, createWebHistory } from 'vue-router';
import MainMenu from '../components/MainMenu.vue';
import GameComponent from '../components/GameComponent.vue';
import UserRegister from '../components/UserRegister.vue';
import GameOver from '../components/GameOver.vue';
import UserSettings from '../components/UserSettings.vue';
import UserAudio from '../components/UserAudio.vue';
import UserLogin from '../components/UserLogin.vue';
import PlayerLeaderboard from '../components/PlayerLeaderboard.vue'; 

const routes = [
  {
    path: '/',
    name: 'MainMenu',
    component: MainMenu,
  },
  {
    path: '/game',
    name: 'Game',
    component: GameComponent,
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
  },
  {
    path: '/settings',
    name: 'UserSettings',
    component: UserSettings
  },
  {
    path: '/audio',
    name: 'UserAudio',
    component: UserAudio
  },
  {
    path: '/login',
    name: 'Login',
    component: UserLogin,
  },
  {
    path: '/leaderboard', 
    name: 'Leaderboard',
    component: PlayerLeaderboard,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;