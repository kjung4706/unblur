<template>
  <div class="bg-white rounded-xl border border-gray-300 p-4 space-y-4 shadow-sm flex flex-col h-full">

    <h2 class="text-lg font-semibold">Input Text</h2>

    <textarea
      v-model="reader.text"
      placeholder="Paste or type text here..."
      class="w-full min-h-[240px] p-4 text-base border border-gray-300 rounded-lg resize-y
             focus:outline-none focus:ring-2 focus:ring-black"
    />

    <button
      @click="optimizeText"
      :disabled="isLoading"
      class="w-full py-3 rounded-lg bg-black text-white transition flex items-center justify-center gap-2
             hover:bg-[#444] disabled:bg-[#777] disabled:cursor-not-allowed"
    >
      <span v-if="!isLoading">Optimize</span>

      <span v-else class="flex items-center gap-2">
        <span class="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></span>
        Optimizing...
      </span>
    </button>

  </div>
</template>

<script setup lang="ts">

/**
 * InputPanel.vue
 * Handles user text input and communicates with the backend /optimize endpoint.
 * Displays loading state during API requests.
 */

import { ref } from 'vue'
import { useReaderStore } from '../store/readerStore.ts'

const reader = useReaderStore()
const API_URL = import.meta.env.VITE_API_URL

const isLoading = ref(false)

async function optimizeText() {
  // Prevent empty submissions and duplicate API calls
  if (!reader.text.trim() || isLoading.value) return

  try {
    isLoading.value = true

    const response = await fetch(`${API_URL}/optimize`, {
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
  } finally {
    isLoading.value = false
  }
}
</script>

