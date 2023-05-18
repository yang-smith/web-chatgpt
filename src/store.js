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
      return axios.post('http://127.0.0.1:1200/api/register', {
        username,
        email,
        password,
      }).then(response => {
        commit('setUser', response.data);
      });
    },
    async login({ commit }, { email, password }) {
      return axios.post('http://127.0.0.1:1200/api/login', { email, password }).then(response => {
        commit('setUser', response.data);
      });
    },
  },
  modules: {},
});
