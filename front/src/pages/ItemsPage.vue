<template>
    <div>
        <header>
            <div class="first">
                <img src="@/assets/flogo.png" height="67" width="229" alt="logo">
                <button><div><span></span><span></span><span></span><span></span></div><p>Каталог товаров</p></button>
            </div>
            <div class="middle">
                <input type="text" placeholder="Поиск по сайту">
                <button><img src="@/assets/phone.png" width="15" height="15" alt=""><p>КОНТАКТЫ</p></button>
            </div>
            <div class="last">
                <p>0</p>
                <button><img src="@/assets/cart.png" width="30" height="30" alt=""></button>
            </div>
        </header>
        <section class="items_content">
            <div class="items_content_header">
                <h1>Каталог товаров</h1>
            </div>
            <div class="items_content_body">
                <div class="items_content_item">
                    <div v-for="item in array.items" :key="item">
                        <img :src="item.image" width="153" height="168" alt="">
                        <div>
                            <p>{{this.array.items[0].name}}</p>
                            <div>
                                <button>в корзину</button>
                                <router-link :to="{ name: 'Item', params: { slug: this.array.items[0].slug } }">страница товара</router-link>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <h1>Категории</h1>
                    <button v-for="tag in tags.tags" :key="tag">{{ tag.name }}</button>
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
                <p>+7(747)855-10-75 +7(708)807-00-18</p>
                </div>
                <div>
                <img src="" alt="">
                <p>+7(727)294-23-30</p>
                </div>
                <div>
                <img src="" alt="">
                <p>ideal.farabi@gmail.com</p>
                </div>
            </div>
            <div class="footer_middle"><div style="position:relative;overflow:hidden;"><a href="https://yandex.kz/maps/162/almaty/?utm_medium=mapframe&utm_source=maps" style="display: none;color:#eee;font-size:12px;position:absolute;top:0px;">Алматы</a><a href="https://yandex.kz/maps/162/almaty/house/Y08YfwdnQEUAQFppfX52eH5hZg==/?ll=76.907887%2C43.279144&utm_medium=mapframe&utm_source=maps&z=17.15" style="color:#eee;font-size:12px;position:absolute;top:14px;">Проспект Рыскулова, 92А — Яндекс Карты</a><iframe src="https://yandex.kz/map-widget/v1/?ll=76.907887%2C43.279144&mode=search&ol=geo&ouri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgg2NzMxMTY5NBJH0prQsNC30LDSm9GB0YLQsNC9LCDQkNC70LzQsNGC0YssINCg0YvRgdKb0rHQu9C-0LIg0LTQsNKj0pPRi9C70YssIDky0JAiCg3Z0JlCFewdLUI%2C&z=17.15" width="530" height="250" frameborder="1" allowfullscreen="true" style="position:relative;border:none;border-radius: 15px;"></iframe></div></div>
            <div class="footer_last">
                <div>red</div>
            </div>
            <img src="@/assets/flogo.png" height="60" width="201"  alt="">
            <p>made by DigitalSolution</p>
        </footer>
    </div>
</template>
  
<script>
import {url} from '@/js/config.js';
import axios from 'axios';
export default {
    name: 'ItemsPage',
    data() {
      return {
        array:{items:[{image:'', slug:'s',name:''},{image:'', slug:'s',name:''},{image:'', slug:'s',name:''},{image:'', slug:'s',name:''},]},
        tags:{tags:[{id:0,name:''}]},
        url:null,
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
            .get("api/items")
            .then((res) => {
                return res.data;
            })
            .catch(() => {
            });
            return result
        },
        async  get_tags() { 
            const result = await axios
            .get("api/tags")
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
            this.tags =await this.get_tags()
            this.cart_length =await this.get_cart_length()
            this.array = arr;
            console.log(this.array);
            console.log(this.tags);
            console.log(this.cart_length);
        }, 100);
    },
}
</script>