<template>
    <div>
        <h1>BasketPage</h1>

        <button @click="showElement">купить</button>
        <div v-show="hidden">
            <div class="input_block">
                <span>name</span>
                <input v-model="name" type="text">
            </div>
            <div class="input_block">
                <span>email</span>
                <input v-model="email" type="text">
            </div>
            <div class="input_block">
                <span>phone</span>
                <input v-model="phone" type="text" v-mask="'+7(###)###-##-##'">
            </div>
            <button @click="send">отправить</button>
        </div>
    </div>
</template>
  <style>.input_block{
    position: relative;
}
.input_block>input{
    border: none;
    font-size: 14px;
    line-height: 20px;
    font-weight: 400;
    background: transparent;
    color: #2e2e2e;
    padding: 26px 12px 5px;
    min-width: 100%;
    max-width: 100%;
    min-height: 51px;
    resize: none;box-sizing: border-box;
    background: #fafafa;
    overflow:visible;
    box-sizing: border-box;
    margin-bottom: 5px;
}
.input_block>span{
    
    font-size: 12px;
    line-height: 16px;
    transform: translateY(0px);
    position: absolute;
    left: 12px;
    top: 10px;
}</style>
<script>


import {url} from '@/js/config.js';
//import {getConfig} from '@/js/cookie.js';
import axios from 'axios';



export default {
    name: 'BasketPage',
    data() {
      return {
        hidden:false,
        email:'',
        name:'',
        phone:''
      }
    },
    methods:{
        send(){
            axios.post(url+'api/create-order',{'email':this.email,'phone':this.phone,'name':this.name} )
        },
        showElement(){
            this.hidden=!this.hidden;
        },
        
    },
}
</script>