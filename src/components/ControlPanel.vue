<template>
    <div class="controls">
        <h2>Reader Controls</h2>

        <label>
            Font Size: {{  reader.fontSize }}px
            <input
            type="range"
            min="14"
            max="30"
            v-model.number="reader.fontSize"
            />
        </label>

        <label>
            Line Height: {{  reader.lineHeight }}
            <input
            type="range"
            min="1.2"
            max="2.2"
            step="0.1"
            v-model.number="reader.lineHeight"
            />
        </label>

        <label>
            Max Width: {{  reader.maxWidth }}px
            <input
            type="range"
            min="500"
            max="900"
            step="10"
            v-model.number="reader.maxWidth"
            />
        </label>

        <label>
            Theme:
            <select v-model="reader.theme">
            <option value="light">Light</option>
            <option value="dark">Dark</option>
            <option value="sepia">Sepia</option>
            </select>
        </label>
    </div>
</template>

<script setup lang="ts">
import { useReaderStore } from '../store/readerStore.ts'

const reader = useReaderStore()
</script>

<style scoped>
.controls {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;
    max-width: 400px;
    margin: 2rem auto;
}

label {
    display: flex;
    flex-direction: column;
    font-size: 0.9rem;
}

input[type="range"] {
    margin-top: 0.5rem;
}
</style>
