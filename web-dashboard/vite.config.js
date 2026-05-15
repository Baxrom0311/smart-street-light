import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { VitePWA } from 'vite-plugin-pwa';

export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      manifest: {
        name: 'Smart Street Light',
        short_name: 'StreetLight',
        description: 'Energiya tejamkor ko\'cha yoritish tizimi',
        theme_color: '#0f172a',
        background_color: '#0f172a',
        display: 'standalone',
        icons: [
          { src: '/icon-192.png', sizes: '192x192', type: 'image/png' },
          { src: '/icon-512.png', sizes: '512x512', type: 'image/png' }
        ]
      },
      workbox: {
        runtimeCaching: [
          {
            urlPattern: /^https:\/\/smart-street-light-iot-default-rtdb\.firebaseio\.com/,
            handler: 'NetworkFirst',
            options: { cacheName: 'firebase-data' }
          }
        ]
      }
    })
  ]
});
