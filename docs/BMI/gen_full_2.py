#!/usr/bin/env python3
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_full.docx')

def hc(t, sz=16):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(t); r.bold = True; r.font.size = Pt(sz); r.font.name = 'Times New Roman'
def h2(t):
    doc.add_paragraph()
    p = doc.add_paragraph(); r = p.add_run(t); r.bold = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'
def t(text):
    p = doc.add_paragraph(text); p.paragraph_format.first_line_indent = Cm(1.25)
    for r in p.runs: r.font.name = 'Times New Roman'; r.font.size = Pt(14)

hc("KIRISH")
doc.add_paragraph()

h2("Mavzuning dolzarbligi.")
t("Hozirgi kunda dunyo miqyosida energiya iste'moli keskin o'sib bormoqda va bu jarayon atrof-muhitga salbiy ta'sir ko'rsatmoqda. Birlashgan Millatlar Tashkilotining ma'lumotlariga ko'ra, ko'cha yoritish tizimlari shahar elektr energiyasi iste'molining 15-25 foizini tashkil etadi. Dunyo bo'ylab ko'cha yoritish uchun yiliga taxminan 320 teravatt-soat (TWh) elektr energiyasi sarflanadi, bu esa 150 million tonna CO2 emissiyasiga teng keladi [1]. Bu ko'rsatkich ayniqsa rivojlanayotgan mamlakatlar uchun jiddiy muammo hisoblanadi, chunki ularning energiya infratuzilmasi cheklangan va har bir kilovatt-soat tejash katta iqtisodiy samara beradi.")
t("An'anaviy ko'cha yoritish tizimlari tun bo'yi — o'rtacha 10-12 soat davomida — uzluksiz ishlaydi. Biroq, kuzatishlar shuni ko'rsatadiki, tun vaqtining 60-70 foizida ko'chalarda harakat deyarli kuzatilmaydi. Masalan, shahar ko'chalarida soat 00:00 dan 05:00 gacha bo'lgan vaqt oralig'ida piyodalar va transport vositalari harakati kunduzi vaqtiga nisbatan 90 foizga kamayadi [6]. Shunga qaramay, yoritgichlar to'liq quvvatda yonib turadi va bu energiyaning behuda sarflanishiga olib keladi.")
t("Internet of Things (IoT) texnologiyasining jadal rivojlanishi aqlli shahar (Smart City) konsepsiyasini amalga oshirish imkonini yaratmoqda. Statista tahliliy kompaniyasining 2024-yildagi hisobotiga ko'ra, dunyo bo'ylab IoT qurilmalari soni 2025-yilga kelib 30 milliarddan oshgan bo'lib, 2030-yilga borib bu ko'rsatkich 75 milliardga yetishi prognoz qilinmoqda [2]. IoT texnologiyalari yordamida ko'cha yoritish tizimlarini aqlli boshqarish — ya'ni faqat kerak bo'lganda yoqish va kerak bo'lmaganda o'chirish — energiya tejashning eng samarali usullaridan biri hisoblanadi.")
t("Ultratovush sensorlari harakatni aniqlash uchun eng ishonchli va arzon vositalardan biri bo'lib, ular bir qator muhim afzalliklarga ega: ob-havo sharoitlariga (yomg'ir, tuman, chang) kam ta'sirchan, keng burchak ostida ishlash qobiliyatiga ega (30-40 gradus), past energiya iste'mol qiladi (2 mA dan kam), va narxi arzon (1-3 AQSh dollari) [3]. Infraqizil (PIR) sensorlardan farqli ravishda, ultratovush sensorlari harorat o'zgarishlariga sezgir emas va aniqroq masofa ma'lumotini beradi.")
t("Ushbu sensorlarni ESP32 mikrokontrolleri bilan birgalikda qo'llash orqali energiya tejamkor yoritish tizimini yaratish mumkin. ESP32 — bu Espressif Systems kompaniyasi tomonidan ishlab chiqilgan ikki yadroli mikrokontroller bo'lib, ichki WiFi va Bluetooth modullariga ega. Bu xususiyatlar tizimni internet orqali masofadan boshqarish va monitoring qilish imkonini beradi. Tizim faqat harakat aniqlanganda yoritgichni yoqadi va ma'lum vaqt o'tgach (5 soniya) avtomatik o'chiradi, shu bilan birga kunduz kuni yoritgichni umuman yoqmaydi.")
t("O'zbekiston Respublikasi Prezidentining 2020-yil 5-oktabrdagi PF-6079-sonli Farmoni asosida qabul qilingan \"Raqamli O'zbekiston — 2030\" strategiyasi IoT va aqlli shahar texnologiyalarini rivojlantirishni ustuvor yo'nalish sifatida belgilab beradi [4]. Strategiyada ko'rsatilishicha, 2030-yilga borib O'zbekiston shaharlarining kamida 30 foizi aqlli texnologiyalar bilan jihozlanishi rejalashtirilgan. Shuningdek, O'zbekiston Respublikasi Vazirlar Mahkamasining 2023-yil 15-martdagi 58-sonli qarori bilan tasdiqlangan \"Energiya tejamkorligi va energiya samaradorligi to'g'risida\"gi dastur energiya resurslaridan oqilona foydalanish zarurligini ta'kidlaydi [5]. Ushbu dasturga ko'ra, 2025-2030 yillarda energiya iste'molini 20 foizga kamaytirish maqsad qilib qo'yilgan.")
t("Yuqoridagilarni hisobga olgan holda, ultratovush sensori asosida energiya tejamkor ko'cha yoritish tizimini ishlab chiqish nafaqat ilmiy, balki amaliy jihatdan ham dolzarb masala hisoblanadi. Bunday tizim O'zbekiston shahar va qishloqlarida energiya tejash, ekologik vaziyatni yaxshilash va fuqarolar xavfsizligini ta'minlash uchun muhim hissa qo'shishi mumkin.")

