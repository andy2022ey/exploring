
<template>
    <header>
      <div class="logo-title-container"> <!-- 新增的容器 -->
      <Logo />
      <div class="title">
        <span class="title-top"><a href="/" class="title-link">第壹号当铺</a></span> <!-- 第一行 -->
        <span class="title-bottom"><a href="/" class="title-link">No.1 Pawnshop</a></span> <!-- 第二行 -->
      </div>
    </div>
      <nav>
        <ul>
            <li><a href="#" @click="selectTheme('default')">主页</a></li>
            <li><a href="#" @click="selectTheme('blog')">博客</a></li>
            <li><a href="#" @click="selectTheme('product')">产品</a></li>
            <li><a href="#" @click="selectTheme('knowledge')">知识库</a></li>
            <li><a href="#" @click="selectTheme('business')">商务合作</a></li>
            <li><a href="#" @click="selectTheme('log')">建站日志</a></li>
        </ul>
      </nav>
    </header>
  </template>
  
  <script setup>
  import { ref, defineEmits } from 'vue';
  import Logo from './Logo.vue'; // 导入Logo组件

  const emit = defineEmits(['themeSelected']);

  const selectTheme = (theme) => {
    emit('themeSelected', theme);
  };
  </script>
  
  <style scoped>

.title {
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: rgb(255, 255, 239);
}

.title-top {
  font-size: 25px; /* 较大的字体大小 */
  line-height: 1; /* 调整行高以确保两行文字紧凑排列 */
  margin-bottom: 5px; /* 调整与下一行文字的间距 */
  margin-left: 5px;
}

.title-bottom {
  font-size: 20px; /* 较小的字体大小 */
  line-height: 1;
  color: rgb(255, 255, 239) ;
  margin-bottom: 5px; /* 调整与下一行文字的间距 */
  margin-left: 5px;
}
  .logo-title-container {
  display: flex;
  align-items: center;
    }

  .title-link {
    text-decoration: none;
    color: rgb(255, 255, 239)
  }
  .title-link:hover{
    text-decoration: none;
    color: rgb(255, 255, 239)
  }

  header {
  top: 0; /* 确保header位于页面顶部 */
  left: 0; /* 与页面左边界对齐 */
  width: 100%; /* header宽度填满整个视口宽度 */
  background-color: #333;
  color: white;
  padding: 30px;
  display: flex;
  justify-content: space-between; /* 左右对齐 */
  align-items: center; /* 垂直居中 */
  box-shadow: 0 2px 5px rgba(0,0,0,0.2); /* 可选：添加一些阴影效果，以提升视觉效果 */
  z-index: 1000; /* 确保header位于页面其他内容之上 */
}
  
  nav ul {
    list-style-type: none; /* 去掉默认的列表样式 */
    margin-right: 80px;
    margin: 0; /* 必须要有，否则padding不为0时，底部会额外增加间距，无法垂直居中显示 */
    margin-right: 150px;
  }
  
  nav ul li {
    display: inline; /* 横向排列 */
    margin-right: 40px;
  }
  
  nav ul li a {
    color: white;
    text-decoration: none; 
  }
  nav ul li a:hover{
    color: rgb(119, 180, 34);
    text-decoration: none;
    font-weight: bold;
  }
  </style>
  