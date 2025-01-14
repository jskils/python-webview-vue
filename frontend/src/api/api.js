import {message} from 'ant-design-vue';

async function getData(res) {
    const {success, message: errorMsg, data} = res;
    if (success) {
        return data
    }
    message.error(`error ${errorMsg}`)
}

export default {
    async test() {
        const res = await window.pywebview.api.test("test123123")
        return getData(res)
    },
    async appInfo() {
        const res = await window.pywebview.api.app_info()
        return getData(res)
    }
}