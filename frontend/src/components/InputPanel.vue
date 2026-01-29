<template>
    <div class="input-panel">
        <h2>Input Text</h2>
        <textarea
            v-model="reader.text"
            placeholder="Paste or type text here..."
            class="input-box"
        />
    </div>
</template>

<script setup lang="ts">
import { useReaderStore } from '../store/readerStore.ts'

const reader = useReaderStore()
</script>

<style scoped>
.input-panel {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    padding: 1.5rem;
    background: #fafafa;
    border-radius: 12px;
    border: 1px solid #eee;
}

.input-box {
    min-height: 150px;
    padding: 1rem;
    font-size: 1rem;
    border-radius: 8px;
    border: 1px solid #ccc;
    resize: vertical;
}
</style>
