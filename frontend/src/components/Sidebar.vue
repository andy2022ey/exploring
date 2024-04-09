<template>
    <div class="sidebar">
      <ul>
        <li v-for="(item, index) in items" :key="`level1-${index}`">
          <div @click="toggle(item)">{{ item.title }}</div>
          <ul v-if="item.children && item.expanded">
          <li v-for="(child, childIndex) in item.children" :key="`level2-${childIndex}`">
            <a href="#" @click.stop.prevent="selectItem(child)">{{ child.title }}</a>
          </li>
          </ul>
        </li>
      </ul>
    </div>
  </template>
  
  <script setup>
  import { defineProps, defineEmits} from 'vue';
  
  const props = defineProps({
    items: Array,
  });

  const toggle = (item) => {
    item.expanded = !item.expanded;
  };

  const emit = defineEmits(['itemSelected']);
  const selectItem = (item) => {  
    emit('itemSelected', item);
  };
  </script>

  <style scoped>
    .sidebar {
        width: 400px;
        padding: 20px;
        background-color: #f0f0f0;
        position: fixed;
        top: 128px;
        bottom: 0;
        overflow-y: auto;
    }
    ul {
      padding-left: 20px; /* 调整内边距以更好地展示层级结构 */
    }
    li {
      list-style-type: none; /* 移除列表项前的默认符号 */
      cursor: pointer; /* 提示用户可以点击 */
    }
    li div {
      font-weight: bold; /* 第一级目录加粗显示 */
    }
    a {
        text-decoration: none;
        color: #333;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
  