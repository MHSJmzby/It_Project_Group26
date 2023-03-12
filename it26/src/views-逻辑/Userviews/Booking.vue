<template>
  <div style="width: 100%; padding: 10px; position: center">
<!--  Search  -->
    <div>
      <el-input v-model="search" placeholder="Please input Movie name"  style="width: 300px" clearable />
      <el-button style="margin: 10px" plain>Search</el-button>
    </div>

    <!--    Table   -->
    <el-table :data="tableData" style="width: 100%; "  default-expand-all>
      <el-table-column type="index"  align="center"/>
      <el-table-column type="expand" style="width: 200px;" header-align="center" >
        <template #default="props">
          <div m="4" style="padding: 10px;">
            <h3>Description</h3>
            <p m="t-0 b-2">Movie: {{ props.row.name }}</p>
            <p m="t-0 b-2">Actor: {{ props.row.actor }}</p>
            <p m="t-0 b-2">Introduction: {{ props.row.introduction }}</p>
          </div>
        </template>
      </el-table-column>

      <el-table-column label="Movie" prop="name"  align="center" sortable/>
      <el-table-column label="Date" prop="date" align="center" sortable/>
      <el-table-column label="Position" prop="position" align="center"/>
      <el-table-column label="Price" prop="price" align="center"/>
      <el-table-column label="Operations" align="center">
        <template #default="scope">
          <el-button size="small" type="primary" @click="Dialogbook = true">Book</el-button>
        </template>
      </el-table-column>
    </el-table>

    <div style="margin: 10px 0; display: flex">
<!--    Button   -->
<!--      <div style="flex: 1"></div>-->
<!--      <div>-->
<!--        <el-button type="primary" plain>Expand All list</el-button>-->
<!--        <el-button style="margin: 10px" type="primary" plain>Wrap up list</el-button>-->
<!--      </div>-->

<!--      Dialog   -->
      <el-dialog
          v-model="Dialogbook"
          title="Tips"
          width="30%"
          align-center
      >
        <span>Do you confirm the booking?</span>
        <template #footer>
        <span class="dialog-footer">
          <el-button type="primary" @click="book">
            Confirm
          </el-button>
          <el-button @click="Dialogbook = false">Cancel</el-button>
        </span>
        </template>
      </el-dialog>
    </div>

  </div>

</template>

<script>
import request from "@/utils/request";
import router from "@/router";

export default {
  name: "Booking",
  components: {

  },
  data() {
    return {
      search: '',
      Dialogbook: false,

      tableData:  [
      {
        date: '2022-05-03',
        name: 'Titanic',
        actor: 'Jack',
        introduction: 'Romantic Movie',
        position: 'Screen1',
        price: 39,
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
      request.get("/booking",{
        params: {
          search: this.search
        }
      }).then(res => {
        console.log(res)
        this.tableData = res.data.record
        this.total = res.data.total
      })
    },
    book()
    {
      request.post("/booking", this.form).then(res => {
        console.log(res)
        if (res.code ==='0') {
          this.$message({
            type:"success",
            message: "Booking Successfully!"
          })
        }
        else {
          this.$message( {
            type:"error",
            message: res.msg,
          })
        }
        this.load()   //刷新表格内容
        this.Dialogbook = false
      })
    },

  }
}
</script>

<style scoped>

</style>