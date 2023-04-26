<template>
  <div class="container">
    <div class="search-container">
      <div class="input-left"></div>
      <div class="input-box">
        <input
          type="text"
          placeholder="Ask something..."
          v-model="apiData"
          @keydown.enter="requestData"
        />
      </div>

      <div class="input-right" @click="requestData">
        <div class="btn">
          <SendIcon />
        </div>
      </div>
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
          <div class="result">{{ item }}</div>
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
      <!-- <evoil /> -->
    </div>
  </div>
</template>

<script lang="ts">
import { ref } from "vue";
import LoadingIndicator from './components/LoadingIndicator.vue'
import AiAvater from './components/AiAvater.vue'
import SendIcon from './components/SendIcon.vue'
import UserAvater from './components/UserAvater.vue'


export default {
   components: { AiAvater, UserAvater, SendIcon, LoadingIndicator },
  setup() {
    const apiData = ref("");
    const resultList = ref([]);
    const qaList = ref([]);
    const loading = ref(false);

    const requestData = () => {
      if (loading.value) return;
      if (!(apiData.value && apiData.value !== "")) return;

      apiData.value = "";
      loading.value = true;
      qaList.value = [...qaList.value, apiData.value];

      const apiUrl = "https://kiritosa.com:1200/api/chart";
      fetch(apiUrl + `?content=${apiData.value}`)
        .then((res) => res.json())
        .then((response) => {
          const htmlString = response.data || "";
          resultList.value = [...resultList.value, htmlString];
        })
        .catch((error) => {
          console.log(error);
          resultList.value = [...resultList.value, "请求出错！"];
        })
        .finally(() => {
          loading.value = false;
        });
    };

    return { apiData, resultList, qaList, loading, requestData };
  },
};
</script>

<style scoped>
@import "./index.css";/* Place your CSS styles here */
</style>

