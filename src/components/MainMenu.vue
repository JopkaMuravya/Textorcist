<template>
  <div class="main-menu">
    <div class="player-cont"><img src="@/assets/main_character.png" alt="Персонаж" class="player"/></div>
    <div id="button-container">
      <div id="upper-container" class="btn-cont-div">
        <button class = "menu-button">Вход</button>
      </div>
      <div id="middle-container" class="btn-cont-div">
        <button class = "menu-button">Таблица лидеров</button>
      </div>
      <div id="bottom-container" class="btn-cont-div">
        <div id="bottom-left">
          <button class = "menu-button" @click="openSettings">Настройки</button>
        </div>
        <div id="bottom-middle">
          <button class = "menu-button" @click="startGame">Начать игру</button>
        </div>
        <div id="bottom-right">
          <button class = "menu-button" @click="exitGame">Выход</button>
        </div>
      </div>
    </div>
  </div>
</template>
<button>Вход</button>
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
  background-image: url("@/assets/background.png");
  background-size: contain;
  background-position: top;
  background-repeat: no-repeat;

  width: 100vw;
  height: 75vw;

  position:relative;
}
.player {
  z-index: 100;
  margin: auto;
  width: 20vw;
  height: 20vw;
}
.player-cont {
  position: absolute;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
}
#button-container {
  position: relative;
  display: flex;
  flex-direction: column;
  bottom: 50px;

  padding-left: auto;
  padding-right: auto;
  width: 100%;

  position: absolute;
}
.btn-cont-div {
  padding-left: 15%;
  padding-right: 15%;
  margin-top: 10px;
}
#bottom-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
#middle-container {
  display: flex;
  justify-content: start;
}
#upper-container {
  display: flex;
  justify-content: start;
}
.menu-button {
  background-color: #7B6E62;
  font-size: 1.12em;
  border: #000000;
  border-radius: 15px;
  border-width: 100px;
  width: 150px;
  height: 50;
  stroke-width: 5px;
  border-color: #000000;
  box-shadow: 3px 3px 2px 1px #000000;

  margin: 10px;
  /* padding: 10px 20px; */
  width: 20vw;
  height: 6vw;
  font-family: 'Krona One'
}

</style>