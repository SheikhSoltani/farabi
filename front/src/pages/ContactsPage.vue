<template>
    <section class="contacts_content">
      <h1>Контактная информация</h1>
      <div>
        <div class="footer_first">
          <div>
            <img src="" alt="">
            <p>Алматы Рыскулова, 92а</p>
          </div>
          <div>
            <img src="" alt="">
            <p>+7(747)855-10-75 +7(708)807-00-18  +7(701)360-93-93</p>
          </div>
          <div>
            <img src="" alt="">
            <p>+7(727)294-23-30</p>
          </div>
          <div>
            <img src="" alt="">
            <p>buhfarabiklei@mail.ru</p>
          </div>
        </div>
        <div class="footer_middle"><div style="position:relative;overflow:hidden;"><a href="https://yandex.kz/maps/162/almaty/?utm_medium=mapframe&utm_source=maps" style="display: none;color:#eee;font-size:12px;position:absolute;top:0px;">Алматы</a><a href="https://yandex.kz/maps/162/almaty/house/Y08YfwdnQEUAQFppfX52eH5hZg==/?ll=76.907887%2C43.279144&utm_medium=mapframe&utm_source=maps&z=17.15" style="color:#eee;font-size:12px;position:absolute;top:14px;">Проспект Рыскулова, 92А — Яндекс Карты</a><iframe src="https://yandex.kz/map-widget/v1/?ll=76.907887%2C43.279144&mode=search&ol=geo&ouri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg2NzMxMTY5NBJH0prQsNC30LDSm9GB0YLQsNC9LCDQkNC70LzQsNGC0YssINCg0YvRgdKb0rHQu9C-0LIg0LTQsNKj0pPRi9C70YssIDky0JAiCg3Z0JlCFewdLUI%2C&z=17.15" width="764" height="353" frameborder="1" allowfullscreen="true" style="position:relative;border:none;border-radius: 15px;"></iframe></div></div>
      </div>
    </section>
    <footer class="min_footer">
      <img src="@/assets/flogo.png" height="60" width="201"  alt="">
      <p>© 2023-2024</p>
    </footer>
</template>
  
<script>
import axios from '@/js/axios.js';
import router from "@/js/router";

export default {
  name: 'ContactsPage',
  data() {
    return {
      cart_length:0
    }
  },
  methods:{
    search(){
      console.log(this.query)
      router.push({path: '/items',query: { query: this.query}})
    },
    async  get_cart_length() { 
        const result = await axios
        .get("/api/get_length_cart")
        .then((res) => {
            return res.data;
        })
        .catch(() => {
        });
        return result.length
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