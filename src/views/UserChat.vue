<template>
      <div class="container">

          <div class="user-info" v-if="userInfo">
            <p>{{ userInfo.email }}
              <button @click="showDetails = !showDetails" class="details-button">
                {{ showDetails ? '▲' : '▼'  }}
              </button>
            </p>
            <div v-show="showDetails">
              <p>余额: {{ userInfo.balance }}</p>
              <router-link to="/UserTopup" class="topup-button">
                <button type="button">充值</button>
              </router-link>
            </div>
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
import router from '../router'; 

export default {
    components: { AiAvater, UserAvater, LoadingIndicator },
    setup() {
    const store = useStore();
    const userQuestion = ref("");
    const showDetails = ref(false);

    const submitQuestion =  () => {
        // Check if user is logged in
      if (!store.state.isLoggedIn) {
        router.push('/UserLogin');
        return;
      }
      if( store.getters.lastAnswerIsNull) return;
      if (store.state.user.balance < 0.01) {
        store.commit('addChatMessage', { question: 'System Message', answer: '余额不足。一个问题约0.01元。注意：这只是一个实验性项目，搞一块钱玩玩可以，不要多充，我无法保证稳定性。' });
        return;
      }
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

    return { userInfo, userQuestion, submitQuestion, qaList: store.state.chatHistory, markdownToHtml, showDetails};
    },
};
</script>
    
    
<style scoped>

@import "./index.css";
</style>
