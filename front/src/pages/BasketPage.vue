<template>
    <header>
      <div class="first">
        <router-link :to="{ name: 'Main' }"><img src="@/assets/flogo.png" height="67" width="229" alt="logo"></router-link>
        <router-link :to="{ name: 'Items' }"><div><span></span><span></span><span></span><span></span></div><p>Каталог товаров</p></router-link>
      </div>
      <div class="middle">
        <input type="text" placeholder="Поиск по сайту" v-model="this.query" v-on:keydown.enter="search">
        <router-link :to="{ name: 'Contacts' }"><img src="@/assets/phone.png" width="15" height="15" alt=""><p>КОНТАКТЫ</p></router-link>
      </div>
      <div class="last">
        <p>{{this.array.items.length}}</p>
        <router-link :to="{ name: 'Basket' }"><img src="@/assets/cart.png" width="30" height="30" alt=""></router-link>
      </div>
    </header>
    <section class="cart_content">
        <div class="cart_content_header">
            <h1>Оформление заказа</h1>
            <img src="@/assets/flogo.png" height="60" width="201"  alt="">
        </div>
        <button @click="deleteAllItems">очистить корзину</button>
        <div class="cart_content_body">
            <div class="cart_content_item">
                <span>{{this.array.items.length}}</span>
                <div v-for="item in array.items" v-bind:key="item" :id="item.id"  class="basket_item">
                    <img :src="this.url+(item.image ? item.image.replace('/', '') : '')" width="153" height="168" alt="">
                    <div>
                        <p>{{item.name}}</p>
                        <div>
                            <p>Количество</p>
                            <input type="text" name="" id="">
                            <span>kg</span>
                            <button @click="deliteItem(item.id)">убать товар из корзины</button>
                        </div>
                    </div>
                </div>
            </div>
            <div>
                <p>Товары:{{this.array.items.length}} шт.</p>
                <input type="text" placeholder="Ваше имя...">
                <input type="text" placeholder="+7(xxx)xxx-xx-xx">
                <input type="text" placeholder="Способ получения...">
                <textarea name="" id="" cols="30" rows="10" placeholder="Комментарий к заказу..."></textarea>
                <button>Подтвердить заказ</button>
            </div>
        </div>

    </section>
    <footer class="min_footer">
      <img src="@/assets/flogo.png" height="60" width="201"  alt="">
      <p>© 2023-2024</p>
    </footer>



    <!-- <div>
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
        <div class="basket_item" :id="item.id">
            <img :src="this.url+(item.image ? item.image.replace('/', '') : '')" width="150" alt="img">
            <p>{{item.name}}</p>
            <button @click="deliteItem(item.id)">убать товар из корзины</button>
            <br/>
        </div>
    </div> -->
</template>
  <style>

  </style>
<script>

import {url} from '@/js/config.js';
import axios from 'axios';
  import {getConfig} from '@/js/cookie.js';
import router from "@/js/router";



export default {
    name: 'BasketPage',
    data() {
      return {
        hidden:false,
        email:'',
        name:'',
        phone:'',
        array:{items:{}},
      }
    },
    methods:{
        search(){
            console.log(this.query)
            router.push({path: '/items',query: { query: this.query}})
        },
        send(){
            axios.post('api/create-order',{'email':this.email,'phone':this.phone,'name':this.name}, getConfig('application/json') )
        },
        deliteItem(id){
            axios.post(
                  'api/delete-from-cart', { 'item_id':id }, getConfig('application/json')
              ).then(data =>{
                if(data.data.result){
                    const index = this.array.items.findIndex(item => item.id === id);
                    if (index !== -1) {
                        this.array.items.splice(index, 1);
                    }
                }
              })
        },
        deleteAllItems(){
            axios.post(
                  'api/flush-cart',{}, getConfig('application/json')
              ).then(data =>{
                if(data.data.result){
                    this.array.items = [];
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
              console.log(res)
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