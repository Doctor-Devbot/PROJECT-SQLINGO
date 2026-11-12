import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
<<<<<<< HEAD
    port: 5174,
    strictPort: true,
    proxy: {
      '/api': {
        target: 'http://localhost:5001',
=======
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
>>>>>>> 213b4cfe8ee907e01c7fb20eeacc431f105244df
        changeOrigin: true,
      },
    },
  },
})