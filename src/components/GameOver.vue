<template>
  <div class="gameover-container">
    <h1>Игра окончена!</h1>
    <h2>Счёт: {{ localScore }}</h2>
    <div id="begin">
      <button @click="restartGame">Начать заново</button>
    </div>
    <div id="menu">
      <button @click="goToMenu">Меню</button>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

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
    };
  },
  methods: {
    ...mapActions(["playClickSound"]), 
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

        console.log(`Текущий рекорд: ${currentRecord}, Локальный счёт: ${this.localScore}`);

        if (this.localScore > currentRecord) {
          console.log("Обновляем рекорд...");
          const updateResponse = await fetch(
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

          if (!updateResponse.ok) {
            throw new Error("Ошибка обновления рекорда.");
          }

          console.log("Рекорд успешно обновлен!");
        } else {
          console.log("Рекорд не превышен. Обновление не требуется.");
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
  },
  async mounted() {
    const score = this.$route.query.score;
    if (score) {
      this.localScore = Number(score);
    }

    await this.fetchAndUpdateRecord();
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");
    .gameover-container {
        display: flex;
        flex-direction: column;
        height: 100vh;
        width: 100vw;
        margin: 0;
        padding: 0;
        background-image: url("@/assets/gameover.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        overflow: hidden;
        font-family: "Press Start 2P", sans-serif;
        position: relative;

    }

    h1 {
        position: relative;
        color: azure;
        top: 60px;
    }

    h2 {
        position: relative;
        color: azure;
        top: 60px;
        left: -80px;
    }

    #begin {
        position: absolute;
        bottom: 80px;
        right: 290px;
    }

    #menu {
        position: absolute;
        left: 290px;
        bottom: 80px;
    }

    button {
        padding: 10px 20px;
        font-size: 35px;
        font-weight: 400;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        background-color: rgba(255, 255, 255, 0.8);
        color: #000;
        transition: 0.3s ease;
    }

    button:hover {
      background-color: rgba(255, 255, 255, 1);
    }
</style>