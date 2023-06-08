<template>
    <div>
        <h1>ItemPage</h1>
    </div>
</template>
  
<script>
import {url} from '@/js/config.js';
import axios from 'axios';
export default {
    name: 'ItemPage',
    props: {
        slug: String,
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
            .get(url+"api/item?slug="+this.slug)
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
            this.item =await this.get_items()
            console.log(this.item);
        }, 100);
    },
}
</script>