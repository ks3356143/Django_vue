<template>
  <div id="app">
    <router-view></router-view>
    <home></home>
  </div>
</template>

<script>
import Home from "@/components/home.vue";

export default {
  name: "app",
  components: {
    Home,
  },
  created() {},
};
</script>

<style></style>
