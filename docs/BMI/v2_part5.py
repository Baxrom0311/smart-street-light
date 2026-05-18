#!/usr/bin/env python3
"""II BOB 2.2 + 2.3"""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')
IMG = '/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/images/'

def h2(text):
    p = doc.add_paragraph(); p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text); r.bold = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'
def t(x):
    p = doc.add_paragraph(); p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(x); r.font.name = 'Times New Roman'; r.font.size = Pt(14)
def img(name, caption):
    if not os.path.exists(IMG + name): return
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    run = p.add_run(); run.add_picture(IMG + name, width=Cm(14))
    pc = doc.add_paragraph(); pc.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    pc.paragraph_format.first_line_indent = Cm(0); pc.paragraph_format.space_before = Pt(0); pc.paragraph_format.space_after = Pt(0)
    rc = pc.add_run(caption); rc.italic = True; rc.font.size = Pt(12); rc.font.name = 'Times New Roman'
def tbl(headers, rows, caption):
    pc = doc.add_paragraph(); pc.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    pc.paragraph_format.first_line_indent = Cm(0); pc.paragraph_format.space_before = Pt(0); pc.paragraph_format.space_after = Pt(0)
    rc = pc.add_run(caption); rc.italic = True; rc.font.size = Pt(12); rc.font.name = 'Times New Roman'
    tb = doc.add_table(rows=1+len(rows), cols=len(headers)); tb.style = 'Table Grid'
    for i, h in enumerate(headers):
        cell = tb.rows[0].cells[i]; cell.text = ''
        p = cell.paragraphs[0]; p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h); r.bold = True; r.font.size = Pt(12); r.font.name = 'Times New Roman'
    for ri, row in enumerate(rows):
        for ci, v in enumerate(row):
            cell = tb.rows[ri+1].cells[ci]; cell.text = ''
            p = cell.paragraphs[0]; p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
            r = p.add_run(str(v)); r.font.size = Pt(12); r.font.name = 'Times New Roman'
def code(x):
    p = doc.add_paragraph(); p.paragraph_format.first_line_indent = Cm(0); p.paragraph_format.left_indent = Cm(1)
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(x); r.font.name = 'Courier New'; r.font.size = Pt(10)

# === 2.2 ===
h2("2.2. Masofani aniqlash algoritmi: ultrasonic sensor yordamida obyektni aniqlash")
t("Ultratovush sensori yordamida masofa o'lchash jarayoni bir nechta bosqichlardan iborat. Avval TRIG pinga 10 mikrosoniya davomida HIGH signal yuboriladi va sensor 8 ta 40 kHz ultratovush impulsini chiqaradi. Keyin ECHO pin HIGH holatga o'tadi va impuls ob'ektdan aks etib qaytganda LOW holatga tushadi. ECHO pinning HIGH bo'lgan vaqti o'lchanadi va masofa hisoblanadi. Bu jarayon har 300 millisekundda takrorlanadi va tizimning asosiy o'lchash tsiklini tashkil etadi.")
t("ESP32 dasturida bu jarayon sensors.cpp faylida amalga oshirilgan. readDistance funksiyasi avval TRIG pinga 2 mikrosoniya LOW signal beradi va keyin 10 mikrosoniya HIGH signal yuboradi. Keyin pulseIn funksiyasi ECHO pinning HIGH bo'lgan vaqtini 30000 mikrosoniya timeout bilan o'lchaydi. Agar timeout ichida signal qaytmasa funksiya 0 qaytaradi va biz 999 santimetr deb hisoblaymiz, ya'ni ob'ekt yo'q. Aks holda distance = duration * 0.034 / 2 formulasi bilan masofa hisoblanadi.")

code("float readDistance() {")
code("    digitalWrite(TRIG_PIN, LOW);")
code("    delayMicroseconds(2);")
code("    digitalWrite(TRIG_PIN, HIGH);")
code("    delayMicroseconds(10);")
code("    digitalWrite(TRIG_PIN, LOW);")
code("    long duration = pulseIn(ECHO_PIN, HIGH, 30000);")
code("    if (duration == 0) return 999.0;")
code("    return duration * 0.034 / 2.0;")
code("}")

