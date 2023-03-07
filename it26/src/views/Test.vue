<template>
  <div>

    <el-table :data="tabledatas" border>
      <el-table-column label="姓名">
        <template slot-scope="scope">
          <el-input placeholder="请输入内容" v-show="scope.row.show" v-model="scope.row.name"></el-input>
          <span v-show="!scope.row.show">{{scope.row.name}}</span>
        </template>
      </el-table-column>

      <el-table-column label="年龄">
        <template slot-scope="scope">
          <el-input placeholder="请输入内容" v-show="scope.row.show" v-model="scope.row.age"></el-input>
          <span v-show="!scope.row.show">{{scope.row.age}}</span>
        </template>
      </el-table-column>
      <el-table-column label="地址">
        <template slot-scope="scope">
          <el-input placeholder="请输入内容" v-show="scope.row.show" v-model="scope.row.address"></el-input>
          <span v-show="!scope.row.show">{{scope.row.address}}</span>
        </template>
      </el-table-column>
      <el-table-column label="学籍">
        <template slot-scope="scope">
          <span v-show="!scope.row.show">{{scope.row.stu}}</span>
          <el-select v-model="scope.row.stu" placeholder="请选择" v-show="scope.row.show" >

            <el-option
                v-for="item in options"
                :key="item.stu"
                :label="item.stu"
                :value="item.stu">
            </el-option>
          </el-select>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button @click="scope.row.show =true" >编辑</el-button>
          <el-button @click="scope.row.show =false">保存</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      options: [{
        value: '选项1',
        stu: '初中'
      }, {
        value: '选项2',
        stu: '高中'
      }, {
        value: '选项3',
        stu: '大专'
      }, {
        value: '选项4',
        stu: '本科'
      }, {
        value: '选项5',
        stu: '博士'
      }],
      value: '',
      tabledatas: [
        {name: '李一', age: '19', address: "宁波", stu: "本科", show: false},
        {name: '郭明', age: '23', address: "四川", stu: "本科", show: false},
        {name: '天天', age: '12', address: "海南", stu: "初中", show: false},
        {name: '隆', age: '40', address: "上海", stu: "博士", show: false},
      ],
    }
  }
}
</script>