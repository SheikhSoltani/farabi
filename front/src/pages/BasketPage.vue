<template>
    <section class="cart_content">
        <div class="cart_content_header">
            <h1>Оформление заказа</h1>
        </div>
        <button @click="deleteAllItems">очистить корзину</button>
        <div class="cart_content_body">
            <div class="cart_content_item">
                <span>{{this.array.items.length}}</span>
                <div v-for="item in array.items" :key="item.id" :id="item.id" class="basket_item">
                    <img :src="this.url+(item.image ? item.image.replace('/', '') : '')" :width="imgwidth" :height="imgheight" alt="">
                    <div>
                        <p>{{item.name}}</p>
                        <div>
                            <p>Количество</p>
                            <input type="number" v-model.number="item.quantity" min="1">
                            <span>kg</span>
                            <button @click="deliteItem(item.id)">убрать товар из корзины</button>
                        </div>
                    </div>
                </div>
            </div>
            <div>
                <p>Товары:{{this.array.items.length}} шт.</p>
                <input v-model="this.name" type="text" placeholder="Ваше имя...">
                <textarea v-model="this.comment" cols="30" rows="10" placeholder="Комментарий к заказу..."></textarea>
                <button @click="sendMessage">Подтвердить заказ</button>
            </div>
        </div>
    </section>
    <footer class="min_footer">
        <img src="@/assets/flogo.png" :height="imageheight" :width="imagewidth" alt="">
        <p>© 2023-2024</p>
    </footer>
</template>

<script>
import { url } from '@/js/config.js';
import axios from '@/js/axios.js';
import { getConfig } from '@/js/cookie.js';
import router from "@/js/router";

export default {
    name: 'BasketPage',
    data() {
        return {
            hidden: false,
            email: '',
            name: '',
            phone: '',
            array: { items: [] },  // Change to an array
            comment: '',
            message: '',
            url2:url,
            isMobile: false, // Проверка мобильного устройства
            imgwidth:153,
            imgheight:168,
            imagewidth:200,
            imageheight:60
        }
    },
    methods: {
        search() {
            console.log(this.query)
            router.push({ path: '/items', query: { query: this.query } })
        },
        sendMessage() {
            this.message = `Информация о заказе:\nИмя: ${this.name}\nКомментарий: ${this.comment}\nТовары:\n${this.array.items.map(item => `- ${item.name} (${item.quantity} kg)`).join('\n')}`;
            let url;
            if(this.isMobile){
                 url = `https://wa.me/+77088070018?text=${encodeURIComponent(this.message)}`;
            }else{
                 url = `https://wa.me/87088070018?text=${encodeURIComponent(this.message)}`;
            }
            window.open(url, '_blank');
        },
        deliteItem(id) {
            axios.post(
                'api/delete-from-cart', { 'item_id': id }, getConfig('application/json')
            ).then(data => {
                if (data.data.result) {
                    const index = this.array.items.findIndex(item => item.id === id);
                    if (index !== -1) {
                        this.array.items.splice(index, 1);
                    }
                }
            })
        },
        deleteAllItems() {
            axios.post(
                'api/flush-cart', {}, getConfig('application/json')
            ).then(data => {
                if (data.data.result) {
                    this.array.items = [];
                }
            })
        },
        showElement() {
            this.hidden = !this.hidden;
        },
        async get_basket_items() {
            const result = await axios
                .get("api/get-cart-items")
                .then((res) => {
                    return res.data;
                })
                .catch(() => { });
            return result
        },
    },
    async mounted() {
        this.url = url;
        setTimeout(async () => {
            let arr = await this.get_basket_items();
            this.array = arr;
            this.array.items.forEach(item => {
                if (!item.quantity) {
                    item.quantity = 1; // Default quantity to 1 if not set
                }
            });
        }, 100);


        // Установка адаптивности
        this.isMobile = window.matchMedia('(max-width: 1500px)').matches;
        const handleResize = () => {
            this.isMobile = window.matchMedia('(max-width: 1500px)').matches;
        };
        window.addEventListener('resize', handleResize);
        if(this.isMobile){
            this.imgwidth=100
            this.imgheight=90
            this.imagewidth=100
            this.imageheight=30
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

<style>
/* Add your styles here */
</style>