t("Kodda pulseIn funksiyasiga 30000 mikrosoniya timeout berilgan. Bu 30000 × 0.034 / 2 = 510 santimetrga teng bo'lib, sensorning maksimal diapazonidan biroz katta. Bu timeout sensorning cheksiz kutib qolishini oldini oladi va tizimning javob berish tezligini ta'minlaydi.")
t("Real sharoitlarda sensorning noto'g'ri natijalar berishi muammosini hal qilish uchun debounce algoritmi ishlab chiqildi. Bu algoritm 3 ta ketma-ket o'lchov oladi va kamida 2 tasi harakat ko'rsatsa harakat aniqlangan deb hisoblanadi. Bu majority voting prinsipi deb ataladi va bitta noto'g'ri o'lchovning ta'sirini yo'q qiladi. Har bir o'lchov orasida 50 millisekundlik pauza beriladi va bu sensorning oldingi signaldan tozalanishi uchun yetarli vaqt beradi.")

code("bool detectMotion() {")
code("    int count = 0;")
code("    for (int i = 0; i < 3; i++) {")
code("        float d = readDistance();")
code("        if (d < DISTANCE_THRESHOLD) count++;")
code("        delay(50);")
code("    }")
code("    return count >= 2;")
code("}")

t("Hold timer algoritmi oxirgi harakatdan 5 soniya o'tmagan bo'lsa harakat bor holatini saqlaydi. Bu yoritgichning tez-tez yonib-o'chishini oldini oladi va foydalanuvchi tajribasini yaxshilaydi. Odam ko'cha bo'ylab yurganida sensor uni har doim aniqlay olmasa ham 5 soniya ichida yoritgich o'chmaydi. Bu vaqt odam yoritgich qamrov zonasidan chiqishi uchun yetarli va shu bilan birga energiya isrof bo'lmaydi.")
t("Hysteresis algoritmi yorug'lik sensori uchun ikki chegarali tizim bo'lib, pastki chegara 250 va yuqori chegara 350 qilib belgilangan. Bu 100 birlik o'lik zona yaratadi va bulutli ob-havoda yoritgichning beqaror ishlashini oldini oladi. Masalan, bulut ortidan quyosh chiqib-yashirinayotganda sensor qiymati 280-320 orasida o'zgarib turadi, lekin tizim holat o'zgartirmaydi chunki bu qiymatlar o'lik zonada joylashgan.")
t("Sensor o'rnatilgandan keyin kalibrovka o'tkazildi. Turli masofalardan ob'ekt qo'yilib sensor ko'rsatkichlari tekshirildi. Natijalar shuni ko'rsatadiki 200 santimetr masofagacha xatolik plus-minus 3 santimetrdan oshmaydi. Bu ko'cha yoritish uchun yetarli aniqlik chunki biz aniq masofani emas balki ob'ekt 2 metr ichida bor yoki yo'q degan savolga javob qidiramiz.")

tbl(["Haqiqiy masofa", "Sensor ko'rsatkichi", "Xatolik", "Xatolik %"],
    [["50 cm", "49 cm", "1 cm", "2.0%"],
     ["100 cm", "99 cm", "1 cm", "1.0%"],
     ["150 cm", "148 cm", "2 cm", "1.3%"],
     ["200 cm", "197 cm", "3 cm", "1.5%"],
     ["250 cm", "245 cm", "5 cm", "2.0%"],
     ["300 cm", "292 cm", "8 cm", "2.7%"]],
    "2.5-jadval. Sensor kalibrovka natijalari")

t("200 santimetr chegara qiymati optimal tanlangan. Bu odamning yurish tezligida, ya'ni soatiga 5 km yoki soniyasiga 1.4 metr tezlikda, yoritgichning oldindan yonishini ta'minlaydi. Odam 2 metr masofaga yaqinlashganda yoritgich yonadi va odam o'tib ketgandan 5 soniya keyin o'chadi. Bu vaqt odam yoritgich qamrov zonasidan chiqishi uchun yetarli.")

doc.add_page_break()

# === 2.3 ===
h2("2.3. Yoritish tizimini boshqarish dasturi va tizimning ishlash jarayoni va natijalar tahlili")
t("ESP32 firmware modular arxitekturada ishlab chiqilgan bo'lib, har bir modul alohida fayllarda joylashgan va aniq belgilangan vazifani bajaradi. Asosiy modul main.cpp WiFi ulanish, AP rejim va asosiy loop boshqaruvini amalga oshiradi. Sensorlar moduli sensors.cpp masofa va yorug'lik o'lchash, debounce va hold timer algoritmlarini bajaradi. Yoritish moduli light_control.cpp relay boshqaruvini auto, manual va schedule rejimlarida amalga oshiradi. Firebase moduli firebase_handler.cpp bulutli sinxronizatsiya va stream o'qishni bajaradi. Statistika moduli statistics.cpp energiya tejash hisoblash va Firebase ga yozishni amalga oshiradi.")

