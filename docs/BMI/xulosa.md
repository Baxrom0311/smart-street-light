XULOSA

Mazkur bitiruv malakaviy ishida "Smart Street tizimida ultratovush sensori orqali energiya tejamkorligini ta'minlovchi yoritish tizimini ishlab chiqish" mavzusi bo'yicha tadqiqot olib borildi va amaliy tizim yaratildi.

Ishning asosiy natijalari quyidagilardan iborat:

1. ESP32 mikrokontrolleri, RCWL-9610A ultratovush sensori va TEMT6000 yorug'lik sensori asosida to'liq ishlaydigan energiya tejamkor ko'cha yoritish tizimi ishlab chiqildi. Tizim harakatni 2 metrgacha masofada aniqlaydi va kunduz/tun holatini avtomatik farqlaydi.

2. Debounce, hold timer va hysteresis algoritmlarini qo'llash orqali sensorlarning ishonchliligi oshirildi. Debounce algoritmi noto'g'ri o'lchov natijalarini filtrlaydi, hold timer yoritgichning tez-tez yonib-o'chishini oldini oladi, hysteresis esa yorug'lik chegarasidagi tebranishlarni bartaraf etadi.

3. Firebase Realtime Database asosida real vaqt rejimida masofadan boshqarish tizimi yaratildi. ESP32 har 3 soniyada sensor ma'lumotlarini bulutga yuboradi va dashboard dan kelgan buyruqlarni stream orqali qabul qiladi. Tizimning javob berish vaqti 200-500 millisekund oralig'ida.

4. React asosida Progressive Web Application (PWA) dashboard ishlab chiqildi. Dashboard desktop va mobil qurilmalarda responsive ishlaydi, offline rejimni qo'llab-quvvatlaydi va native ilova sifatida o'rnatilishi mumkin. Optimistic UI pattern qo'llanilgan bo'lib, foydalanuvchi buyruq berganda UI darhol yangilanadi.

5. Non-blocking WiFi boshqaruv algoritmi ishlab chiqildi. Tizim internet aloqasi bo'lmagan holda ham avtonom ishlaydi — sensorlar va relay to'xtamaydi. WiFi uzilganda captive portal (AP) ochiladi va foydalanuvchi yangi WiFi ma'lumotlarini kiritishi mumkin. Ma'lumotlar NVS (Non-Volatile Storage) ga saqlanadi.

6. 5 kunlik amaliy sinov natijalari shuni ko'rsatdiki, tizim o'rtacha 80.8% energiya tejash imkonini beradi. Bu an'anaviy tizimga nisbatan 5 barobar kam energiya sarflanishini anglatadi. Bitta 60W yoritgich uchun yillik tejamkorlik 212.4 kWh yoki 106,200 so'mni tashkil etadi.

7. Tizimning umumiy narxi (ESP32 + sensorlar + relay) taxminan 50,000-70,000 so'mni tashkil etadi, bu tijorat yechimlariga (Philips CityTouch, Telensa) nisbatan 10-50 marta arzon.

Ishning amaliy ahamiyati shundaki, ishlab chiqilgan tizim kichik hududlar — bog'lar, parkovkalar, qishloq ko'chalari, sanoat korxonalari uchun arzon va samarali yechim sifatida qo'llanilishi mumkin. Tizim ochiq kodli (open-source) bo'lib, GitHub platformasida joylashtirilgan va har kim foydalanishi mumkin.

Kelajakda tizimni yanada rivojlantirish yo'nalishlari:
- OTA (Over-The-Air) yangilash — firmware ni masofadan yangilash;
- LoRa tarmoq — keng hududlarda bir nechta yoritgichni boshqarish;
- Machine Learning — harakat naqshlarini o'rganish va bashorat qilish;
- Quyosh paneli integratsiyasi — to'liq avtonom energiya ta'minoti;
- Dimmer funksiyasi — yorug'lik darajasini bosqichma-bosqich boshqarish.


FOYDALANILGAN ADABIYOTLAR RO'YXATI

[1] International Energy Agency (IEA). "Energy Efficiency 2023: Lighting." IEA Publications, 2023. https://www.iea.org/reports/energy-efficiency-2023 [Murojaat sanasi: 2026-yil 10-may]

[2] Statista Research Department. "Number of Internet of Things (IoT) connected devices worldwide from 2019 to 2030." Statista, 2024. https://www.statista.com/statistics/1183457/iot-connected-devices-worldwide/ [Murojaat sanasi: 2026-yil 10-may]

