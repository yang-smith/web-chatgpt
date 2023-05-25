<template>
      <div class="container">
        <div class="user-info" v-if="userInfo">
        <h2>User Info:</h2>
        <p>Email: {{ userInfo.email }}</p>
        <p>Balance: {{ userInfo.balance }}</p>
        </div>
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
            <div v-if="item.answer === null" class="result typewriter">
              <LoadingIndicator />
            </div>
            <div v-else class="result typewriter">
              <div v-html="markdownToHtml(item.answer)"></div>
            </div>


          </div>

          </div>
        </div>
      </div>
</template>
    
<script>
import { ref, computed } from "vue";
import { useStore } from "vuex"; 
import LoadingIndicator from '../components/LoadingIndicator.vue';
import AiAvater from '../components/AiAvater.vue';
import UserAvater from '../components/UserAvater.vue';
import MarkdownIt from 'markdown-it';


export default {
    components: { AiAvater, UserAvater, LoadingIndicator },
    setup() {
    const store = useStore();
    const userQuestion = ref("");

    const submitQuestion =  () => {
      if( store.getters.lastAnswerIsNull) return;
      if (userQuestion.value.trim() !== "") {
        store.dispatch('submitQuestion', userQuestion.value);
        userQuestion.value = "";
      }
      console.log(store.state.user);
    };

    const markdownToHtml = (markdown) => {
      const md = new MarkdownIt();
      return md.render(markdown || '');
    };

    const userInfo = computed(() => store.state.user);

    return { userInfo, userQuestion, submitQuestion, qaList: store.state.chatHistory, markdownToHtml};
    },
};
</script>
    
    
<style scoped>

@import "./index.css";
</style>
