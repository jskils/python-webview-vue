<template>
  <a-config-provider :theme="themeConfig">
    <a-layout>
      <a-layout-header class="header">
        <a-menu
            v-model:selectedKeys="selectedKeys"
            mode="horizontal"
            :style="{ width: '100%',lineHeight: '40px'}"
        >
          <a-menu-item key="1">
            <RouterLink to="/">Home</RouterLink>
          </a-menu-item>
          <a-menu-item key="2">
            <RouterLink to="/test">Test</RouterLink>
          </a-menu-item>
        </a-menu>
      </a-layout-header>
      <a-layout-content class="content">
        <div class="view">
          <RouterView/>
        </div>
      </a-layout-content>
    </a-layout>
  </a-config-provider>
</template>
<script setup>
import {ref} from "vue";
import {theme} from 'ant-design-vue';

const themeConfig = {algorithm: theme.darkAlgorithm, token: {colorPrimary: '#ffffff', borderRadius: 2}}

const selectedKeys = ref(['1']);

</script>
<style scoped>
.header {
  background: #141414;
  position: fixed;
  z-index: 1;
  width: 100%;
  height: 40px
}

.content {
  margin-top: 30px;
}

.view {
  padding: 24px 12px 0 12px;
  height: calc(100vh - 30px);
}
</style>