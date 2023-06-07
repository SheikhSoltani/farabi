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
        const data =axios.post('farabi-admin/login', {'username': this.username, 'password': this.password})
        .then(result => result.data);
        console.log(data)
        const printAddress = async () => {
          const a = await data;
          if(a.status){
            await router.push({path: '/home'})
          }else{
            alert("неправильные данные")
          }
        };
        printAddress();
      
      },
        
    },
    mounted() {
      async function logged_or_not() {
      const result = await axios
        .get("farabi-admin/login")
        .then((res) => {
          return res.data;
        })
        .catch(() => {
          console.log("fail");
        });
      if (result.status === true) {
        await router.push({path: '/home'})
      }
      return result.status
    }
    logged_or_not()
    }
  }
  
  </script>