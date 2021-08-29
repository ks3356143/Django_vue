<template>
  <div id="app">
    <router-view></router-view>
    <home></home>
  </div>
</template>

<script>
import Home from "@/components/home.vue";
import Antd from "ant-design-vue";
import "ant-design-vue/dist/antd.css";
export default {
  name: "app",
  components: {
    Home,
  },
  created() {},
};
</script>

<style></style>
