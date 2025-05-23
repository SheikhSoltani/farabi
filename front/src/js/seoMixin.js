// Миксин для управления SEO мета-тегами
export const seoMixin = {
  methods: {
    updateSEO({ title, description, keywords, canonical }) {
      // Обновляем title
      if (title) {
        document.title = `${title} | ТОО "Фараби-Клей"`;
      }
      
      // Обновляем description
      if (description) {
        this.updateMetaTag('description', description);
      }
      
      // Обновляем keywords
      if (keywords) {
        this.updateMetaTag('keywords', keywords);
      }
      
      // Обновляем canonical URL
      if (canonical) {
        this.updateCanonical(canonical);
      }
      
      // Обновляем Open Graph теги
      if (title) {
        this.updateMetaProperty('og:title', `${title} | ТОО "Фараби-Клей"`);
      }
      if (description) {
        this.updateMetaProperty('og:description', description);
      }
    },
    
    updateMetaTag(name, content) {
      let element = document.querySelector(`meta[name="${name}"]`);
      if (element) {
        element.setAttribute('content', content);
      } else {
        element = document.createElement('meta');
        element.setAttribute('name', name);
        element.setAttribute('content', content);
        document.head.appendChild(element);
      }
    },
    
    updateMetaProperty(property, content) {
      let element = document.querySelector(`meta[property="${property}"]`);
      if (element) {
        element.setAttribute('content', content);
      } else {
        element = document.createElement('meta');
        element.setAttribute('property', property);
        element.setAttribute('content', content);
        document.head.appendChild(element);
      }
    },
    
    updateCanonical(url) {
      let element = document.querySelector('link[rel="canonical"]');
      if (element) {
        element.setAttribute('href', url);
      } else {
        element = document.createElement('link');
        element.setAttribute('rel', 'canonical');
        element.setAttribute('href', url);
        document.head.appendChild(element);
      }
    }
  }
};