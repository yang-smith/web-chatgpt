<template>
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
    </form>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useStore } from 'vuex';

export default {
  setup() {
    const store = useStore();
    const email = ref('');
    const password = ref('');

    const login = () => {
      store.dispatch('login', { email: email.value, password: password.value });
    };

    return { email, password, login };
  },
};
</script>

<style scoped>
.login {
  text-align: center;
  margin-top: 40px;
}
</style>
