import {request} from '@/network/request.js'
import axios from 'axios'

export default {
    login({commit},user){
        return new Promise((resolve,reject)=>{
            commit('auth_request')
            request({
                url:'api-token-auth/',
                data:user,
                method:'POST'
            }).then(res=>{
                const token = res.data.token
                const user = res.data.username
                localStorage.setItem('token',token)
                localStorage.setItem('user',user)
                axios.defaults.headers.common['Authorization'] = 'Token ' + token
                commit('auth_success_token',token)
                commit('auth_success_user',user)
                resolve(res)
                //上面是在登录后将token家到默认headers里面，便于后续调用需要登录权限的api
                }).catch(err=>{
                    commit('auth_error')
                    localStorage.removeItem('token')
                    reject(err)
            })
        })
    },
    logout({commit}){
        return new Promise((resolve,reject)=>{
            commit('logout')
            localStorage.removeItem('token')
            localStorage.removeItem('user')
            delete axios.defaults.headers.common['Authorization']
            resolve()
        })
    }
}