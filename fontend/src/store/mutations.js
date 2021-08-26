export default {
    auth_request(state){
        state.status = 'loading'
    },
    auth_success_token(state,token){
        state.status = 'success'
        state.token = token //这里不在state初始化就是实时获取
    },
    auth_success_user(state,user){
        state.status = 'success'
        state.user = user
    },
    auth_error(state){
        state.status = 'error'
    },
    logout(state){
        state.status = '',
        state.token = '',
        state.user = ''
    }
}