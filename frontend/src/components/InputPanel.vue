<template>
    <div class="input-panel">
        <h2>Input Text</h2>
        <textarea
            v-model="reader.text"
            placeholder="Paste or type text here..."
            class="input-box"
        />
        <button @click="optimizeText" class="optimize-btn">
            Optimize
        </button>
    </div>
</template>

<script setup lang="ts">
import { useReaderStore } from '../store/readerStore.ts'

const reader = useReaderStore()

async function optimizeText() {
  try {
    const response = await fetch("http://127.0.0.1:8000/optimize", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: reader.text }),
    })

    const data = await response.json()
    reader.text = data.optimized_text
  } catch (error) {
    console.error("Optimization failed:", error)
  }
}

</script>

<style scoped>
.input-panel {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    padding: 1.5rem;
    background: #FFF;
    border-radius: 12px;
    border: 1px solid #888;
}

.input-box {
    min-height: 150px;
    padding: 1rem;
    font-size: 1rem;
    border-radius: 8px;
    border: 1px solid #888;
    resize: vertical;
}

.optimize-btn {
  margin-top: 1rem;
  padding: 0.6rem 1rem;
  border-radius: 6px;
  border: none;
  background: #333;
  color: #EEE;
  cursor: pointer;
}
</style>
