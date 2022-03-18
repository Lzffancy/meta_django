<template>
  <!--  一个叫row的样式类-->
  <div class="row">
    <div class="col-md-8">
      <table class="table table-bordered">
        <thead>
        <tr>
          <!--        表头-->
          <th>title</th>
          <th>author</th>
          <th>content</th>
          <th>time</th>
          <th>option</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="item in ly_list" :key="item.url">
          <!--        内容-->
          <td>{{item.title}}</td>
          <td>{{item.author}}</td>
          <td>{{item.content}}</td>
          <td>{{item.c_time}}</td>
          <td>
            <button class="btn btn-success" title="add" style="margin:0 10px ">
              <p>add</p>
              <i class="bi bi-plus-circle"></i>
            </button>
            <button class="btn btn-delete" title="delete">
              <p>delete</p>
              <i class="bi bi-x-square"></i>
            </button>
          </td>

        </tr>
        </tbody>
      </table>
    </div>

    <div class="col-md-4">
    </div>
  </div>

</template>

<script>
import axios from "axios";
import {reactive, onMounted, toRefs} from "vue";

export default {
  name: "message_board",
  setup() {
    let base_url = "http://127.0.0.1:8001/rest_api/message_board/"
    const state = reactive({
      ly_list: []
    })
    const get_message_board = () => {
      axios.get(base_url).then(res => {
        state.ly_list = res.data
      }).catch(err => {
        console.log(err)
      })
    }
    onMounted(() => {
      get_message_board()
    })
    return {
      ...toRefs(state)
    }
  }
}
</script>

<style scoped>

</style>