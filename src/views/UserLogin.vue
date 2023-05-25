<template>
  <transition name="modal">
    <div class="modal-mask" v-if="showModal">
      <div class="login">
        <h1>Login</h1>
        <form @submit.prevent="login">
          <div>
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="email" />
          </div>
          <div>
            <label for="password">Password:</label>
            <input type="password" id="password" v-model="password" />
          </div>
          <button type="submit">Login</button>
          <button type="button" @click="closeModal">Close</button>
        </form>
      </div>
    </div>
  </transition>
</template>

<script>
import { ref, watch } from 'vue';
import { useStore } from 'vuex';
import router from '../router'; 

export default {
  setup() {
    const store = useStore();
    const email = ref('');
    const password = ref('');
    const showModal = ref(true);
    const error = ref('');

    const login = () => {
      store.dispatch('login', { email: email.value, password: password.value })
        .then(() => {
          // 在成功登录后跳转到 userChat 页面
          router.push('/userChat');
        })
        .catch(err => {
          error.value = 'Error logging in: ' + err.message;
        });
    };

    watch(() => store.state.isLoggedIn, (newValue) => {
      if (newValue) {
        showModal.value = false;
      }
    });

    const closeModal = () => {
      showModal.value = false;
    }

    return { email, password, login, showModal, closeModal, error };
  },
};
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.login {
  background: #f5f5f5;
  padding: 20px;
  border-radius: 5px;
  width: 300px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  border: 1px solid #ccc;
}

.login h1 {
  color: #333;
  font-size: 24px;
  margin-bottom: 20px;
}

.login label {
  color: #333;
  font-size: 14px;
  font-weight: bold;
}

.login input {
  margin-top: 10px;
  margin-bottom: 20px;
  padding: 10px;
  border-radius: 3px;
  border: 1px solid #ccc;
  width: 100%;
}

.login button {
  background-color: #4CAF50;
  color: white;
  padding: 15px 20px;
  margin: 10px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}

.login button:hover {
  opacity:1;
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  transform: scale(1.1);
}
</style>
