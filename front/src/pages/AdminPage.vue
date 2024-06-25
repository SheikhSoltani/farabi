<template>
    <section class="admin_page">
        <button class="admin_buttons" @click="logOut">Выход</button>
        <div class="admin_header_buttons">
            <button @click="showElement(this.hidden_1,'hidden_1',false),fill('category_name','')">Добавить категорию</button>
            <button @click="showElement(this.hidden_2,'hidden_2',false)">Добавить товар</button>
        </div>
        <div class="admin_item_panel" v-show="hidden_1">
            <button class="admin_exit_button admin_buttons" @click="showElement(this.hidden_1,'hidden_1',false),fill('category_name','')">Закрыть</button>
            <label for="">Название категории</label>
            <input type="text" v-model="category_name">
            <button v-show="!eddit" @click="addCategory">Добавить</button>
            <button v-show="eddit" @click="editTag(this.previous_category_name,this.category_name)">Заменить</button>
        </div>
        <div class="admin_item_panel" v-show="hidden_2">
            <button class="admin_exit_button admin_buttons"  @click="showElement(this.hidden_2,'hidden_2',false),changeValueToFalse()">Закрыть</button>
            <label for="">Название товара</label>
            <input type="text" v-model="item_name">
  <div class="select-dropdown">
            <select v-model="category_id">
                <option disabled value="">Выберите категорию</option>
                <option v-for="item in array_tags.tags" v-bind:key="item" :value="item.id">{{ item.name }}</option>
            </select></div>
            <label for="avatar" class="input-file">
                <input  onmouseout="this.blur();"  type="file" id="avatar" name="avatar" accept="image/png, image/jpeg" >
                <span>Выберите фото товара</span>
            </label>
            <div class="admin_price"> 
                <div v-for="i in price_array" v-bind:key="i">
                    <label for="volume">Объём:</label>
                    <input type="text" name="volume" id="" v-bind:value="i.volume" @input="i.volume=$event.target.value">
                    <label for="bulk">Оптом:</label>
                    <input type="text" name="bulk" id="" v-bind:value="i.bulk" @input="i.bulk=$event.target.value" v-mask="'############'">
                    <label for="retail">Розница:</label>
                    <input type="text" name="retail" id="" v-bind:value="i.retail" @input="i.retail=$event.target.value" v-mask="'############'">
                </div>
                <div>
                    <button class="admin_buttons" @click="AddPrice">Добавить цену</button>
                    <button class="admin_buttons" @click="PopPrice">Удалить цену</button>
                </div>
            </div>
            <div class="admin_hidden">
                <label v-show="show_array[0].description" for="">Описание товара</label>
                <input v-show="show_array[0].description" type="text" v-model="description">
                <label v-show="show_array[0].purpose" for="">Назначение товара</label>
                <input v-show="show_array[0].purpose" type="text" v-model="purpose">
                <label v-show="show_array[0].color" for="">Цвет товара</label>
                <input v-show="show_array[0].color" type="text" v-model="color">
                <label v-show="show_array[0].degree_of_gloss" for="">Степень глянца товара</label>
                <input v-show="show_array[0].degree_of_gloss" type="text" v-model="degree_of_gloss">
                <label v-show="show_array[0].warranty" for="">Гарантия товара</label>
                <input v-show="show_array[0].warranty" type="text" v-model="warranty">
                <label v-show="show_array[0].expiration_date" for="">Срок хранения</label>
                <input v-show="show_array[0].expiration_date" type="text" v-model="expiration_date">
                <label v-show="show_array[0].composition" for="">Состав товара</label>
                <input v-show="show_array[0].composition" type="text" v-model="composition">
                <label v-show="show_array[0].method_of_use" for="">Метод использования товара</label>
                <input v-show="show_array[0].method_of_use" type="text" v-model="method_of_use">
                <label v-show="show_array[0].expense" for="">Расход товара</label>
                <input v-show="show_array[0].expense" type="text" v-model="expense">
                <label v-show="show_array[0].flammable" for="">Огнеопасно товара</label>
                <input v-show="show_array[0].flammable" type="checkbox" v-model="flammable">
                <label v-show="show_array[0].traits" for="">Свойства товара</label>
                <input v-show="show_array[0].traits" type="text" v-model="traits">
            </div>
            
  <div class="select-dropdown">
            <select v-model="selectedCategory">
                <option disabled value="">Выберите новое поле</option>
                <option v-show="!value" v-for="(value, key) in show_array[0]" v-bind:key="key" :value="key">{{  translatedLabel(key)  }}</option>
            </select></div>
            <!-- <div v-for="(value, key) in show_array[0]" v-bind:key="key">
                <div v-if="value===false">
                    <button @click="changeValue(key)">{{ key }}</button>
                </div>
            </div> -->
            <button class="admin_buttons" v-show="!eddit" @click="addItem">Добавить</button>
            <button class="admin_buttons" v-show="eddit" @click="editItem">Заменить</button>
        </div>
        <div class="admin_content">
            <div>
                <button :class="{ active: hidden_3 === true }" @click="showElement_2(true)">Категории</button>
                <button :class="{ active: hidden_3 === false }" @click="showElement_2(false)">Товары</button>
            </div>
            <div class="admin_content_items" v-show="!hidden_3" v-for="item in array.items" v-bind:key="item">
                <div>
                    <p>{{item.name}}</p>
                    <button :id="item.id" @click="deleteItem(item.id)">удалить</button>
                    <button @click="showElement(this.hidden_2,'hidden_2',true),fill('item_id',item.id)">редактировать</button>
                </div>
            </div>
            <div class="admin_content_tags" v-show="hidden_3" v-for="item in array_tags.tags" v-bind:key="item">
                <div>
                    <p>{{item.name}}</p>
                    <button :id="item.name" @click="deleteTag(item.name)">удалить</button>
                    <button @click="showElement(this.hidden_1,'hidden_1',true),fill('category_name',item.name)">редактировать</button>
                </div>
            </div>
        </div>
    </section>
  </template>
  <script>
  import axios from 'axios';
  import router from "@/js/router";

  import {getConfig} from '@/js/cookie.js';
  
  
  
  export default {
  
    data() {
      return {
        username:'',
        password:'',
        image:null,
        hidden_1:false,
        hidden_2:false,
        hidden_3:true,
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
        selectedCategory: '',
        expense:'',
        flammable: false,
        traits:'',
        canSend:true,
        array:[],
        show_array:[{
            description: false,
            purpose: false,
            color: false,
            degree_of_gloss: false,
            warranty: false,
            expiration_date: false,
            composition: false,
            method_of_use: false,
            expense: false,
            flammable: false,
            traits: false,
        }],
        array_tags:[],
        price_array: [{volume:"",bulk:"",retail:""},],
      }
    }, 
    watch: {
      selectedCategory: function (newValue) {
        if (newValue !== '') {
          this.show_array[0][newValue] = true;
          this.selectedCategory="Выберите новое поле"
        }
      }
    }, computed: {
      translatedLabel: function () {
        return function (key) {
          if (key === 'description') {
            return 'Описание товара';
          }
          if (key === 'purpose') {
            return 'Назначение товара';
          }
          if (key === 'color') {
            return 'Цвет товара';
          }
          if (key === 'degree_of_gloss') {
            return 'Степень глянца товара';
          }
          if (key === 'warranty') {
            return 'Гарантия товара';
          }
          if (key === 'expiration_date') {
            return 'Срок хранения';
          }
          if (key === 'composition') {
            return 'Состав товара';
          }
          if (key === 'method_of_use') {
            return 'Метод использования товара';
          }
          if (key === 'expense') {
            return 'Расход товара';
          }
          if (key === 'flammable') {
            return 'Огнеопасно товара';
          }
          if (key === 'traits') {
            return 'Свойства товара';
          }
        }
      }
    },
    name: 'AdminPage',
    methods: {
        logOut () {
            axios.post('farabi-admin/logout',{} ,getConfig('application/json'));
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
        CanSendTag(){
        if(this.category_name===''){
            alert("Вы не заполнили название категории")
            return false
        }
            return true
        },
        CanSend(){
            let input = document.querySelector('#avatar');
            if(this.item_name===''){
                this.canSend=false
                alert("Вы не заполнили название товара")
            }
            else if(this.category_id===''){
                this.canSend=false
                alert("Вы не выбрали категорию для товара")
            }
            else if(input.files[0]===undefined && this.image===null){
                this.canSend=false
                alert("Вы не добавили фото товара")
            }else{
                this.canSend=true
                
                for(let i in this.price_array){
                    if(this.price_array[i].volume===''){
                    this.canSend=false
                    }
                    if(this.price_array[i].bulk===''){
                    this.canSend=false
                    }
                    if(this.price_array[i].retail===''){
                    this.canSend=false
                    }
                }
                if(this.canSend===false){
                    alert("Вы не полностью заполнили цену товара")
                }
            }
        },
        addItem (event) {
            event.preventDefault();
            this.CanSend();
            if(this.canSend){
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
                for (const value of data.values()) {
                  console.log(value);
}                axios.post('farabi-admin/create-item',data , getConfig('multipart/form-data')
                )
            }
        },
        addCategory (event) {
            if(this.CanSendTag()){
                event.preventDefault();
                axios.post('farabi-admin/create-tag', {'tag_name': this.category_name}, getConfig('application/json'))
                .then(result => result.data);
                setTimeout(async ()=>{
                    let arr2 =await this.get_tags()
                    this.array_tags = arr2;
                }, 100);
            }
        },
        changeValue(value){
            this.show_array[0][value] = true;
        },
        changeValueToFalse(){
            for(let i in this.show_array[0]){
                this.show_array[0][i] = false;
            }
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
        showElement_2(value){
            if(this.hidden_3!=value){
                this.hidden_3=value;
            }
        },
        deleteTag(tag_name){
            axios.post(
                'farabi-admin/delete-tag', { 'tag_name': tag_name }, getConfig('application/json')
            ).then(data =>{
            if(data.data.result){
                let child = document.getElementById(tag_name);
                child.parentElement.remove();
            }
            })
        },
        deleteItem(item_id){
            
            axios.post(
                'farabi-admin/delete-item', { 'id': item_id }, getConfig('application/json')
            ).then(data =>{
            if(data.data.result){
                let child = document.getElementById(item_id);
                child.parentElement.remove();
            }
            })
        },
        editTag(tag_name,tag_new_name){
            if(this.CanSendTag()){
                axios.patch(
                    'farabi-admin/edit-tag', { 'tag_name': tag_name,'tag_new_name':tag_new_name }, getConfig('application/json')
                ).then(() =>{
                    for(let i in this.array_tags.tags){
                        if(this.array_tags.tags[i].name===tag_name){
                            this.array_tags.tags[i].name=tag_new_name;
                        }
                    }
                })
            }
        },
        editItem(){
            this.CanSend();
            if(this.canSend){
                let data = new FormData();
                let input = document.querySelector('#avatar');
                if(input.files[0]===undefined){
                    data.append('image', '')
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
                axios.patch('farabi-admin/edit-item',data , getConfig('multipart/form-data'))
            }
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
    mounted() {
        async function logged_or_not() {
            const result = await axios
            .get("farabi-admin/logged")
            .then((res) => {
            return res.data;
            })
            .catch(() => {
            console.log("fail");
            });
            console.log(result.result)
            if (result.result === false) {
                await router.push({path: '/login'})
            }
            return result.result
        }
        logged_or_not()
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