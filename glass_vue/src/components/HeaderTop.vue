<template>
  <div>
    <div class="header-component" :class="{ 'header-hidden': isHeaderHidden }">
      <h1>智能玻璃缺陷检测系统</h1>
      <nav>
        <button @click="showComponent = 'home'">主页</button>
        <button @click="showComponent = 'analyze'">数据分析</button>
        <button @click="showComponent = 'images'">查看数据</button>
      </nav>
    </div>
    <div class="content-container">
      <!-- 根据 showComponent 的值动态显示组件 -->
      <div v-if="showComponent === 'home'" class="home-page">
        <h2>欢迎来到智能玻璃缺陷检测系统</h2>
        <p>通过导航栏进入相应的功能</p>
      </div>
      <div v-else-if="showComponent === 'analyze'">
        <DataAnalyze />
      </div>
      <div v-else-if="showComponent === 'images'">
        <ImageView />
      </div>
    </div>
  </div>
</template>

<script>
import DataAnalyze from '@/components/DataAnalyze.vue';
import ImageView from '@/components/ImageView.vue';

export default {
  name: 'HeaderComponent',
  components: {
    DataAnalyze,
    ImageView,
  },
  data() {
    return {
      showComponent: 'home', // 默认显示主页
      lastScrollTop: 0,
      isHeaderHidden: false,
    };
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleScroll() {
      const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      if (scrollTop > this.lastScrollTop) {
        // 下滑隐藏导航栏
        this.isHeaderHidden = true;
      } else {
        // 上滑显示导航栏
        this.isHeaderHidden = false;
      }
      this.lastScrollTop = scrollTop;
    },
  },
};
</script>

<style scoped>
.header-component {
  position: sticky; /* 使用 sticky 使导航栏在页面上滑时停留在顶部 */
  top: 0;
  left: 0;
  width: 100%;
  background-color: #89dbef;
  padding: 10px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0 2px 50px rgba(24, 22, 22, 0.893);
  transition: transform 0.3s ease; /* 添加过渡效果 */
  z-index: 1000; /* 确保导航栏在顶部 */
}
.header-component h1 {
  margin: 0;
}
.header-component nav button {
  margin-left: 10px;
}

.header-hidden {
  transform: translateY(-100%);
} 

.content-container {
  margin-top: 1px; /* 调整内容显示位置，避免被导航栏遮挡 */
}

.home-page {
  background-image: url('https://vip.helloimg.com/i/2024/07/12/6690f9d13a013.jpg');
  background-size: cover;
  background-position: center;
  height: calc(100vh - 10px); /* 计算内容区域高度，减去导航栏高度 */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  color: #fff;
  padding: 20px;
}
.home-page h2 {
  font-size: 2.5rem;
  margin-bottom: 10px;
}
.home-page p {
  font-size: 1.5rem;
  max-width: 600px;
  text-align: center;
}
</style>