<template>
  <div id="settings-container">
    <h1 id="settings-title">Настройки</h1>
    <form @submit.prevent="settings">
      <button class="settings-button" @click="navigateToAudio">Звук</button>
      <!--<button class="settings-button" @click="navigateToAccount">Редактировать профиль</button>-->
    </form>
    <button class="menu-button" @click="navigateToMainMenu">Назад в главное меню</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'UserSettings',
  methods: {
    ...mapActions(['playClickSound']), 
    navigateToAudio() {
      this.playClickSound(); 
      this.$router.push('/audio');
    },
    navigateToAccount() {
      this.playClickSound();
      this.$router.push('/account');
    },
    navigateToMainMenu() {
      this.playClickSound(); 
      this.$router.push('/'); 
    }
  }
}
</script>
  
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");
  
#settings-container {
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
  
#settings-container::after {
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0.6);
z-index: 1;
}
  
#settings-container > * {
position: relative;
z-index: 2;
}
  
#settings-title {
color: white;
font-size: 24px;
font-family: "Press Start 2P", sans-serif;
text-shadow: 0 0 5px black, 0 0 10px gray, 0 0 15px gray;
border-bottom: 2px dashed gray;
padding-bottom: 5px;
margin-bottom: 10px;
text-align: center;
margin-top: -60px;
}
  
form {
display: flex;
flex-direction: column;
align-items: center;
width: 320px;
margin: 0 auto;
}
  
button {
padding: 12px;
font-size: 14px;
font-family: "Press Start 2P", sans-serif;
border: none;
border-radius: 10px;
cursor: pointer;
background-color: #333;
color: white;
text-transform: uppercase;
transition: background-color 0.3s ease, transform 0.2s ease;
margin-top: 20px;
}
  
button:hover {
background-color: #555;
transform: scale(1.05);
}
  
  
.menu-button {
background-color: #444;
color: white;
width: auto;
padding: 10px 20px;
text-align: center;
}
  
.menu-button:hover {
background-color: #666;
}

.settings-button {
background-color: rgba(255, 255, 255, 0.85);
color: #555;
width: auto;
padding: 10px 20px;
text-align: center;
width: 250px;
}
  
.settings-button:hover {
background-color: rgba(255, 255, 255, 255);
}
</style>  