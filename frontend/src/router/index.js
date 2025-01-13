// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';

// 引入页面组件
import Home from '../views/Home.vue';
import Test from '../views/Test.vue';

// 路由配置
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/test',
    name: 'Test',
    component: Test
  }
];

// 创建路由实例
const router = createRouter({
  history: createWebHistory(), // 使用 HTML5 History 模式
  routes
});

export default router;
