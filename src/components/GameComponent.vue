<template>
    <div id="game-container" :class="{ 'error-shake': isError }">
        <div id="live-container">
            <img v-for="(heart, index) in hearts.slice().reverse()"
                 :key="index"
                 :src="heart.broken ? deadheartImage : liveheartImage"
                 :class="{ deadheart: heart.broken }"
                 class="liveheart" />
        </div>
        <div id="word-container" :class="{ error: isError }">
            <span v-for="(letter, index) in currentWord"
                  :key="index"
                  :class="{ correct: index < typedWord.length }">
                {{ letter }}
            </span>
        </div>
        <div id="character">
            <img src="@/assets/main_character.png" alt="Персонаж" />
        </div>
        <button @click="$router.push('/')">Вернуться в меню</button>
        <div id="score">Счёт: {{ score }}</div>

    </div>
</template>

<script>
export default {
  name: "GameComponent",
  data() {
    return {
      words: [
        "арбуз", "банан", "яблоко", "груша", "персик", "пицца", "суши", "пельмени",
        "кот", "собака", "волк", "тигр", "лев", "жираф", "слон", "попугай",
        "река", "гора", "лес", "луна", "солнце", "ветер", "дождь", "облако",
        "поезд", "самолет", "машина", "трамвай", "катер", "велосипед",
        "учитель", "врач", "повар", "строитель", "полицейский", "пожарный",
        "компьютер", "телефон", "стол", "книга", "лампа", "часы", "ручка",
        "игра", "танец", "звезда", "мечта", "праздник", "работа", "дружба",
      ],
      currentWord: [],
      typedWord: "",
      isError: false,
      score: 0,
      hearts: [ { broken: false }, { broken: false }, { broken: false } ],
      liveheartImage: require('@/assets/live.png'),
      deadheartImage: require('@/assets/dead.png'),
    };
  },
  methods: {
    generateWord() {
      const randomIndex = Math.floor(Math.random() * this.words.length);
      this.currentWord = this.words[randomIndex].split("");
      this.typedWord = "";
      this.isError = false;
    },
    handleInput(event) {
      const input = event.key;
      const currentLetterIndex = this.typedWord.length;

      if (input === this.currentWord[currentLetterIndex]) {
        this.typedWord += input;
        if (this.typedWord === this.currentWord.join("")) {
          this.score += 10
          this.generateWord();
        }
      } else {
        //this.showError();
        this.typedWord = "";
        if (this.score > 0) {
          this.score -= 5;
        }
        this.showError();
      }
    },
    showError() {
      this.isError = true;
      setTimeout(() => {
        this.isError = false;
      }, 500);

      const lifeIndex = this.hearts.findIndex(heart => !heart.broken);
      if (lifeIndex !== -1) {

        this.hearts[lifeIndex].broken = true;

        setTimeout(() => {
          this.hearts.splice(lifeIndex, 1);
          if (this.hearts.length === 0) {
            const scoree = this.score;
            //console.log('Game Over! Score:', scoree);
            this.$router.push({ name: 'GameOver', query: { score: scoree } });
          }

        }, 500);

      }
    },
  },
  mounted() {
    this.generateWord();
    window.addEventListener("keydown", this.handleInput);
  },
  beforeUnmount() {
    window.removeEventListener("keydown", this.handleInput);
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");

#game-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  width: 100vw;
  margin: 0;
  padding: 0;
  background-image: url("@/assets/background.png");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  overflow: hidden;
  font-family: "Press Start 2P", sans-serif;
  position: relative;
}

#game-container.error-shake {
  animation: shake 0.5s;
}

@keyframes shake {
  0% {
    transform: translateX(-5px);
  }
  25% {
    transform: translateX(5px);
  }
  50% {
    transform: translateX(-5px);
  }
  75% {
    transform: translateX(5px);
  }
  100% {
    transform: translateX(0);
  }
}

#live-container {
    position: absolute;
    display: flex;
    left: 7px;
    top: 10px;
}

.liveheart {
    width: 40px;
    height: auto;
    margin-right: 3px;
}

.deadheart {
    animation: dying 0.5s forwards; 
}

@keyframes dying {
  0% {
    transform: scale(0.5);
    opacity: 0;
  } 
}

#word-container {
  position: absolute;
  top: 38%;
  font-size: 15px;
  line-height: 1;
  font-weight: 400;
  color: white;
  text-shadow: 0 2px 5px rgba(0, 0, 0, 0.7);
  display: flex;
  gap: 5px;
  justify-content: center;
}

#word-container.error {
  color: red;
  animation: flash 0.5s;
}

@keyframes flash {
  0% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
  100% {
    opacity: 1;
  }
}

#word-container span.correct {
  color: green;
}

#character {
  margin-top: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

#character img {
  width: 170px;
  height: auto;
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 16px;
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

#score {
    position: absolute;
    right: 30px;
    bottom: 25px;
    background-color: black;
    color: azure;
    padding: 5px 10px 5px 10px;
    border-radius: 5px;
}
</style>