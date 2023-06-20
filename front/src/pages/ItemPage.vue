<template>
    <div>
        <h1>ItemPage</h1>
        <button @click="addToBasket">добавить в корзину</button>
    </div>
</template>
  
<script>
import axios from 'axios';
import {getConfig} from '@/js/cookie.js';

export default {
    name: 'ItemPage',
    props: {
        slug: String,
        id:Number
    },
    data(){
        return{
          item:[
          ],
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
            .get("/api/item?slug="+this.slug)
            .then((res) => {
                return res.data;
            })
            .catch(() => {
            });
            return result
        },
        addToBasket(event){
            event.preventDefault();
            axios.post('/api/add-to-cart', {'item_id': this.item.item.id}, getConfig('application/json'))
            .then(result => result.data);
        }
    },
    async mounted() {
        setTimeout(async ()=>{
            this.item =await this.get_items()
            this.cart_length =await this.get_cart_length()
            console.log(this.item);
            console.log(this.cart_length);
        }, 100);
    },
}
</script>