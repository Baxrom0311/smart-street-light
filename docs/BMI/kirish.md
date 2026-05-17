O'ZBEKISTON RESPUBLIKASI OLIY TA'LIM, FAN VA INNOVATSIYALAR VAZIRLIGI
MUHAMMAD AL-XORAZMIY NOMIDAGI
TOSHKENT AXBOROT TEXNOLOGIYALARI UNIVERSITETI
"KOMPYUTER INJINIRINGI" FAKULTETI
"DASTURIY INJINIRING" KAFEDRASI


BITIRUV MALAKAVIY ISHI

Mavzu:
"SMART STREET TIZIMIDA ULTRATOVUSH SENSORI ORQALI ENERGIYA TEJAMKORLIGINI TA'MINLOVCHI YORITISH TIZIMINI ISHLAB CHIQISH"


Bajardi: _______________________
Ilmiy rahbar: _______________________

Toshkent — 2026


MUNDARIJA

KIRISH ............................................................................................................. 4

I BOB. SMART STREET TIZIMIDA YORITISH TIZIMLARI TIZIMLI TAHLILI VA MASALANING QO'YILISHI
1.1. Smart Street tizimlarida energiya tejamkor yoritish tizimlari va ularning ahamiyati ............................................................. 9
1.2. Ultratovush sensorlarning ishlash prinsipi va texnik xususiyatlari ................................................................................. 19
1.3. Masalaning qo'yilishi ............................................................................. 32

II BOB. AMALIY QISM
2.1. Tizimni loyihalash: texnik vositalar va komponentlarni tanlash .......... 40
2.2. Masofani aniqlash algoritmi: ultrasonic sensor yordamida obyektni aniqlash .......................................................... 49
2.3. Yoritish tizimini boshqarish dasturi va tizimning ishlash jarayoni va natijalar tahlili .................................................... 58

XULOSA ............................................................................................................. 65
FOYDALANILGAN ADABIYOTLAR RO'YXATI ............................................. 68
ILOVALAR ......................................................................................................... 70


KIRISH

Mavzuning dolzarbligi.

Hozirgi kunda dunyo miqyosida energiya iste'moli keskin o'sib bormoqda va bu jarayon atrof-muhitga salbiy ta'sir ko'rsatmoqda. Birlashgan Millatlar Tashkilotining ma'lumotlariga ko'ra, ko'cha yoritish tizimlari shahar elektr energiyasi iste'molining 15-25 foizini tashkil etadi [1]. An'anaviy ko'cha yoritish tizimlari tun bo'yi uzluksiz ishlaydi, ya'ni harakat bo'lmagan vaqtlarda ham energiya sarflanadi. Bu holat nafaqat iqtisodiy zarar keltiradi, balki karbon izini oshiradi va ekologik muammolarni kuchaytiradi.

Internet of Things (IoT) texnologiyasining jadal rivojlanishi aqlli shahar (Smart City) konsepsiyasini amalga oshirish imkonini yaratmoqda. Statista tahliliy kompaniyasining 2024-yildagi hisobotiga ko'ra, dunyo bo'ylab IoT qurilmalari soni 2025-yilga kelib 30 milliarddan oshgan bo'lib, 2030-yilga borib bu ko'rsatkich 75 milliardga yetishi prognoz qilinmoqda [2]. Aqlli ko'cha yoritish tizimlari IoT ning eng samarali qo'llanilish sohalaridan biri hisoblanadi.

Ultratovush sensorlari harakatni aniqlash uchun eng ishonchli va arzon vositalardan biri bo'lib, ular ob-havo sharoitlariga kam ta'sirchan, keng burchak ostida ishlash qobiliyatiga ega va past energiya iste'mol qiladi [3]. Ushbu sensorlarni mikrokontroller bilan birgalikda qo'llash orqali energiya tejamkor yoritish tizimini yaratish mumkin bo'lib, bu tizim faqat harakat aniqlanganda yoritgichni yoqadi va ma'lum vaqt o'tgach avtomatik o'chiradi.

O'zbekiston Respublikasi Prezidentining 2020-yil 5-oktabrdagi PF-6079-sonli Farmoni asosida qabul qilingan "Raqamli O'zbekiston — 2030" strategiyasi IoT va aqlli shahar texnologiyalarini rivojlantirishni ustuvor yo'nalish sifatida belgilab beradi [4]. Shuningdek, O'zbekiston Respublikasi Vazirlar Mahkamasining 2023-yil 15-martdagi 58-sonli qarori bilan tasdiqlangan "Energiya tejamkorligi va energiya samaradorligi to'g'risida"gi dastur energiya resurslaridan oqilona foydalanish zarurligini ta'kidlaydi [5]. Aynan shu hujjatlar bilan belgilangan vazifalarni bajarish nuqtai nazaridan ham mazkur mavzu juda dolzarbdir.

Ishning ilmiy yangiligi.

Mazkur bitiruv malakaviy ishida ishlab chiqilgan tizim quyidagi ilmiy va amaliy yangiliklarga ega:

