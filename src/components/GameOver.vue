<template>
  <div class="gameover-container">
    <h1>Игра окончена!</h1>
    <h2>Счёт: {{ localScore }}</h2>
    <div id="begin">
      <button @click="$router.push('/game')">Начать заново</button>
    </div>
    <div id="menu">
      <button @click="$router.push('/')">Меню</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "GameOver",
  props: {
    score: {
      type: Number,
      default: 0 
    }
  },
  data() {
    return {
      localScore: this.score
    };
  },
  mounted() {
    const score = this.$route.query.score;
    //console.log('Received score:', score);

    if (score) {
      this.localScore = Number(score); 
    }
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