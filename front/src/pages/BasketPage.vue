<template>
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
            <p>{{this.array.items.length}}</p>
            <router-link :to="{ name: 'Basket' }"><img src="@/assets/cart.png" width="30" height="30" alt=""></router-link>
        </div>
    </header>
    <section class="cart_content">
        <div class="cart_content_header">
            <h1>Оформление заказа</h1>
            <img src="@/assets/flogo.png" height="60" width="201" alt="">
        </div>
        <button @click="deleteAllItems">очистить корзину</button>
        <div class="cart_content_body">
            <div class="cart_content_item">
                <span>{{this.array.items.length}}</span>
                <div v-for="item in array.items" :key="item.id" :id="item.id" class="basket_item">
                    <img :src="url+this.url+(item.image ? item.image.replace('/', '') : '')" width="153" height="168" alt="">
                    <div>
                        <p>{{item.name}}</p>
                        <div>
                            <p>Количество</p>
                            <input type="number" v-model.number="item.quantity" min="1">
                            <span>kg</span>
                            <button @click="deliteItem(item.id)">убать товар из корзины</button>
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
        <img src="@/assets/flogo.png" height="60" width="201" alt="">
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
            message: ''
        }
    },
    methods: {
        search() {
            console.log(this.query)
            router.push({ path: '/items', query: { query: this.query } })
        },
        sendMessage() {
            this.message = `Информация о заказе:\nИмя: ${this.name}\nКомментарий: ${this.comment}\nТовары:\n${this.array.items.map(item => `- ${item.name} (${item.quantity} kg)`).join('\n')}`;
            const url = `https://wa.me/87079207675?text=${encodeURIComponent(this.message)}`;
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
    },
}
</script>

<style>
/* Add your styles here */
</style>
