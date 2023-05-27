<template>
  <div class="router">
    <nav>
      <!-- <router-link to="/">Home</router-link> -->
      <div class="auth-links">
        <router-link to="/UserRegister">Register</router-link>
        <router-link to="/Userlogin">Login</router-link>
        <router-link to="/UserChat">Chat</router-link>
      </div>
    </nav>
    <router-view />
  </div>
  </template>
  
  <script>

  export default {
   
    setup() {
    }
  };
  </script>
  
  <style scoped>

  </style>
  