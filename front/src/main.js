import { createApp } from 'vue'
import App from './App.vue'
import router from "@/js/router";
import axios from 'axios';

const app=createApp(App)
app.use(router)
app.use(axios,{baseUrl:"https://api.idealf.kz/"})
app.mount('#app')


import VueTheMask from 'vue-the-mask'
app.use(VueTheMask)
