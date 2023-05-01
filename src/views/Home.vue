<template>
  <div class="home">
    <h1>Welcome to Home page</h1>
    <p v-if="user">Welcome, {{ user.username }}!</p>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
  setup() {
    const store = useStore();
    const user = computed(() => store.state.user);

    return { user };
  },
};
</script>

<style scoped>
.home {
  text-align: center;
  margin-top: 40px;
}
</style>
