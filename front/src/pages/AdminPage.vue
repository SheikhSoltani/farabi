<template>
    <section class="admin_page">
        <button @click="logOut">Выход</button>
        <button @click="showElement(this.hidden_2,'hidden_2',false)">Добавить товар</button>
        <button @click="showElement(this.hidden_1,'hidden_1',false),fill('category_name','')">Добавить категорию</button>
        <div v-show="hidden_1">
            <label for="">Название категории</label>
            <input type="text" v-model="category_name">
            <button v-show="!eddit" @click="addCategory">Добавить</button>
            <button v-show="eddit" @click="editTag(this.previous_category_name,this.category_name)">Заменить</button>
        </div>
        <div class="admin_item_panel" v-show="hidden_2">
            <label for="">Название товара</label>
            <input type="text" v-model="item_name">
            <select v-model="category_id">
                <option disabled value="">Выберите категорию</option>
                <option v-for="item in array_tags.tags" v-bind:key="item" :value="item.id">{{ item.name }}</option>
            </select>
            <label for="">Описание товара</label>
            <input type="text" v-model="description">
            <label for="">Назначение товара</label>
            <input type="text" v-model="purpose">
            <label for="avatar" class="input-file">
                <input  onmouseout="this.blur();"  type="file" id="avatar" name="avatar" accept="image/png, image/jpeg" >
                <span>Выберите файл</span>
            </label>
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
            <button v-show="!eddit" @click="addItem">Добавить</button>
            <button v-show="eddit" @click="editItem">Заменить</button>
        </div>
        <div v-for="item in array.items" v-bind:key="item">
            <div style="margin: 5px;">
                <p style="width: 100px;display: inline-block;overflow: hidden;">{{item.name}}</p>
                <button :id="item.id" @click="deleteItem(item.id)">удалить</button>
                <button @click="showElement(this.hidden_2,'hidden_2',true),fill('item_id',item.id)">редактировать</button>
            </div>
        </div>
        <div v-for="item in array_tags.tags" v-bind:key="item">
            <div style="background: #313131;color: white;margin: 5px;">
                <p style="width: 100px;display: inline-block;overflow: hidden;">{{item.name}}</p>
                <button :id="item.name" @click="deleteTag(item.name)">удалить</button>
                <button @click="showElement(this.hidden_1,'hidden_1',true),fill('category_name',item.name)">редактировать</button>
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
        image:null,
        hidden_1:false,
        hidden_2:false,
        eddit:false,
        category_name:'',
        previous_category_name:'',
        category_id:'',
        item_id:'',
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
        flammable: false,
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
        fill(name,value){
            if(name==='category_name'){
                this.category_name = value;
                this.previous_category_name = value;
            }
            if(name==='item_id'){
                this.item_id = value;
                for(let i in this.array.items){
                    if(this.array.items[i].id===value){
                        this.item_name=this.array.items[i].name,
                        this.image=this.array.items[i].image,
                        this.description=this.array.items[i].description,
                        this.category_id=this.array.items[i].tag_serialized.id,
                        this.purpose=this.array.items[i].purpose,
                        this.color=this.array.items[i].color,
                        this.degree_of_gloss=this.array.items[i].degree_of_gloss,
                        this.warranty=this.array.items[i].warranty,
                        this.expiration_date=this.array.items[i].expiration_date,
                        this.composition=this.array.items[i].composition,
                        this.method_of_use=this.array.items[i].method_of_use,
                        this.expense=this.array.items[i].expense,
                        this.flammable=this.array.items[i].flammable,
                        this.traits=this.array.items[i].traits,
                        this.price_array=this.array.items[i].price_serialized
                    }
                }
            }
        },
        addItem (event) {
            event.preventDefault();

            let data = new FormData();
            let input = document.querySelector('#avatar');
            if(input.files[0]===undefined){
                data.append('image', '');
            }else{
                data.append('image', input.files[0]);
            }
            data.append('name', this.item_name);
            data.append('description', this.description);
            data.append('tag',this.category_id);
            data.append('purpose', this.purpose);
            data.append('color', this.color);
            data.append('degree_of_gloss', this.degree_of_gloss);
            data.append('warranty', this.warranty);
            data.append('expiration_date', this.expiration_date);
            data.append('composition', this.composition);
            data.append('method_of_use',this.method_of_use);
            data.append('expense', this.expense);
            data.append('flammable', JSON.parse(this.flammable));
            data.append('traits', this.traits);
            data.append('price_array', JSON.stringify(this.price_array));
            console.log(data)
            axios.post(url+'farabi-admin/create-item',data , getConfig('multipart/form-data')
            )
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
        showElement (hideElem,name,eddit) {
            if(eddit===true){
                this.eddit=true;
            }else{
                this.eddit=false;
            }
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
        },
        deleteTag(tag_name){
            axios.post(
                url+'farabi-admin/delete-tag', { 'tag_name': tag_name }, getConfig('application/json')
            ).then(data =>{
            if(data.data.result){
                let child = document.getElementById(tag_name);
                child.parentElement.remove();
            }
            })
        },
        deleteItem(item_id){
            
            axios.post(
                url+'farabi-admin/delete-item', { 'id': item_id }, getConfig('application/json')
            ).then(data =>{
            if(data.data.result){
                let child = document.getElementById(item_id);
                child.parentElement.remove();
            }
            })
        },
        editTag(tag_name,tag_new_name){
            axios.patch(
                url+'farabi-admin/edit-tag', { 'tag_name': tag_name,'tag_new_name':tag_new_name }, getConfig('application/json')
            ).then(() =>{
                for(let i in this.array_tags.tags){
                    if(this.array_tags.tags[i].name===tag_name){
                        this.array_tags.tags[i].name=tag_new_name;
                    }
                }
            })
        },
        editItem(){

            
            let data = new FormData();
            let input = document.querySelector('#avatar');
            if(input.files[0]===undefined){
                data.append('image', this.image.replace("/media",""));
            }else{
                data.append('image', input.files[0]);
            }
            data.append('name', this.item_name);
            data.append('id', this.item_id);
            data.append('description', this.description);
            data.append('tag',this.category_id);
            data.append('purpose', this.purpose);
            data.append('color', this.color);
            data.append('degree_of_gloss', this.degree_of_gloss);
            data.append('warranty', this.warranty);
            data.append('expiration_date', this.expiration_date);
            data.append('composition', this.composition);
            data.append('method_of_use',this.method_of_use);
            data.append('expense', this.expense);
            data.append('flammable', JSON.parse(this.flammable));
            data.append('traits', this.traits);
            data.append('price_array', JSON.stringify(this.price_array));
            console.log(data)
            axios.patch(url+'farabi-admin/edit-item',data , getConfig('multipart/form-data'))

           
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
    mounted() {
        // async function logged_or_not() {
        //     console.log('logged_or_not');
        //     const result = await axios
        //     .get(url+"farabi-admin/logged")
        //     .then((res) => {
        //     return res.data;
        //     })
        //     .catch(() => {
        //     console.log("fail");
        //     });
        //     if (result.result === false) {
        //         console.log(result.result);
        //         await router.push({path: '/login'})
        //     }
        //     return result.result
        // }
        // logged_or_not()
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