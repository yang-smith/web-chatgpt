<template>
    <div class="topup">
      <h1>Top Up</h1>
      <form @submit.prevent="topUp">
        <div>
          <label for="amount">Amount:</label>
          <input type="number" id="amount" min="0.01" step="0.01" v-model.number="amount" />
        </div>
        <button type="submit">Top Up</button>
        <button type="button" @click="backToChat">Back to Chat</button>
      </form>
    </div>
  </template>
  
<script>
  import { ref } from 'vue';
  import { useStore } from 'vuex';
  import router from '../router'; 
  
  export default {
    setup() {
      const store = useStore();
      const amount = ref(0.0);
      const error = ref('');
  
      const topUp = () => {
        store.dispatch('topUp', { amount: amount.value })
          .then(() => {
            // 在成功充值后跳转到 userChat 页面
            router.push('/userChat');
          })
          .catch(err => {
            error.value = 'Error in top up: ' + err.message;
          });
      };
  
      const backToChat = () => {
        router.push('/userChat');
      }
  
      return { amount, topUp, backToChat, error };
    },
  };
  </script>
  
  <style scoped>
  .topup {
    width: 300px;
    margin: 0 auto;
    padding: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
    border-radius: 5px;
  }
  
  .topup h1 {
    color: #333;
    font-size: 24px;
    margin-bottom: 20px;
  }
  
  .topup label {
    color: #333;
    font-size: 14px;
    font-weight: bold;
  }
  
  .topup input {
    margin-top: 10px;
    margin-bottom: 20px;
    padding: 10px;
    border-radius: 3px;
    border: 1px solid #ccc;
    width: 100%;
  }
  
  .topup button {
    background-color: #4CAF50;
    color: white;
    padding: 15px 20px;
    margin: 10px 0;
    border: none;
    cursor: pointer;
    width: 100%;
    opacity: 0.9;
  }
  
  .topup button:hover {
    opacity:1;
  }
  </style>
  