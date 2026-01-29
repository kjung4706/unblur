<template>
  <main>
    <h1>Unblur</h1>

    <textarea
      v-model="reader.text"
      placeholder="Paste text here..."
      class="input"
    />

    <ControlPanel />
    <ReaderView />
  </main>
</template>

<script setup lang="ts">
import { useReaderStore } from './store/readerStore.ts'
import ControlPanel from './components/ControlPanel.vue'
import ReaderView from './components/ReaderView.vue'

const reader = useReaderStore()
</script>

<style scoped>
main {
  padding: 2rem;
}

.input {
  width: 100%;
  min-height: 120px;
  margin-bottom: 2rem;
  padding: 1rem;
  font-size: 1rem;
}
</style>
