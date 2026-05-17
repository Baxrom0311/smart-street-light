II BOB. AMALIY QISM

2.1. Tizimni loyihalash: texnik vositalar va komponentlarni tanlash

2.1.1. Mikrokontroller tanlovi

Tizimning asosiy boshqaruv elementi sifatida ESP32 DevKit (38-pin) mikrokontrolleri tanlandi. Tanlash jarayonida bir nechta alternativalar ko'rib chiqildi:

2.1-jadval. Mikrokontrollerlarning qiyosiy tahlili

| Parametr | Arduino Uno | ESP8266 | ESP32 | Raspberry Pi |
|----------|-------------|---------|-------|--------------|
| Protsessor | ATmega328P | Tensilica L106 | Xtensa LX6 (2 yadro) | ARM Cortex-A72 |
| Taktli chastota | 16 MHz | 80 MHz | 240 MHz | 1.5 GHz |
| RAM | 2 KB | 80 KB | 520 KB | 4 GB |
| Flash | 32 KB | 4 MB | 4 MB | microSD |
| WiFi | Yo'q | 802.11 b/g/n | 802.11 b/g/n | 802.11 ac |
| Bluetooth | Yo'q | Yo'q | BLE 4.2 | BLE 5.0 |
| ADC | 6 kanal (10-bit) | 1 kanal (10-bit) | 18 kanal (12-bit) | Yo'q |
| GPIO | 14 | 11 | 34 | 40 |
| Narx | ~$5 | ~$3 | ~$5 | ~$35 |
| Energiya iste'moli | 50 mA | 80 mA | 150 mA | 600 mA |

ESP32 quyidagi sabablarga ko'ra tanlandi:
1) Ichki WiFi moduli — tashqi modul kerak emas;
2) Ikki yadroli protsessor — bir yadro sensorlar, ikkinchisi WiFi uchun;
3) 12-bitli ADC — yorug'lik sensorini aniq o'qish uchun;
4) Arzon narx — loyiha byudjetiga mos;
5) Keng jamoa va kutubxonalar — ishlab chiqish oson;
6) 3.3V logika — RCWL-9610A bilan to'g'ridan-to'g'ri ulash mumkin.

2.1.2. Tizim arxitekturasi

Tizim uch qatlamli arxitekturaga ega:

2.1-rasm. Tizimning umumiy arxitekturasi

Quyi qatlam (Hardware):
- ESP32 DevKit mikrokontroller
- RCWL-9610A ultratovush sensori
- TEMT6000 yorug'lik sensori
- Relay moduli (3.3V)
- LED yoritgich

O'rta qatlam (Cloud):
- Firebase Realtime Database
- Firebase Authentication
- Firebase Hosting

Yuqori qatlam (Client):
- React PWA Dashboard
- Responsive UI (desktop + mobile)

2.1.3. Elektr sxemasi va pin konfiguratsiya

2.2-jadval. ESP32 pin tayinlash

| ESP32 Pin | Komponent | Signal turi | Yo'nalish |
|-----------|-----------|-------------|-----------|
| GPIO 4 | RCWL-9610A TRIG | Digital | OUTPUT |
| GPIO 16 | RCWL-9610A ECHO | Digital | INPUT |
| GPIO 34 | TEMT6000 OUT | Analog (ADC1) | INPUT |
| GPIO 26 | Relay IN | Digital | OUTPUT |
| GPIO 2 | Onboard LED | Digital | OUTPUT |
| 3.3V | Sensorlar VCC | Quvvat | — |
| GND | Umumiy GND | Quvvat | — |

2.2-rasm. Tizimning elektr ulash sxemasi

Pin tanlashda quyidagi qoidalarga amal qilindi:
- GPIO 0, 2, 5, 12, 15 — strapping pinlar, flash jarayonida ishlatiladi;
- GPIO 6-11 — ichki flash SPI uchun band;
- GPIO 34-39 — faqat input (analog o'qish uchun ideal);
- GPIO 4, 16, 26 — xavfsiz, har qanday maqsadda ishlatish mumkin.

2.1.4. Quvvat ta'minoti

Tizim quyidagi quvvat manbalaridan ishlashi mumkin:
1) USB (5V) — ishlab chiqish va sinov uchun;
2) Quyosh paneli (6V) + Li-ion akkumulyator (3.7V) — avtonom ishlash uchun;
3) Tashqi quvvat manbai (5-12V) — doimiy o'rnatish uchun.

Tizimning umumiy energiya iste'moli:
- ESP32 (WiFi faol): ~150 mA
- RCWL-9610A: ~2 mA
- TEMT6000: ~0.1 mA
- Relay moduli: ~70 mA (yoqilganda)
- Jami: ~222 mA (maksimal)


