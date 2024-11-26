<template>
  <div id="game-container" :class="{ 'error-shake': isError }">
    <div id="word-container" :class="{ error: isError }">
      <span
        v-for="(letter, index) in currentWord"
        :key="index"
        :class="{ correct: index < typedWord.length }"
      >
        {{ letter }}
      </span>
    </div>
    <div id="character">
      <img src="@/assets/main_character.png" alt="Персонаж" />
    </div>
    <button @click="endGame">Вернуться в меню</button>
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
    };
  },
  methods: {
    endGame() {
      this.$emit("game-ended");
    },
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
          this.generateWord();
        }
      } else {
        this.showError();
        this.typedWord = "";
      }
    },
    showError() {
      this.isError = true;
      setTimeout(() => {
        this.isError = false;
      }, 500);
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

#word-container {
  position: absolute;
  top: 35%;
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
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

#character img {
  width: 120px;
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
</style>