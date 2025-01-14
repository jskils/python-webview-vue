import {resolve} from 'path'
import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig(({command, mode}) => {
    const alias = {
        '~': `${resolve(__dirname, './')}`,
        '@/': `${resolve(__dirname, 'src')}/`
    }

    return {
        devtool: 'cheap-module-source-map',
        resolve: {
            alias
        },
        build: {
            outDir: '../build/gui',
            manifest: true,
            brotliSize: false,
            rollupOptions: {
                output: {
                    manualChunks: {
                        echarts: ['echarts'],
                        'ant-design-vue': ['ant-design-vue'],
                        vue: ['vue', 'vue-router', 'pinia', 'vue-i18n']
                    }
                }
            },
            chunkSizeWarningLimit: 1000
        },
        plugins: [
            vue({
                script: {
                    refTransform: true
                }
            }),
        ],
        css: {
            preprocessorOptions: {
                less: {
                    javascriptEnabled: true
                }
            }
        },
        optimizeDeps: {}
    }
})
