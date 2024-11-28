<template>
    <div id="login-container">
      <div id="login-link-container">
        <p>Нет аккаунта?</p>
        <button @click="navigateToReg">Зарегистрироваться</button>
      </div>
      <h1 id="login-title">Вход</h1>
      <form @submit.prevent="login">
        <input type="text" v-model="username" placeholder="Имя пользователя" required />
        <input type="password" v-model="password" placeholder="Пароль" required />
        <button type="submit" @click="navigateToLogin">Войти</button>
      </form>
      <button @click="navigateToMenu">Назад в главное меню</button>
      <div v-if="message" id="login-message">{{ message }}</div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  import { mapActions } from 'vuex';
  
  export default {
    data() {
      return {
        username: "",
        password: "",
        message: "",
      };
    },
    methods: {
      ...mapActions(['playClickSound']),
      navigateToLogin() {
        this.playClickSound();
      },
      navigateToReg() {
        this.playClickSound();
        this.$router.push('/register');
      },
      navigateToMenu() {
        this.playClickSound();
        this.$router.push('/');
      },
      async login() {
        try {
          const response = await axios.post("http://127.0.0.1:8000/api/token/", {
            username: this.username,
            password: this.password,
          });
  
          localStorage.setItem("accessToken", response.data.access);
          localStorage.setItem("refreshToken", response.data.refresh);
          localStorage.setItem(
            "currentUser",
            JSON.stringify({
              name: this.username,
            })
          );
  
          this.message = "Вход выполнен успешно!";
          this.username = "";
          this.password = "";
  
          this.$router.push("/");
        } catch (error) {
          if (error.response) {
            this.message = "Ошибка входа: " + error.response.data.detail;
          } else if (error.request) {
            this.message = "Ошибка: сервер не ответил";
          } else {
            this.message = "Ошибка: " + error.message;
          }
        }
      }
    },
  };
</script>

  
  <style scoped>
  @import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");
  
  #login-container {
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
    user-select: none;
  }
  
  #login-container::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6);
    z-index: 1;
  }
  
  #login-container > * {
    position: relative;
    z-index: 2;
  }
  
  #login-link-container {
    position: absolute;
    top: 30px; 
    right: 30px;
    display: flex;
    align-items: center;
    gap: 8px; 
  }
  
  #login-link-container p {
    color: white;
    font-size: 12px;
    font-family: "Press Start 2P", sans-serif;
    margin: 0;
  }
  
  #login-link-container button {
    padding: 4px 12px; 
    font-size: 10px; 
    font-family: "Press Start 2P", sans-serif;
    border: 2px solid rgba(255, 165, 0, 0.8);
    border-radius: 8px;
    background-color: rgba(255, 165, 0, 0.85);
    color: black;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  #login-link-container button:hover {
    background-color: rgba(255, 140, 0, 0.9);
  }
  
  #login-title {
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
  
  button:not([type="submit"]) {
    background-color: #444;
    color: white;
    width: auto;
    padding: 10px 20px;
    text-align: center;
  }
  
  button:not([type="submit"]):hover {
    background-color: #666;
  }
  
  #login-message {
    margin-top: 10px;
    color: white;
    text-shadow: 0px 1px 3px rgba(0, 0, 0, 0.7);
    font-size: 12px;
    font-family: "Press Start 2P", sans-serif;
    text-align: center;
  }
  </style>  