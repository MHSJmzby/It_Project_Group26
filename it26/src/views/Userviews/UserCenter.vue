<template>
  <div style="width: 100%; padding: 10px; position: center">
<!--    Personal Information-->
    <div style="margin: 10px" class="demo-basic--circle">
      <div class="block">
        <el-avatar :size="100" :src="'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png'" />
      </div>
    </div>


    <el-descriptions
        title=""
        direction="horizontal"
        :column="1"
        border
        style="margin-top: 10px"
    >
      <el-descriptions-item label="ID">vip123</el-descriptions-item>
      <el-descriptions-item label="Username">Zoe</el-descriptions-item>
      <el-descriptions-item label="Email">123@123.com</el-descriptions-item>
<!--      <el-descriptions-item label="Remarks">-->
<!--        <el-tag>VIP</el-tag>-->
<!--      </el-descriptions-item>-->
      <el-descriptions-item label="Address"
      >No.1188, Wuzhong Avenue, Wuzhong District, Suzhou, Jiangsu Province
      </el-descriptions-item>
    </el-descriptions>
    <div style="display: flex">
      <div style="flex: 1"></div>
      <div style="width: 80px">
        <el-button style="margin-top: 10px; width: 80px" type="danger" @click="edit">Edit</el-button>
      </div>

      <div>
        <el-dialog
            v-model="Dialoguser"
            title="User Information"
            width="30%"
            align-center
        >
          <el-form :model="form" label-width="80px" :label-position="'top'">
            <el-form-item label="ID">
              <el-input v-model="form.userid" disabled/>
            </el-form-item>
            <el-form-item label="Username">
              <el-input v-model="form.name" />
            </el-form-item>
            <el-form-item label="Email" >
              <el-input v-model="form.email" />
            </el-form-item>
            <el-form-item label="Address" >
              <el-input v-model="form.address" type="textarea"/>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" @click="save">Save</el-button>
              <el-button @click="Dialoguser = false">Cancel</el-button>
            </el-form-item>
          </el-form>
        </el-dialog>
      </div>
    </div>


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
      form: {

      },

      tableData: [
        {
          date: '2022-05-03',
          name: 'Titanic',
          actor: 'Jack',
          introduction: 'Romantic Movie',
          position: 'Screen1',
          price: 39,
          state: 1,
        },
        {
          date: '2022-05-02',
          name: 'Avatar2',
          actor: 'Alsa',
          introduction: 'Good',
          position: 'Screen2',
          price: 39,
        },
        {
          date: '2022-05-04',
          name: 'Spider man',
          actor: 'Simon',
          introduction: 'Cool',
          position: 'Screen3',
          price: 59,
        },
        {
          date: '2022-05-01',
          name: 'Romantic',
          actor: 'Wendy',
          introduction: 'Love',
          position: 'Screen2',
          price: 39,
        },
      ]
    }


  },

  methods: {
    load() {
      request.get("/historyorder",{
        params: {
          pageNum: this.currentPage,
          pageSize: this.pageSize,
          search: this.search
        }

      }).then(res => {
        console.log(res)
        this.tableData = res.data.record
        this.total = res.data.total
      })
    },
    edit() {
      this.Dialoguser = true
      this.form = {

      }
    },
    save() {
      // if(this.form.id) {
      //   request.post("/movies", this.form).then(res => {
      //     console.log(res)
      // if (res.code ==='0') {
      this.$message({
        type:"success",
        message: "Edit Successfully!"
      })
      // }
      // })
      // }
      this.load()
      this.Dialoguser = false
    }

  }
}
</script>

<style scoped>

</style>