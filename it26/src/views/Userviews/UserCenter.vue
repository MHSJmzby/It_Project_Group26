<template>
  <div style="width: 100%; padding: 10px; position: center">
<!--    Personal Information-->
    <div style="margin: 10px" class="demo-basic--circle">
      <div class="block">
        <el-avatar :size="100" :src="'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'" />
      </div>
    </div>
    <el-card style="width: 40%; ">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="ID" prop="id">
          <el-input v-model="form.id" disabled></el-input>
        </el-form-item>
        <el-form-item label="Username" prop="name">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="Email" prop="email">
          <el-input v-model="form.email"></el-input>
        </el-form-item>
        <el-form-item label="Password" prop="password">
          <el-input v-model="form.password" show-password></el-input>
        </el-form-item>
      </el-form>
      <div style="text-align: center">
        <el-button type="primary" @click="Dialoguser=true">Save</el-button>
      </div>
    </el-card>
  </div>

  <div>
    <el-dialog
        v-model="Dialoguser"
        title="Tips"
        width="30%"
        align-center
    >
      <span>Do you confirm the Edit?</span>
      <template #footer>
        <span class="dialog-footer">
          <el-button type="primary" @click="update">
            Confirm
          </el-button>
          <el-button @click="Dialoguser = false">Cancel</el-button>
        </span>
      </template>
    </el-dialog>
  </div>
</template>

<script>
import request from "@/utils/request";

export default {
  name: "UserCenter",
  components: {

  },
  data() {
    return {
      Dialoguser: false,
      form: {},

    }


  },
  created() {
    let str = sessionStorage.getItem("user") || "{}"
    console.log(JSON.parse(JSON.parse(str))[0]["fields"])
    let temp=JSON.parse(JSON.parse(str))[0]["fields"]
    temp["id"]=JSON.parse(JSON.parse(str))[0]["pk"]
    this.form = temp
  },
  methods: {
    update() {
      request.put("/usercenter/", this.form).then(res => {
        console.log(res)
        if (res.code === '0') {
          this.$message({
            type: "success",
            message: "Update Successfully"
          })
          sessionStorage.setItem("user", JSON.stringify(this.form))
          // 触发Layout更新用户信息
          this.$emit("userInfo")
        } else {
          this.$message({
            type: "error",
            message: res.msg
          })
        }
        this.Dialoguser = false
      })
    }

  }
}
</script>

<style scoped>

</style>