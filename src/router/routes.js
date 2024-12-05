import MainMenu from "src/components/MainMenu.vue"
import UserRegister from "src/components/UserRegister.vue"
import UserSettings from "src/components/UserSettings.vue"
import UserAudio from "src/components/UserAudio.vue"
import GameComponent from "src/components/GameComponent.vue"
import GameOver from "src/components/GameOver.vue"
import PlayerLeaderboard from "src/components/PlayerLeaderboard.vue"
import UserLogin from "src/components/UserLogin.vue"
const routes = [
  {path: '/', component: MainMenu},
  {path: '/register', component: UserRegister},
  {path: '/settings', component: UserSettings},
  {path: '/audio', component: UserAudio},
  {path: '/game', component: GameComponent},
  {path: '/gameover', component: GameOver, name: 'GameOver', props: true},
  {path: '/leaderboard', component: PlayerLeaderboard},
  {path: '/login', component: UserLogin},
]

export default routes
