<template>
  <div :class="['reader-wrapper', reader.theme]">
    <div class="reader" :style="readerStyles">
      <p v-for="(paragraph, index) in paragraphs" :key="index">
        {{ paragraph }}
      </p>
    </div>
  </div>
</template>

<script setup lang="ts">
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
  margin: '0 auto'
}))
</script>

<style scoped>
.reader-wrapper {
  padding: 2rem 1rem;
  height: 200px;
  overflow-y: auto;
  border-radius: 12px;
  transition: background 0.3s, color 0.3s;
}

.reader-wrapper.light {
  background: #ffffff;
  color: #111111;
}

.reader-wrapper.sepia {
  background: #f4ecd8;
  color: #5b4636;
}

.reader-wrapper.dark {
  background: #1e1e1e;
  color: #eaeaea;
}

.reader {
  transition: all 0.2s ease;
  overflow-wrap: break-word;
  word-break: break-word;
  white-space: pre-wrap;
  padding: 0 2rem;
}

.reader p {
  margin-bottom: 1.2em;
}
</style>
