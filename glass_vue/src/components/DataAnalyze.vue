<template>
  <div class="data-analyze-container">
    <h1 class="title">数据分析</h1>
    <div class="input-container">
      <label for="year">年:</label>
      <input type="text" id="year" v-model="year" placeholder="Enter year" />

      <label for="month">月:</label>
      <input type="text" id="month" v-model="month" placeholder="Enter month" />

      <button @click="generateBarChart">生成柱状图</button>
      <button @click="generatePieChart">生成饼图</button>
    </div>

    <div class="chart-container">
      <div v-if="barChartFilename" class="chart">
        <img :src="getImageUrl(barChartFilename)" alt="Bar Chart" />
      </div>

      <div v-if="pieChartFilename" class="chart" style="margin-top: -20px;">
        <img :src="getImageUrl(pieChartFilename)" alt="Pie Chart" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from '@/utils/axios.js';

export default {
  name: 'DataAnalyze',
  data() {
    return {
      Baseurl:'http://192.168.123.84:8081',
      year: '',
      month: '',
      barChartFilename: null,
      pieChartFilename: null
    };
  },
  watch: {
    // Reset chart filenames when year or month changes
    year() {
      this.resetChartFilenames();
    },
    month() {
      this.resetChartFilenames();
    }
  },
  methods: {
    async generateBarChart() {
      await this.generateChart('bar');
    },
    async generatePieChart() {
      await this.generateChart('pie');
    },
    async generateChart(type) {
      try {
        const response = await axios.get(`/api/labels/${type}_chart`, {
          params: {
            year: this.year,
            month: this.month
          }
        });
        if (type === 'bar') {
          this.barChartFilename = response.data.filename;
        } else if (type === 'pie') {
          this.pieChartFilename = response.data.filename;
        }
      } catch (error) {
        console.error(`Error generating ${type} chart:`, error);
      }
    },
    resetChartFilenames() {
      this.barChartFilename = null;
      this.pieChartFilename = null;
    },
    getImageUrl(filename) {
      return `${this.Baseurl}/api/labels/show_image/${filename}`;
    }
  }
};
</script>

<style scoped>
.data-analyze-container {
  background-image: url('https://vip.helloimg.com/i/2024/07/12/66914398ea7d3.png');
  background-size: cover;
  background-position: center;
  padding: 20px;
}

.title {
  text-align: center;
  color: #fff; /* White text color for contrast */
}

.input-container {
  text-align: center;
  margin-top: 20px;
}

.input-container label {
  font-size: 18px;
  color: #fff; /* White text color for contrast */
}

.input-container input {
  font-size: 18px;
  padding: 5px 10px;
  margin-left: 10px;
}

.input-container button {
  font-size: 18px;
  padding: 5px 10px;
  margin-left: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  cursor: pointer;
}

.chart-container {
  display: flex;
  justify-content: space-around;
  margin-top: 40px; /* Increased margin for spacing */
}

.chart {
  flex: 0 0 45%; /* Each chart takes up 45% width */
  text-align: center;
  margin-bottom: 40px; /* Increased margin for spacing */
}

.chart img {
  max-width: 100%; /* Ensure the image does not exceed its container */
}
</style>