<template>
  <div class="min-h-screen px-4 md:px-6 py-6 max-w-6xl mx-auto">
    <!--header-->
    <header class="text-center mb-6">
      <h1 class="text-3xl md:text-4xl font-bold">
        Unblur
      </h1>
      <p class="text-gray-700 mt-2">
        A clearer way to read.
      </p>
    </header>
    <!--input row-->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6 items-stretch">
      <div class="md:col-span-2">
        <InputPanel />
      </div>
      <div>
        <ControlPanel />
      </div>
    </div>
    <!--reader row-->
    <div>
      <ReaderView />
    </div>
  </div>
</template>

<script setup lang="ts">
import InputPanel from './components/InputPanel.vue'
import ControlPanel from './components/ControlPanel.vue'
import ReaderView from './components/ReaderView.vue'
</script>
