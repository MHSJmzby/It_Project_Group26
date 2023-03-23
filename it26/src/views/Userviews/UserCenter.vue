<template>
<div>
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
        <el-button type="primary" @click="outerVisible=true">Save</el-button>
      </div>
    </el-card>
  </div>

  <div>
    <el-dialog v-model="outerVisible" title="Tips" width="30%">
    <span>
      If you change your information, you will need to log in again.
      Do you confirm the Edit?
    </span>
      <template #footer>
      <span class="dialog-footer">
        <el-button @click="outerVisible = false">Cancel</el-button>
        <el-button type="primary" @click="innerVisible = true">
          Confirm
        </el-button>
      </span>
      </template>
    </el-dialog>
    <el-dialog
          v-model="innerVisible"
          width="30%"
          title="Warning"
          append-to-body
      >
      <span>Are you sure to log out?</span>
      <template #footer>
      <el-button @click="cancel">Cancel</el-button>
      <el-button type="primary" @click="update">
        Log out
      </el-button>
      </template>
    </el-dialog>
  </div>
</div>
</template>

<script>
import request from "@/utils/request";
import router from "@/router";

export default {
  name: "UserCenter",
  components: {

  },
  data() {
    return {
      outerVisible: false,
      innerVisible: false,
      form: {},

    }


  },
  created() {
    this.load()
  },
  methods: {
    load() {
      let str = sessionStorage.getItem("user") || "{}"
      // console.log(JSON.parse(JSON.parse(str))[0]["fields"])
      let temp=JSON.parse(JSON.parse(str))[0]["fields"]
      console.log(temp)
      temp["id"]=JSON.parse(JSON.parse(str))[0]["pk"]
      this.form = temp
      console.log(temp)
    },
    update() {
      request.put("/usercenter/", this.form).then(res => {
        // console.log(res)
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
        router.push("/")
      })
    },
    cancel(){
      this.outerVisible = false
      this.innerVisible = false
    }

  }
}
</script>

<style scoped>

</style>
