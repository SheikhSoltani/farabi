
<template>
    <header class="header">
        <div class="container">
            <div class="logo">
                <router-link to="/" class="logo-link">
                    <h1>Фараби-Клей</h1>
                    <span class="tagline">Производство с 2002 года</span>
                </router-link>
            </div>
            
            <nav class="navigation">
                <ul class="nav-list">
                    <li><router-link to="/" class="nav-link">Главная</router-link></li>
                    <li><router-link to="/items" class="nav-link">Каталог</router-link></li>
                    <li><router-link to="/about" class="nav-link">О компании</router-link></li>
                    <li><router-link to="/contacts" class="nav-link">Контакты</router-link></li>
                    <li><router-link to="/cart" class="nav-link basket-link">Корзина</router-link></li>
                </ul>
            </nav>
            
            <button class="mobile-menu-btn" @click="toggleMobileMenu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
        
        <nav class="mobile-nav" :class="{ 'active': mobileMenuOpen }">
            <ul class="mobile-nav-list">
                <li><router-link to="/" @click="closeMobileMenu">Главная</router-link></li>
                <li><router-link to="/items" @click="closeMobileMenu">Каталог</router-link></li>
                <li><router-link to="/about" @click="closeMobileMenu">О компании</router-link></li>
                <li><router-link to="/contacts" @click="closeMobileMenu">Контакты</router-link></li>
                <li><router-link to="/cart" @click="closeMobileMenu">Корзина</router-link></li>
            </ul>
        </nav>
    </header>
</template>

<script>
export default {
    name: 'HeaderComponent',
    data() {
        return {
            mobileMenuOpen: false
        }
    },
    methods: {
        toggleMobileMenu() {
            this.mobileMenuOpen = !this.mobileMenuOpen
        },
        closeMobileMenu() {
            this.mobileMenuOpen = false
        }
    }
}
</script>

<style scoped>
.header {
    background: #2c3e50;
    color: white;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    position: sticky;
    top: 0;
    z-index: 1000;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    min-height: 70px;
}

.logo-link {
    text-decoration: none;
    color: white;
}

.logo h1 {
    margin: 0;
    font-size: 1.8rem;
    font-weight: bold;
}

.tagline {
    font-size: 0.8rem;
    color: #bdc3c7;
    display: block;
    margin-top: -5px;
}

.navigation {
    display: flex;
}

.nav-list {
    display: flex;
    list-style: none;
    margin: 0;
    padding: 0;
    gap: 30px;
}

.nav-link {
    color: white;
    text-decoration: none;
    padding: 10px 15px;
    border-radius: 5px;
    transition: all 0.3s ease;
    font-weight: 500;
}

.nav-link:hover,
.nav-link.router-link-active {
    background: #34495e;
    color: #3498db;
}

.basket-link {
    background: #e74c3c;
    color: white;
}

.basket-link:hover {
    background: #c0392b;
    color: white;
}

.mobile-menu-btn {
    display: none;
    flex-direction: column;
    background: transparent;
    border: none;
    cursor: pointer;
    padding: 5px;
    z-index: 1;
}

.mobile-menu-btn span {
    width: 25px;
    height: 3px;
    background: white;
    margin: 3px 0;
    transition: 0.3s;
}

.mobile-nav {
    display: none;
    background: #34495e;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    transform: translateY(-100%);
    opacity: 0;
    transition: all 0.3s ease;
}

.mobile-nav.active {
    transform: translateY(0);
    opacity: 1;
}

.mobile-nav-list {
    list-style: none;
    margin: 0;
    padding: 20px;
}

.mobile-nav-list li {
    margin-bottom: 15px;
}

.mobile-nav-list a {
    color: white;
    text-decoration: none;
    font-size: 1.1rem;
    display: block;
    padding: 10px;
    border-radius: 5px;
    transition: background 0.3s ease;
}

.mobile-nav-list a:hover,
.mobile-nav-list a.router-link-active {
    background: #2c3e50;
    color: #3498db;
}

@media (max-width: 768px) {
    .navigation {
        display: none;
    }
    
    .mobile-menu-btn {
        display: flex;
    }
    
    .mobile-nav {
        display: block;
    }
    
    .logo h1 {
        font-size: 1.5rem;
    }
    
    .tagline {
        font-size: 0.7rem;
    }
}

@media (max-width: 480px) {
    .container {
        padding: 0 15px;
    }
    
    .logo h1 {
        font-size: 1.3rem;
    }
}
</style>