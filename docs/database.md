# Firebase Database Strukturasi

## Umumiy ko'rinish

```
smart-street-light-iot-default-rtdb
├── device/
│   ├── status/        ← ESP32 yozadi (har 3s)
│   ├── control/       ← Dashboard yozadi, ESP32 tinglaydi
│   └── config/        ← Dashboard yozadi, ESP32 o'qiydi
├── history/           ← ESP32 yozadi (har 60s)
└── motion_log/        ← ESP32 yozadi (harakat aniqlanganda)
```

## device/status (ESP32 → Cloud)

| Maydon | Turi | Tavsif |
|--------|------|--------|
| light_on | boolean | Relay holati |
| motion_detected | boolean | Harakat bormi |
| distance_cm | number | Ultrasonic masofa (cm) |
| ambient_light | number | Yorug'lik qiymati (0-4095) |
| mode | string | Hozirgi rejim |
| last_motion | number | Oxirgi harakat (unix timestamp) |
| uptime | number | Ishlash vaqti (soniya) |
| wifi_rssi | number | WiFi signal kuchi (dBm) |

## device/control (Dashboard → ESP32)

| Maydon | Turi | Tavsif |
|--------|------|--------|
| mode | string | "auto" / "manual" / "schedule" |
| manual_light | boolean | Qo'lda yoqish/o'chirish |
| schedule_on | string | Yoqish vaqti "HH:MM" |
| schedule_off | string | O'chirish vaqti "HH:MM" |

## device/config (Dashboard → ESP32)

| Maydon | Turi | Default | Tavsif |
|--------|------|---------|--------|
| timeout_sec | number | 30 | Harakat timeout |
| light_threshold | number | 300 | Yorug'lik chegarasi |
| distance_threshold | number | 200 | Aniqlash masofasi (cm) |

## history/{YYYY-MM-DD} (Kunlik statistika)

| Maydon | Turi | Tavsif |
|--------|------|--------|
| motions_count | number | Kunlik harakat soni |
| on_duration_min | number | Yonish vaqti (daqiqa) |
| energy_saved_percent | number | Tejash foizi |

## motion_log/{push_id} (Harakat logi)

| Maydon | Turi | Tavsif |
|--------|------|--------|
| time | number | Timestamp (ms) |
| distance | number | Aniqlangan masofa |
| light | number | Yorug'lik qiymati |

## Xavfsizlik qoidalari

```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```

> Eslatma: Production uchun `"auth != null"` qo'yish tavsiya etiladi.
