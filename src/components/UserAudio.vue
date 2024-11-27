<template>
  <div id="audio-container">
    <div class="header">
      <h1 id="audio-title">Звук</h1>
      <img :src="isMuted ? require('@/assets/none.png') : require('@/assets/max.png')" alt="Sound Icon" class="sound-icon" />
    </div>
    <div class="form">
      <button class="max-button" @click="toggleMute">{{ isMuted ? 'Включить звук' : 'Выключить звук' }}</button>
      <input type="range" min="0" max="1" step="0.01" v-model="localVolume" @input="updateVolume">
    </div>
    <button class="menu-button" @click="navigateToSettings">Назад</button>
  </div>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex';

export default {
  data() {
    return {
      localVolume: this.volume, 
    };
  },
  computed: {
    ...mapState(['volume', 'isMuted']),
  },
  methods: {
    ...mapMutations(['setVolume', 'mute', 'unmute']),
    ...mapActions(['playClickSound']), 
    toggleMute() {
      this.playClickSound();
      if (this.isMuted) {
        this.unmute();
      } else {
        this.mute();
      }
    },
    updateVolume() {
      this.setVolume(this.localVolume);
      this.playClickSound();
    },
    navigateToSettings() {
      this.playClickSound(); 
      this.$router.push('/settings'); 
    },
  },
  watch: {
    volume(newVolume) {
      this.localVolume = newVolume;
    },
  },
  mounted() {
    this.localVolume = this.volume; 
    this.$store.dispatch('playBackgroundMusic'); 
  },
}
</script>

  
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");
  
#audio-container {
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
  
#audio-container::after {
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0.6);
z-index: 1;
}
  
#audio-container > * {
position: relative;
z-index: 2;
}

.header {
  display: flex;
  align-items: center;
  justify-content: center;
  
  max-width: 320px; /* Максимальная ширина для заголовка */
}
 

#audio-title {
color: white;
font-size: 24px;
font-family: "Press Start 2P", sans-serif;
text-shadow: 0 0 5px black, 0 0 10px gray, 0 0 15px gray;
border-bottom: 2px dashed gray;
padding-bottom: 5px;
margin-bottom: 10px;
text-align: center;
margin-top: -30px;
}

.sound-icon {
width: 70px;
height: auto; 
margin-left: 10px;
margin-top: -40px;
}
  
.form {
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
width: 320px;
margin: 0 20px;
}
  
  
button {
padding: 12px;
font-size: 14px;
font-family: "Press Start 2P", sans-serif;
color: white;
text-transform: uppercase;
border: none;
border-radius: 10px;
cursor: pointer;
background-color: transparent;
transition: background-color 0.3s ease, transform 0.2s ease;
margin: 30px 0;
}
  
button:hover {
transform: scale(1.05);
}
  
.max-button {
background-color: rgba(255, 255, 255, 0.85);
color: #555;
width: auto;
padding: 10px 20px;
text-align: center;
width: 250px;
}

.menu-button {
background-color: #444;
color: white;
width: auto;
padding: 10px 20px;
text-align: center;
margin-top: 20px;
}
  
.menu-button:hover {
background-color: #666;
}

input[type="range"] {
  width: 100%;
  height: 20px;
  margin: 10px;
  -webkit-appearance: none;
  appearance: none;
  border-radius: 10px;
  background: #ccc;
  outline: none;
}
input[type="range"]::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #666;
  cursor: pointer;
}
input[type="range"]::-moz-range-thumb {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #666;
  cursor: pointer;
}

</style>