<template>
  <a-menu mode="horizontal" :default-selected-keys="[defaultMenuKey]" @menu-item-click="loadComponent">
    <a-menu-item key="0" :style="{ padding: 0, marginRight: '38px' }" disabled>
      <a-avatar :size="30"><img alt="avatar" :src="Logo"/></a-avatar>
      <span class="app_name">Python Webview Vue</span>
    </a-menu-item>
    <a-menu-item v-for="menu in menus" :key="menu.key">{{ menu.name }}</a-menu-item>
  </a-menu>
  <div class="content">
    <component :is="currentComponent"></component>
  </div>
</template>
<script setup>
import Logo from "@/assets/favicon.ico"
import {menus} from './menus.js';
import {ref} from "vue";

const defaultMenuKey = ref(menus[0].key)
const currentComponent = ref(null)

const loadComponent = async (key) => {
  const menu = menus.find(menu => menu.key === key);
  if (menu) {
    currentComponent.value = (await menu.component()).default;
  }
};
loadComponent(defaultMenuKey.value);
</script>
<style scoped>

.app_name {
  margin-left: 10px;
  background-image: linear-gradient(to right, #a727b2, #2cbbd9, #2a3b91);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.content {
  margin: 3px 2px 0 2px;
  background-color: white;
  border-radius: 5px;
  height: 90vh;
}

</style>