<template>
    <div class="about-page">
        <div class="container">
            <h1>О компании ТОО "Фараби-Клей"</h1>
            
            <section class="company-intro">
                <h2>Производство лакокрасочных материалов с 2002 года</h2>
                <p>
                    ТОО "Фараби-Клей" — современный завод по производству высококачественных 
                    лакокрасочных материалов, водоэмульсионных красок, клеев и декоративных покрытий. 
                    Более 20 лет мы обеспечиваем строительный рынок надежными и проверенными продуктами.
                </p>
            </section>

            <section class="products-section">
                <h2>Наша продукция</h2>
                <div class="products-grid">
                    <div class="product-item">
                        <h3>Краски</h3>
                        <p>Широкий ассортимент красок для внутренних и наружных работ</p>
                    </div>
                    <div class="product-item">
                        <h3>Водоэмульсии</h3>
                        <p>Экологически чистые водоэмульсионные покрытия</p>
                    </div>
                    <div class="product-item">
                        <h3>Клеи</h3>
                        <p>Профессиональные клеевые составы для различных материалов</p>
                    </div>
                    <div class="product-item">
                        <h3>Декоративные покрытия</h3>
                        <p>Современные решения для создания уникальных интерьеров</p>
                    </div>
                </div>
            </section>

            <section class="partners-section">
                <h2>Партнерские условия</h2>
                <p>
                    Мы ценим долгосрочное сотрудничество и предлагаем выгодные условия 
                    для наших партнеров. Скидки для оптовых покупателей достигают 10%.
                </p>
                <div class="partner-benefits">
                    <ul>
                        <li>Индивидуальный подход к каждому клиенту</li>
                        <li>Гибкая система скидок</li>
                        <li>Качественная продукция по доступным ценам</li>
                        <li>Техническая поддержка специалистов</li>
                    </ul>
                </div>
            </section>

            <section class="experience-section">
                <h2>Опыт и качество</h2>
                <p>
                    За годы работы мы накопили богатый опыт в производстве лакокрасочных 
                    материалов. Наша продукция соответствует всем современным стандартам 
                    качества и безопасности.
                </p>
            </section>
        </div>
    </div>
</template>

<script>
import { seoMixin } from '@/js/seoMixin.js';

export default {
    name: 'AboutPage',
    mixins: [seoMixin],
    mounted() {
        this.updateSEO({
            title: 'О компании - Производство красок и клея с 2002 года',
            description: 'ТОО "Фараби-Клей" - ведущий казахстанский производитель красок, водоэмульсии, клея и декоративных покрытий. Работаем с 2002 года. Партнерские скидки до 10%.',
            keywords: 'о компании Фараби-Клей, производство красок Казахстан, история компании, лакокрасочный завод',
            canonical: 'https://idealf.kz/about'
        });
    }
}
</script>

<style scoped>
.about-page {
    min-height: 100vh;
    background: #f5f5f5;
    padding: 40px 20px;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    background: white;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

h1 {
    color: #2c3e50;
    text-align: center;
    margin-bottom: 40px;
    font-size: 2.5rem;
}

h2 {
    color: #34495e;
    margin-bottom: 20px;
    font-size: 1.8rem;
}

h3 {
    color: #2c3e50;
    margin-bottom: 10px;
}

section {
    margin-bottom: 40px;
}

.company-intro p {
    font-size: 1.1rem;
    line-height: 1.6;
    color: #555;
}

.products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
    margin-top: 20px;
}

.product-item {
    background: #f8f9fa;
    padding: 20px;
    border-radius: 8px;
    border-left: 4px solid #3498db;
}

.partners-section {
    background: #ecf0f1;
    padding: 30px;
    border-radius: 8px;
}

.partner-benefits ul {
    list-style: none;
    padding: 0;
}

.partner-benefits li {
    padding: 8px 0;
    position: relative;
    padding-left: 20px;
}

.partner-benefits li:before {
    content: "✓";
    color: #27ae60;
    font-weight: bold;
    position: absolute;
    left: 0;
}

.experience-section p {
    font-size: 1.1rem;
    line-height: 1.6;
    color: #555;
}

@media (max-width: 768px) {
    .container {
        padding: 20px;
    }
    
    h1 {
        font-size: 2rem;
    }
    
    .products-grid {
        grid-template-columns: 1fr;
    }
}
</style>