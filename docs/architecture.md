# Tizim Arxitekturasi

## Umumiy ko'rinish

```
┌──────────────────────────────────────────────────────────────────┐
│                        CLOUD (Firebase)                           │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────────┐    │
│  │  Realtime   │  │    Auth      │  │     Hosting          │    │
│  │  Database   │  │  (Email/Pass)│  │  (smart-street-      │    │
│  │             │  │              │  │   light-iot.web.app) │    │
│  └──────┬──────┘  └──────────────┘  └─────────────────────┘    │
└─────────┼────────────────────────────────────────────────────────┘
          │
          │ HTTPS / WebSocket
          │
    ┌─────┴─────┐                    ┌────────────────────┐
    │           │◄───── WiFi ───────►│                    │
    │  ESP32    │                    │  React PWA         │
    │  DevKit   │                    │  Dashboard         │
    │           │                    │                    │
    └─────┬─────┘                    └────────────────────┘
          │
    ┌─────┴─────────────────────┐
    │      Sensorlar + Relay     │
    │  ┌─────────┐ ┌─────────┐ │
    │  │RCWL-9610│ │TEMT6000 │ │
    │  │Ultrasonic│ │Light    │ │
    │  └─────────┘ └─────────┘ │
    │  ┌─────────┐ ┌─────────┐ │
    │  │  Relay  │ │  LED    │ │
    │  │  Module │ │  Lamp   │ │
    │  └─────────┘ └─────────┘ │
    └───────────────────────────┘
```

## Ma'lumot oqimi

```
Sensor → ESP32 → Firebase RTDB → Web Dashboard (real-time)
                                        │
Web Dashboard → Firebase RTDB → ESP32 → Relay → LED
(buyruq)         (control)      (stream)
```

## Rejimlar

```
┌─────────────────────────────────────────────┐
│              REJIM TANLASH                    │
├─────────────┬──────────────┬────────────────┤
│   AUTO      │   MANUAL     │   SCHEDULE     │
│             │              │                │
│ Sensor →    │ Dashboard →  │ Vaqt →         │
│ Qaror →     │ Toggle →     │ Qaror →        │
│ Relay       │ Relay        │ Relay          │
└─────────────┴──────────────┴────────────────┘
```

## Auto rejim logikasi

```
        ┌─────────────┐
        │   START     │
        └──────┬──────┘
               ▼
        ┌─────────────┐     Ha
        │ Yorug'mi?   ├──────────► LED O'CHIQ
        │ Light > 350 │
        └──────┬──────┘
               │ Yo'q
               ▼
        ┌─────────────┐     Yo'q
        │ Harakat     ├──────────► LED O'CHIQ
        │ bormi?      │            (5s kutish)
        │ Dist < 200  │
        └──────┬──────┘
               │ Ha
               ▼
        ┌─────────────┐
        │  LED YONIQ  │
        └─────────────┘
```