h2("Ishning ilmiy yangiligi.")
t("Mazkur bitiruv malakaviy ishida ishlab chiqilgan tizim quyidagi ilmiy va amaliy yangiliklarga ega:")
t("Birinchidan, ESP32 mikrokontrolleri asosida ultratovush sensori (RCWL-9610A) va yorug'lik sensori (TEMT6000) birgalikda qo'llanilgan energiya tejamkor yoritish tizimi ishlab chiqildi. Mavjud yechimlardan farqli ravishda, tizim bir vaqtning o'zida harakatni aniqlash va kunduz/tun holatini farqlash imkoniyatiga ega. Bu ikki sensorning birgalikda ishlashi tizimning energiya samaradorligini sezilarli darajada oshiradi — kunduz kuni yoritgich umuman yonmaydi, tunda esa faqat harakat aniqlanganda yonadi.")
t("Ikkinchidan, Firebase Realtime Database asosida real vaqt rejimida masofadan boshqarish va monitoring tizimi yaratildi. Bu tizim qurilmaning holatini har 3 soniyada yangilab turadi va foydalanuvchiga veb-interfeys orqali boshqarish imkonini beradi. Firebase ning stream texnologiyasi yordamida dashboard dan yuborilgan buyruqlar 200-500 millisekund ichida qurilmaga yetib boradi.")
t("Uchinchidan, non-blocking WiFi boshqaruv algoritmi ishlab chiqildi. Tizim internet aloqasi uzilgan holda ham avtonom ravishda ishlashda davom etadi — sensorlar va relay to'xtamaydi. Aloqa tiklanganda avtomatik sinxronizatsiya qiladi. Bundan tashqari, WiFi topilmagan holda captive portal (AP rejim) ochiladi va foydalanuvchi yangi WiFi ma'lumotlarini kiritishi mumkin. Bu ma'lumotlar NVS (Non-Volatile Storage) ga saqlanadi va qurilma qayta ishga tushganda ham saqlanib qoladi.")
t("To'rtinchidan, Progressive Web Application (PWA) texnologiyasi asosida cross-platform dashboard yaratildi. U desktop kompyuterlarda sidebar navigatsiya bilan, mobil qurilmalarda esa bottom navigation bilan ishlaydi. Dashboard offline rejimni qo'llab-quvvatlaydi (Service Worker orqali), native ilova sifatida o'rnatilishi mumkin va Optimistic UI pattern qo'llanilgan — foydalanuvchi buyruq berganda interfeys darhol yangilanadi, server javobini kutmasdan.")

