import { createApp } from 'vue'
import App from '@/App.vue'
import router from './router'
import store from './store'
import axios from 'axios'


const app = createApp(App).use(store).use(router).mount('#app')

const token = localStorage.getItem("token"); //读取本地token
console.log(token);
if (token) {
  axios.defaults.headers.common["Authorization"] = "Token " + token;
}


