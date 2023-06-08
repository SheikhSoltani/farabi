<template>
    <div>
        <h1>BasketPage</h1>
    </div>
</template>
  
<script>


import {url} from '@/js/config.js';
//import {getConfig} from '@/js/cookie.js';
import axios from 'axios';



export default {
    name: 'BasketPage',
    methods:{
        /*
        deleteItem(id){
            axios.post(
                url+'api/delete_block', { 'block_id':id }, getConfig('application/json')
            ).then(data =>{
                if(data.data.status){
                    let child = document.getElementById(id);
                    child.parentElement.remove();
                }
                for(let i=0;i<this.sortSite.length;i++){
                    this.sortSite.splice(i, 1);
                }
                        
                let arr = this.get_items()
                arr.then((data2)=>{
                this.site.splice(0);
                    if(data2){
                        this.site.push({title:data2.site.title,get_blocks:data2.site.get_blocks})
                    }
                this.sortSite=test(this.site);
                this.order=this.sortSite.length;
                })
            })
        },*/
        async  get_items() { 
            const result = await axios
            .get(url+"api/cart")
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