h2("Ishning maqsadi.")
t("Bitiruv malakaviy ishining asosiy maqsadi — ultratovush sensori yordamida harakatni aniqlash va yorug'lik sensori orqali kunduz/tun holatini farqlash asosida energiya tejamkor ko'cha yoritish tizimini ishlab chiqish, uni masofadan boshqarish imkoniyatini yaratish va energiya tejash samaradorligini amaliy tajribalar orqali isbotlashdan iborat. Tizim real sharoitlarda sinovdan o'tkazilishi va uning samaradorligi raqamlar bilan isbotlanishi kerak.")

h2("Ishning vazifalari.")
t("Yuqorida belgilangan maqsadga erishish uchun quyidagi vazifalar amalga oshirildi:")
t("1) Ko'cha yoritish tizimlarining hozirgi holati, mavjud muammolar va energiya tejamkorlik yondashuvlarini chuqur o'rganish. Dunyo tajribasini o'rganish va mavjud tijorat yechimlarini (Philips CityTouch, Telensa, Tvilight) qiyosiy tahlil qilish;")
t("2) Ultratovush sensorlarining ishlash prinsipini, fizik asoslarini va texnik xususiyatlarini tadqiq qilish. RCWL-9610A va HC-SR04 sensorlarini qiyoslash va loyiha uchun optimal variantni tanlash;")
t("3) ESP32 mikrokontrolleri asosida hardware platformani loyihalash va komponentlarni tanlash. Pin konfiguratsiyasini aniqlash, strapping pinlarni hisobga olish va elektr sxemasini ishlab chiqish;")
t("4) Harakatni aniqlash algoritmini ishlab chiqish. Debounce (tebranishni bartaraf etish), hold timer (ushlab turish) va hysteresis (gisterezis) mexanizmlarini qo'llash orqali sensorning ishonchliligini oshirish;")
t("5) Firebase Realtime Database bilan real vaqt sinxronizatsiya tizimini yaratish. ESP32 dan bulutga ma'lumot yuborish, dashboard dan buyruqlarni qabul qilish va stream texnologiyasini amalga oshirish;")
t("6) React framework asosida Progressive Web Application (PWA) dashboard ishlab chiqish. Responsive dizayn, offline support, Optimistic UI va real-time ma'lumot ko'rsatish funksiyalarini amalga oshirish;")
t("7) Tizimning energiya tejash samaradorligini hisoblash va amaliy tajribalar o'tkazish. 5 kunlik sinov o'tkazish va natijalarni statistik tahlil qilish;")
t("8) Tizimni real sharoitlarda sinab ko'rish, yuzaga kelgan muammolarni aniqlash va bartaraf etish, yakuniy natijalarni tahlil qilish.")

h2("Tadqiqot obyekti.")
t("Tadqiqot obyekti — ko'cha yoritish tizimlari va ularda energiya tejamkorlikni ta'minlash uchun ishlatiladigan sensorli boshqaruv tizimlari. Tadqiqot davomida ESP32 mikrokontrolleri, RCWL-9610A ultratovush sensori, TEMT6000 yorug'lik sensori va relay moduli asosida amaliy prototip yaratildi. Prototip real sharoitlarda — yopiq xonada va ochiq havoda — sinovdan o'tkazildi.")

