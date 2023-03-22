<template>
  <div >
    <el-menu
        style="width: 210px; min-height: calc(100vh - 50px);"
        default-active="movies"
        class="el-menu-vertical-demo"
        router
    >
      <el-menu-item index="movies" style="padding-left: 35px">
        <span  class="menu-item-text">Movie Management</span>
      </el-menu-item>
      <el-menu-item index="schedule" style="padding-left: 25px">
        <span>Schedule Management</span>
      </el-menu-item>
      <el-menu-item index="dataAnalysis" style="padding-left: 50px">
        <span>Data Analysis</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "ManagerAside"
}
</script>

<style scoped>

</style>
