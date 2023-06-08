<template>
    <div>
        <h1>MainPage</h1>
    </div>
    <ItemPage slug="klei"/>
</template>
  
<script>


import ItemPage from '@/pages/ItemPage.vue'

export default {
  name: 'MainPage',
  components: {
    ItemPage,
  },
}
</script>