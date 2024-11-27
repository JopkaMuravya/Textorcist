<template>
    <div id="audio-container">
      <h1 id="audio-title">Звук</h1>
      <form @submit.prevent="audio">
          <button class="max-button">
              <img src="@/assets/max.png" alt="Макс" class="button-icon" />
          </button>
          <button class="min-button">
              <img src="@/assets/none.png" alt="Мин" class="button-icon" />
          </button>
          <button class="plus-button">
              <img src="@/assets/plus.png" alt="Плюс" class="button-icon" />
          </button>
          <button class="minus-button">
              <img src="@/assets/minus.png" alt="Минус" class="button-icon" />
          </button>
      </form>
      <button class="menu-button" @click="$router.push('/settings')">Назад</button>
    </div>
</template>
  
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
  
form {
display: flex;
flex-direction: row;
justify-content: center;
align-items: center;
width: 320px;
margin: 0 auto;
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
margin: 30px 10px;
}
  
button:hover {
transform: scale(1.05);
}
  
.max-button {
display: flex;
align-items: center;
border: none;
padding: 0;
cursor: pointer;
background-color: none;
}

.min-button {
display: flex;
align-items: center;
border: none;
padding: 0;
cursor: pointer;
background-color: none;
}

.plus-button {
display: flex;
align-items: center;
border: none;
padding: 0;
cursor: pointer;
background-color: none;
}

.minus-button {
display: flex;
align-items: center;
border: none;
padding: 0;
cursor: pointer;
background-color: none;
}

.button-icon {
width: 80px;
height: auto; 
}
  
.menu-button {
background-color: #444;
color: white;
width: auto;
padding: 10px 20px;
text-align: center;
margin-top: -10px;
}
  
.menu-button:hover {
background-color: #666;
}

</style>  