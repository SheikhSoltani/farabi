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
        }
    },
    methods:{
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
            console.log(this.item);
        }, 100);
    },
}
</script>