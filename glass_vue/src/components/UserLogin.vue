<template>
  <div class="login-container">
    <div class="login-form">
      <h2 class="login-title">登录</h2>
      <form @submit.prevent="login">
        <div class="form-group">
          <label for="Username">用户名</label>
          <input
            v-model="username"
            type="text"
            id="username"
            class="form-control"
            :class="{'is-invalid': errorMessage}"
            required
          />
        </div>
        <div class="form-group">
          <label for="Password">密码</label>
          <input
            v-model="password"
            type="password"
            id="password"
            class="form-control"
            :class="{'is-invalid': errorMessage}"
            required
          />
        </div>    
        <div v-if="errorMessage" class="alert alert-danger">{{ errorMessage }}</div>
        <button type="submit" class="btn btn-primary">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from '@/utils/axios.js';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    async login() {
      try {
        await axios.post('/api/authentic', {
          username: this.username,
          password: this.password,
        });
        // alert(response.data.message);
        this.$router.push('/Header');
      } catch (error) {
        this.errorMessage = error.response.data.message || 'Login failed';
      }
    },
  },
};
</script>

<style scoped>
.login-container {
  background-image: url('https://vip.helloimg.com/i/2024/07/12/669105d0570e0.png');
  background-size: cover;
  background-position: center;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}


.login-form {
  width: 100%;
  max-width: 300px;
  height: 100%;
  max-height: 400px;
  padding: 20px;
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  align-items: center;
}
.login-title{
  text-align: center;
  margin-bottom: 50px;
}
.form-group {
  margin-bottom: 50px;
}
label {
  font-weight: bold;
}

.form-control {
  display: block;
  width: 100%;
  height: calc(2.25rem + 2px);
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #495057;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ced4da;
  border-radius: 0.25rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
}


.btn-primary {
  background-color: #007bff;
  color: #ffffff;
  border: none;
  cursor: pointer;
  padding: 10px 20px;
  border-radius: 4px;
  position: absolute;
  top: 85%;
  left: 75%;
  transform: translate(-50%, -50%);
}

.btn-primary:hover {
  background-color: #0056b3;
}
</style>