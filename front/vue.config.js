const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer:{
    proxy: 'https://api.idealf.kz',
    host: '127.0.0.1',
    allowedHosts: 'all'
  }
})
