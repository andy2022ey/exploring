
<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const items = ref([]);
const error = ref(null);


onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/items/');
    items.value = response.data;
  } catch (err) {
    error.value = err.message;
  }
});
</script>


<template>
  <div id="app">
    <div>
    <h1>Hello World!</h1>
    </div>
    <br>
    <ul>
      <li v-for="item in items" :key="item.id">
        {{ item.title }}
      </li>
    </ul>
    <div v-if="error">
      {{ error }}
      </div>
  </div>
</template>


<style>
/* Your styles here */
</style>
