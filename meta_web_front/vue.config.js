const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
devServer: {
      //使用本地局域网的Ip
    host:'0.0.0.0',   //主机 访问的主机
    port: 8080,  //  端口 可以设置（9090）
    //代理
    proxy:{ }
    },
     assetsDir: 'static',// 静态资源打包输出目录 (js, css, img, fonts)，相应的url路径也会改变
})
