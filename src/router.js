import { createRouter, createWebHistory } from 'vue-router'
import UserLogin from './views/UserLogin.vue'
import UserRegister from './views/UserRegister.vue'
import UserProfile from './views/UserProfile.vue'

const routes = [
  { path: '/Userlogin', component: UserLogin },
  { path: '/Userregister', component: UserRegister },
  { path: '/user', component: UserProfile }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
