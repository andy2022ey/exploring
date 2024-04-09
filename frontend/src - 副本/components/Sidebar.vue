<template>
    <div class="sidebar">
      <ul>
        <li v-for="(item, index) in items" :key="index">
            <a href="#" @click="selectItem(item)">{{ item.title }}</a>
        </li>
      </ul>
    </div>
  </template>
  
  <script setup>
  import { defineProps, defineEmits } from 'vue';
  
  const props = defineProps(['items']);
  const emit = defineEmits(['itemSelected']);
  
  const selectItem = (item) => {
    console.log('Item selected:', item);
    emit('itemSelected', item);
  };
  </script>

  <style scoped>
    .sidebar {
        width: 400px;
        padding: 20px;
        background-color: #f0f0f0;
        position: fixed;
        top: 125px;
        bottom: 0;
        overflow-y: auto;
    }
    ul {
        list-style-type: none;
        padding-left: 0;
    }
    li {
        margin-bottom: 0px;
    }
    a {
        text-decoration: none;
        color: #333;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
  