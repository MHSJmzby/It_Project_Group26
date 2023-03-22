<template>
  <div style="padding: 10px; width: 100%">
    <div style="padding: 10px;">
      <el-table :data="tableData " stripe>
        <el-table-column label="Timing" prop="timing" style="color:black; font-weight: bolder" align="center" >
          <template v-slot="{ row }">
          <el-input v-model="row.timing"></el-input>
          </template>
        </el-table-column>
        <el-table-column label="Monday" prop="monday"  align="center">
          <template v-slot="{ row }">
            <el-input v-model="row.monday"></el-input>
          </template>
        </el-table-column>
        <el-table-column label="Tuesday" prop="tuesday" align="center" >
          <template v-slot="{ row }">
            <el-input v-model="row.tuesday"></el-input>
          </template>
        </el-table-column>
        <el-table-column label="Wednesday" prop="wednesday" align="center" >
          <template v-slot="{ row }">
            <el-input v-model="row.wednesday"></el-input>
          </template>
        </el-table-column>
        <el-table-column label="Thursday" prop="thursday" align="center">
          <template v-slot="{ row }">
            <el-input v-model="row.thursday"></el-input>
          </template>
        </el-table-column>
        <el-table-column label="Friday" prop="friday" align="center">
          <template v-slot="{ row }">
            <el-input v-model="row.friday"></el-input>
          </template>
        </el-table-column>
        <el-table-column label="Saturday" prop="saturday" align="center">
          <template v-slot="{ row }">
            <el-input v-model="row.saturday"></el-input>
          </template>
        </el-table-column>
        <el-table-column label="Sunday" align="center">
          <template v-slot="{ row }">
            <el-input v-model="row.sunday"></el-input>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <div style="display: flex">
      <div style="width: 700px; flex: 1"/>
      <div style="width: 150px">
        <el-button type="primary" @click="load">Recover</el-button>
        <el-popconfirm title="Do you confirm the Edit?" @confirm="edit">
          <template #reference>
            <el-button type="danger">Save</el-button>
          </template>
        </el-popconfirm>
      </div>
    </div>
  </div>
</template>

<script>
import request from "@/utils/request";

export default {
  name: "Schedule",
  components: {

  },
  data() {
    return {
      tableData: [
        {
          timing: '9:00',
          tuesday: 'Spider man',
        },
        {
          timing: '13:00',
          monday: 'Titanic',
          wednesday: 'Romantic',
        },
        {
          timing: '17:00',
          thursday: 'Avatar2',
          tuesday: 'Avatar2',
        },
      ]
    }
  },
  created() {
    this.load()
  },
  methods: {
    load() {
      request.get("/schedule/",{
        params: {
          search: this.search
        }
      }).then(res => {
        console.log(res)
        this.tableData = res.data
        this.total = res.data.total
      })
    },
    edit(){
      request.put("/schedule/", this.tableData).then(res => {
        console.log(res)
        if (res.code ==='0') {
          this.$message({
            type:"success",
            message: "Edit Successfully!"
          })
        }
        else {
          this.$message( {
            type:"error",
            message: res.msg,
          })
        }
        this.load()   //刷新表格内容
      })
    }

  },
}
</script>

<style scoped>

</style>