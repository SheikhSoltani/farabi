<template>
    <div>
        <h1>ContactsPage</h1>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
  name: 'ContactsPage',
  data() {
    return {
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
  },
  async mounted() {
      setTimeout(async ()=>{
          this.cart_length =await this.get_cart_length()
            console.log(this.cart_length);
      }, 100);
  },
}
</script>