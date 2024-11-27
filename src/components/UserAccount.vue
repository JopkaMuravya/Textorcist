<template>
    <div id="account-container">
      <h1 id="account-title">Аккаунт</h1>
      <form @submit.prevent="account">
        <input type="text" v-model="username" placeholder="Имя" required />
        <input type="email" v-model="email" placeholder="Почта" required />
        <button type="submit" @click="$router.push('/settings')">Сохранить изменения</button>
      </form>
      <button class="menu-button" @click="$router.push('/settings')">Назад</button>
    </div>
</template>
  
  
<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");
  
#account-container {
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
  
#account-container::after {
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0.6);
z-index: 1;
}
  
#account-container > * {
position: relative;
z-index: 2;
}
  

  
#account-title {
color: white;
font-size: 24px;
font-family: "Press Start 2P", sans-serif;
text-shadow: 0 0 5px black, 0 0 10px gray, 0 0 15px gray;
border-bottom: 2px dashed gray;
padding-bottom: 5px;
margin-bottom: 20px;
text-align: center;
}
  
form {
display: flex;
flex-direction: column;
align-items: center;
gap: 20px;
width: 320px;
margin: 0 auto;
}
  
input {
padding: 15px;
width: 100%;
border: 2px solid rgba(255, 255, 255, 0.8);
border-radius: 10px;
font-size: 16px;
font-family: "Press Start 2P", sans-serif;
background-color: rgba(255, 255, 255, 0.85);
box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
transition: border-color 0.3s ease, background-color 0.3s ease;
margin-bottom: 5px;
}
  
input:focus {
outline: none;
border-color: #008cff;
background-color: rgba(255, 255, 255, 1);
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
}
  
button:hover {
background-color: #555;
transform: scale(1.05);
}
  
button[type="submit"] {
background-color: #008cff;
color: white;
width: 100%;
margin-bottom: 10px;
}
  
button[type="submit"]:hover {
background-color: #005f99;
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

.info {
padding: 15px;
width: 100%;
border: 2px solid rgba(255, 255, 255, 0.8);
border-radius: 10px;
font-size: 16px;
font-family: "Press Start 2P", sans-serif;
background-color: rgba(255, 255, 255, 0.85);
color: #555;
box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
transition: border-color 0.3s ease, background-color 0.3s ease;
margin-top: -5px;
margin-bottom: 5px;

}
</style>  