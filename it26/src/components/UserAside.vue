<template>
  <div >
    <el-menu
        style="width: 150px; min-height: calc(100vh - 50px)"
        default-active="booking"
        class="el-menu-vertical-demo"
        router
    >
      <el-menu-item index="booking" style="padding-left: 25px">
        <span>Movie Booking</span>
      </el-menu-item>
      <el-menu-item index="historyorder" style="padding-left: 25px">
        <span>History Order</span>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: "Aside"
}
</script>

<style scoped>

</style>