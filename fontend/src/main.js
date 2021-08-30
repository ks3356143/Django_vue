import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.less'



const app = createApp(App)

app.use(store)
app.use(router)
app.use(Antd)
app.mount('#app')


const token = localStorage.getItem("token"); //读取本地token
console.log(token);
if (token) {
  axios.defaults.headers.common["Authorization"] = "Token " + token;
}

//然后在原先的home.vue中新增一句，加一个antd的button
//app.use(Antd)



