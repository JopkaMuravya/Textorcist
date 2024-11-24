<template>
  <div class="main-menu">
    <h1>Главное меню</h1>
    <button @click="$router.push('/game')">Начать игру</button>
    <button @click="openSettings">Настройки</button>
    <button @click="$router.push('/register')">Зарегистрироваться</button>
    <button @click="exitGame">Выход</button>
  </div>
</template>

<script>
export default {
  name: 'MainMenu',
  methods: {
    openSettings() {
      // Логика для открытия настроек
      alert('Настройки будут реализованы позже');
    },
    exitGame() {
      // Логика для выхода из игры
      window.close();
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