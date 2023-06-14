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
        const data =axios.post('farabi-admin/login', {'username': this.username, 'password': this.password}, {withCredentials: true})
        .then(result => result.data);
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
    mounted() {
      
        async function logged_or_not() {
            const result = await axios
            .get("farabi-admin/logged")
            .then((res) => {
            return res.data;
            })
            .catch(() => {
            console.log("fail");
            });
            if (result.result === true) {
                await router.push({path: '/admin'})
            }
            return result.result
        }
        logged_or_not()

    }
  }
  
  </script>