<template>
    <div>
        <h1>ItemsPage</h1>
    </div>
    <div v-for="item in array.items" v-bind:key="item">
        <div>
            <img :src="this.url+(item.image ? item.image.replace('/', '') : '')" width="150" alt="img">
            <p>{{item.name}}</p>
            <br/>
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
      }
    },
    methods:{
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
            this.array = arr;
            console.log(this.array);
        }, 100);
    },
}
</script>