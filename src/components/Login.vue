<template>
    <div>
      <h2>Login</h2>
      <form @submit.prevent="loginUser">
        <div>
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div>
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        email: "",
        password: "",
      };
    },
    methods: {
      loginUser() {
        // 发送请求到后端进行登录
        fetch("http://49.234.79.245:1200/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
          body: new URLSearchParams({
            email: this.email,
            password: this.password,
          }),
        })
          .then((res) => {
            if (res.ok) {
              alert("Login successful!");
              this.$router.push("/"); // 重定向到主页面
            } else {
              alert("Login failed. Please try again.");
            }
          })
          .catch((error) => {
            console.error("Error:", error);
            alert("Loginfailed. Please try again.");
            });
        },
    },
};
</script>
  