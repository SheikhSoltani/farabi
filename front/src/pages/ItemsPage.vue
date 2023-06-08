<template>
    <div>
        <h1>ItemsPage</h1>
    </div>
</template>
  
<script>
import {url} from '@/js/config.js';
import axios from 'axios';
export default {
  name: 'ItemsPage',
    methods:{
        async  get_items() { 
            const result = await axios
            .get(url+"api/items")
            .then((res) => {
                return res.data;
            })
            .catch(() => {
            });
            return result
        },
    },
    async mounted() {
        setTimeout(async ()=>{
            let arr =await this.get_items()
            console.log(arr);
            if(arr){
            this.site.push({title:arr.site.title,get_blocks:arr.site.get_blocks})
            }
            this.sortSite=this.site;
            this.order=this.sortSite.length;
        }, 100);
    },
}
</script>