[3] Carullo A., Parvis M. "An ultrasonic sensor for distance measurement in automotive applications." IEEE Sensors Journal, vol. 1, no. 2, pp. 143-147, 2001.

[4] O'zbekiston Respublikasi Prezidentining Farmoni. "Raqamli O'zbekiston — 2030 strategiyasi." PF-6079, 2020-yil 5-oktabr.

[5] O'zbekiston Respublikasi Vazirlar Mahkamasi. "Energiya tejamkorligi va energiya samaradorligi to'g'risida." 58-son qaror, 2023-yil 15-mart.

[6] Kostic M., Djokic L. "Recommendations for energy efficient and visually acceptable street lighting." Energy, vol. 34, no. 10, pp. 1565-1572, 2009.

[7] Rea M.S. "The IESNA Lighting Handbook: Reference and Application." Illuminating Engineering Society of North America, 9th edition, 2000.

[8] Zanella A., Bui N., Castellani A., Vangelista L., Zorzi M. "Internet of Things for Smart Cities." IEEE Internet of Things Journal, vol. 1, no. 1, pp. 22-32, 2014.

[9] Radulovic D., Skok S., Kirincic V. "Energy efficiency public lighting management in the cities." Energy, vol. 36, no. 4, pp. 1908-1915, 2011.

[10] Leccese F. "Remote-control system of high efficiency and intelligent street lighting using a ZigBee network of devices and sensors." IEEE Transactions on Power Delivery, vol. 28, no. 1, pp. 21-28, 2013.

[11] Philips Lighting. "CityTouch: Connected street lighting management." Philips Technical Documentation, 2022. https://www.lighting.philips.com/main/systems/connected-lighting/citytouch [Murojaat sanasi: 2026-yil 12-may]

[12] Telensa Ltd. "Smart Street Lighting Solutions." Technical White Paper, 2023. https://www.telensa.com/smart-street-lighting [Murojaat sanasi: 2026-yil 12-may]

[13] Tvilight BV. "Dynamic Street Lighting with CitySense." Product Documentation, 2023. https://www.tvilight.com/citysense [Murojaat sanasi: 2026-yil 12-may]

[14] Parkash, Prabu V., Rajendra D. "Internet of Things Based Intelligent Street Lighting System for Smart City." International Journal of Innovative Research in Science, Engineering and Technology, vol. 5, no. 5, 2016.

[15] Kinsler L.E., Frey A.R., Coppens A.B., Sanders J.V. "Fundamentals of Acoustics." John Wiley & Sons, 4th edition, 2000.

[16] Borenstein J., Everett H.R., Feng L. "Navigating Mobile Robots: Systems and Techniques." A.K. Peters Ltd., 1996.

[17] RCWL-9610A Datasheet. "Ultrasonic Ranging Module." Shenzhen RCWL Electronics, 2021.

[18] Vishay Semiconductors. "TEMT6000 - Ambient Light Sensor." Datasheet, Document Number 81579, 2011.

[19] Elmenreich W. "Sensor Fusion in Time-Triggered Systems." PhD Thesis, Vienna University of Technology, 2002.

[20] Espressif Systems. "ESP32 Technical Reference Manual." Version 4.8, 2023. https://www.espressif.com/sites/default/files/documentation/esp32_technical_reference_manual_en.pdf [Murojaat sanasi: 2026-yil 15-may]

[21] Firebase Documentation. "Firebase Realtime Database." Google LLC, 2024. https://firebase.google.com/docs/database [Murojaat sanasi: 2026-yil 15-may]

[22] React Documentation. "React: A JavaScript library for building user interfaces." Meta Platforms, 2024. https://react.dev [Murojaat sanasi: 2026-yil 15-may]

[23] Mobizt. "Firebase ESP32 Client Library." GitHub Repository, 2024. https://github.com/mobizt/Firebase-ESP32 [Murojaat sanasi: 2026-yil 15-may]

[24] PlatformIO. "PlatformIO: Professional collaborative platform for embedded development." 2024. https://platformio.org [Murojaat sanasi: 2026-yil 15-may]

[25] Vite.js. "Vite: Next Generation Frontend Tooling." 2024. https://vitejs.dev [Murojaat sanasi: 2026-yil 16-may]
