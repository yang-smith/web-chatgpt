import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
// import store from './store'  // Uncomment this line if you're using Vuex

createApp(App)
  .use(router)
  // .use(store)  // Uncomment this line if you're using Vuex
  .mount('#app')