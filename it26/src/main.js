import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementPlus from 'element-plus'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import 'element-plus/dist/index.css'


import '@/assets/css/global.css'
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    createApp(App).use(store).use(router).use(ElementPlus, {size: 'small', color: 'black'}).component(key, component).mount('#app')
}