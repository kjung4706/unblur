<template>
  <div
    :class="[
      'rounded-xl border border-gray-300 shadow-sm p-6 overflow-y-auto max-h-[275px] transition-colors duration-300',
      themeClasses
    ]"
  >
    <div
      v-if="paragraphs.length === 0"
      class="text-gray-400 italic text-center"
    >
      Your optimized reading view will appear here.
    </div>
    <div
      :style="readerStyles"
      class="mx-auto break-words whitespace-pre-wrap transition-all duration-200"
    >
      <p
        v-for="(paragraph, index) in paragraphs"
        :key="index"
        class="mb-5"
      >
        {{ paragraph }}
      </p>
    </div>
  </div>
</template>


<script setup lang="ts">

/**
 * ReaderView.vue
 * Renders formatted text based on current reader settings.
 * Applies dynamic typography styles and theme.
 */

import { computed } from 'vue'
import { useReaderStore } from '../store/readerStore'

const reader = useReaderStore()

const paragraphs = computed(() =>
  reader.text.split('\n').filter(p => p.trim().length > 0)
)

const readerStyles = computed(() => ({
  fontSize: `${reader.fontSize}px`,
  lineHeight: reader.lineHeight,
  letterSpacing: `${reader.letterSpacing}px`,
  wordSpacing: `${reader.wordSpacing}px`,
  maxWidth: `${reader.maxWidth}px`,
}))

const themeClasses = computed(() => {
  switch (reader.theme) {
    case "dark":
      return "bg-gray-900 text-gray-100"
    case "sepia":
      return "bg-[#f4ecd8] text-[#5b4636]"
    default:
      return "bg-white text-gray-900"
  }
})

</script>
