<template>
    <div class="game">
      <h2>Игра началась!</h2>
      <button @click="endGame">Вернуться в меню</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'GameComponent',
    methods: {
      endGame() {
        this.$emit('game-ended'); // Это событие можно использовать для возврата в меню
      }
    }
  }
  </script>
  
  <style scoped>
  .game {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
  }
  </style>