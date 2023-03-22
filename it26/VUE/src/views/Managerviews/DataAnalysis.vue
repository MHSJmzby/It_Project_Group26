<template>
  <div ref="pieChart" id="pieChart" style="margin: 15px">

  </div>
</template>

<script>
import * as echarts from "echarts";

export default {
  mounted () {
    let pieChart = echarts.init(this.$refs.pieChart)
    let data = [
      { value: 40, name: 'CREED III' },
      { value: 38, name: 'SHAZAM! FURY OF THE GODS' },
      { value: 32, name: 'SCREAM VI' },
      { value: 30, name: 'The Legend of 1900' },
      { value: 28, name: 'Good Will Hunting' },
      { value: 26, name: 'The Shawshank Redemption' },
      { value: 22, name: 'Forrest Gump' },
      { value: 18, name: 'The Kite Runner' },

      // { value: 40, name: 'CREED III' },
      // { value: 18, name: 'SHAZAM! FURY OF THE GODS' },
      // { value: 28, name: 'SCREAM VI' },
      // { value: 80, name: 'The Legend of 1900' },
      // { value: 35, name: 'Good Will Hunting' },
      // { value: 43, name: 'The Shawshank Redemption' },
      // { value: 22, name: 'Forrest Gump' },
      // { value: 65, name: 'The Kite Runner' }
    ]

    let option =  {
      title: {
        text: "Viewings of the month",
        left: "center"
      },
      legend: {
        left: "left",
        orient: "vertical"
      },
      tooltip: {
        trigger: 'item'
      },
      toolbox: {
        show: true,
        feature: {
          mark: { show: true },
          dataView: { show: true, readOnly: false },
          restore: { show: true },
          saveAsImage: { show: true }
        }
      },
      series: [
        {
          name: 'Movie Pie',
          type: 'pie',
          radius: [50, 150],
          center: ['50%', '50%'],
          roseType: 'area',
          itemStyle: {
            borderRadius: 4
          },
          emphasis: {
            itemStyle: {
              shadowBlur: 10,
              shadowOffsetX: 0,
              shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
          },
          data
        }
      ],

    }

    pieChart.setOption(option)
  }
}
</script>

<style>
#myChart {
  width: 300px;
  height: 300px;
  border: 1px solid red;
}
</style>