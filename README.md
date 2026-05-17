# 🔆 Smart Street Light - IoT Energiya Tejamkor Yoritish Tizimi

ESP32 mikrokontroller asosida ultratovush sensori orqali harakatni aniqlash va energiya tejamkorligini ta'minlovchi aqlli ko'cha yoritish tizimi.

## 📋 Loyiha haqida

**Diplom ishi mavzusi:** Ultratovush sensori orqali energiya tejamkorligini ta'minlovchi yoritish tizimini ishlab chiqish

**Maqsad:** Ko'cha yoritgichlarini faqat kerak bo'lganda (tunda + harakat aniqlanganda) yoqish orqali energiya tejash. Tizim masofadan boshqariladi va real-time monitoring imkoniyatiga ega.

## 🏗 Arxitektura

```
┌─────────────────┐         ┌──────────────────┐         ┌─────────────────┐
│   ESP32 + LED   │◄──WiFi──►│  Firebase RTDB   │◄──WS───►│  React PWA      │
│   + Sensorlar   │         │  (Cloud)         │         │  (Dashboard)    │
└─────────────────┘         └──────────────────┘         └─────────────────┘
```

## 🔧 Hardware komponentlari

| Komponent | Model | Vazifasi |
|-----------|-------|----------|
| Mikrokontroller | ESP32 DevKit (38 pin) | Asosiy boshqaruv |
| Ultratovush sensor | RCWL-9610A | Harakatni aniqlash (masofa o'lchash) |
| Yorug'lik sensor | TEMT6000 | Kunduz/tun aniqlash |
| LED strip | WS2812B (13 LED) | Ko'cha yoritgichi |
| Quyosh paneli | Mini panel | Energiya manbai (maket) |

## 📌 Pin konfiguratsiya

| ESP32 Pin | Komponent | Turi |
|-----------|-----------|------|
| GPIO 4 | RCWL-9610A TRIG | OUTPUT |
| GPIO 16 | RCWL-9610A ECHO | INPUT |
| GPIO 34 | TEMT6000 OUT | ANALOG INPUT |
| GPIO 26 | WS2812B DATA | OUTPUT |
| GPIO 2 | Onboard LED | STATUS |

## 💡 Ishlash logikasi

```
Kunduz (Light > 350)     → LED O'CHIQ (energiya tejash)
Tun (Light < 250)        → Harakat kutish rejimi
Tun + Harakat (< 200cm)  → LED YONIQ (100%)
Tun + 5s harakat yo'q    → LED O'CHIQ
Manual rejim             → Dashboard dan boshqarish
Jadval rejimi            → Belgilangan vaqtda yonish
```

## 🌐 Web Dashboard (PWA)

**URL:** https://smart-street-light-iot.web.app

### Funksiyalar:
- 🔐 **Login/Auth** — Firebase Email/Password authentication
- 📊 **Real-time monitoring** — sensor qiymatlari jonli ko'rinadi
- 🖐 **Manual boshqarish** — LED ni yoqish/o'chirish
- 🤖 **Auto rejim** — sensor asosida avtomatik
- 📅 **Jadval rejimi** — vaqt bo'yicha yoqish/o'chirish
- 🎨 **LED rang tanlash** — Oq, Issiq, Ko'k, Yashil, Qizil
- 🔆 **Brightness slider** — 10-100% yorug'lik
- 📈 **Statistika** — haftalik energiya tejash grafiklari
- 📋 **Harakat logi** — oxirgi 50 ta event
- 📱 **PWA** — telefondan native app sifatida o'rnatish
- 🟡 **Demo rejim** — mock datalar bilan ishlash (offline)

## 🛠 Texnologiya Stack

| Qatlam | Texnologiya |
|--------|-------------|
| MCU Firmware | ESP32 + Arduino Framework (PlatformIO) |
| Cloud | Firebase Realtime Database + Auth + Hosting |
| Frontend | React + Vite + Recharts |
| PWA | vite-plugin-pwa + Service Worker |
| LED Control | FastLED (WS2812B) |
| Sensor | Ultrasonic (RCWL-9610A) + Light (TEMT6000) |

## 📁 Loyiha strukturasi

```
smart-street-light/
├── firmware/                    # ESP32 firmware (PlatformIO)
│   ├── platformio.ini          # PlatformIO konfiguratsiya
│   ├── include/
│   │   ├── config.h            # Pin, WiFi, Firebase sozlamalari
│   │   ├── sensors.h
│   │   ├── light_control.h
│   │   ├── firebase_handler.h
│   │   └── statistics.h
│   └── src/
│       ├── main.cpp            # Asosiy dastur
│       ├── sensors.cpp         # Sensor o'qish (ultrasonic + light)
│       ├── light_control.cpp   # LED strip boshqaruv
│       ├── firebase_handler.cpp # Firebase ulanish va sync
│       └── statistics.cpp      # Energiya tejash hisoblash
├── web-dashboard/              # React PWA Dashboard
│   ├── src/
│   │   ├── App.jsx             # Asosiy komponent
│   │   ├── App.css             # Stillar
│   │   ├── firebase.js         # Firebase config
│   │   ├── mockData.js         # Demo rejim uchun
│   │   └── components/
│   │       ├── Login.jsx       # Auth sahifasi
│   │       ├── Dashboard.jsx   # Boshqaruv paneli
│   │       ├── Statistics.jsx  # Grafiklar
│   │       └── MotionLog.jsx   # Harakat logi
│   ├── vite.config.js          # Vite + PWA config
│   └── index.html
├── firebase.json               # Firebase Hosting config
├── database.rules.json         # DB xavfsizlik qoidalari
└── README.md
```

## 🚀 O'rnatish va ishga tushirish

### 1. ESP32 Firmware

```bash
cd firmware

# WiFi va Firebase ma'lumotlarini sozlang:
# include/config.h faylida WIFI_SSID, WIFI_PASS, FIREBASE_API_KEY ni o'zgartiring

# Kompilatsiya va yuklash:
~/.platformio/penv/bin/pio run --target upload

# Serial Monitor:
~/.platformio/penv/bin/pio device monitor
```

### 2. Web Dashboard (lokal ishga tushirish)

```bash
cd web-dashboard
npm install
npm run dev
```

### 3. Firebase Deploy

```bash
cd web-dashboard && npm run build
cd .. && firebase deploy --only hosting
```

## 📊 Firebase Database strukturasi

```json
{
  "device": {
    "status": {
      "light_on": false,
      "motion_detected": false,
      "distance_cm": 150,
      "ambient_light": 820,
      "mode": "auto",
      "last_motion": 1716000000,
      "uptime": 3600,
      "wifi_rssi": -45
    },
    "control": {
      "mode": "auto",
      "manual_light": false,
      "brightness": 100,
      "led_color": "#ffffff",
      "schedule_on": "18:00",
      "schedule_off": "06:00"
    },
    "config": {
      "timeout_sec": 30,
      "light_threshold": 300,
      "distance_threshold": 200
    }
  },
  "history": {
    "2026-05-15": {
      "motions_count": 45,
      "on_duration_min": 120,
      "energy_saved_percent": 75
    }
  },
  "motion_log": {}
}
```

## ⚡ Energiya tejash prinsipi

Oddiy ko'cha chiroqlari tun bo'yi (12 soat) yonib turadi. Bizning tizim:
- Faqat **harakat aniqlanganda** yonadi
- Harakat to'xtagandan **5 soniya** keyin o'chadi
- **Kunduz kuni** umuman yonmaydi
- Natija: **60-80% energiya tejash**

## 📱 PWA o'rnatish

1. https://smart-street-light-iot.web.app sahifani telefondan oching
2. "Add to Home Screen" / "Bosh ekranga qo'shish" tugmasini bosing
3. Native app kabi ishlaydi

## 👤 Muallif

**Baxrom** — Diplom ishi, 2026

## 📚 Dokumentatsiya

| Hujjat | Tavsif |
|--------|--------|
| [Arxitektura](docs/architecture.md) | Tizim diagrammasi, ma'lumot oqimi |
| [Hardware](docs/hardware.md) | Ulash sxemasi, pin konfiguratsiya |
| [Software](docs/software.md) | Dasturiy ta'minot tuzilishi |
| [Database](docs/database.md) | Firebase DB strukturasi |
| [Energiya tejash](docs/energy-saving.md) | Hisoblash va natijalar |
| [Foydalanuvchi qo'llanmasi](docs/user-guide.md) | Ishlatish bo'yicha |

## 📄 Litsenziya

MIT License
