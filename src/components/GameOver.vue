<template>
  <div class="gameover-container">
    <h1>Игра окончена!</h1>
    <h2>Счёт: {{ localScore }}</h2>
    <div id="gameover-buttons">
      <button @click="restartGame">Начать заново</button>
      <button @click="goToMenu">Меню</button>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import sound_win from '../assets/win6.mp3';

export default {
  name: "GameOver",
  props: {
    score: {
      type: Number,
      default: 0,
    },
  },
  data() {
    return {
      localScore: this.score,
      soundWin: sound_win,
    };
  },
  methods: {
    ...mapActions(["playClickSound", "stopBackgroundMusic", "playBackgroundMusic"]),
    playWinSound() {
      this.winSoundAudio = new Audio(this.soundWin); 
      this.winSoundAudio.play(); 
    },
        
    stopWinSound() {
      if (this.winSoundAudio) {
        this.winSoundAudio.pause(); 
        this.winSoundAudio.currentTime = 0; 
      }
    },
    async fetchAndUpdateRecord() {
      try {
        const token = localStorage.getItem("accessToken");
        if (!token) {
          console.error("Access token not found. Please log in.");
          return;
        }

        const username = JSON.parse(localStorage.getItem("currentUser")).name;

        const recordResponse = await fetch(
          `http://127.0.0.1:8000/api/get-record/${encodeURIComponent(username)}/`,
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );

        if (!recordResponse.ok) {
          throw new Error("Ошибка получения текущего рекорда.");
        }

        const recordData = await recordResponse.json();
        const currentRecord = recordData.record || 0;

        if (this.localScore > currentRecord) {
          await fetch(
            `http://127.0.0.1:8000/api/update-record/${encodeURIComponent(username)}/`,
            {
              method: "PUT",
              headers: {
                "Content-Type": "application/json",
                Authorization: `Bearer ${token}`,
              },
              body: JSON.stringify({ record: this.localScore }),
            }
          );
        }
      } catch (error) {
        console.error("Ошибка при работе с рекордом:", error);
      }
    },
    restartGame() {
      this.playClickSound();
      this.$router.push("/game");
    },
    goToMenu() {
      this.playClickSound();
      this.$router.push("/");
    },
    handleKeyPress(event) {
      if (event.key === "Enter") {
        this.playClickSound();
        this.restartGame();
      } else if (event.key === "Escape") {
        this.playClickSound();
        this.goToMenu();
      }
    },
  },
  mounted() {
    const score = this.$route.query.score;
    if (score) {
      this.localScore = Number(score);
    }

    this.$store.dispatch('stopBackgroundMusic');

    this.playWinSound();

    const winSoundDuration = 3000; 
    setTimeout(async () => {
      this.$store.dispatch('playBackgroundMusic');
    }, winSoundDuration);

    this.fetchAndUpdateRecord();

    window.addEventListener("keydown", this.handleKeyPress);
  },
  beforeUnmount() {
    window.removeEventListener("keydown", this.handleKeyPress);
    this.stopWinSound();
    this.$store.dispatch('playBackgroundMusic');
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");

.gameover-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-image: url("../assets/gameover.png");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  font-family: "Press Start 2P", sans-serif;
}

h1 {
  color: white;
  font-size: 40px;
  text-shadow: 0 0 5px black, 0 0 10px gray, 0 0 15px gray;
  margin-top: 80px; 
}

h2 {
  color: white;
  font-size: 20px;
  margin-top: 5px; 
  margin-bottom: 30px; 
  text-shadow: 0 0 5px black, 0 0 10px gray, 0 0 15px gray;
}

#gameover-buttons {
  display: flex;
  flex-direction: column;
  gap: 20px;
  width: 320px;
  margin-top: auto; 
  margin-bottom: 40px; 
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