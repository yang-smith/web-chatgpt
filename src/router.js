import { createRouter, createWebHistory } from 'vue-router'
import UserLogin from './views/UserLogin.vue'
import UserRegister from './views/UserRegister.vue'
import UserProfile from './views/UserProfile.vue'
import UserChat from './views/UserChat.vue'
import UserTopup from './views/UserTopup'

const routes = [
  { path: '/Userlogin', component: UserLogin },
  { path: '/Userregister', component: UserRegister },
  { path: '/user', component: UserProfile },
  { path: '/UserChat', component: UserChat },
  { path: '/UserTopup', component: UserTopup }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
