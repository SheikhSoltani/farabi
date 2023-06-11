<template>
    <section class="admin_page">
        <button @click="logOut">Выход</button>
        <button @click="showElement(this.hidden_2,'hidden_2')">Добавить товар</button>
        <button @click="showElement(this.hidden_1,'hidden_1')">Добавить категорию</button>
        <div v-show="hidden_1">
            <label for="">Название категории</label>
            <input type="text" v-model="category_name">
            <button @click="addCategory">Добавить</button>
        </div>
        <div class="admin_item_panel" v-show="hidden_2">
            <label for="">Название товара</label>
            <input type="text" v-model="item_name">
            <label for="">ID категории</label>
            <input type="text" v-model="category_id">
            <label for="">Описание товара</label>
            <input type="text" v-model="description">
            <label for="">Назначение товара</label>
            <input type="text" v-model="purpose">
            <label for="">Цвет товара</label>
            <input type="text" v-model="color">
            <label for="">Степень глянца товара</label>
            <input type="text" v-model="degree_of_gloss">
            <label for="">Гарантия товара</label>
            <input type="text" v-model="warranty">
            <label for="">Срок хранения</label>
            <input type="text" v-model="expiration_date">
            <label for="">Состав товара</label>
            <input type="text" v-model="composition">
            <label for="">Метод использования товара</label>
            <input type="text" v-model="method_of_use">
            <label for="">Расход товара</label>
            <input type="text" v-model="expense">
            <label for="">Огнеопасно товара</label>
            <input type="checkbox" v-model="flammable">
            <label for="">Свойства товара</label>
            <input type="text" v-model="traits">
            <div v-for="i in price_array" v-bind:key="i">
                <label for="volume">volume:</label>
                <input type="text" name="volume" id="" v-bind:value="i.volume" @input="i.volume=$event.target.value">
                <label for="bulk">bulk:</label>
                <input type="text" name="bulk" id="" v-bind:value="i.bulk" @input="i.bulk=$event.target.value">
                <label for="retail">retail:</label>
                <input type="text" name="retail" id="" v-bind:value="i.retail" @input="i.retail=$event.target.value">
            </div>
            <button @click="AddPrice">AddPrice</button>
            <button @click="PopPrice">DellPrice</button>
            <br/>
            <button @click="addItem">Добавить</button>
        </div>
        <div v-for="item in array.items" v-bind:key="item">
            <div style="margin: 5px;">
                <p style="width: 100px;display: inline-block;overflow: hidden;">{{item.name}}</p>
                <button>удалить</button>
                <button>редактировать</button>
            </div>
        </div>
        <div v-for="item in array_tags.tags" v-bind:key="item">
            <div style="background: #313131;color: white;margin: 5px;">
                <p style="width: 100px;display: inline-block;overflow: hidden;">{{item.name}}</p>
                <button :id="item.name" @click="deleteTag(item.name)">удалить</button>
                <button>редактировать</button>
            </div>
        </div>
    </section>
  </template>
  <script>
  import axios from 'axios';
  import router from "@/js/router";
  import {url} from '@/js/config.js';
  import {getConfig} from '@/js/cookie.js';
  
  
  
  export default {
  
    data() {
      return {
        username:'',
        password:'',
        hidden_1:false,
        hidden_2:false,
        category_name:'',
        category_id:'',
        item_name:'',
        description:'',
        purpose:'',
        color:'',
        degree_of_gloss:'',
        warranty:'',
        expiration_date:'',
        composition:'',
        method_of_use:'',
        expense:'',
        flammable: null,
        traits:'',
        array:[],
        array_tags:[],
        price_array: [{volume:"",bulk:"",retail:""},],
      }
    },
    name: 'AdminPage',
    methods: {
        logOut () {
            axios.post(url+'farabi-admin/logout');
            setTimeout(()=>{router.push({path: '/login'})}, 200);
            
        },
        AddPrice(){
            this.price_array.push({volume:"",bulk:"",retail:""})
        },
        PopPrice(){
            this.price_array.pop()
        },
        addItem (event) {
            event.preventDefault();
            const data =axios.post(url+'farabi-admin/create-item', 
            {
                'name':this.item_name,
                'image': '',
                'description':this.description,
                'tag': this.category_id,
                'purpose':this.purpose,
                'color':this.color,
                'degree_of_gloss':this.degree_of_gloss,
                'warranty':this.warranty,
                'expiration_date':this.expiration_date,
                'composition':this.composition,
                'method_of_use':this.method_of_use,
                'expense':this.expense,
                'flammable':this.flammable,
                'traits':this.traits,'price_array':this.price_array
            })
            .then(result => result.data);
            console.log(data);
        },
        addCategory (event) {
            event.preventDefault();
            axios.post(url+'farabi-admin/create-tag', {'tag_name': this.category_name})
            .then(result => result.data);
            setTimeout(async ()=>{
                let arr2 =await this.get_tags()
                this.array_tags = arr2;
            }, 100);
        },
        showElement (hideElem,name) {
            if(hideElem===true){
                if(name==='hidden_1'){
                    this.hidden_1=false;
                }
                else if(name==='hidden_2'){
                    this.hidden_2=false;
                }
            }else{
                if(name==='hidden_1'){
                    this.hidden_1=true;
                }
                else if(name==='hidden_2'){
                    this.hidden_2=true;
                }
            }
        },deleteTag(tag_name){
              
              axios.post(
                    url+'farabi-admin/delete-tag', { 'tag_name': tag_name }, getConfig('application/json')
                ).then(data =>{
                if(data.data.result){
                  let child = document.getElementById(tag_name);
                  child.parentElement.remove();
                }
              })
            },
        async  get_items() { 
            const result = await axios
            .get(url+"api/items")
            .then((res) => {
                return res.data;
            })
            .catch(() => {
            });
            return result
        },
        async  get_tags() { 
            const result = await axios
            .get(url+"api/tags")
            .then((res) => {
                return res.data;
            })
            .catch(() => {
            });
            return result
        },

    },
    mounted() {/*
        async function logged_or_not() {
            const result = await axios
            .get(url+"farabi-admin/login")
            .then((res) => {
            return res.data;
            })
            .catch(() => {
            console.log("fail");
            });
            if (result === true) {
                console.log(result)
                await router.push({path: '/home'})
            }
            return result
        }
        logged_or_not()*/
        setTimeout(async ()=>{
            let arr =await this.get_items()
            let arr2 =await this.get_tags()
            this.array = arr;
            this.array_tags = arr2;
            console.log(this.array);
            console.log(this.array_tags);
        }, 100);
    }
  }
  
  </script>