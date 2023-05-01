import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    user: null,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
  },
  actions: {
    async register({ commit }, { username, email, password }) {
      try {
        const response = await axios.post('/register', {
          username,
          email,
          password,
        });
        commit('setUser', response.data);
      } catch (error) {
        console.error('Error registering:', error);
      }
    },
    async login({ commit }, { email, password }) {
      try {
        const response = await axios.post('/login', { email, password });
        commit('setUser', response.data);
      } catch (error) {
        console.error('Error logging in:', error);
      }
    },
  },
  modules: {},
});
