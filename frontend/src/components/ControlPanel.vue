<template>
  <div class="bg-white rounded-xl border border-gray-300 p-4 space-y-4 shadow-sm h-full">

    <h2 class="text-lg font-semibold">Reader Controls</h2>

    <!-- Font Size -->
    <div class="space-y-2">
      <label class="text-sm font-medium">
        Font Size: {{ reader.fontSize }}px
      </label>
      <input
        type="range"
        min="14"
        max="30"
        v-model.number="reader.fontSize"
        class="w-full"
      />
    </div>

    <!-- Line Height -->
    <div class="space-y-2">
      <label class="text-sm font-medium">
        Line Height: {{ reader.lineHeight }}
      </label>
      <input
        type="range"
        min="1.2"
        max="2.2"
        step="0.1"
        v-model.number="reader.lineHeight"
        class="w-full"
      />
    </div>

    <!-- Max Width -->
    <div class="space-y-2">
      <label class="text-sm font-medium">
        Max Width: {{ reader.maxWidth }}px
      </label>
      <input
        type="range"
        min="500"
        max="900"
        step="10"
        v-model.number="reader.maxWidth"
        class="w-full"
      />
    </div>

    <!-- Letter Spacing -->
    <div class="space-y-2">
      <label class="text-sm font-medium">
        Letter Spacing: {{ reader.letterSpacing }}px
      </label>
      <input
        type="range"
        min="0"
        max="4"
        step="0.1"
        v-model.number="reader.letterSpacing"
        class="w-full"
      />
    </div>

    <!-- Theme -->
    <div class="space-y-2">
      <label class="text-sm font-medium">Theme</label>
      <select
        v-model="reader.theme"
        class="w-full border border-gray-300 rounded-md px-3 py-2 text-sm"
      >
        <option value="light">Light</option>
        <option value="dark">Dark</option>
        <option value="sepia">Sepia</option>
      </select>
    </div>

  </div>
</template>

<script setup lang="ts">

/**
 * ControlPanel.vue
 * Provides UI controls for adjusting reader settings
 * such as typography, spacing, width, and theme.
 * Updates shared state via Pinia store.
 */

import { useReaderStore } from '../store/readerStore.ts'
const reader = useReaderStore()
</script>
