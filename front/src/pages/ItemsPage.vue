<template>
    <div>
        <h1>ItemsPage</h1>
    </div>
    <div v-for="item in array.items" v-bind:key="item">
        <div>
            <img :src="this.url+(item.image ? item.image.replace('/', '') : '')" width="150" alt="img">
            <p>{{item.name}}</p>
            <br/>
            <router-link :to="{ name: 'Item', params: { slug: item.slug } }">перейти на страницу товара</router-link>
        </div>
    </div>
</template>
  
<script>
import {url} from '@/js/config.js';
import axios from 'axios';
export default {
    name: 'ItemsPage',
    data() {
      return {
        array:[],
        url:null,
        cart_length:0
      }
    },
    methods:{
        async  get_cart_length() { 
            const result = await axios
            .get("/api/get_length_cart")
            .then((res) => {
                return res.data;
            })
            .catch(() => {
            });
            return result
        },
        async  get_items() { 
            const result = await axios
            .get("api/items")
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
            let arr =await this.get_items()
            this.cart_length =await this.get_cart_length()
            this.array = arr;
            console.log(this.array);
            console.log(this.cart_length);
        }, 100);
    },
}
</script>