h2("Tadqiqot predmeti.")
t("Tadqiqot predmeti — ultratovush sensori yordamida harakatni aniqlash algoritmlari, IoT texnologiyalari asosida masofadan boshqarish tizimlari va ularning energiya tejamkorlikka ta'siri. Tadqiqot doirasida sensorlarning aniqligi, tizimning javob berish tezligi va energiya tejash ko'rsatkichlari o'rganildi.")

h2("Tadqiqot usullari.")
t("Bitiruv ishi davomida quyidagi tadqiqot usullaridan foydalanildi:")
t("— Ilmiy adabiyotlarni tahlil va sintez qilish: mavjud tadqiqotlar, patentlar va texnik hujjatlarni o'rganish;")
t("— Sistemali yondashuv: tizimni qatlamlar bo'yicha loyihalash (hardware, firmware, cloud, frontend);")
t("— Eksperimental tadqiqotlar: prototipni yaratish va real sharoitlarda sinash;")
t("— Qiyosiy tahlil: mavjud yechimlar bilan solishtirib baholash;")
t("— Matematik modellashtirish: energiya tejash formulalarini ishlab chiqish va hisoblash;")
t("— Dasturiy injiniring printsiplari: modular arxitektura, version control (Git), CI/CD;")
t("— Prototiplash va iterativ ishlab chiqish: har bir komponentni alohida sinab, keyin birlashtirish.")

h2("Ishning amaliy ahamiyati.")
t("Ishlab chiqilgan tizim quyidagi amaliy maqsadlarda foydalanish mumkin:")
t("— Shahar va qishloq ko'chalarida energiya tejamkor yoritish tizimini joriy etish. Bitta yoritgich uchun yillik tejamkorlik 212 kWh yoki 106,000 so'mni tashkil etadi;")
t("— Bog'lar, parkovkalar va yopiq hududlarda avtomatik yoritish. Tizim faqat odam yaqinlashganda yonadi va xavfsizlikni ta'minlaydi;")
t("— Sanoat korxonalari va omborxonalarda energiya sarfini kamaytirish. Katta hududlarda bir nechta sensor o'rnatish orqali zonali boshqarish mumkin;")
t("— Aqlli shahar (Smart City) loyihalarida yoritish infratuzilmasini modernizatsiya qilish. Firebase orqali markazlashtirilgan monitoring;")
t("— Ta'lim muassasalarida IoT, embedded systems va veb-dasturlash bo'yicha amaliy o'quv materiali sifatida. Loyiha ochiq kodli (open-source) va GitHub da joylashtirilgan.")

h2("Bitiruv malakaviy ishining tarkibi va hajmi.")
t("Bitiruv malakaviy ishi kirish, ikkita asosiy bob, xulosa, foydalanilgan adabiyotlar ro'yxati va ilovalardan iborat. Birinchi bobda ko'cha yoritish tizimlari, ultratovush sensorlari va IoT texnologiyalari nazariy jihatdan tahlil qilingan, mavjud yechimlar qiyosiy o'rganilgan va masala qo'yilishi shakllantirilgan. Ikkinchi bobda esa tizim arxitekturasi, hardware va software qismlarini amalda ishlab chiqish, dasturlash jarayoni va sinov natijalari batafsil bayon etilgan. Ishning umumiy hajmi 72 sahifani tashkil etadi, matn ichida 12 ta rasm, 10 ta jadval va dastur kodi fragmentlari keltirilgan. Foydalanilgan adabiyotlar ro'yxati 25 manbadan iborat bo'lib, ular orasida xalqaro ilmiy maqolalar, texnik hujjatlar, rasmiy me'yoriy hujjatlar va zamonaviy veb-resurslar mavjud.")

doc.add_page_break()
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_full.docx')
print("KIRISH done (~8 pages)")
