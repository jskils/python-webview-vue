export const menus = [
    {
        key: 'home',
        hidden: false,
        name: '首页',
        component: () => import('./home/Index.vue'),
    },
    {
        key: 'test',
        hidden: false,
        name: '测试',
        component: () => import('./test/Index.vue'),
    }
]