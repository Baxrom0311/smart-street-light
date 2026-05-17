# Dasturiy ta'minot tuzilishi

## Firmware (ESP32)

```
firmware/
├── platformio.ini          # Konfiguratsiya
├── include/
│   ├── config.h            # Barcha sozlamalar (pin, WiFi, Firebase)
│   ├── sensors.h           # Sensor funksiyalari deklaratsiyasi
│   ├── light_control.h     # LED boshqaruv deklaratsiyasi
│   ├── firebase_handler.h  # Firebase deklaratsiyasi
│   └── statistics.h        # Statistika deklaratsiyasi
└── src/
    ├── main.cpp            # Setup + Loop
    ├── sensors.cpp         # RCWL-9610A + TEMT6000 o'qish
    ├── light_control.cpp   # Relay boshqaruv logikasi
    ├── firebase_handler.cpp # Firebase RTDB sync
    └── statistics.cpp      # Energiya tejash hisoblash
```

### Modullar vazifasi

| Modul | Vazifasi |
|-------|----------|
| `main.cpp` | WiFi ulanish, barcha modullarni ishga tushirish, loop |
| `sensors.cpp` | Har 300ms da sensor o'qish, debounce, 5s hold timer |
| `light_control.cpp` | Auto/Manual/Schedule logika, relay boshqaruv |
| `firebase_handler.cpp` | Status yuborish (3s), stream tinglash, motion_log |
| `statistics.cpp` | Kunlik yonish vaqti, harakat soni, tejash % |

### Kutubxonalar

| Kutubxona | Versiya | Vazifasi |
|-----------|---------|----------|
| Firebase ESP32 Client | 4.4.17 | Firebase RTDB ulanish |
| Arduino ESP32 | 2.0.17 | WiFi, GPIO, ADC |

## Web Dashboard (React PWA)

```
web-dashboard/
├── index.html
├── vite.config.js          # Vite + PWA plugin
├── src/
│   ├── main.jsx            # Entry point
│   ├── App.jsx             # Router, auth, state management
│   ├── App.css             # Barcha stillar
│   ├── firebase.js         # Firebase config
│   ├── mockData.js         # Demo rejim uchun
│   └── components/
│       ├── Dashboard.jsx   # Bosh sahifa - power toggle, sensors
│       ├── Statistics.jsx  # Grafiklar (Recharts)
│       └── MotionLog.jsx   # Harakat tarixi
└── public/
    ├── favicon.svg
    ├── icon-192.png
    └── icon-512.png
```

### Texnologiyalar

| Texnologiya | Vazifasi |
|-------------|----------|
| React 19 | UI framework |
| Vite 8 | Build tool |
| Firebase SDK 10 | Realtime DB + Auth |
| Recharts | Grafiklar |
| vite-plugin-pwa | Service Worker, offline |
