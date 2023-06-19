import LoginPage from "@/pages/LoginPage";
import {createRouter,createWebHistory} from "vue-router";
import MainPage from "@/pages/MainPage";
import NotFound from "@/pages/NotFound";
import AdminPage from "@/pages/AdminPage";
import ItemPage from "@/pages/ItemPage";
import ItemsPage from "@/pages/ItemsPage";
import BasketPage from "@/pages/BasketPage";
import ContactsPage from "@/pages/ContactsPage";

const routes =[
    { 
      path: '/404', 
      name: '404', 
      component: NotFound, 
    },
    { path: '/:pathMatch(.*)*', component: NotFound },
    {
        path:'/',
        component: MainPage,
    },
    {
        path:'/contacts',
        component: ContactsPage,
    },
    {
        path:'/login',
        component: LoginPage,
    },
    {
        path:'/admin',
        component: AdminPage,
    },
    {
        name:'Item',
        path:'/item/:slug',
        component: ItemPage,
        props: (route) => ({  slug: route.params.slug }),
    },
    {
        path:'/items',
        component: ItemsPage,
    },
    {
        path:'/cart',
        component: BasketPage,
    },
]

const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;