2.2. Masofani aniqlash algoritmi: ultrasonic sensor yordamida obyektni aniqlash

2.2.1. Asosiy o'lchash jarayoni

Ultratovush sensori yordamida masofa o'lchash quyidagi bosqichlardan iborat:

1-bosqich: TRIG pinga 10 mikrosekundlik HIGH signal yuboriladi;
2-bosqich: Sensor 40 kHz chastotada 8 ta ultratovush impulsi yuboradi;
3-bosqich: Sensor ECHO pinni HIGH holatga o'tkazadi;
4-bosqich: Ultratovush to'lqini to'siqdan aks etib qaytadi;
5-bosqich: Sensor ECHO pinni LOW holatga qaytaradi;
6-bosqich: ECHO signalining davomiyligi o'lchanadi;
7-bosqich: Masofa hisoblanadi: d = duration × 0.034 / 2

2.3-rasm. Ultratovush sensori ishlash diagrammasi (timing diagram)

ESP32 dasturida bu jarayon quyidagicha amalga oshiriladi:

    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);
    long duration = pulseIn(ECHO_PIN, HIGH, 30000);
    float distance = (duration > 0) ? duration * 0.034 / 2.0 : 999;

30000 mikrosekundlik timeout — bu taxminan 5 metr masofaga teng. Agar echo qaytmasa, masofa 999 cm deb belgilanadi (to'siq yo'q).

2.2.2. Debounce algoritmi

Ultratovush sensorining o'lchov natijalari ba'zan noto'g'ri bo'lishi mumkin — shovqin, ko'p yo'lli aks etish yoki vaqtinchalik to'siqlar sababli. Shuning uchun debounce algoritmi qo'llanildi:

    Har 300ms da o'lchov olinadi
    3 ta ketma-ket o'lchov yig'iladi
    Agar 3 tadan kamida 2 tasi harakat ko'rsatsa:
        → Harakat aniqlangan (lastMotionTime yangilanadi)
    Aks holda:
        → O'zgarmaydi

2.4-rasm. Debounce algoritmining blok-sxemasi

2.2.3. Hold timer mexanizmi

Harakat aniqlangandan keyin yoritgich darhol o'chmasligi uchun 5 soniyalik hold timer ishlatiladi:

    motion = (millis() - lastMotionTime < 5000)

Bu degani: oxirgi harakat aniqlangandan beri 5 soniya o'tmagan bo'lsa — "harakat bor" holati saqlanadi. Bu mexanizm yoritgichning tez-tez yonib-o'chishini oldini oladi va foydalanuvchi uchun qulay muhit yaratadi.

2.2.4. Hysteresis (gisterezis) mexanizmi

Yorug'lik sensori qiymati chegara atrofida tebranishi mumkin (masalan, 295-305 orasida). Bu holda yoritgich tez-tez yonib-o'chadi. Buni oldini olish uchun hysteresis qo'llanildi:

    Agar light < (threshold - 50): isDark = true   // 250 dan past
    Agar light > (threshold + 50): isDark = false  // 350 dan yuqori
    250-350 orasida: holat o'zgarmaydi

2.5-rasm. Hysteresis mexanizmining grafik ko'rinishi


2.3. Yoritish tizimini boshqarish dasturi va tizimning ishlash jarayoni va natijalar tahlili

2.3.1. Dasturiy ta'minot arxitekturasi

Firmware modular arxitekturada yozilgan — har bir funksional blok alohida faylda:

2.3-jadval. Firmware modullari

| Modul | Fayl | Vazifasi | O'lcham |
|-------|------|----------|---------|
| Asosiy | main.cpp | WiFi, AP, loop | 153 qator |
| Sensorlar | sensors.cpp | O'lchash, debounce | 61 qator |
| Yoritish | light_control.cpp | Relay boshqaruv | 62 qator |
| Firebase | firebase_handler.cpp | Cloud sync | 129 qator |
| Statistika | statistics.cpp | Energiya hisob | 68 qator |
| Konfiguratsiya | config.h | Sozlamalar | 28 qator |

2.3.2. Ishlash rejimlari

Tizim uchta rejimda ishlaydi:

1) AUTO rejim — sensor asosida avtomatik boshqaruv:
   - Yorug' (Light > 350) → Relay O'CHIQ
   - Qorong'u (Light < 250) + Harakat (Distance < 200cm) → Relay YONIQ
   - Qorong'u + Harakat yo'q (5s) → Relay O'CHIQ

2) MANUAL rejim — foydalanuvchi dashboard dan boshqaradi:
   - Toggle tugmasi orqali yoqish/o'chirish
   - Sensor ta'sir qilmaydi

3) SCHEDULE rejim — vaqt jadvali bo'yicha:
   - Belgilangan vaqtda yoqish (masalan, 18:00)
   - Belgilangan vaqtda o'chirish (masalan, 06:00)

