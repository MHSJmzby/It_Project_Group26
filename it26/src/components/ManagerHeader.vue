<template>
  <div style=" height: 50px; line-height: 50px; border-bottom: 1px solid #ccc; display: flex">
    <div style=" width: 500px; padding-left: 30px; font-weight: bold; color: dodgerblue">Movie Ticket Online Ordering System —— Manager</div>
    <div style="flex: 1"></div>
    <div style="width: 130px; padding-top: 15px">
      <el-dropdown>
        <span class="el-dropdown-link">
          Manager Centre
        </span>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item @click="$router.push('/login')">Log out</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
    </div>
  </div>
</template>

<script>
export default {
  name: "ManagerHead"
}
</script>

<style scoped>

</style>