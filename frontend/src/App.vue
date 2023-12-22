<script setup>
import { ref, reactive, computed, onMounted, watch} from 'vue'
import ChildComp from './ChildComp.vue'
import TimelineItem from './TimelineItem.vue'
const msg1 = ref('Hello Vue 3 + Vite')
const msg2 = reactive({ text: 'Hello' })
const msg3 = ref(0)
const red_class = ref('red_text')
const msg4 = ref()
const msg5 = ref(true)

// v-for :todo list
let id = 0
const newTodo = ref('')
const hideCompleted = ref(false)
const todos = ref([
  { id: id++, text: 'Learn HTML', done: true},
  { id: id++, text: 'Learn JavaScript', done: true },
  { id: id++, text: 'Learn Vue', doen: false }])
const filteredTodos = computed(() => {
  return hideCompleted.value
    ? todos.value.filter((todo) => !todo.done)
    : todos.value
})
const pElementRef = ref(null)
const todoId = ref(1)
const todoData = ref(null)
const greeting = ref('Hello from parent')
const childMsg = ref('No child msg yet')
const slot_msg = ref('slot msg from parent')

const timelineItems = ref([
  {id: 1,
    title: "Freelance",
    time: "2010 - 2016",
    description: 'Som freelance Fullstack Developer arbejder jeg med et hav af kunder, hjemmesider og apps. Jeg har tidligere designet og udviklet hjemmesider og andre løsninger for arkitekter, bilforhandlere, skoler, designere, fotografer og manger flere. Læs mere: <a href="https://tristanwhite.info" target="_top">https://tristanwhite.info</a>'
  },
  {id: 2,
    title: "Uddannelse",
    time: "2016 - 2020",
    description: 'Jeg har læst til multimediedesigner på Erhvervsakademi Dania i Skive. Jeg har lært at designe og udvikle hjemmesider, apps, spil og meget mere. Jeg har også lært at arbejde med SEO, marketing og kommunikation. Læs mere: <a href="https://eadania.dk" target="_top">https://eadania.dk</a>'
  },
]);


function toggle() {
  msg5.value = !msg5.value
}

function increment() {
  msg3.value++
}

function addTodo() {
  todos.value.push({ id: id++, text: newTodo.value , done: false})
  newTodo.value = '' // clear input
}
function removeTodo(todo) {
  todos.value = todos.value.filter((t) => t !== todo)
}
onMounted(() => {
  pElementRef.value.textContent = 'i have been mounted'
})
async function fetchData() {
  todoData.value = null
  const res = await fetch(`https://jsonplaceholder.typicode.com/todos/${todoId.value}`)
  todoData.value = await res.json()
}

fetchData()
watch(todoId, fetchData)


</script>

<template>
<p>{{ msg1 }}</p>
<p >{{ msg2.text }}</p>
<!--v-on:监听DOM事件-->
<button @click="increment">count is: {{ msg3 }}</button>
<!--v-bind：给属性绑定动态值-->
<p :class="red_class">red text</p>
<!--v-model：双向绑定-->
<input v-model="msg4"/>

<p>{{ msg4 }}</p>

<button @click="toggle">toggle</button>
<h1 v-if="msg5">v-if</h1>
<h1 v-else>v-else</h1>


<form @submit.prevent="addTodo">
  <input v-model="newTodo" />
  <button>Add Todo</button>
</form>
<ul>
  <li v-for="todo in filteredTodos" :key="todo.id">
    <input type="checkbox" v-model="todo.done"/>
    <span :class="{ done: todo.done }"> {{ todo.text }} </span>
    <button @click="removeTodo(todo)">x</button>
  </li>
</ul>
<button @click="hideCompleted = !hideCompleted">
{{ hideCompleted ? 'Show all' : 'Hide completed' }}
</button>
<p ref="pElementRef">hello</p>

<p>Todo id: {{ todoId }}</p>
<button @click="todoId++">Fetch next data</button>
<p v-if="!todoData">Loading...</p>
<pre v-else>{{ todoData }}</pre>
<ChildComp :msg="greeting" @response="(msg) => childMsg = msg">
  {{ slot_msg }}
</ChildComp>
<p>Child msg: {{ childMsg }}</p>

<ul class="timeline">
    <timeline-item
      v-for="item in timelineItems"
      :key="item.id"
      :title="item.title"
      :time="item.time"
      :description="item.description"
    ></timeline-item>
  </ul>
</template>

<style scoped lang="scss">
@import './assets/css/app.scss';
@import './assets/css/timeline.scss';
</style>
