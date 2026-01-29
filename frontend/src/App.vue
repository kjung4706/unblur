<template>
  <div class="app">
    <header class="header">
      <h1>Unblur</h1>
      <p class="tagline">A clearer way to read.</p>
    </header>

    <div class="grid-layout">
      <div class="top-row">
        <InputPanel />
        <ControlPanel />
      </div>

      <div class="bottom-row">
        <ReaderView />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import InputPanel from './components/InputPanel.vue'
import ControlPanel from './components/ControlPanel.vue'
import ReaderView from './components/ReaderView.vue'
</script>

<style scoped>
.app {
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.header {
  text-align: center;
  margin-bottom: 2rem;
}

.tagline {
  color: #666;
  margin-top: 0.25rem;
}

.grid-layout {
  display: grid;
  gap: 2rem;
}

.top-row {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 2rem;
  align-items: stretch;
}

.bottom-row {
  width: 100%;
}
</style>
