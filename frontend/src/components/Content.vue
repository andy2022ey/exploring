<template>
    <div v-html="content"></div>
  </template>
  
  <script setup>
  import { defineProps } from 'vue';
  
  const props = defineProps(['content']);
  </script>

<style scoped>
  div {
    padding: 20px;
    margin-left: 400px;
    position: fixed;
    top: 125px;
    bottom: 0;
  }
</style>