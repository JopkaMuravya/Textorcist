<template>
    <div id="leaderboard-container">
      <h1 id="leaderboard-title">Рейтинг игроков</h1>
      <table>
        <thead>
          <tr>
            <th>Место</th>
            <th>Имя игрока</th>
            <th>Рекорд</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(player, index) in players" :key="index">
            <td>{{ index + 1 }}</td>
            <td>{{ player.name }}</td>
            <td>{{ player.record }}</td>
          </tr>
        </tbody>
      </table>
      <button @click="$router.push('/')">Назад в главное меню</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        players: [], 
      };
    },
    async created() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/leaderboard/');
        this.players = response.data; 
      } catch (error) {
        console.error('Ошибка загрузки данных рейтинга:', error);
      }
    },
  };
  </script>
  
  <style scoped>
  @import url("https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap");
  
  #leaderboard-container {
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
  
  #leaderboard-container::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.6);
    z-index: 1;
  }
  
  #leaderboard-container > * {
    position: relative;
    z-index: 2;
  }
  
  #leaderboard-title {
    color: white;
    font-size: 24px;
    font-family: "Press Start 2P", sans-serif;
    text-shadow: 0 0 5px black, 0 0 10px gray, 0 0 15px gray;
    border-bottom: 2px dashed gray;
    padding-bottom: 5px;
    margin-bottom: 10px;
    text-align: center;
  }
  
  table {
    width: 80%;
    border-collapse: collapse;
    margin: 20px 0;
    font-family: "Press Start 2P", sans-serif;
    background-color: rgba(255, 255, 255, 0.85);
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  }
  
  thead {
    background-color: rgba(0, 0, 0, 0.85);
    color: white;
  }
  
  th, td {
    padding: 15px;
    text-align: center;
    border-bottom: 1px solid rgba(0, 0, 0, 0.2);
  }
  
  tbody tr:nth-child(even) {
    background-color: rgba(0, 0, 0, 0.05);
  }
  
  tbody tr:hover {
    background-color: rgba(0, 0, 0, 0.1);
  }
  
  button {
    margin-top: 20px;
    padding: 12px;
    font-size: 14px;
    font-family: "Press Start 2P", sans-serif;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    background-color: #008cff;
    color: white;
    text-transform: uppercase;
    transition: background-color 0.3s ease, transform 0.2s ease;
  }
  
  button:hover {
    background-color: #005f99;
    transform: scale(1.05);
  }
  </style>  