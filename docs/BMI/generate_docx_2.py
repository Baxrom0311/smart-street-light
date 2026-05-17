#!/usr/bin/env python3
"""Part 2: KIRISH qismini qo'shish"""

from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/bmi_draft.docx')

def h(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(16)
    r.font.name = 'Times New Roman'

def h2(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True
    r.font.size = Pt(14)
    r.font.name = 'Times New Roman'

def t(text):
    p = doc.add_paragraph(text)
    p.paragraph_format.first_line_indent = Cm(1.25)
    for run in p.runs:
        run.font.name = 'Times New Roman'
        run.font.size = Pt(14)

h("KIRISH")
doc.add_paragraph()

h2("Mavzuning dolzarbligi.")
t("Hozirgi kunda dunyo miqyosida energiya iste'moli keskin o'sib bormoqda va bu jarayon atrof-muhitga salbiy ta'sir ko'rsatmoqda. Birlashgan Millatlar Tashkilotining ma'lumotlariga ko'ra, ko'cha yoritish tizimlari shahar elektr energiyasi iste'molining 15-25 foizini tashkil etadi [1]. An'anaviy ko'cha yoritish tizimlari tun bo'yi uzluksiz ishlaydi, ya'ni harakat bo'lmagan vaqtlarda ham energiya sarflanadi. Bu holat nafaqat iqtisodiy zarar keltiradi, balki karbon izini oshiradi va ekologik muammolarni kuchaytiradi.")
t("Internet of Things (IoT) texnologiyasining jadal rivojlanishi aqlli shahar (Smart City) konsepsiyasini amalga oshirish imkonini yaratmoqda. Statista tahliliy kompaniyasining 2024-yildagi hisobotiga ko'ra, dunyo bo'ylab IoT qurilmalari soni 2025-yilga kelib 30 milliarddan oshgan bo'lib, 2030-yilga borib bu ko'rsatkich 75 milliardga yetishi prognoz qilinmoqda [2]. Aqlli ko'cha yoritish tizimlari IoT ning eng samarali qo'llanilish sohalaridan biri hisoblanadi.")
t("Ultratovush sensorlari harakatni aniqlash uchun eng ishonchli va arzon vositalardan biri bo'lib, ular ob-havo sharoitlariga kam ta'sirchan, keng burchak ostida ishlash qobiliyatiga ega va past energiya iste'mol qiladi [3]. Ushbu sensorlarni mikrokontroller bilan birgalikda qo'llash orqali energiya tejamkor yoritish tizimini yaratish mumkin bo'lib, bu tizim faqat harakat aniqlanganda yoritgichni yoqadi va ma'lum vaqt o'tgach avtomatik o'chiradi.")
t("O'zbekiston Respublikasi Prezidentining 2020-yil 5-oktabrdagi PF-6079-sonli Farmoni asosida qabul qilingan \"Raqamli O'zbekiston — 2030\" strategiyasi IoT va aqlli shahar texnologiyalarini rivojlantirishni ustuvor yo'nalish sifatida belgilab beradi [4]. Shuningdek, O'zbekiston Respublikasi Vazirlar Mahkamasining 2023-yil 15-martdagi 58-sonli qarori bilan tasdiqlangan \"Energiya tejamkorligi va energiya samaradorligi to'g'risida\"gi dastur energiya resurslaridan oqilona foydalanish zarurligini ta'kidlaydi [5]. Aynan shu hujjatlar bilan belgilangan vazifalarni bajarish nuqtai nazaridan ham mazkur mavzu juda dolzarbdir.")

doc.add_paragraph()
h2("Ishning ilmiy yangiligi.")
t("Mazkur bitiruv malakaviy ishida ishlab chiqilgan tizim quyidagi ilmiy va amaliy yangiliklarga ega:")
t("1. ESP32 mikrokontrolleri asosida ultratovush sensori (RCWL-9610A) va yorug'lik sensori (TEMT6000) birgalikda qo'llanilgan energiya tejamkor yoritish tizimi ishlab chiqildi. Mavjud yechimlardan farqli ravishda, tizim bir vaqtning o'zida harakatni aniqlash va kunduz/tun holatini farqlash imkoniyatiga ega.")
t("2. Firebase Realtime Database asosida real vaqt rejimida masofadan boshqarish va monitoring tizimi yaratildi. Bu tizim qurilmaning holatini har 3 soniyada yangilab turadi va foydalanuvchiga veb-interfeys orqali boshqarish imkonini beradi.")
t("3. Non-blocking WiFi boshqaruv algoritmi ishlab chiqildi: tizim internet aloqasi uzilgan holda ham avtonom ravishda ishlashda davom etadi va aloqa tiklanganda avtomatik sinxronizatsiya qiladi.")
t("4. Progressive Web Application (PWA) texnologiyasi asosida cross-platform dashboard yaratildi. U desktop va mobil qurilmalarda bir xil samarali ishlaydi, offline rejimni qo'llab-quvvatlaydi va native ilova sifatida o'rnatilishi mumkin.")

doc.add_paragraph()
h2("Ishning maqsadi.")
t("Bitiruv malakaviy ishining asosiy maqsadi — ultratovush sensori yordamida harakatni aniqlash va yorug'lik sensori orqali kunduz/tun holatini farqlash asosida energiya tejamkor ko'cha yoritish tizimini ishlab chiqish, uni masofadan boshqarish imkoniyatini yaratish va energiya tejash samaradorligini amaliy tajribalar orqali isbotlashdan iborat.")

doc.add_paragraph()
h2("Ishning vazifalari.")
t("Yuqorida belgilangan maqsadga erishish uchun quyidagi vazifalar amalga oshirildi:")
t("1) Ko'cha yoritish tizimlarining hozirgi holati va energiya tejamkorlik muammolarini o'rganish;")
t("2) Ultratovush sensorlarining ishlash prinsipini va texnik xususiyatlarini tadqiq qilish;")
t("3) ESP32 mikrokontrolleri asosida hardware platformani loyihalash va komponentlarni tanlash;")
t("4) Harakatni aniqlash algoritmini ishlab chiqish (debounce, hold timer, hysteresis);")
t("5) Firebase Realtime Database bilan real vaqt sinxronizatsiya tizimini yaratish;")
t("6) React asosida Progressive Web Application (PWA) dashboard ishlab chiqish;")
t("7) Tizimning energiya tejash samaradorligini hisoblash va amaliy tajribalar o'tkazish;")
t("8) Tizimni real sharoitlarda sinab ko'rish va natijalarni tahlil qilish.")

doc.add_paragraph()
h2("Tadqiqot obyekti.")
t("Tadqiqot obyekti — ko'cha yoritish tizimlari va ularda energiya tejamkorlikni ta'minlash uchun ishlatiladigan sensorli boshqaruv tizimlari. Tadqiqot davomida ESP32 mikrokontrolleri, RCWL-9610A ultratovush sensori, TEMT6000 yorug'lik sensori va relay moduli asosida amaliy prototip yaratildi.")

doc.add_paragraph()
h2("Tadqiqot predmeti.")
t("Tadqiqot predmeti — ultratovush sensori yordamida harakatni aniqlash algoritmlari, IoT texnologiyalari asosida masofadan boshqarish tizimlari va ularning energiya tejamkorlikka ta'siri.")

doc.add_paragraph()
h2("Tadqiqot usullari.")
t("Bitiruv ishi davomida quyidagi tadqiqot usullaridan foydalanildi: ilmiy adabiyotlarni tahlil va sintez qilish; sistemali yondashuv; eksperimental tadqiqotlar; qiyosiy tahlil; matematik modellashtirish (energiya tejash formulalari); dasturiy injiniring printsiplari; prototiplash va iterativ ishlab chiqish metodologiyasi.")

doc.add_paragraph()
h2("Ishning amaliy ahamiyati.")
t("Ishlab chiqilgan tizim quyidagi amaliy maqsadlarda foydalanish mumkin: shahar va qishloq ko'chalarida energiya tejamkor yoritish tizimini joriy etish; bog'lar, parkovkalar va yopiq hududlarda avtomatik yoritish; sanoat korxonalari va omborxonalarda energiya sarfini kamaytirish; aqlli shahar (Smart City) loyihalarida yoritish infratuzilmasini modernizatsiya qilish; ta'lim muassasalarida IoT va embedded systems bo'yicha amaliy o'quv materiali sifatida.")

doc.add_paragraph()
h2("Bitiruv malakaviy ishining tarkibi va hajmi.")
t("Bitiruv malakaviy ishi kirish, ikkita asosiy bob, xulosa, foydalanilgan adabiyotlar ro'yxati va ilovalardan iborat. Birinchi bobda ko'cha yoritish tizimlari, ultratovush sensorlari va IoT texnologiyalari nazariy jihatdan tahlil qilingan, masala qo'yilishi shakllantirilgan. Ikkinchi bobda esa tizim arxitekturasi, hardware va software qismlarini amalda ishlab chiqish, dasturlash va sinov natijalari batafsil bayon etilgan. Ishning umumiy hajmi 70 sahifani tashkil etadi, matn ichida rasmlar, sxemalar, jadvallar va kod fragmentlari keltirilgan. Foydalanilgan adabiyotlar ro'yxati 25 manbadan iborat.")

doc.add_page_break()
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/bmi_draft.docx')
print("Part 2 done: KIRISH")
