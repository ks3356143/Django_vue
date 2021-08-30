<template>
  <div id="app">
    <a-layout>
      <a-layout-sider
        breakpoint="lg"
        collapsedWidth="0"
        @collapse="onCollapse"
        @breakpoint="onBreakpoint"
        style="background: #2f4f4f"
      >
        <div class="logo">
          <router-link to="/">
            <HomeFilled></HomeFilled>
            <!--<font-awesome-icon :icon="['fab', 'autoprefixer']" size="3x" inverse />-->
            <h2 style="color: #fff; margin: 10px">Automation Center</h2>
          </router-link>
        </div>
        <hr style="width: 90%" />
        <a-menu
          mode="inline"
          :openKeys="openKeys"
          @openChange="onOpenChange"
          style="background: #2f4f4f; color: #fff"
        >
          <a-sub-menu key="sub1">
            <template v-slot:title>
              <span><a-icon type="project" /><span>Projects</span></span>
            </template>
            <a-menu-item key="1">ByBlog</a-menu-item>
            <a-menu-item key="2">MobileSTF</a-menu-item>
            <a-menu-item key="3">RestAPI</a-menu-item>
          </a-sub-menu>
          <a-sub-menu key="sub2">
            <template v-slot:title>
              <span><a-icon type="setting" /><span>Settings</span></span>
            </template>
            <a-menu-item key="1">Projects</a-menu-item>
            <a-menu-item key="2">Users</a-menu-item>
          </a-sub-menu>
        </a-menu>
      </a-layout-sider>
      <a-layout>
        <a-affix style="height: 64px">
          <a-layout-header style="background: #fff; border-bottom: 1px solid #e8e8e8">
            <a-input-search
              placeholder="input keyword..."
              @search="onSearch"
              enterButton
              style="width: 40%; margin: 15px 0px; float: left"
            />
            <div id="header-right" style="float: right">
              <font-awesome-layers class="fa-fw fa-1x">
                <font-awesome-icon :icon="['fas', 'bell']" />
                <font-awesome-layers class="fa-layers-counter fa-layers-top-right">{{
                  notifications
                }}</font-awesome-layers> </font-awesome-layers
              >&emsp;{{ notifications }}
              <a-divider type="vertical" />
              Bob Jiang
              <a-icon type="tool" />
            </div>
          </a-layout-header>
        </a-affix>
        <a-layout-footer style="text-align: center">
          {{ fullCopyRight }}
        </a-layout-footer>
      </a-layout>
    </a-layout>
    <router-view />
  </div>
</template>

<script>
import axios from "axios";
import HomeFilled from "@ant-design/icons-vue/HomeFilled";
export default {
  name: "App",

  data() {
    return {
      rootSubmenuKeys: ["sub1", "sub2"],
      openKeys: ["sub1"],
      notifications: 3,
      copyRightPrefix: "Copyright © ",
      copyRightSuffix: " BobJiang | byincd.com",
    };
  },

  created: function () {
    axios.interceptors.response.use(
      (response) => {
        return response;
      },
      (error) => {
        if (error.response) {
          switch (error.response.status) {
            case 401:
              // 返回 401 清除token信息并跳转到登录页面
              console.log("unauthorized or expired, Please login first");
              this.$store.dispatch("logout");
              this.$router.replace({
                path: "login",
                query: { redirect: this.$router.currentRoute.fullPath },
              });
          }
        }
        return Promise.reject(error.response.data); // 返回接口返回的错误信息
      }
    );
  },

  methods: {
    onCollapse(collapsed, type) {
      console.log(collapsed, type);
    },

    onBreakpoint(broken) {
      console.log(broken);
    },

    onOpenChange(openKeys) {
      const latestOpenKey = openKeys.find((key) => this.openKeys.indexOf(key) === -1);
      if (this.rootSubmenuKeys.indexOf(latestOpenKey) === -1) {
        this.openKeys = openKeys;
      } else {
        this.openKeys = latestOpenKey ? [latestOpenKey] : [];
      }
    },

    onSearch(value) {
      console.log(value);
    },
  },

  computed: {
    fullCopyRight: function () {
      return this.copyRightPrefix + new Date().getFullYear() + this.copyRightSuffix;
    },
  },

  components: {
    HomeFilled,
  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  min-height: 100%;
}

.logo {
  margin: 10px 5px;
}

.ant-menu {
  text-align: left;
}

#root,
body,
html {
  height: 100%;
}

.ant-layout {
  display: flex;
  width: 100%;
  min-height: 100%;
}
</style>
