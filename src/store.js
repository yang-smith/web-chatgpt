import { createStore } from 'vuex';
import axios from 'axios';
import router from './router'; 

export default createStore({
  state: {
    user: null,
    isLoggedIn: false,
    isRegistered: false,
    chatHistory: [],
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
      state.isLoggedIn = !!user;
    },
    setRegistered(state, status) {
      state.isRegistered = status;
    },
    addChatMessage(state, { question, answer }) {
        state.chatHistory.push({ question, answer });
      },
      updateChatMessage(state, { index, answer }) {
        state.chatHistory[index].answer = answer;
      },
  },
  actions: {
    async register({ commit }, { username, email, password }) {
      return axios.post('http://49.234.79.245:1200/api/register', {
        username,
        email,
        password,
      }).then(response => {
        commit('setUser', response.data);
        commit('setRegistered', true); 
        router.push('/Userlogin'); 
      });
    },
    async login({ commit }, { email, password }) {
      return axios.post('http://49.234.79.245:1200/api/login', { email, password }).then(response => {
        commit('setUser', response.data);
      });
    },
    async updateBalance({ state }, new_balance) {
      return axios.post('http://49.234.79.245:1200/api/update_balance', {
          token: state.user.token,
          new_balance
      }).then(() => {
          state.user.balance = new_balance;
      }).catch(error => {
          console.error('Update balance failed: ', error);
      });
    },
  
    async submitQuestion({ commit, state, dispatch }, question) {
        commit('addChatMessage', { question, answer: null });
        const apiUrl = "http://38.60.204.205:1200/api/chart";
        return axios.get(apiUrl, { params: { content: question } })
        .then(response => {
          state.chatHistory[state.chatHistory.length - 1].answer = response.data.message || "";
          return dispatch('updateBalance', state.user.balance - 0.01);
        })
        .then(() => {
            state.user.balance = state.user.balance - 0.01;
        })
        .catch(() => {
          state.chatHistory[state.chatHistory.length - 1].answer = "请求出错！";
        });
      },
  },
  getters:{
    lastAnswerIsNull: (state) => {
      if(state.chatHistory.length > 0) {
        const lastMessage = state.chatHistory[state.chatHistory.length - 1];
        return lastMessage.answer === null;
      }
      // If chatHistory is empty, we return null as well
      return null;
    },
  },
  modules: {},
});
