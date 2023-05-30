<template>
  <transition name="modal">
    <div class="modal-mask" v-if="showModal">
      <div class="register">
        <h2>Register</h2>
        <button class="close-button" type="button" @click="closeModal">X</button>
        <form @submit.prevent="registerUser">
          <div>
            <label for="username">Username:</label>
            <input type="text" id="username" v-model="username" required />
          </div>
          <div>
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="email" required />
          </div>
          <div>
            <label for="password">Password:</label>
            <input type="password" id="password" v-model="password" required />
          </div>
          <button type="submit">Register</button>
        </form>
      </div>
    </div>
  </transition>
</template>

<script>
import { ref, watch } from 'vue';
import { useStore } from 'vuex';

export default {
  setup() {
    const store = useStore();
    const username = ref('');
    const email = ref('');
    const password = ref('');
    const showModal = ref(true);
    const error = ref('');

    const registerUser = () => {
      store.dispatch('register', { 
        username: username.value,
        email: email.value,
        password: password.value,
      }).catch(err => {
        error.value = 'Error registering: ' + err.message;
      });
    };

    watch(() => store.state.isRegistered, (newValue) => {
      if (newValue) {
        showModal.value = false;
      }
    });

    const closeModal = () => {
      showModal.value = false;
    }

    return { username, email, password, registerUser, showModal, closeModal, error };
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

.register {
  position: relative;
  background: #f5f5f5;
  padding: 20px;
  border-radius: 5px;
  width: 300px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  border: 1px solid #ccc;
}

.register h2 {
  color: #333;
  font-size: 24px;
  margin-bottom: 20px;
}

.register label {
  color: #333;
  font-size: 14px;
  font-weight: bold;
}

.register input {
  margin-top: 10px;
  margin-bottom: 20px;
  padding: 10px;
  border-radius: 3px;
  border: 1px solid #ccc;
  width: 100%;
}
.close-button {
  position: absolute;
  top: 0;
  right: 0;
  margin: auto;
  background-color: transparent;
  border: none;
  font-size: 1.2rem;
  cursor: pointer;
  display: inline-block;
  color: #4CAF50;
}
.register form button {
  background-color: #4CAF50;
  color: white;
  padding: 15px 20px;
  margin: 10px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}

.register button:hover {
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
