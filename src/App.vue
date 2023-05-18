<template>
  <div class="router">
    <nav>
      <router-link to="/">Home</router-link>
      <router-link to="/UserRegister">Register</router-link>
      <router-link to="/Userlogin">Login</router-link>
    </nav>
    <router-view />
  </div>
    <div class="container">
      <div class="search-container">
        <div class="input-left"></div>
        <div class="input-box">
        <input
          type="text"
          placeholder="Ask something..."
          v-model="userQuestion"
          @keydown.enter="submitQuestion"
        />
      </div>
        <button @click="submitQuestion">Ask</button>
      </div>
      <div class="back-container">
      <div
        class="result-container"
        v-for="(item, index) in qaList"
        :key="index"
      >
      <div class="question-container">
        <div class="avater">
            <UserAvater />
          </div>
          <div class="result">{{ item.question }}</div>
        </div>
        
        <div class="ai-container">
          <div class="avater">
            <AiAvater />
          </div>
          <div v-if="resultList[index]" class="result typewriter">
            <div v-html="resultList[index]"></div>
          </div>
          <LoadingIndicator v-else />
        </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from "vue";
  import LoadingIndicator from './components/LoadingIndicator.vue'
  import AiAvater from './components/AiAvater.vue'
  // import SendIcon from './components/SendIcon.vue'
  import UserAvater from './components/UserAvater.vue'
  
  export default {
    components: { AiAvater, UserAvater, LoadingIndicator },
    setup() {
      const userQuestion = ref("");
      const qaList = ref([]);
      const resultList = ref([]);
      const loading = ref(false);

      const submitQuestion = () => {
        if (loading.value) return;
        if (userQuestion.value.trim() === "") return;
  
        loading.value = true;
        // Replace this with an actual call to an AI API to get the answer
        const fakeAnswer = `AI's response to: ${userQuestion.value}`;
        const apiUrl = "http://38.60.204.205:1200/api/chart";
        // const apiUrl = "http://49.234.79.245:1200/api/chart";
        fetch(apiUrl + `?content=${userQuestion.value}`)
          .then((res) => res.json())
          .then((response) => {
            console.log(response);
            const htmlString = response.message || "";
            resultList.value = [...resultList.value, htmlString];
          })
          .catch((error) => {
            console.log(error);
            resultList.value = [...resultList.value, "请求出错！"];
          })
          .finally(() => {
            loading.value = false;
            userQuestion.value = "";
          });

        qaList.value.push({
          question: userQuestion.value,
          answer: fakeAnswer,
        });
  
        userQuestion.value = "";
      };
  
      return { userQuestion, qaList, resultList, submitQuestion };
    },
  };
  </script>
  
  <style scoped>

@import "./index.css";/* Place your CSS styles here */
  /* .container {
    width: 100%;
    max-width: 600px;
    margin: 0 auto;
    padding: 2rem;
  }
  .search-container {
    display: flex;
    margin-bottom: 2rem;
  }
  input {
    flex-grow: 1;
    padding: 0.5rem;
    margin-right: 0.5rem;
  }
  button {
    padding: 0.5rem 1rem;
  }
  .qa-list {
    display: flex;
    flex-direction: column;
  }
  .qa-item {
    display: flex;
    flex-direction: column;
    margin-bottom: 1rem;
  }
  .question {
    font-weight: bold;
  }
  .answer {
    margin-left: 1rem;
  } */
  </style>
  