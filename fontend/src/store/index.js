import { createStore } from 'vuex'
import mutations from '@/store/mutations'
import actions from '@/store/actions'
import getters from '@/store/getters'


const state = {
  status:'',
  token:localStorage.getItem('token') || '',
  user:localStorage.getItem('user') || '',
}

export default createStore({
  state,
  mutations,
  actions,
  getters,
  modules: {
  }
})
