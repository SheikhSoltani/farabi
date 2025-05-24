<template>
    <div>
        <section class="items_content">
            <div class="items_content_header">
                <h1>Каталог товаров</h1>
            </div>
            <div class="items_content_body">
                <div class="items_content_item">
                    <div v-for="item,index in array.items" :key="item">
                        <img :src="this.url2+item.image" :width="imagewidth" :height="imageheight" alt="">
                        <div>
                            <p>{{this.array.items[index].name}}</p>
                            <div>
                                <button @click="addToBasket(this.array.items[index].id)">в корзину</button>
                                <router-link :to="{ name: 'Item', params: { slug: this.array.items[index].slug } }">страница товара</router-link>
                            </div>
                        </div>
                    </div>
                </div>
                <div>
                    <h1>Категории</h1>
                    <button :class="{ active: selectTag === tag.name }" v-for="tag in tags.tags" :key="tag" @click="searchByTag(tag.name)">{{ tag.name }}</button>
                    <button @click="cleanFilter">Сбросить фильтр</button>
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
import {url} from '@/js/config.js';
import {getConfig} from '@/js/cookie.js';
import axios from '@/js/axios.js';
import { seoMixin } from '@/js/seoMixin.js';
export default {
    name: 'ItemsPage',
  mixins: [seoMixin],
    data() {
      return {
        array:{items:[{image:'', slug:'s',name:''},{image:'', slug:'s',name:''},{image:'', slug:'s',name:''},{image:'', slug:'s',name:''},]},
        tags:{tags:[{id:0,name:''}]},
        url:null,
        url2:url,
        query:'',
        selectTag:'',
        cart_length:0,
        isMobile: false, // Проверка мобильного устройства
        mapwidth:530,
        mapheight:250,
        imgwidth:201,
        imgheight:60,
        imagewidth:100,
        imageheight:90
      }
    },
    methods:{
        cleanFilter(){
            this.selectTag='';
            this.query='';
            let arr = this.get_items()
            arr.then((value) => {
                this.array = value;
            });
        },
        search(){
            let arr = this.get_items()
            arr.then((value) => {
                this.array = value;
            });
        },
        searchByTag(tag){
            this.selectTag=tag;
            this.query='';
            let arr = this.get_items()
            arr.then((value) => {
                this.array = value;
            });
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
            .get("api/items?"+"q="+this.query+"&tag="+this.selectTag)
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
        async addToBasket(itemId) {
            try {
                const result =await axios.post('/api/add-to-cart', { 'item_id': itemId }, getConfig('application/json')).then((res) => {
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
        this.updateSEO({
  title: 'Каталог товаров - Краски, клей, водоэмульсия',
  description: 'Полный каталог продукции ТОО "Фараби-Клей": краски, водоэмульсионные покрытия, клей, декоративные материалы. Оптовые и розничные цены.',
  canonical: 'https://idealf.kz/items'
});
        this.url=url;
        console.log(url)
        console.log(this.url)
        console.log(this.url2)
        if(this.$route.query.query){
            this.query=this.$route.query.query;
        }
        setTimeout(async ()=>{
            let arr =await this.get_items()
            this.tags =await this.get_tags()
            this.cart_length =await this.get_cart_length()
            this.array = arr;
            console.log(this.array);
            console.log(this.tags);
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
            this.imagewidth=100
            this.imageheight=90
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