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
          :rules="rules"
      >
        <el-form-item label="Email">
          <el-input v-model="form.email" />
        </el-form-item>
        <el-form-item label="Username">
          <el-input v-model="form.name" />
        </el-form-item>
        <el-form-item label="Password">
          <el-input v-model="form.password" />
        </el-form-item>
        <el-form-item label="Confirm Password">
          <el-input v-model="form.confirm" />
        </el-form-item>
        <el-form-item style=" padding-left: 150px; padding-top: 10px">
          <el-button color='black' @click="regist">
            Sign up
          </el-button>
        </el-form-item>
      </el-form>
    </el-tabs>
  </div>
</template>

<script>
import router from "@/router";
import request from "@/utils/request";

export default {
  name: "Register",
  components: {},
  data() {
    return {
      form: {},
      rules: {
        email: [
          {required: true, message: 'Please input Email', trigger: 'blur'},
        ],
        name: [
          {required: true, message: 'Please input Username', trigger: 'blur'},
        ],
        password: [
          {required: true, message: 'Please input Password', trigger: 'blur'},
        ],
        confirm: [
          {required: true, message: 'Please confirm Password', trigger: 'blur'},
        ],
      },
    }
  },
  methods: {
    regist() {
      if (this.form.password !== this.form.confirm) {
        this.$message({
          type: "error",
          message: 'The 2 passwords entered are inconsistent!'
        })
        return
      }

      this.$refs['form'].validate((valid) => {
        if (valid) {
			console.log(this.form)
          // if (this.form.id) {
            request.post("/register/", this.form).then(res => {
              console.log(res)
              if (res.code === '0') {
                this.$message({
                  type: "success",
                  message: "Register Successfully!"
                })
                router.push("/")
              } else {
                this.$message({
                  type: "error",
                  message: "res.msg"
                })
              }
            })
          // }
        }
      })
    }
  }
}
</script>

<style scoped>

</style>