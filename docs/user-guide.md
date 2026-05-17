# Foydalanuvchi qo'llanmasi

## 1. Tizimni ishga tushirish

1. ESP32 ni quvvat manbaiga ulang (USB yoki quyosh paneli)
2. ESP32 avtomatik WiFi ga ulanadi
3. Serial Monitor da "Tizim tayyor!" yozuvi chiqadi
4. Dashboard: https://smart-street-light-iot.web.app

## 2. Dashboard ga kirish

1. Brauzerda https://smart-street-light-iot.web.app oching
2. Login: `device@smartlight.com` / `SmartLight2026!`
3. Bosh sahifa ochiladi

## 3. Rejimlar

### 🤖 Avtomatik (Auto)
- Tizim o'zi qaror qabul qiladi
- Qorong'u + harakat = yonadi
- Yorug' = o'chiq
- 5s harakat yo'q = o'chadi

### 🖐 Qo'lda (Manual)
- Power tugmasini bosib yoqish/o'chirish
- Sensor ta'sir qilmaydi

### 📅 Jadval (Schedule)
- Sozlamalar → Yoqish/O'chirish vaqtini belgilang
- Masalan: 18:00 da yonsin, 06:00 da o'chsin

## 4. Statistika

- **Statistika** tabini bosing
- Haftalik energiya tejash grafigi
- Kunlik harakat soni
- Bugungi xulosa

## 5. Harakat logi

- **Log** tabini bosing
- Oxirgi 50 ta harakat ko'rinadi
- Vaqt, masofa, yorug'lik qiymati

## 6. Sozlamalar

| Parametr | Tavsif | Default |
|----------|--------|---------|
| Harakat timeout | Necha soniya kutish | 30s |
| Yorug'lik chegarasi | Qachon "qorong'u" | 300 |
| Aniqlash masofasi | Necha cm gacha | 200cm |

## 7. PWA o'rnatish (telefon)

1. Telefondan sahifani oching
2. "Bosh ekranga qo'shish" tugmasini bosing
3. Native app kabi ishlaydi

## 8. Demo rejim

- Yuqori o'ng burchakda "Demo/Live" tugmasi
- Demo: mock datalar bilan ishlaydi (offline)
- Live: haqiqiy qurilmadan ma'lumot oladi

## 9. Muammolar va yechimlar

| Muammo | Yechim |
|--------|--------|
| Dashboard "kutmoqda" | ESP32 yoqilganmi tekshiring |
| WiFi ulanmaydi | SSID/parol to'g'riligini tekshiring |
| Relay ishlamaydi | 3.3V relay ishlatayotganingizni tekshiring |
| Sensor noto'g'ri | Simlarni tekshiring (TRIG→4, ECHO→16) |
