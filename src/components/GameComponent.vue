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
        <button @click="goToMenu">Вернуться в меню</button>
        <div id="score">Счёт: {{ score }}</div>
        <div v-for="(enemy, index) in enemies" :key="index" class="enemy" :style="{ left: enemy.x + 'px', top: enemy.y + 'px' }">
          <img :src="enemyImage" alt="Враг" />
        </div>

        <div v-if="isPaused" class="modal">
            <div class="modal-content">
                <h2>Пауза</h2>
                <button @click="togglePause">Продолжить</button>
                <button @click="$router.push('/')">Выход</button>
            </div>
        </div>

    </div>
</template>

<script>
import { mapActions } from 'vuex';
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

      // enemies
      enemies: [],
      enemyImage: require('@/assets/book.png'),
      enemySpeed: 1,

      // pause
      isPaused: false
    };
  },
  methods: {
    ...mapActions(['playClickSound']),
    goToMenu() {
      this.playClickSound(); 
      this.$router.push('/');
    },
    togglePause() {
      this.isPaused = !this.isPaused;
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

      if (input === 'Escape'){
          this.togglePause();
      }      
      if (!this.isPaused && input != 'Alt' && input != 'Shift' && input != 'Escape'){
        if (input === this.currentWord[currentLetterIndex]) {
          this.typedWord += input;
          if (this.typedWord === this.currentWord.join("")) {
            this.score += 10
            this.enemies.splice(0, 1)
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
      }
    },
    showError() {
      this.isError = true;
      setTimeout(() => {
        this.isError = false;
      }, 500);

      // const lifeIndex = this.hearts.findIndex(heart => !heart.broken);
      // if (lifeIndex !== -1) {

      //   this.hearts[lifeIndex].broken = true;

      //   setTimeout(() => {
      //     this.hearts.splice(lifeIndex, 1);
      //     if (this.hearts.length === 0) {
      //       const scoree = this.score;
      //       //console.log('Game Over! Score:', scoree);
      //       this.$router.push({ name: 'GameOver', query: { score: scoree } });
      //     }

      //   }, 500);

      // }
    },
    // enemies
    generateEnemy() {
      const side = Math.floor(Math.random() * 4);
      let x, y, speed;

      switch (side) {
        case 0: // Сверху
          x = window.innerWidth / 2 - 100;
          y = -30;
          break;
        case 1: // Снизу
          x = window.innerWidth / 2 - 100;
          y = window.innerHeight + 15;
          break;
        case 2: // Слева
          x = -100;
          y = window.innerHeight / 2;
          break;
        case 3: // Справа
          x = window.innerWidth - 50;
          y = window.innerHeight / 2;
          break;
      }
      speed = this.enemySpeed + this.score / 100;
      if (!this.isPaused){
        this.enemies.push({x, y, side, speed});
      }
      setTimeout(() => {this.generateEnemy();}, 2000 - this.score);
    },
    updateEnemies() {
      this.enemies.forEach((enemy, index) => {

        switch (enemy.side) {
          case 0:
            enemy.y += enemy.speed;
            if (enemy.y % 100 === 0) {
              enemy.x += 3;
            }
            if (enemy.y % 100 === 50) {
              enemy.x -= 3;
            }
            break;
          case 1:
            enemy.y -= enemy.speed;
            if (enemy.y % 100 === 0) {
              enemy.x += 3;
            }
            if (enemy.y % 100 === 50) {
              enemy.x -= 3;
            }
            break;
          case 2:
            enemy.x += enemy.speed;
            if (enemy.x % 100 === 0) {
              enemy.y += 3;
            }
            if (enemy.x % 100 === 50) {
              enemy.y -= 3;
            }
            break;
          case 3:
            enemy.x -= enemy.speed;
            if (enemy.x % 100 === 0) {
              enemy.y += 3;
            }
            if (enemy.x % 100 === 50) {
              enemy.y -= 3;
            }
            break;
        }

        if (enemy.x >= window.innerWidth / 2 - 120 && enemy.x <= window.innerWidth / 2 - 75 && enemy.y >= window.innerHeight / 2 - 50 && enemy.y <= window.innerHeight / 2 + 50) {
          this.enemies.splice(index, 1);
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
        }
      });
    },
    gameLoop() {
      if (!this.isPaused){
        this.updateEnemies();
      }
      requestAnimationFrame(this.gameLoop);
    },
  },
  mounted() {
    this.generateWord();
    window.addEventListener("keydown", this.handleInput);
    this.generateEnemy();
    this.gameLoop();

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
  top: 47%;
  margin-left: 25px;
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
  margin-top: 220px;
  margin-left: 20px;
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

.enemy {
  position:absolute;
  width: 50px;
  height: auto;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
}

.modal-content {
  font-family: "Press Start 2P", sans-serif;
  padding: 325px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  text-align: center;
  color: white;
}

.modal-content button {
  margin: 0 10px;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #751c6991;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s;
  font-family: "Press Start 2P", sans-serif;;
}
</style>