<script setup>
import api from "@/api/api.js";
import {Modal} from "ant-design-vue";

const test = async () => {
  const result = await api.test()
  Modal.confirm({
    title: 'test',
    content: result,
    okText: 'Yes',
    okType: 'danger',
    cancelText: 'No',
    onOk() {
      console.log('OK');
    },
    onCancel() {
      console.log('Cancel');
    },
  });
}
</script>

<template>
  <a @click="test">点我试一下</a>
</template>

<style scoped>

</style>