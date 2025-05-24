<template>
  <div class="main_page">
    <section>
      <section class="first_section">
        <div>
          <img src="@/assets/main_banner.png" alt="">
        </div>
        <div>
          <img src="@/assets/main_banner_2.png" alt="">
        </div>
      </section>
      <div>
        <div>
          <img src="@/assets/heart.svg" alt="">
          <h1>БЕЗОПАСНОСТЬ</h1>
          <p>Мы ответственно относимся к изготовлению продукции, чтобы она была безопасна при работе и после.</p>
        </div>
        <img src="@/assets/polygon_1.svg" alt="">
        <div>
          <img src="@/assets/quality.svg" alt="">
          <h1>КАЧЕСТВО</h1>
          <p>Мы стремимся к высочайшему качеству, чтобы наша продукция соответствовала самым строгим стандартам.</p>
        </div>
        <img src="@/assets/polygon_1.svg" alt="">
        <div>
          <img src="@/assets/arms.svg" alt="">
          <h1>СОТРУДНИЧЕСТВО</h1>
          <p>Мы ценим взаимовыгодное сотрудничество и строим прочные партнерские отношения, направленные на совместный успех и развитие.</p>
        </div>
      </div>
      <section class="second_section">
        <h1>ПОПУЛЯРНЫЕ ТОВАРЫ</h1>
        <div>
          <div v-for="item in this.array.items" :key="item.id">
            <img :src="this.url2+item.image" alt="">
            <h1>{{item.name}}</h1>
            <button @click="addToBasket(item.id)">в корзину</button>
            <router-link :to="{ name: 'Item', params: { slug: item.slug } }">страница товара</router-link>
          </div>
          <!-- <div>
            <img :src="this.array.items[1].image" alt="">
            <h1>{{this.array.items[1].name}}</h1>
            <button @click="addToBasket(this.array.items[1].id)">в корзину</button>
            <router-link :to="{ name: 'Item', params: { slug: this.array.items[1].slug } }">страница товара</router-link>
          </div>
          <div>
            <img :src="this.array.items[2].image" alt="">
            <h1>{{this.array.items[2].name}}</h1>
            <button @click="addToBasket(this.array.items[2].id)">в корзину</button>
            <router-link :to="{ name: 'Item', params: { slug: this.array.items[2].slug } }">страница товара</router-link>
          </div>
          <div>
            <img :src="this.array.items[3].image" alt="">
            <h1>{{this.array.items[3].name}}</h1>
            <button @click="addToBasket(this.array.items[3].id)">в корзину</button>
            <router-link :to="{ name: 'Item', params: { slug: this.array.items[3].slug } }">страница товара</router-link>
          </div> -->
        </div>
        <router-link :to="{ name: 'Items' }">СМОТРЕТЬ ЕЩЕ</router-link>
      </section>
    </section>
    <footer>
      <div class="footer_first">
        <h1>Контакты</h1>
        <div>
          <img src="" alt="">
          <p>Алматы Рыскулова, 92а</p>
        </div>
        <div>
          <img src="" alt="">
          <p>+7(747)855-10-75 +7(708)807-00-18 +7(701)360-93-93</p>
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
      <div class="footer_middle"><div style="position:relative;overflow:hidden;"><a href="https://yandex.kz/maps/162/almaty/?utm_medium=mapframe&utm_source=maps" style="display: none;color:#eee;font-size:12px;position:absolute;top:0px;">Алматы</a><a href="https://yandex.kz/maps/162/almaty/house/Y08YfwdnQEUAQFppfX52eH5hZg==/?ll=76.907887%2C43.279144&utm_medium=mapframe&utm_source=maps&z=17.15" style="color:#eee;font-size:12px;position:absolute;top:14px;">Проспект Рыскулова, 92А — Яндекс Карты</a><iframe src="https://yandex.kz/map-widget/v1/?ll=76.907887%2C43.279144&mode=search&ol=geo&ouri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg2NzMxMTY5NBJH0prQsNC30LDSm9GB0YLQsNC9LCDQkNC70LzQsNGC0YssINCg0YvRgdKb0rHQu9C-0LIg0LTQsNKj0pPRi9C70YssIDky0JAiCg3Z0JlCFewdLUI%2C&z=17.15" :width="mapwidth" :height="mapheight" frameborder="1" allowfullscreen="true" style="position:relative;border:none;border-radius: 15px;"></iframe></div></div>
      
      <img src="@/assets/flogo.png" :height="imgheight" :width="imgwidth"  alt="">
      <p>© 2023-2024</p>
    </footer>
  </div>
</template>
  
<script>
import {url} from '@/js/config.js';
import {getConfig} from '@/js/cookie.js';
import axios from '@/js/axios.js';
import router from "@/js/router";


export default {
  name: 'MainPage',
  mixins: [seoMixin],
  data() {
    return {
      cart_length:0,
      query:'',
      url:null,
      url2:url,
      array:{items:[{image:'', slug:'s',name:''},{image:'', slug:'s',name:''},{image:'', slug:'s',name:''},{image:'', slug:'s',name:''},],},
      isMobile: false, // Проверка мобильного устройства
      mapwidth:530,
      mapheight:250,
      imgwidth:201,
      imgheight:60
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
    async  get_items() { 
        const result = await axios
        .get("api/main_page_items")
        .then((res) => {
            return res.data;
        })
        .catch(() => {
        });
        return result
    },
    async addToBasket(itemId) {
      try {
        console.log('Item added to basket');
        const result =await axios.post('/api/add-to-cart', { 'item_id': itemId }, getConfig('application/json'))
        .then((res) => {
            return res.data;
        });
        this.cart_length=result.length;
      } catch (error) {
        console.error('Error adding item to basket:', error);
      }
    },
  },
  async mounted() {
    this.updateSEO({
  title: 'Главная - Производство красок и клея с 2002 года',
  description: 'ТОО "Фараби-Клей" - ведущий производитель красок, водоэмульсии, клея и декоративных покрытий в Казахстане с 2002 года. Качественная продукция, партнерские скидки до 10%.',
  canonical: 'https://idealf.kz/'
});
    this.url=url;
    console.log(url)
    console.log(this.url)
    console.log(this.url2)
      setTimeout(async ()=>{
            let arr =await this.get_items()
arr.items.pop(); // удаляем последний элемент
            this.array = arr;
            this.cart_length =await this.get_cart_length()
            console.log(this.array);
            console.log(this.cart_length);
            //console.log(this.array.items[0].image);
      }, 100);

    
  // Установка адаптивности
  this.isMobile = window.matchMedia('(max-width: 1500px)').matches;
  const handleResize = () => {
    this.isMobile = window.matchMedia('(max-width: 1500px)').matches;
  };
  window.addEventListener('resize', handleResize);
  if(this.isMobile){
    this.mapwidth=230
    this.imgwidth=100
    this.imgheight=30
  }
  // Убираем слушатель события при уничтожении компонента
  this.$watch(
    () => this.$el,
    (newValue) => {
      if (!newValue) {
        window.removeEventListener('resize', handleResize);
      }
    }
  );

  },
}
</script>