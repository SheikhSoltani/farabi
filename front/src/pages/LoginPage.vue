<template>
    <section class="login_page">
      <div>
        <h1>Вход</h1>
          <form ref="form">
            <input id="username" placeholder="Логин" type="text" v-model="username"/>
            <input id="password" placeholder="Пароль" type="password" v-model="password" v-on:keydown.enter="signInButtonPressed">
            <button @click="signInButtonPressed">Вход</button>
          </form>
      </div>
    </section>
  </template>
  <script>
  import axios from 'axios';
  import router from "@/js/router";
import {url} from '@/js/config.js';
  
  
  
  export default {
  
    data() {
      return {
        username:'',
        password:'',
      }
    },
    name: 'LoginPage',
    methods: {
      signInButtonPressed (event) {
        event.preventDefault();
        const data =axios.post(url+'farabi-admin/login', {'username': this.username, 'password': this.password})
        .then(result => result.data);
        console.log(data)
        const printAddress = async () => {
          const a = await data;
          if(a.logged===true){
            await router.push({path: '/admin'})
          }else{
            alert("неправильные данные")
          }
        };
        printAddress();
      
      },
        
    },
    mounted() {/*
      async function logged_or_not() {
        const result = await axios
          .get(url+"farabi-admin/login")
          .then((res) => {
            return res.data;
          })
          .catch(() => {
            console.log("fail");
          });
        if (result === true) {
          console.log(result)
          await router.push({path: '/home'})
        }
        return result
      }
      logged_or_not()*/

    }
  }
  
  </script>