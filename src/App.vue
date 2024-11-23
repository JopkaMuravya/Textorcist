<template>
  <div id="app">
    <MainMenu v-if="!isGameStarted" @start-game="startGame" @open-settings="openSettings" @exit-game="exitGame" />
    <GameComponent v-if="isGameStarted" @game-ended="endGame" />
  </div>
</template>

<script>
import MainMenu from './components/MainMenu.vue';
import GameComponent from './components/GameComponent.vue'; // Предположим, что у вас есть компонент игры

export default {
  name: 'App',
  components: {
    MainMenu,
    GameComponent
  },
  data() {
    return {
      isGameStarted: false,
    };
  },
  methods: {
    startGame() {
      this.isGameStarted = true;
    },
    openSettings() {
      // Здесь вы можете открыть компонент настроек или модальное окно
      alert('Настройки будут реализованы позже.');
    },
    exitGame() {
      // Закрытие приложения
      window.close(); // Это закроет окно Electron
    },
    endGame() {
      this.isGameStarted = false; // Возвращает в главное меню
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

html, body, #app {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background: none; 
}

</style>
