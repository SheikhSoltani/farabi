<template>
    <div>
        <header>
        <div class="first">
            <router-link :to="{ name: 'Main' }"><img src="@/assets/flogo.png" height="67" width="229" alt="logo"></router-link>
            <router-link :to="{ name: 'Items' }"><div><span></span><span></span><span></span><span></span></div><p>Каталог товаров</p></router-link>
        </div>
        <div class="middle">
            <input type="text" placeholder="Поиск по сайту" v-model="this.query" v-on:keydown.enter="search">
            <router-link :to="{ name: 'Contacts' }"><img src="@/assets/phone.png" width="15" height="15" alt=""><p>КОНТАКТЫ</p></router-link>
        </div>
        <div class="last">
            <p>{{this.cart_length}}</p>
            <router-link :to="{ name: 'Basket' }"><img src="@/assets/cart.png" width="30" height="30" alt=""></router-link>
        </div>
        </header>
        <section class="item_content">
            <div>
                <h1>{{this.item.item.name}}</h1>
            </div>
            <div class="item_content_body">
                <img :src="this.url+this.item.item.image" width="300" height="300" alt="">
                <p v-if="this.item.item.description"> Описание: {{ this.item.item.description }}</p>
                <p v-if="this.item.item.purpose"> Назначение: {{ this.item.item.purpose }}</p>
                <p v-if="this.item.item.color"> Цвет: {{ this.item.item.color }}</p>
                <p v-if="this.item.item.degree_of_gloss"> Степень глянца: {{ this.item.item.degree_of_gloss }}</p>
                <p v-if="this.item.item.warranty">Гарантия: {{ this.item.item.warranty }}</p>
                <p v-if="this.item.item.expiration_date"> Срок годности: {{ this.item.item.expiration_date }}</p>
                <p v-if="this.item.item.composition"> Состав: {{ this.item.item.composition }}</p>
                <p v-if="this.item.item.method_of_use"> Метод использования: {{ this.item.item.method_of_use }}</p>
                <p v-if="this.item.item.expense"> Расход: {{ this.item.item.expense }}</p>
                <!-- <p v-if="this.item.item.flammable"> Огнеопасный!</p> -->
                <p v-if="this.item.item.traits===true"> Особенность: {{ this.item.item.traits }}</p>
                <button @click="addToBasket">Добавить в корзину</button>
            </div>
            <div v-if="this.item.item.price_serialized" class="item_table">
                <div>
                    <div>Объём</div><div>Оптом</div><div>Розница</div>
                </div>
                <div v-for="item in this.item.item.price_serialized" :key="item.id">
                    <div>{{ item.volume }} кг.</div><div>{{ item.bulk }} тг.</div><div>{{item.retail}} тг.</div>
                </div>
            </div>
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
import axios from '@/js/axios.js';
import {getConfig} from '@/js/cookie.js';
import router from "@/js/router";
import {url} from '@/js/config.js'

export default {
    name: 'ItemPage',
    props: {
        slug: String,
        id:Number
    },
    data(){
        return{
            item:{item:{image:'', slug:'s',name:''}},
            cart_length:0,
            url:url,
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
            .get("/api/item?slug="+this.slug)
            .then((res) => {
                return res.data;
            })
            .catch(() => {
            });
            return result
        },
        async addToBasket() {
            try {
                const result =await axios.post('/api/add-to-cart', { 'item_id': this.item.item.id }, getConfig('application/json')).then((res) => {
                    return res.data;
                });
                console.log('Item added to basket');
                this.cart_length=result.length;
            } catch (error) {
                console.error('Error adding item to basket:', error);
            }
        },
    },
    async mounted() {
        setTimeout(async ()=>{
            this.item =await this.get_items()
            this.cart_length =await this.get_cart_length()
            console.log(this.item);
            console.log(this.cart_length);
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