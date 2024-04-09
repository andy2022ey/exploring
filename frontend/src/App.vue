
<script setup>
import { ref, reactive, onMounted } from 'vue';
import axios from 'axios';
import Header from './components/Header.vue';
import Sidebar from './components/Sidebar.vue';
import Content from './components/Content.vue';

const items = ref([]);
const selectedContent = ref('');
const themes = ref({});

const loadThemes = async () => {
  const response = await fetch('content.json'); // 假设文件位于public目录
  if (response.ok) {
    const data = await response.json();
    themes.value = data;
    console.log('Themes loaded:', themes.value);
  } else {
    console.error('Failed to load themes:', response.statusText);
  }
};

onMounted(loadThemes);

const handleThemeSelected = (theme) => {
  items.value = themes[theme];
  selectedContent.value = items.value[0]?.content || ''; // 使用可选链和空值合并操作符
};

const handleItemSelected = (item) => {
  selectedContent.value = item.content;
};

//const items = ref([]);
//const error = ref(null);
//onMounted(async () => {
//  try {
//    const response = await axios.get('http://127.0.0.1:8000/items/');
//    items.value = response.data;
//  } catch (err) {
//    error.value = err.message;
//  }
// });
</script>


<template>

  <div id="app">
    <Header @themeSelected="handleThemeSelected" />
    <div class="container">
      <Sidebar :items="items" @itemSelected="handleItemSelected" />
      <Content :content="selectedContent" />
    </div>
  </div>

</template>


<style>
  .container {
    display: flex;
    width: 100%; /* 可根据需要调整 */
  }
</style>