2.6-rasm. Tizim rejimlari state diagrammasi

2.3.3. Firebase integratsiya

Firebase Realtime Database tizimning "miyasi" vazifasini bajaradi — ESP32 va Dashboard o'rtasida real vaqt aloqasini ta'minlaydi:

ESP32 → Firebase (har 3 soniyada):
- device/status: yoritgich holati, sensor qiymatlari, WiFi signal, uptime

Dashboard → Firebase → ESP32 (stream):
- device/control: rejim, manual_light
- device/config: timeout, threshold qiymatlari

2.4-jadval. Firebase ma'lumotlar strukturasi

| Yo'l | Turi | Yangilanish | Manba |
|------|------|-------------|-------|
| device/status | JSON | Har 3s | ESP32 |
| device/control | JSON | Foydalanuvchi | Dashboard |
| device/config | JSON | Foydalanuvchi | Dashboard |
| history/{sana} | JSON | Har 60s | ESP32 |
| motion_log/{id} | JSON | Harakat vaqtida | ESP32 |

2.3.4. Web Dashboard

Dashboard React framework asosida Progressive Web Application (PWA) sifatida ishlab chiqilgan:

Texnologiyalar:
- React 19 — UI framework
- Vite 8 — build tool
- Firebase SDK 10 — real-time ma'lumot
- Recharts — grafiklar
- vite-plugin-pwa — offline support

Dashboard funksiyalari:
1) Login sahifasi — Firebase Authentication
2) Bosh sahifa — power toggle, rejim tanlash, sensor qiymatlari
3) Statistika — haftalik energiya tejash grafiklari
4) Harakat logi — oxirgi 50 ta event
5) Sozlamalar — threshold, timeout, jadval

2.7-rasm. Dashboard bosh sahifasi (desktop ko'rinishi)
2.8-rasm. Dashboard bosh sahifasi (mobile ko'rinishi)

2.3.5. WiFi boshqaruv va offline ishlash

Tizim internet aloqasi bo'lmagan holda ham to'liq avtonom ishlaydi:

1) Yoqilganda NVS (Non-Volatile Storage) dan saqlangan WiFi ma'lumotlarini o'qiydi;
2) 10 soniya ichida WiFi ga ulanishga harakat qiladi;
3) Ulanmasa — "SmartLight-Setup" AP ochadi (captive portal);
4) Sensorlar va relay DOIMO ishlaydi (WiFi bo'lmasa ham);
5) Har 60 soniyada WiFi qayta tekshiriladi;
6) WiFi topilsa — Firebase sinxronizatsiya boshlanadi, AP o'chadi.

2.9-rasm. WiFi boshqaruv algoritmining blok-sxemasi

2.3.6. Sinov natijalari

Tizim 5 kun davomida real sharoitlarda sinovdan o'tkazildi:

2.5-jadval. 5 kunlik sinov natijalari

| Kun | Harakatlar soni | Yonish vaqti (min) | Energiya tejash % |
|-----|----------------|--------------------|--------------------|
| 1 | 45 | 120 | 83.3% |
| 2 | 62 | 155 | 78.5% |
| 3 | 38 | 95 | 86.8% |
| 4 | 71 | 180 | 75.0% |
| 5 | 55 | 140 | 80.6% |
| **O'rtacha** | **54.2** | **138** | **80.8%** |

2.10-rasm. 5 kunlik energiya tejash grafigi

Natijalar shuni ko'rsatadiki, tizim o'rtacha **80.8%** energiya tejash imkonini beradi. Bu an'anaviy tizimga nisbatan 5 barobar kam energiya sarflanishini anglatadi.

2.3.7. Qiyosiy tahlil

2.6-jadval. An'anaviy va Smart Street tizimining qiyosiy ko'rsatkichlari

| Ko'rsatkich | An'anaviy | Smart Street | Farq |
|-------------|-----------|--------------|------|
| Kunlik iste'mol (60W lamp) | 720 Wh | 138 Wh | -80.8% |
| Oylik iste'mol | 21.6 kWh | 4.14 kWh | -80.8% |
| Yillik iste'mol | 262.8 kWh | 50.4 kWh | -80.8% |
| Yillik xarajat (1 kWh = 500 so'm) | 131,400 so'm | 25,200 so'm | -106,200 so'm |
| CO2 emissiya (yiliga) | 157.7 kg | 30.2 kg | -127.5 kg |

Hisoblash asosi:
- Tun davomiyligi: 12 soat
- Lamp quvvati: 60W
- Elektr narxi: 500 so'm/kWh (O'zbekiston tarifi)
- CO2 koeffitsienti: 0.6 kg CO2/kWh
