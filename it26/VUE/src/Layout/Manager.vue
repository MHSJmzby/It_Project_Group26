<template>
  <!--    Head   -->
  <ManagerHeader/>

  <!--    Body     -->
  <div style="display: flex">
    <!--      Sidebar  侧边栏   -->
    <ManagerAside/>
    <!--  Content    -->
    <router-view style="flex: 1"/>
  </div>
</template>

<script>
import ManagerAside from "@/components/ManagerAside";
import ManagerHeader from "@/components/ManagerHeader";

export default {
  name: "Manager",
  components: {
    ManagerHeader,
    ManagerAside
  }
}
</script>

<style scoped>

</style>