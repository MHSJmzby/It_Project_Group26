<template>
  <div style="padding: 10px; width: 100%">
    <div style="padding: 10px;">
      <el-table :data="tableData " stripe :editable="true" @cell-click="handleCellClick">
        <el-table-column label="Timing" prop="timing" style="color:black; font-weight: bolder" align="center" />
        <el-table-column label="Monday" prop="monday"  align="center" :editable="true"/>
        <el-table-column label="Tuesday" prop="tuesday" align="center" />
        <el-table-column label="Wednesday" prop="wednesday" align="center" />
        <el-table-column label="Thursday" prop="thursday" align="center"/>
        <el-table-column label="Friday" prop="friday" align="center"/>
      </el-table>
    </div>

    <div style="display: flex">
      <div style="width: 700px; flex: 1"/>
      <div style="width: 80px">
        <el-button type="danger">Edit</el-button>
      </div>
    </div>

    <div>
      <el-tooltip
          class="box-item"
          effect="dark"
          content="Screen 1, 120, $39"
          placement="right"
      >
        <el-button>Titanic</el-button>
      </el-tooltip>
    </div>

    <div>
      <el-dialog
          v-model="Dialogadd"
          title="Tips"
          width="30%"
          align-center
      >
        <span>Do you confirm the refund?</span>
        <template #footer>
        <span class="dialog-footer">
          <el-button type="primary" @click="Dialogrefund = false">
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
    handleCellClick(row, column, cell, event) {
      // 开始编辑单元格
      this.$refs.table.editCell(row, column)
    }
  },
}
</script>

<style scoped>

</style>