import { createRouter, createWebHistory } from 'vue-router'

const Home = () => import('@/components/home.vue')
const Login = () => import('@/components/login.vue')


const routes = [
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path:'',
    name:Home,
    component:Home
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
