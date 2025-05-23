<template>
  <div id="app">
    <HeaderComponent v-if="!isLoginPage && !isAdminPage" />
    <router-view v-slot="{ Component }">
      <transition>
        <component :is="Component" />
      </transition>
    </router-view>
  </div>
</template>

<script>
import HeaderComponent from '@/components/HeaderComponent.vue'

export default {
  name: 'App',
  components: {
    HeaderComponent
  },
  computed: {
    isLoginPage() {
      return this.$route.path === '/login'
    },
    isAdminPage() {
      return this.$route.path === '/admin'
    }
  }
}
</script>
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  line-height: 1.6;
  color: #333;
}

#app {
  min-height: 100vh;
}
</style>
