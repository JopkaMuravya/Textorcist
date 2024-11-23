<template>
  <div class="main-menu">
    <h1>Главное меню</h1>
    <button @click="startGame">Начать игру</button>
    <button @click="openSettings">Настройки</button>
    <button @click="exitGame">Выход</button>
  </div>
</template>

<script>
export default {
  name: 'MainMenu',
  methods: {
    startGame() {
      // Логика для начала игры
      this.$emit('start-game');
    },
    openSettings() {
      // Логика для открытия настроек
      this.$emit('open-settings');
    },
    exitGame() {
      // Логика для выхода из игры
      this.$emit('exit-game');
    }
  }
}
</script>

<style scoped>
.main-menu {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}
button {
  margin: 10px;
  padding: 10px 20px;
  font-size: 16px;
}
</style>