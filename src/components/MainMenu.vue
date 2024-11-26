<template>
  <div id="main-menu-container">
    <h1 id="main-menu-title">Textorcist</h1>
    <div id="main-menu-buttons">
      <button @click="$router.push('/game')">Начать игру</button>
      <button @click="$router.push('/register')">Регистрация</button>
      <button @click="$router.push('/leaderboard')">Рейтинг игроков</button>
      <button @click="openSettings">Настройки</button>
      <button @click="exitGame">Выход</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "MainMenu",
  methods: {
    openSettings() {
      alert("Настройки будут реализованы позже");
    },
    exitGame() {
      window.close();
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");

#main-menu-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100vw;
  margin: 0;
  padding: 0;
  background-image: url("@/assets/background_registration.jpg");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  position: relative;
}

#main-menu-container::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.6);
  z-index: 1;
}

#main-menu-container > * {
  position: relative;
  z-index: 2;
}

#main-menu-title {
  color: white;
  font-size: 40px;
  font-family: "Press Start 2P", sans-serif;
  text-shadow: 0 0 5px black, 0 0 10px gray, 0 0 15px gray;
  border-bottom: 2px dashed gray;
  padding-bottom: 10px;
  margin-bottom: 30px;
  text-align: center;
}

#main-menu-buttons {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 320px;
}

button {
  padding: 15px;
  font-size: 14px;
  font-family: "Press Start 2P", sans-serif;
  border: 2px solid rgba(255, 255, 255, 0.8);
  border-radius: 10px;
  cursor: pointer;
  background-color: rgba(255, 255, 255, 0.85);
  color: black;
  text-transform: uppercase;
  width: 100%;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease, transform 0.2s ease;
}

button:hover {
  background-color: rgba(255, 255, 255, 1);
  transform: scale(1.05);
}

button:active {
  background-color: #ccc;
}
</style>