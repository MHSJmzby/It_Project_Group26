<template>
  <!--    Head   -->
  <UserHeader/>

  <!--    Body     -->
  <div style="display: flex">
    <!--      Sidebar  侧边栏   -->
    <UserAside/>
    <!--  Content    -->
    <router-view style="flex: 1"/>
  </div>
</template>

<script>
import UserAside from "@/components/UserAside";
import UserHeader from "@/components/UserHeader";

export default {
  name: "Layout",
  components: {
    UserHeader,
    UserAside
  }
}
</script>

<style scoped>

</style>