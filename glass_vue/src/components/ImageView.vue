<template>
  <div class="container">
    <h1 class="title">数据管理</h1>
    <div v-if="error" class="error">{{ error }}</div>
    <div v-if="images.length === 0">No images found.</div>
    <div class="image-grid">
      <div v-for="image in images" :key="image" class="image-item">
        <img :src="getImageUrl(image)" :alt="image" @click="openModal(image)" />
        <button class="delete-btn" @click="deleteImage(image)">删除</button>
      </div>
    </div>
    <div class="pagination">
      <button @click="previousPage" :disabled="page <= 1">上一页</button>
      <span>第 {{ page }} 页，共 {{ totalPages }} 页</span>
      <button @click="nextPage" :disabled="page >= totalPages">下一页</button>
    </div>

    <!-- 放大图片模态框 -->
    <div v-if="modalVisible" class="modal" @click.self="closeModal">
      <span class="close" @click="closeModal">&times;</span>
      <img class="modal-content" :src="modalImageUrl" />
    </div>
  </div>
</template>

<script>
import axios from '@/utils/axios.js';

export default {
  name: 'ImageView',
  data() {
    return {
      Baseurl:'http://192.168.123.84:8081',
      images: [],
      page: 1,
      totalPages: 1,
      error: null,
      modalVisible: false,
      modalImageUrl: ''
     
    };
  },
  methods: {
    async fetchImages(page) {
      try {
        const response = await axios.get(`/api/images?page=${page}`);
        this.images = response.data.images;
        this.page = response.data.page;
        this.totalPages = response.data.total_pages;
      } catch (error) {
        this.error = "Failed to load images.";
        this.handleError(error);
      }
    },
    getImageUrl(image) {
      return `${this.Baseurl}/api/image/${image}`;
    },
    async deleteImage(imageName) {
      if (confirm("确定要删除这个图片及其对应的标签吗？")) {
        try {
          const response = await axios.delete(`/api/image/${imageName}`);
          alert(response.data.message);
          this.fetchImages(this.page);
        } catch (error) {
          this.error = "Failed to delete image.";
          this.handleError(error);
        }
      }
    },
    nextPage() {
      if (this.page < this.totalPages) {
        this.page++;
        this.fetchImages(this.page);
      }
    },
    previousPage() {
      if (this.page > 1) {
        this.page--;
        this.fetchImages(this.page);
      }
    },
    openModal(image) {
      this.modalImageUrl = this.getImageUrl(image);
      this.modalVisible = true;
    },
    closeModal() {
      this.modalVisible = false;
      this.modalImageUrl = '';
    },
    handleError(error) {
      if (error.response) {
        console.error("Error response:", error.response.data);
        console.error("Error status:", error.response.status);
        console.error("Error headers:", error.response.headers);
      } else if (error.request) {
        console.error("Error request:", error.request);
      } else {
        console.error("Error message:", error.message);
      }
    }
  },
  mounted() {
    this.fetchImages(this.page);
  }
};
</script>

<style scoped>
.container {
  max-width: 100%;
  margin: 0 auto;
  padding: 20px;
  background-image: url('https://vip.helloimg.com/i/2024/07/12/669142567008f.jpg');
  background-size: cover;
  background-position: center;
}

.title {
  text-align: center;
}

.image-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  gap: 10px;
}

.image-item {
  flex: 0 0 calc(20% - 20px); /* 计算每张图片占据的宽度，考虑到间距 */
  position: relative;
}

.image-item img {
  width: 100%; /* 图片宽度占满父容器 */
  height: auto; /* 高度自适应 */
  max-height: 200px; /* 最大高度限制 */
  border: 1px solid #ccc;
  cursor: pointer;
}

.delete-btn {
  position: absolute;
  top: 5px;
  right: 5px;
  background: red;
  color: white;
  border: none;
  padding: 5px;
  cursor: pointer;
}

.pagination {
  margin-top: 20px;
  text-align: center;
}

.pagination button {
  margin: 0 5px;
  padding: 5px 10px;
}

/* 放大图片样式 */
.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.9);
}

.modal-content {
  max-width: 700px;
  width: 80%;
}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #fff;
  font-size: 40px;
  font-weight: bold;
  cursor: pointer;
}

.close:hover,
.close:focus {
  color: #bbb;
  text-decoration: none;
}

.error {
  color: red;
}
</style>