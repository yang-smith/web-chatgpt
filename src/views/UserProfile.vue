<template>
    <div>
      <h2>Register</h2>
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
  </template>
    
  <script>
    export default {
      data() {
        return {
          username: "",
          email: "",
          password: "",
        };
      },
      methods: {
        registerUser() {
          // 发送请求到后端进行注册
          fetch("http://49.234.79.245:1200/register", {
            method: "POST",
            headers: {
              "Content-Type": "application/x-www-form-urlencoded",
            },
            body: new URLSearchParams({
              username: this.username,
              email: this.email,
              password: this.password,
            }),
          })
            .then((res) => {
              if (res.ok) {
                alert("Registration successful! Please log in.");
                this.$router.push("/login");
              } else {
                alert("Registration failed. Please try again.");
              }
            })
            .catch((error) => {
              console.error("Error:", error);
              alert("Registration failed. Please try again.");
            });
        },
      },
    };
  </script>
    