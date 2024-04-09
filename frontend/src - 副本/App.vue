
<script setup>
import { ref, reactive } from 'vue';
import axios from 'axios';
import Header from './components/Header.vue';
import Sidebar from './components/Sidebar.vue';
import Content from './components/Content.vue';

const items = ref([]);
const selectedContent = ref('');

const themes = reactive({
  default: [
    { title: '目录1', content: '主题1的内容1' },
    { title: '目录2', content: '主题1的内容2' },
  ],
  blog: [
    { title: '目录A', content: '主题2的内容A' },
    { title: '目录B', content: '主题2的内容B' },
  ],
  product: [
    { title: '目录X', content: '主题3的内容X' },
    { title: '目录Y', content: '主题3的内容Y' },
  ],
  knowledge: [
    { title: '目录M', content: '主题4的内容M' },
    { title: '目录N', content: '主题4的内容N' },
  ],
  business: [
    { title: '目录P', content: '主题5的内容P' },
    { title: '目录Q', content: '主题5的内容Q' },
  ],
  log: [
    { title: '目录Z', content: '主题6的内容Z' },
    { title: '目录W', content: '主题6的内容W' },
  ],
});

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
