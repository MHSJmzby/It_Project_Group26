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
          style="margin-top: 50px; max-width: 460px;"
      >
        <el-form-item label="Username">
          <el-input v-model="form.name" />
        </el-form-item>
        <el-form-item label="Password">
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
            <el-radio label="1" border @click="form.state = 0">User</el-radio>
            <el-radio label="2" border @click="form.state = 1">Admin</el-radio>
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
  rules: {
    username: [
      {required: true, message: '请输入用户名', trigger: 'blur'},
    ],
    password: [
      {required: true, message: '请输入密码', trigger: 'blur'},
    ],
  },
  data() {
    return {
      radio: '1',
      form: [
        {
          state: 0,
        }
      ],
    }
  },
  methods: {
    login () {
      this.$refs['form'].validate((valid) => {
        if (valid) {
          request.post("/", this.form).then(res => {
            if (res.code === '0') {
              this.$message({
                type: "success",
                message: "Login Successfully"
              })
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