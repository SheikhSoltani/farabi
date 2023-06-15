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
        <button @click="deleteAllItems">очистить корзину</button>
    </div>
    <div v-for="item in array.items" v-bind:key="item">
        <div>
            <img :src="this.url+(item.image ? item.image.replace('/', '') : '')" width="150" alt="img">
            <p>{{item.name}}</p>
            <br/>
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
import axios from 'axios';
  import {getConfig} from '@/js/cookie.js';



export default {
    name: 'BasketPage',
    data() {
      return {
        hidden:false,
        email:'',
        name:'',
        phone:'',
        array:[],
      }
    },
    methods:{
        send(){
            axios.post('api/create-order',{'email':this.email,'phone':this.phone,'name':this.name} )
        },
        deliteItem(id){
            axios.post(
                  'api/delete-from-cart', { 'item_id':id }, getConfig('application/json')
              ).then(data =>{
                if(data.data.status){
                  let child = document.getElementById(id);
                  child.parentElement.remove();
                }
              })
        },
        deleteAllItems(){
            axios.post(
                  'api/flush-cart', getConfig('application/json')
              ).then(data =>{
                if(data.data.status){
                  let child = document.getElementById('');
                  child.parentElement.remove();
                }
              })
        },
        showElement(){
            this.hidden=!this.hidden;
        },
        async  get_basket_items() { 
            const result = await axios
            .get("api/get-cart-items")
            .then((res) => {
                return res.data;
            })
            .catch(() => {
            });
            return result
        },
    },
    async mounted() {
        this.url=url;
        setTimeout(async ()=>{
            let arr =await this.get_basket_items()
            this.array = arr;
            console.log(this.array);
        }, 100);
    },
}
</script>