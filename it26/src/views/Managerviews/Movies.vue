<template>
  <div style="padding: 10px; width: 100%">
    <!--    <span style="font-size: xx-large; font-weight: bold">History Order</span>-->
<!--    Search   -->
    <div style=" height: 50px; line-height: 50px; border-bottom: 1px solid #ccc; display: flex">
      <div style=" width: 700px; padding-left: 10px; font-weight: bold; color: dodgerblue">
        <el-input v-model="search" placeholder="Please input Movie name"  style="width: 300px" clearable />
        <el-button style="margin: 10px" >Search</el-button>
      </div>
      <div style="flex: 1"></div>
      <!--    Button   -->
      <div style="width: 160px">
        <el-button type="primary" @click="add">Add</el-button>
        <el-button style="margin: 10px" type="danger" @click="Dialogdelete = true">Delete</el-button>
      </div>
    </div>

<!--   Table   -->
    <div style="padding: 10px;">
      <el-table
          :data="tableData"
          highlight-current-row
          stripe

          :editable="true"
          ref="table"
          @cell-click="handleCellClick"
      >
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

        <el-table-column label="Movie" prop="movies" :editable="true" sortable>
<!--          <el-input v-model="inputValue" :value="tableData.name" placeholder="tableData.name"></el-input>-->
        </el-table-column>
        <el-table-column label="Release" prop="releaseDate" align="center" :editable="true" sortable/>
        <el-table-column label="Down" prop="downDate" align="center" :editable="true" sortable/>
        <el-table-column label="Duration" prop="duration" align="center" :editable="true"/>
        <el-table-column label="Price" prop="price" align="center" :editable="true"/>
      </el-table>
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
<!--    Dialog   -->
    <div>
      <el-dialog
          v-model="Dialogadd"
          title="Movie Information"
          width="50%"
          align-center
      >
        <el-form :model="form" label-width="120px">
          <el-form-item label="Movie name">
            <el-input v-model="form.movie" />
          </el-form-item>
          <el-form-item label="Position" >
            <el-select v-model="form.position" placeholder="Please select the position" style="width: 180px">
              <el-option label="Screen 1" value="1" />
              <el-option label="Screen 2" value="2" />
              <el-option label="Screen 3" value="3" />
            </el-select>
          </el-form-item>
          <el-form-item label="Date">
            <el-col :span="11">
              <el-date-picker
                  v-model="form.releaseDate"
                  type="date"
                  placeholder="Pick a release date"
                  style="width: 100%"
              />
            </el-col>
            <el-col :span="2" class="text-center">
              <span class="text-gray-500">-</span>
            </el-col>
            <el-col :span="11">
              <el-date-picker
                  v-model="form.downDate"
                  placeholder="Pick a down date"
                  style="width: 100%"
              />
            </el-col>
          </el-form-item>
          <el-form-item label="State">
            <el-switch v-model="form.state" />
          </el-form-item>
          <el-form-item label="Duration">
            <el-input-number v-model="form.duration" :min="1" :max="300" :step="10"/>
          </el-form-item>
          <el-form-item label="Price">
            <el-input-number v-model="form.price" :min="1" :max="200" />
          </el-form-item>
          <el-form-item label="Actor">
            <el-input v-model="form.actor" type="textarea" />
          </el-form-item>
          <el-form-item label="Introduction">
            <el-input v-model="form.introduction" type="textarea" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="save">Create</el-button>
            <el-button @click="Dialogadd = false">Cancel</el-button>
          </el-form-item>
        </el-form>
      </el-dialog>

      <el-dialog
          v-model="Dialogdelete"
          title="Tips"
          width="30%"
          align-center
      >
        <span>Do you confirm Delete?</span>
        <template #footer>
        <span class="dialog-footer">
          <el-button type="primary" @click="Dialogdelete = false">
            Confirm
          </el-button>
          <el-button @click="Dialogdelete = false">Cancel</el-button>
        </span>
        </template>
      </el-dialog>
    </div>
  </div>
</template>

<script>


import request from "@/utils/request";

export default {
  name: "Movies",

  components: {

  },
  data() {
    return {
      search: '',
      inputValue: '',
      pageSize: 1,
      currentPage: 4,
      Dialogadd: false,
      form: {
        duration: 120,
      },
      Dialogdelete: false,

      tableData: [
        {
          name: 'Titanic',
          releasedate: '2022-05-03',
          downdate: '2023-05-03',
          duration: 120,
          actor: 'Jack',
          introduction: 'Romantic Movie',
          position: 'Screen1',
          price: 39,
          state: 'Unused',
        },
        {
          name: 'Avatar2',
          releasedate: '2022-05-02',
          downdate: '2023-05-02',
          duration: 150,
          actor: 'Alsa',
          introduction: 'Good',
          position: 'Screen2',
          price: 39,
          state: 'Watching',
        },
        {
          name: 'Spider man',
          releasedate: '2022-05-04',
          downdate: '2023-05-02',
          duration: 120,
          actor: 'Simon',
          introduction: 'Cool',
          position: 'Screen3',
          price: 59,
          state: 'Finish',
        },
        {

          name: 'Romantic',
          releasedate: '2022-05-01',
          downdate: '2023-05-02',
          duration: 120,
          actor: 'Wendy',
          introduction: 'Love',
          position: 'Screen2',
          price: 39,
          state: 'Finish',
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

    add() {
      this.Dialogadd = true
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
              message: "Add Successfully!"
            })
          // }
        // })
      // }

      this.load()
      this.Dialogadd = false
    },
    handleCellClick(row, column, cell, event) {
      this.$nextTick(() => {
        this.$refs.table.editCell(row, column)
      })
    },


  },
}
</script>

<style scoped>

</style>