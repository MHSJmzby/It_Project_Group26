<template>
  <div
      style="width: 400px; margin: 60px auto"
      class="flex flex-col justify-center items-center inline-flex"
      :style="{boxShadow: '--el-box-shadow-dark',}"
  >
    <el-tabs type="border-card">
      <div style="margin: 10px; font-size: large; font-weight: bold; text-align: center">
        Movie Ticket Online Ordering System
      </div>

      <el-form
          :label-position="'top'"
          label-width="100px"
          ref="form"
          :model="form"
          :rules="rules"
          style="margin-top: 50px; max-width: 460px;"
      >
        <el-form-item label="Username" prop="name">
          <el-input v-model="form.name" />
        </el-form-item>
        <el-form-item label="Password" prop="password">
          <el-input v-model="form.password" />
        </el-form-item>
        <el-form-item style=" padding-left: 150px; padding-top: 10px">
          <el-button color='black' type="primary" @click="login">
            Login
          </el-button>
        </el-form-item>
        <el-form-item style="margin-left: 110px">
          <div style="width: 100%">Don't have a Account?</div>
          <el-link style="margin-left: 40px" type="primary" @click="$router.push('/register')">Sign up</el-link>
        </el-form-item>
        <el-form-item style="margin-left: 100px">
          <el-radio-group v-model="form.state" class="ml-4" size="small">
            <el-radio label="0" border >User</el-radio>
            <el-radio label="1" border >Admin</el-radio>
          </el-radio-group>
        </el-form-item>
      </el-form>
    </el-tabs>
  </div>
</template>

<script>
import router from "@/router";
import request from "@/utils/request";
export default {
  name: "Login",
  components: {},
  data() {
    return {
      form: {
        state: '0',
      },
      rules: {
        name: [
          {required: true, message: 'Please input username', trigger: 'blur'},
        ],
        password: [
          {required: true, message: 'Please inout password', trigger: 'blur'},
        ],
      },
    }
  },
  methods: {
    login () {
      this.$refs['form'].validate((valid) => {
        if (valid) {
          request.post("/login/", this.form).then(res => {
            if (res.code === '0') {
              this.$message({
                type: "success",
                message: "Login Successfully"
              })
              console.log(JSON.parse(res.data))
              sessionStorage.setItem("user", JSON.stringify(res.data))  // 缓存用户信息
              // 登录成功的时候更新当前路由
              // activeRouter()
              if (this.form.state == 0) {  //User
                router.push("/booking")
              } else {
                router.push("/movies")  //Admin
              }
            } else {
              this.$message({
                type: "error",
                message: res.msg
              })
            }
          })
        }
      })
    }
  }
}
</script>

<style scoped>
</style>
