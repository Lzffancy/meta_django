<template>

 <div class="row">
   <message_board/>
 </div>

</template>

<script>
//注册组件
// import HelloWorld from './components/HelloWorld.vue'
import message_board from "@/components/message_board";
export default {
  name: 'App',
  components: {
    message_board
  }
}
</script>

<style>
</style>
