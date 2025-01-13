<script setup>


const test = () => {
  window.pywebview.api.test("test").then((res) => {
    console.log(res)
  })
}
</script>

<template>
  <div>点我试一下：
    <a @click="test">
      test
    </a>
  </div>
</template>

<style scoped>

</style>