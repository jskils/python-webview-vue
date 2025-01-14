import {createApp} from 'vue'
import App from './App.vue';
import router from './router';
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/reset.css';
import './assets/tailwind.css'


const app = createApp(App);

app.use(Antd)
app.use(router)

app.mount('#app');