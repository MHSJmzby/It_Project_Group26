<template>
  <div style="padding: 10px; width: 100%">
    <!--    <span style="font-size: xx-large; font-weight: bold">History Order</span>-->
    <!--    Search   -->
    <div style=" height: 50px; line-height: 50px; border-bottom: 1px solid #ccc; display: flex">
      <div style=" width: 700px; padding-left: 10px; font-weight: bold; color: dodgerblue">
        <el-input v-model="search" placeholder="Please input Movie name"  style="width: 300px" clearable />
        <el-button style="margin: 10px" @click="load">Search</el-button>
      </div>
      <div style="flex: 1"></div>
      <!--    Button   -->
      <div style="width: 60px">
        <el-button type="primary" @click="add">Add</el-button>
        <!--        <el-button style="margin: 10px" type="danger" @click="Dialogdelete = true"></el-button>-->
      </div>
    </div>

    <!--   Table   -->
    <div style="padding: 10px;">
      <el-table
          :data="tableData"
          highlight-current-row
          stripe
          ref="table"
          default-expand-all
      >
        <el-table-column type="index" align="center" />
        <el-table-column type="expand" >
          <template #default="props">
            <div m="4" style="padding: 10px;">
              <h3>Description</h3>
              <p m="t-0 b-2">Movie: {{ props.row.movie }}</p>
              <p m="t-0 b-2">Actor: {{ props.row.actor }}</p>
              <p m="t-0 b-2">Introduction: {{ props.row.introduction }}</p>
            </div>
          </template>
        </el-table-column>

        <el-table-column label="Movie" prop="name" :editable="true" sortable>
          <!--          <el-input v-model="inputValue" :value="tableData.name" placeholder="tableData.name"></el-input>-->
        </el-table-column>
        <el-table-column label="Release" prop="releaseTime" align="center" :editable="true" sortable/>
        <el-table-column label="Down" prop="downTime" align="center" :editable="true" sortable/>
        <el-table-column label="Duration" prop="timeLength" align="center" :editable="true"/>
        <el-table-column label="Position" prop="screen" align="center" :editable="true"/>
        <el-table-column label="Price" prop="price" align="center" :editable="true"/>
        <el-table-column label="Operation" align="center" :editable="true">
          <template #default="scope">
            <el-button size="small" type="danger" @click="edit(scope.row)">Edit</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <!--    Dialog   -->
    <div>
      <el-dialog
          v-model="Dialogadd"
          title="Movie Information"
          width="50%"
          align-center
      >
        <el-form ref="form" :model="form" label-width="120px">
          <el-form-item label="Movie name">
            <el-input v-model="form.name" />
          </el-form-item>
          <el-form-item label="Position" >
            <el-select v-model="form.screen" placeholder="Please select the position" style="width: 180px">
              <el-option label="Screen 1" value="1" />
              <el-option label="Screen 2" value="2" />
              <el-option label="Screen 3" value="3" />
            </el-select>
          </el-form-item>
          <el-form-item label="Date">
            <el-col :span="11">
              <el-date-picker
                  v-model="form.releaseTime"
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
                  v-model="form.downTime"
                  placeholder="Pick a down date"
                  style="width: 100%"
              />
            </el-col>
          </el-form-item>
          <el-form-item label="State">
            <el-switch v-model="form.state" />
          </el-form-item>
          <el-form-item label="Duration">
            <el-input-number v-model="form.timeLength" :min="1" :max="300" :step="10"/>
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
      total: 0,
      Dialogadd: false,
      form: {
      },
      Dialogdelete: false,
      tableData: []
    }
  },
  created() {
    this.load()
  },
  methods: {
    load() {
      request.get("/movies/",{
        params: {
          search: this.search
        }
      }).then(res => {
        console.log(res)
        this.tableData = res.data
        this.total = res.data.total
      })
    },
    add() {
      this.Dialogadd = true
      this.form = {}
    },
    edit(row) {
      this.form = JSON.parse(JSON.stringify(row))
      console.log(this.form)
      this.Dialogadd = true
    },
    save() {
      if(this.form.id) {  //Edit
        request.put("/movies/", this.form).then(res => {
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
          this.Dialogadd = false
        })
      }
      else {  //Add
        request.post("/movies/", this.form).then(res => {
          console.log(res)
          if (res.code ==='0') {
            this.$message({
              type:"success",
              message: "Add Successfully!"
            })
          }
          else {
            this.$message( {
              type:"error",
              message: res.msg,
            })
          }
          this.load()   //刷新表格内容
          this.Dialogadd = false
        })
      }
    },
  },
}
</script>

<style scoped>
</style>
