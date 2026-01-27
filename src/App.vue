<template>
  <main class="container">
    <h1>Unblur</h1>
    <p class="tagline">A clearer way to read.</p>

    <textarea
      v-model="text"
      placeholder="Paste text here..."
      class="input"
    ></textarea>

    <button class="button">
      Analyze & Optimize
    </button>
  </main>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const text = ref('')
</script>

<style scoped>
.container {
  max-width: 700px;
  margin: 4rem auto;
  padding: 2rem;
  text-align: center;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.tagline {
  color: #666;
  margin-bottom: 2rem;
}

.input {
  width: 100%;
  min-height: 150px;
  padding: 1rem;
  font-size: 1rem;
  margin-bottom: 1rem;
}

.button {
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  cursor: pointer;
}
</style>
