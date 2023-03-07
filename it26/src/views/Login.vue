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
          :model="ruleFormRef"
          style="margin-top: 50px; max-width: 460px;"
      >
        <el-form-item label="Username">
          <el-input v-model="ruleFormRef.name" />
        </el-form-item>
        <el-form-item label="Password">
          <el-input v-model="ruleFormRef.password" />
        </el-form-item>
        <el-form-item style=" padding-left: 150px; padding-top: 10px">
          <el-button color='black' type="primary" @click="login(ruleFormRef)">
            Login
          </el-button>
        </el-form-item>
        <el-form-item style="margin-left: 110px">
          <div style="width: 100%">Don't have a Account?</div>
          <el-link style="margin-left: 40px" type="primary" @click="$router.push('/register')">Sign up</el-link>
        </el-form-item>
        <el-form-item style="margin-left: 100px">
          <el-radio-group v-model="radio" class="ml-4" size="small">
            <el-radio label="1" border @click="$router.push('/user')">User</el-radio>
            <el-radio label="2" border @click="$router.push('/manager')">Admin</el-radio>
          </el-radio-group>
        </el-form-item>
      </el-form>
    </el-tabs>
  </div>
</template>

<script>
import router from "@/router";

export default {
  name: "Login",
  components: {},
  data() {
    return {
      radio: '1',
      ruleFormRef: [
        {
          name: '',
          password: '',
        }
      ],
    }
  },
  methods: {
    login() {
      // if(this.form.id) {
      //   request.post("/movies", this.form).then(res => {
      //     console.log(res)
      // if (res.code ==='0') {
      this.$message({
        type:"success",
        message: "Login Successfully!"
      })
      router.push("/user")
      // }
      // else {
      //   this.$message({
      //     type:"error",
      //     message: "res.mss"
      //   }
      // })
      // }
    }
  }
}
</script>

<style scoped>

</style>