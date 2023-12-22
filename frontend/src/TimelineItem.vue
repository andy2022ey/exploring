<template>
    <li>
      <div class="direction-r">
        <div class="flag-wrapper">
          <span class="flag">{{ title }}</span>
          <span class="time-wrapper"><span class="time">{{ time }}</span></span>
        </div>
        <div class="desc" v-html="description"></div>
      </div>
    </li>
  </template>
  
  <script setup>
  import { defineProps } from 'vue';
  
  const props = defineProps({
    title: String,
    time: String,
    description: String
  });
  </script>
  <style scoped lang="scss"> //需要安装相关库 npm install --save-dev sass-loader sass
  @import './assets/css/timeline.scss';
  </style>
  