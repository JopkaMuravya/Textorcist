<template>
    <div>
      <h1>Регистрация</h1>
      <form @submit.prevent="register">
        <input type="text" v-model="username" placeholder="Имя пользователя" required />
        <input type="email" v-model="email" placeholder="Email" required />
        <input type="password" v-model="password" placeholder="Пароль" required />
        <button type="submit">Зарегистрироваться</button>
      </form>
      <button @click="$router.push('/')">Назад в главное меню</button>
      <div v-if="message">{{ message }}</div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        email: '',
        password: '',
        message: ''
      };
    },
    methods: {
      async register() {
        try {
          await axios.post('http://127.0.0.1:8000/api/users/', {
            username: this.username,
            email: this.email,
            password: this.password
          });
          this.message = 'Регистрация успешна!';
          // Очистка полей формы
          this.username = '';
          this.email = '';
          this.password = '';
        } catch (error) {
          if (error.response) {
            this.message = 'Ошибка регистрации: ' + error.response.data;
          } else if (error.request) {
            this.message = 'Ошибка: сервер не ответил';
          } else {
            this.message = 'Ошибка: ' + error.message;
          }
          
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Добавьте стили по желанию */
  </style>