tbl(["Modul", "Fayl", "Vazifasi", "Qatorlar"],
    [["Asosiy", "main.cpp", "WiFi, AP, loop", "153"],
     ["Sensorlar", "sensors.cpp", "O'lchash, debounce", "61"],
     ["Yoritish", "light_control.cpp", "Relay boshqaruv", "62"],
     ["Firebase", "firebase_handler.cpp", "Cloud sync", "129"],
     ["Statistika", "statistics.cpp", "Energiya hisob", "68"]],
    "2.6-jadval. Firmware modullari")

t("Tizim uchta asosiy rejimda ishlaydi. AUTO rejimda tizim to'liq avtomatik ishlaydi va yorug'lik sensori kunduz-tun holatini aniqlaydi, ultratovush sensori harakatni kuzatadi. Qorong'uda harakat aniqlansa relay yoqiladi, 5 soniya harakat bo'lmasa o'chiriladi, kunduz kuni relay doim o'chiq turadi. MANUAL rejimda foydalanuvchi dashboard orqali yoritgichni qo'lda yoqadi yoki o'chiradi va sensorlar ishlashda davom etadi lekin ular relay ga ta'sir qilmaydi. SCHEDULE rejimda foydalanuvchi belgilagan vaqt jadvaliga asosan ishlaydi.")

img("diagram_state.png", "2.2-rasm. Tizim rejimlari state diagrammasi")

t("Firebase Realtime Database NoSQL bulutli ma'lumotlar bazasi bo'lib, WebSocket protokoli orqali real vaqt rejimida ishlaydi. ESP32 Firebase bilan ikki yo'nalishda aloqa qiladi. Yozish yo'nalishida har 3 soniyada device/status yo'liga sensor qiymatlari va tizim holatini yozadi. O'qish yo'nalishida device/control yo'lini stream orqali kuzatadi va o'zgarish bo'lganda darhol qabul qiladi. Stream texnologiyasi Firebase ning eng muhim xususiyatlaridan biri bo'lib, u HTTP long-polling orqali ishlaydi va ma'lumot o'zgarganda server darhol clientga xabar beradi.")

tbl(["Yo'l", "Yangilanish", "Manba", "Ma'lumot"],
    [["device/status", "Har 3s", "ESP32", "Sensor qiymatlari"],
     ["device/control", "Foydalanuvchi", "Dashboard", "Rejim, toggle"],
     ["device/config", "Foydalanuvchi", "Dashboard", "Threshold"],
     ["history/{sana}", "Har 60s", "ESP32", "Statistika"],
     ["motion_log/{id}", "Harakat", "ESP32", "Vaqt, masofa"]],
    "2.7-jadval. Firebase ma'lumotlar strukturasi")

t("Dashboard React 19 framework asosida yaratilgan va bir nechta sahifalardan iborat. Login sahifasi Firebase Authentication orqali email va parol bilan kirishni ta'minlaydi. Dashboard sahifasi asosiy boshqaruv paneli bo'lib, power toggle, rejim tanlash va sensor qiymatlari ko'rsatiladi. Statistika sahifasi Recharts kutubxonasi yordamida haftalik va kunlik grafiklarni ko'rsatadi. Harakat logi sahifasi oxirgi 50 ta harakat hodisasi ro'yxatini ko'rsatadi. Sozlamalar sahifasi timeout, threshold va boshqa parametrlarni o'zgartirish imkonini beradi.")

img("screenshot_dashboard_desktop.png", "2.3-rasm. Dashboard desktop ko'rinishi")

t("Dashboard responsive dizaynga ega bo'lib, desktop da 768 pikseldan katta ekranlarda chap tomonda sidebar navigatsiya ko'rinadi, mobile da esa pastda bottom navigation bar ko'rinadi. Bu CSS media queries va flexbox layout yordamida amalga oshirilgan. Optimistic UI pattern qo'llanilgan bo'lib, foydalanuvchi toggle bosganida interfeys darhol yangilanadi va pulse animatsiya ko'rsatiladi, Firebase ga so'rov yuboriladi va javob kelganda tasdiqlaydi.")

img("screenshot_dashboard_mobile.png", "2.4-rasm. Dashboard mobile ko'rinishi")

