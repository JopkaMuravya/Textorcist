<template>
  <div id="main-menu-container">
    <audio ref="backgroundAudio" loop>
      <source src="@/assets/background-music.mp3" type="audio/mpeg">
      Ваш браузер не поддерживает аудио.
    </audio>
    <div id="user-info" @click="logout">
      <img :src="user.avatar" alt="Avatar" />
      <div>
        <p>{{ user.name }}</p>
        <p>Личный рекорд: {{ user.record }}</p>
      </div>
    </div>
    <h1 id="main-menu-title">Textorcist</h1>
    <div id="main-menu-buttons">
      <button @click="navigateToGame">Начать игру</button>
      <button @click="navigateToRegister">Регистрация</button>
      <button @click="navigateToLeaderboard">Рейтинг игроков</button>
      <button @click="navigateToSettings">Настройки</button>
      <button @click="exitGame">Выход</button>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';

export default {
  name: 'MainMenu',
  data() {
    return {
      user: {
        name: "Анонимус",
        avatar: require("@/assets/default_avatar.png"),
        record: 0,
      },
    };
  },
  computed: {
    ...mapState(['isMuted', 'volume']),
  },
  methods: {
    ...mapActions(['playClickSound']), // Подключаем действие для воспроизведения звука нажатия
    exitGame() {
      this.playClickSound();
      window.close();
    },
    navigateToRegister() {
      this.playClickSound(); // Воспроизводим звук нажатия
      this.$router.push('/register');
    },
    navigateToSettings() {
      this.playClickSound(); // Воспроизводим звук нажатия
      this.$router.push('/settings');
    },
    navigateToGame() {
      this.playClickSound(); // Воспроизводим звук нажатия
      this.$router.push('/game');
    },
    navigateToLeaderboard() {
      this.playClickSound();
      this.$router.push('/leaderboard')
    },
    playMusic() {
      this.$store.dispatch('playBackgroundMusic'); // Вызов действия Vuex для воспроизведения музыки
    },
    logout() {
      localStorage.removeItem("currentUser");
      this.user = {
        name: "Анонимус",
        avatar: require("@/assets/default_avatar.png"),
        record: 0,
      };
      this.$router.push("/register");
    },
  },
  mounted() {
    this.playMusic(); // Воспроизвести музыку при монтировании компонента
    const currentUser = JSON.parse(localStorage.getItem("currentUser"));
    if (currentUser) {
      this.user.name = currentUser.name || "Анонимус";
      this.user.avatar = require("@/assets/default_avatar.png");

      fetch(`http://127.0.0.1:8000/api/get-record/${encodeURIComponent(this.user.name)}/`)
        .then(response => {
          if (!response.ok) {
            throw new Error("Ошибка запроса");
          }
          return response.json();
        })
        .then(data => {
          this.user.record = data.record;
        })
        .catch(error => {
          console.error("Ошибка получения личного рекорда:", error);
        });
    }
  },
}
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
  user-select: none;
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
  user-select: none;
}

button:hover {
  background-color: rgba(255, 255, 255, 1);
  transform: scale(1.05);
}

button:active {
  background-color: #ccc;
}

#user-info {
  position: absolute;
  top: 20px;
  left: 20px;
  display: flex;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.85); 
  padding: 10px; 
  border-radius: 12px; 
  color: white;
  font-family: "Press Start 2P", sans-serif;
  font-size: 10px; 
  gap: 10px;
  box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.3);
  user-select: none;
  cursor: pointer;
}

#user-info img {
  width: 40px; 
  height: 40px;
  border-radius: 50%;
  border: 2px solid white;
  object-fit: cover;
}

#user-info div {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

#user-info p {
  margin: 3px 0; 
}

#user-info p:first-child {
  font-size: 12px; 
  font-weight: bold;
  color: #fff;
  text-shadow: 0px 0px 3px rgba(255, 255, 255, 0.5); 
}

#user-info p:last-child {
  font-size: 10px; 
  color: #bbb; 
}

</style>