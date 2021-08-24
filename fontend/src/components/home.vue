<template>
  <div>
    <h3>{{ msg }}</h3>
    <button
      type="button"
      @click="getProjects"
      :style="{ margin: '10px', padding: '5px' }"
    >
      获取project数据
    </button>
    <table
      :style="{ border: '2px solid gray', borderRadius: '5px', padding: '10px' }"
      align="center"
    >
      <tr v-for="p in projects" v-bind:key="p">
        <td>{{ p.id }}</td>
        <td>{{ p.name }}</td>
        <td>{{ p.create_time }}</td>
        <td>{{ p.update_time }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import { request } from "@/network/request.js";
export default {
  name: "Home",
  data() {
    return {
      msg: "获取数据哦！",
      projects: [],
    };
  },

  methods: {
    getProjects() {
      request({ url: "/api/projects" }).then((res) => {
        {
          console.log(res);
          this.projects = res.data;
        }
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