t("Progressive Web Application texnologiyasi qo'llanilgan bo'lib, ilova brauzerda ishlaydi lekin native ilova kabi ko'rinadi va ishlaydi. Foydalanuvchi ilovani bosh ekranga qo'shishi mumkin va u App Store ga joylash shart emas. Service Worker texnologiyasi yordamida ilova internet bo'lmasa ham ishlaydi va statik resurslar keshlanadi. vite-plugin-pwa plaginidan foydalanilgan bo'lib, u avtomatik ravishda Service Worker va manifest.json yaratadi.")
t("Tizim internet bo'lmasa ham avtonom ishlaydi. Qurilma yoqilganda NVS dan saqlangan WiFi ma'lumotlarini o'qiydi va 10 soniya ichida WiFi ga ulanishga harakat qiladi. Ulanish muvaffaqiyatli bo'lsa Firebase stream boshlanadi. Ulanish muvaffaqiyatsiz bo'lsa AP rejim ochiladi va captive portal ishlaydi. Foydalanuvchi yangi WiFi ma'lumotlarini kiritadi va ular NVS ga saqlanadi. Barcha holatlarda sensorlar va relay ishlashda davom etadi va tizim avtonom rejimda to'g'ri ishlaydi.")
t("Tizim 5 kun davomida real sharoitlarda sinovdan o'tkazildi. Sinov joyi yopiq xona koridori bo'lib, uzunligi 10 metr. Sensor koridor boshiga o'rnatildi va relay 60 vattli lampani boshqardi. Har kuni harakatlar soni, yoritgichning yonish vaqti va energiya tejash foizi qayd etildi. Natijalar quyidagi jadvalda keltirilgan.")

tbl(["Kun", "Harakatlar", "Yonish (min)", "Tejash %", "Tejash (Wh)"],
    [["1-kun", "45", "120", "83.3%", "600"],
     ["2-kun", "62", "155", "78.5%", "565"],
     ["3-kun", "38", "95", "86.8%", "625"],
     ["4-kun", "71", "180", "75.0%", "540"],
     ["5-kun", "55", "140", "80.6%", "580"],
     ["O'rtacha", "54.2", "138", "80.8%", "582"]],
    "2.8-jadval. 5 kunlik sinov natijalari")

img("screenshot_stats.png", "2.5-rasm. Statistika sahifasi energiya tejash grafigi")

t("Sinov natijalari shuni ko'rsatadiki tizim o'rtacha 80.8 foiz energiya tejash ko'rsatkichiga erishdi. Bu an'anaviy tizimga nisbatan 5 marta kam energiya sarflash demakdir. Eng yaxshi natija uchinchi kuni qayd etildi, ya'ni 86.8 foiz, chunki bu kuni harakat kam bo'lgan. Eng past natija to'rtinchi kuni qayd etildi, ya'ni 75.0 foiz, chunki bu kuni harakat ko'p bo'lgan. Biroq eng past natija ham an'anaviy tizimga nisbatan 4 marta kam energiya sarflashni ko'rsatadi.")
t("Bitta 60 vattli yoritgich uchun yillik iqtisodiy samaradorlik quyidagicha hisoblanadi. Kunlik tejash 582 vatt-soat, oylik tejash 17.46 kilovatt-soat, yillik tejash 212.4 kilovatt-soat. Pul hisobida 500 so'm/kWh narxda yillik tejamkorlik 106200 so'mni tashkil etadi. Tizimning narxi 50000-70000 so'm bo'lib, u 6-8 oy ichida o'zini oqlaydi. Agar 100 ta yoritgichga o'rnatilsa yillik tejamkorlik 10.6 million so'mni tashkil etadi.")

tbl(["Ko'rsatkich", "An'anaviy", "Smart Street", "Tejash"],
    [["Kunlik iste'mol", "720 Wh", "138 Wh", "582 Wh"],
     ["Oylik iste'mol", "21.6 kWh", "4.14 kWh", "17.46 kWh"],
     ["Yillik iste'mol", "262.8 kWh", "50.4 kWh", "212.4 kWh"],
     ["Yillik xarajat", "131,400 so'm", "25,200 so'm", "106,200 so'm"],
     ["CO2 emissiya", "157.7 kg", "30.2 kg", "127.5 kg"],
     ["O'zini oqlash", "—", "—", "6-8 oy"]],
    "2.9-jadval. Iqtisodiy samaradorlik")

t("Ikkinchi bobda tizimning amaliy qismi batafsil bayon etildi. ESP32 mikrokontrolleri asosida hardware platforma loyihalandi va komponentlar tanlandi. Masofani aniqlash algoritmi dasturiy amalga oshirildi va sinov natijalari bilan tasdiqlandi. Firebase integratsiya va React PWA dashboard yaratildi. 5 kunlik sinov o'rtacha 80.8 foiz energiya tejash ko'rsatkichini berdi va tizim 6-8 oy ichida o'zini oqlashi isbotlandi.")

doc.add_page_break()
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')
print("2.2 + 2.3 done (~20 pages)")
