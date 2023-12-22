<script setup>
const props = defineProps({
  msg: String
})
// 声明触发的事件
const emit = defineEmits(['response'])
// 带参数触发事件，第一个参数是事件名，第二个参数是传递的参数
emit('response', 'hello from child')

</script>

<template>
    <h2>加载子组件</h2>
    <h2> {{ msg || 'No props passed yet' }}</h2>
    <slot> Fallback content </slot>
    
</template>