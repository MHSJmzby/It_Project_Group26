<template>
  <!--    OrderTable   -->
  <div style="padding: 10px; width: 100%;">
<!--    <span style="font-size: xx-large; font-weight: bold">History Order</span>-->
    <!--    Search   -->
    <div style="display: flex">
      <div style="width: 600px;">
          <el-input v-model="search" placeholder="Please input Movie name"  style="width: 300px" clearable />
          <el-button style="margin: 10px" plain @click="search">Search</el-button>
      </div>
    </div>

    <div style="padding: 10px;">
    <el-table :data="tableData ">
      <el-table-column type="index" align="center" />
      <el-table-column type="expand" >
        <template #default="props">
          <div m="4" style="padding: 10px;">
            <h3>Description</h3>
            <p m="t-0 b-2">Movie: {{ props.row.name }}</p>
            <p m="t-0 b-2">Actor: {{ props.row.actor }}</p>
            <p m="t-0 b-2">Introduction: {{ props.row.introduction }}</p>
          </div>
        </template>
      </el-table-column>

      <el-table-column label="ID" prop="uuid" sortable/>
      <el-table-column label="Movie" prop="name" sortable/>
      <el-table-column label="Date" prop="date" align="center" sortable/>
      <el-table-column label="Position" prop="position" align="center" />
      <el-table-column label="Price" prop="price" align="center"/>
      <el-table-column label="State" prop="state" align="center"/>
      <el-table-column label="Operations" align="center" >
        <template #default="scope">
          <el-button size="small" type="danger" @click="Dialogrefund = true">Refund</el-button>
        </template>
      </el-table-column>
    </el-table>
    </div>

    <div style="margin: 10px">
      <el-pagination
          v-model:current-page="currentPage"
          v-model:page-size="pageSize"
          :page-sizes="[1, 3, 5, 7]"
          :small="false"
          :disabled="false"
          :background="false"
          layout="total, sizes, prev, pager, next, jumper"
          :total="total"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
      />

      <el-dialog
          v-model="Dialogrefund"
          title="Tips"
          width="30%"
          align-center
      >
        <span>Do you confirm the refund?</span>
        <template #footer #default="scope">
        <span class="dialog-footer">
<!--          <template #default="scope">-->
            <el-button type="primary" @click="confirm(scope.row.uuid)">
              Confirm
            </el-button>
            <el-button @click="Dialogrefund = false">Cancel</el-button>
<!--          </template>-->
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
  name: "HistoryOrder",

  components: {},
  data() {
    return {
      search: '',
      pageSize: 1,
      currentPage: 4,
      Dialogrefund: false,
      total: 10,

      tableData: [
        {
          uuid: 1,
          date: '2022-05-03',
          name: 'Titanic',
          actor: 'Jack',
          introduction: 'Romantic Movie',
          position: 'Screen1',
          price: 39,
          state: 'Unused',
        },
        {
          uuid: 2,
          name: 'Avatar2',
          date: '2022-05-02',
          actor: 'Alsa',
          introduction: 'Good',
          position: 'Screen2',
          price: 39,
          state: 'Watching',
        },
        {
          uuid: 3,
          name: 'Spider man',
          date: '2022-05-04',
          actor: 'Simon',
          introduction: 'Cool',
          position: 'Screen3',
          price: 59,
          state: 'Finish',
        },
        {
          uuid: 4,
          name: 'Romantic',
          date: '2022-05-01',
          actor: 'Wendy',
          introduction: 'Love',
          position: 'Screen2',
          price: 39,
          state: 'Finish',
        },
      ]
    }


  },
  created() {
    this.load()
  },

  methods: {
    load() {
      request.get("/historyorder", {
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
    confirm(id) {
      console.log(id)
      request.delete("/historyorder" + id).then(res => {
        if(res.code === '0')
        {
          this.$message({
            type: "success",
            message: "Refund Successfully!"
          })
        }
        else
        {
          this.$message({
            type: "error",
            message: res.msg,
          })
        }
        this.load()   //刷新表格内容
        this.Dialogrefund = false
      })
    },

    handleSizeChange(pageSize) {
      this.pageSize = pageSize
      this.load()
    },
    handleCurrentChange(pageNum) {
      this.pageNum = pageNum
      this.load()
    },
  }
}
</script>

<style scoped>

</style>