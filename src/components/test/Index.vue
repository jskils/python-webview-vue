<script setup>
import {Message} from "@arco-design/web-vue";

const test = () => {
  window.pywebview.api.test("test").then((res) => {
    Message.info(res)
  })
}
</script>

<template>
  <a-empty/>
  <div>点我试一下：
    <a-link @click="test">
      test
    </a-link>
  </div>
</template>

<style scoped>

</style>