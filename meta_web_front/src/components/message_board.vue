<template>
<div class="row">
  <div class="row">
  <div class="col-sm-6 col-md-4">
    <div class="thumbnail">
<!--      <img src="..." alt="...">-->
      <div class="caption">
        <h3>Thumbnail label</h3>
        <p v-for ="item in ly_lits" :key="item.url">...</p>
        <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
      </div>
    </div>
  </div>
</div>
</div>
</template>

<script>
import axios from "axios";
import {reactive, onMounted,toRefs} from "vue";
export default {
  name: "message_board",
  setup(){
    let base_url = "http://127.0.0.1:8001/rest_api/message_borad/"
    const state =reactive({
      ly_list:[]
    })
    const get_message_board = () =>{
      axios.get(base_url).then(res=>{
          state.ly_list =res.data
      }).catch(err=>{console.log(err)})
    }
      onMounted(()=>{
    get_message_board()
})
    return{
      ...toRefs(state)
    }
  }
}
</script>

<style scoped>

</style>