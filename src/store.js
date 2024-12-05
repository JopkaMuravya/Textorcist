import { createStore } from 'vuex';
import sound_click from 'assets/click-sound.mp3'
import sound_background from 'assets/background-music.mp3'

const store = createStore({
  state: {
    volume: 0.5, 
    isMuted: false, 
    backgroundMusic: null, 
    clickSound: new Audio(sound_click), 
  },
  mutations: {
    setVolume(state, volume) {
      state.volume = volume;
      if (state.backgroundMusic) {
        state.backgroundMusic.volume = state.isMuted ? 0 : volume;
      }
      state.clickSound.volume = state.isMuted ? 0 : volume;
    },
    mute(state) {
      state.isMuted = true;
      if (state.backgroundMusic) {
        state.backgroundMusic.volume = 0;
      }
      state.clickSound.volume = 0; 
    },
    unmute(state) {
      state.isMuted = false;
      if (state.backgroundMusic) {
        state.backgroundMusic.volume = state.volume; 
      }
      state.clickSound.volume = state.volume;
    },
    setBackgroundMusic(state, music) {
      state.backgroundMusic = music;
      state.backgroundMusic.volume = state.isMuted ? 0 : state.volume; 
    }
  },
  actions: {
    playBackgroundMusic({ state, commit }) {
      if (!state.backgroundMusic) {
        const music = new Audio(sound_background); 
        music.loop = true; 
        commit('setBackgroundMusic', music);
      }
      state.backgroundMusic.volume = state.isMuted ? 0 : state.volume; 
      state.backgroundMusic.play(); 
    },
    stopBackgroundMusic({ state }) {
      if (state.backgroundMusic) {
        state.backgroundMusic.pause(); 
        state.backgroundMusic.currentTime = 0; 
      }
    },
    playClickSound({ state }) {
      state.clickSound.currentTime = 0;
      state.clickSound.play();
    }
  }
});

export default store;