1. ESP32 mikrokontrolleri asosida ultratovush sensori (RCWL-9610A) va yorug'lik sensori (TEMT6000) birgalikda qo'llanilgan energiya tejamkor yoritish tizimi ishlab chiqildi. Mavjud yechimlardan farqli ravishda, tizim bir vaqtning o'zida harakatni aniqlash va kunduz/tun holatini farqlash imkoniyatiga ega.

2. Firebase Realtime Database asosida real vaqt rejimida masofadan boshqarish va monitoring tizimi yaratildi. Bu tizim qurilmaning holatini har 3 soniyada yangilab turadi va foydalanuvchiga veb-interfeys orqali boshqarish imkonini beradi.

3. Non-blocking WiFi boshqaruv algoritmi ishlab chiqildi: tizim internet aloqasi uzilgan holda ham avtonom ravishda ishlashda davom etadi va aloqa tiklanganda avtomatik sinxronizatsiya qiladi.

4. Progressive Web Application (PWA) texnologiyasi asosida cross-platform dashboard yaratildi. U desktop va mobil qurilmalarda bir xil samarali ishlaydi, offline rejimni qo'llab-quvvatlaydi va native ilova sifatida o'rnatilishi mumkin.

Ishning maqsadi.

Bitiruv malakaviy ishining asosiy maqsadi — ultratovush sensori yordamida harakatni aniqlash va yorug'lik sensori orqali kunduz/tun holatini farqlash asosida energiya tejamkor ko'cha yoritish tizimini ishlab chiqish, uni masofadan boshqarish imkoniyatini yaratish va energiya tejash samaradorligini amaliy tajribalar orqali isbotlashdan iborat.

Ishning vazifalari.

Yuqorida belgilangan maqsadga erishish uchun quyidagi vazifalar amalga oshirildi:

1) Ko'cha yoritish tizimlarining hozirgi holati va energiya tejamkorlik muammolarini o'rganish;
2) Ultratovush sensorlarining ishlash prinsipini va texnik xususiyatlarini tadqiq qilish;
3) ESP32 mikrokontrolleri asosida hardware platformani loyihalash va komponentlarni tanlash;
4) Harakatni aniqlash algoritmini ishlab chiqish (debounce, hold timer, hysteresis);
5) Firebase Realtime Database bilan real vaqt sinxronizatsiya tizimini yaratish;
6) React asosida Progressive Web Application (PWA) dashboard ishlab chiqish;
7) Tizimning energiya tejash samaradorligini hisoblash va amaliy tajribalar o'tkazish;
8) Tizimni real sharoitlarda sinab ko'rish va natijalarni tahlil qilish.

Tadqiqot obyekti.

Tadqiqot obyekti — ko'cha yoritish tizimlari va ularda energiya tejamkorlikni ta'minlash uchun ishlatiladigan sensorli boshqaruv tizimlari. Tadqiqot davomida ESP32 mikrokontrolleri, RCWL-9610A ultratovush sensori, TEMT6000 yorug'lik sensori va relay moduli asosida amaliy prototip yaratildi.

Tadqiqot predmeti.

Tadqiqot predmeti — ultratovush sensori yordamida harakatni aniqlash algoritmlari, IoT texnologiyalari asosida masofadan boshqarish tizimlari va ularning energiya tejamkorlikka ta'siri.

Tadqiqot usullari.

Bitiruv ishi davomida quyidagi tadqiqot usullaridan foydalanildi: ilmiy adabiyotlarni tahlil va sintez qilish; sistemali yondashuv; eksperimental tadqiqotlar; qiyosiy tahlil; matematik modellashtirish (energiya tejash formulalari); dasturiy injiniring printsiplari; prototiplash va iterativ ishlab chiqish metodologiyasi.

Ishning amaliy ahamiyati.

Ishlab chiqilgan tizim quyidagi amaliy maqsadlarda foydalanish mumkin:
- Shahar va qishloq ko'chalarida energiya tejamkor yoritish tizimini joriy etish;
- Bog'lar, parkovkalar va yopiq hududlarda avtomatik yoritish;
- Sanoat korxonalari va omborxonalarda energiya sarfini kamaytirish;
- Aqlli shahar (Smart City) loyihalarida yoritish infratuzilmasini modernizatsiya qilish;
- Ta'lim muassasalarida IoT va embedded systems bo'yicha amaliy o'quv materiali sifatida.

Bitiruv malakaviy ishining tarkibi va hajmi.

Bitiruv malakaviy ishi kirish, ikkita asosiy bob, xulosa, foydalanilgan adabiyotlar ro'yxati va ilovalardan iborat. Birinchi bobda ko'cha yoritish tizimlari, ultratovush sensorlari va IoT texnologiyalari nazariy jihatdan tahlil qilingan, masala qo'yilishi shakllantirilgan. Ikkinchi bobda esa tizim arxitekturasi, hardware va software qismlarini amalda ishlab chiqish, dasturlash va sinov natijalari batafsil bayon etilgan. Ishning umumiy hajmi 70 sahifani tashkil etadi, matn ichida rasmlar, sxemalar, jadvallar va kod fragmentlari keltirilgan. Foydalanilgan adabiyotlar ro'yxati 20 dan ortiq manbadan iborat.
