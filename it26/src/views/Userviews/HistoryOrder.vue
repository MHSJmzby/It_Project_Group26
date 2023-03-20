<template>
  <!--    OrderTable   -->
  <div style="padding: 10px; width: 100%;">
    <!--    <span style="font-size: xx-large; font-weight: bold">History Order</span>-->
    <!--    Search   -->
    <div style="display: flex">
      <div style="width: 600px;">
        <el-input v-model="search" placeholder="Please input Movie name"  style="width: 300px" clearable />
        <el-button style="margin: 10px" plain>Search</el-button>
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

        <el-table-column label="Movie" prop="filmName" sortable/>
        <el-table-column label="Date" prop="time" align="center" sortable/>
        <el-table-column label="Position" prop="screen" align="center" />
        <el-table-column label="Price" prop="price" align="center"/>
        <el-table-column label="State" prop="state" align="center"/>
        <el-table-column label="Operations" align="center" >
          <template #default="scope">
            <el-button size="small" type="danger" @click="refund(scope.row)">Refund</el-button>
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
          :total="10"
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
        <template #footer>
        <span class="dialog-footer">
          <el-button type="primary" @click="confirm">
            Confirm
          </el-button>
          <el-button @click="Dialogrefund = false">Cancel</el-button>
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
      tableData: [],
    }


  },
  created() {
    this.load()
  },

  methods: {
    load() {
      request.get("/historyorder/", {
        params: {
          pageNum: this.currentPage,
          pageSize: this.pageSize,
          search: this.search
        }

      }).then(res => {
        console.log(res)
        this.tableData = res.data
        this.total = res.data.total
      })
    },
    refund(row) {
      this.Dialogrefund = true
      this.form = JSON.parse(JSON.stringify(row))
      console.log(this.form)
    },
    confirm()
    {
      if(this.form.id) {  //Edit
        request.post("/refund/", this.form).then(res => {
          console.log(res)
          if (res.code === '0') {
            this.$message({
              type: "success",
              message: "Refund Successfully!"
            })
          } else {
            this.$message({
              type: "error",
              message: res.msg,
            })
          }
          this.load()   //刷新表格内容
          this.Dialogrefund = false
        })
      }
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
