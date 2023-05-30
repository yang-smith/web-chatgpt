<template>
    <div class="topup">
      <h1>充值</h1>
      <form @submit.prevent="topUp">
        <div>
          <label for="amount">金额:    </label>
          <input type="number" id="amount" min="1" step="1" max="25" v-model.number="amount" /> 元
        </div>
        <div class="qrcode">
          <img src="../../img/qrcode.jpg" alt="QR Code">
        </div>
        <button type="submit">
          <span v-if="isLoading">
            <div class="loading"></div>
            校验中Loading
          </span>
          <span v-else>确认充值</span>
        </button>
        <button type="button" @click="backToChat">back</button>
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
      const amount = ref(1);
      const error = ref('');
      const isLoading = ref(false);

      const topUp = () => {
        isLoading.value = true;
        store.dispatch('topUp', { amount: amount.value })
          .then(() => {
            setTimeout(() => {
              isLoading.value = false;
              router.push('/userChat');
            }, 8000); // 8 seconds
          })
          .catch(err => {
            error.value = 'Error in top up: ' + err.message;
          });
      };
  
      const backToChat = () => {
        router.push('/userChat');
      }
  
      return { amount, topUp, backToChat, error, isLoading};
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
    width: 30%;
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
  .qrcode {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px 0;
}

.qrcode img {
  max-width: 100%; 
  height: auto;    
}
.loading {
  display: inline-block;
  vertical-align: middle;
  border: 6px solid #f3f3f3;
  border-radius: 50%;
  border-top: 6px solid #3498db;
  width: 20px;
  height: 20px;
  -webkit-animation: spin 2s linear infinite; /* Safari */
  animation: spin 2s linear infinite;
}

@-webkit-keyframes spin { /* Safari */
  0% { -webkit-transform: rotate(0deg); }
  100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

  </style>
  