/**
 * readerStore.ts
 * Centralized Pinia store for reader customization.
 * Manages text content, typography controls, spacing,
 * layout width, and theme preferences.
 */

import { defineStore } from 'pinia'

export const useReaderStore = defineStore('reader', {
  state: () => ({
    text: '',
    fontSize: 18,
    lineHeight: 1.6,
    letterSpacing: 0,
    wordSpacing: 0,
    maxWidth: 700,
    theme: 'light' as 'light' | 'dark' | 'sepia',
    }),
})
