import { createStore } from 'vuex';
import axios from 'axios';
import router from './router'; // 导入了你的路由器

export default createStore({
    state: {
      user: null,
      isLoggedIn: false,
      isRegistered: false,  // 新增的状态
    },
    mutations: {
      setUser(state, user) {
        state.user = user;
        state.isLoggedIn = !!user;
      },
      setRegistered(state, status) { // 新增的 mutation
        state.isRegistered = status;
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
          commit('setRegistered', true); // 在注册成功后设置 isRegistered 为 true
          router.push('/Userlogin'); // 在注册成功后跳转到登录页面
        });
      }, 
    async login({ commit }, { email, password }) {
      return axios.post('http://49.234.79.245:1200/api/login', { email, password }).then(response => {
        commit('setUser', response.data);
      });
    },
  },
  modules: {},
});
