<template>
  <div>
    <h3>{{ msg }}</h3>
    <button
      type="button"
      @click="getProjects"
      :style="{ margin: '10px', padding: '5px' }"
    >
      获得Projects数据
    </button>
    <a
      v-if="this.$store.state.token"
      @click="logout"
      :style="{ margin: '10px', padding: '5px' }"
      >Logout</a
    >
    <router-link v-else to="/login" :style="{ margin: '10px', padding: '5px' }"
      >点击登录</router-link
    >
    <p>{{ auth_text }}</p>
    <p>{{ this.$store.state.token }}</p>
    <p>{{ this.$store.state.status }}</p>
    <p>{{ this.$store.state.user }}</p>
    <p>{{ this.$store.getters.isLoggedIn }}</p>
    <p>{{ this.$store.getters.authStatus }}</p>
    <table
      v-if="auth.length > 0"
      :style="{ border: '2px solid gray', borderRadius: '5px', padding: '10px' }"
      align="center"
    >
      <tr v-for="a in auth" :key="a">
        <td>{{ a.id }}</td>
        <td>{{ a.username }}</td>
        <td>{{ a.email }}</td>
        <td>{{ a.token }}</td>
      </tr>
    </table>
    <table
      :style="{ border: '2px solid gray', borderRadius: '5px', padding: '10px' }"
      align="center"
    >
      <tr v-for="p in projects" :key="p">
        <td>{{ p.id }}</td>
        <td>{{ p.name }}</td>
        <td>{{ p.create_time }}</td>
        <td>{{ p.update_time }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import { request } from "@/network/request";
export default {
  name: "Home",
  data() {
    return {
      msg: "Projects数据在项目Automation Center里",
      projects: [],
      auth: [],
      auth_text: "",
    };
  },

  created: function () {
    if (this.$store.state.token) {
      this.auth_text = "已登录";
    } else {
      this.auth_text = "暂未登录";
    }
  },

  methods: {
    getProjects() {
      request("api/projects").then((response) => {
        (this.projects = response.data), (this.msg = "已获得Django数据");
      });
    },

    logout: function () {
      this.$store.dispatch("logout").then(() => {
        this.$router.push("/login");
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
