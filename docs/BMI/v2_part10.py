#!/usr/bin/env python3
"""Final 30 pages"""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')
IMG = '/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/images/'

def h2(t_):
    p = doc.add_paragraph(); p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(t_); r.bold = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'
def t(x):
    p = doc.add_paragraph(); p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(x); r.font.name = 'Times New Roman'; r.font.size = Pt(14)
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

doc.add_page_break()
h2("NG ilova. Relay modulining ishlash prinsipi va texnik tavsifi")
t("Relay elektromexanik kalit bo'lib, kichik boshqaruv signali yordamida katta quvvatli yukni yoqish va o'chirish imkonini beradi. Bizning tizimimizda 3.3V logika darajasidagi relay moduli ishlatilgan bo'lib, u ESP32 ning GPIO pinidan to'g'ridan-to'g'ri boshqariladi. Relay moduli optokuplyor orqali izolyatsiya qilingan bo'lib, bu ESP32 ni yuqori kuchlanish yukidan himoya qiladi.")
t("Relay modulining ishlash prinsipi quyidagicha. ESP32 GPIO 26 pinga LOW signal berganda, optokuplyor yonadi va tranzistor ochiladi. Tranzistor relay katushkasiga tok beradi va relay kontaktlari yopiladi, ya'ni yuk yoqiladi. ESP32 HIGH signal berganda, optokuplyor o'chadi, tranzistor yopiladi va relay kontaktlari ochiladi, ya'ni yuk o'chiriladi. Bu active LOW logika deb ataladi.")
t("Relay modulining texnik xususiyatlari quyidagilardan iborat. Boshqaruv kuchlanishi 3.3-5V bo'lib, ESP32 bilan to'g'ridan-to'g'ri ulash mumkin. Boshqaruv toki 15-20 mA bo'lib, ESP32 ning GPIO pini 40 mA gacha tok bera oladi. Kontakt kuchlanishi 250V AC yoki 30V DC gacha. Kontakt toki 10A gacha. Mexanik ishlash muddati 100000 marta yoqish-o'chirish. Elektrik ishlash muddati 50000 marta.")
t("Relay tanlashda bir nechta alternativ variantlar ko'rib chiqildi. Solid State Relay mexanik kontaktlarsiz ishlaydi va uzoqroq xizmat qiladi, lekin narxi 3-5 marta yuqori. MOSFET kalit relay dan tezroq ishlaydi va cheksiz ishlash muddatiga ega, lekin faqat DC yuk bilan ishlaydi. Oddiy mexanik relay arzon, ishonchli va AC hamda DC yuk bilan ishlaydi. Bizning loyihamiz uchun oddiy relay tanlandi, chunki u arzon va ko'cha yoritgichlari odatda AC yuk hisoblanadi.")
t("Relay modulini ulash sxemasi quyidagicha. VCC pini ESP32 ning 3.3V yoki 5V piniga ulanadi. GND pini ESP32 ning GND piniga ulanadi. IN pini ESP32 ning GPIO 26 piniga ulanadi. COM kontakti elektr manbaiga ulanadi. NO kontakti yukka, ya'ni yoritgichga ulanadi. NC kontakti ishlatilmaydi. NO normally open degan ma'noni anglatadi, ya'ni relay yoqilmaganda kontakt ochiq va yuk o'chiq.")

doc.add_page_break()
h2("O' ilova. WiFi texnologiyasi va ESP32 da amalga oshirilishi")
t("WiFi 802.11 standarti IEEE tomonidan ishlab chiqilgan simsiz tarmoq texnologiyasi bo'lib, 2.4 GHz va 5 GHz chastotalarda ishlaydi. ESP32 faqat 2.4 GHz chastotani qo'llab-quvvatlaydi va 802.11 b, g va n standartlarini ishlatadi. 802.11b maksimal 11 Mbps tezlikda ishlaydi va eng keng qamrovga ega. 802.11g maksimal 54 Mbps tezlikda ishlaydi. 802.11n maksimal 150 Mbps tezlikda ishlaydi va MIMO texnologiyasini qo'llab-quvvatlaydi.")
t("ESP32 da WiFi ulanish jarayoni bir nechta bosqichdan iborat. Avval WiFi.mode funksiyasi chaqiriladi va WiFi moduli Station rejimiga o'tkaziladi. Keyin WiFi.begin funksiyasi SSID va parol bilan chaqiriladi va ulanish jarayoni boshlanadi. ESP32 ko'rsatilgan SSID li tarmoqni qidiradi, topgandan keyin WPA2 autentifikatsiya jarayonini boshlaydi va muvaffaqiyatli bo'lsa IP manzil oladi. Bu jarayon odatda 2-5 soniya davom etadi.")
t("Bizning tizimimizda WiFi ulanish non-blocking usulda amalga oshirilgan. Bu shuni anglatadiki, WiFi ulanish jarayoni asosiy dastur tsiklini to'xtatmaydi. Buning uchun WiFi.begin chaqirilgandan keyin 10 soniya davomida WiFi.status tekshiriladi. Agar 10 soniya ichida ulanish bo'lmasa, tizim AP rejimga o'tadi. Bu vaqt davomida sensorlar o'qiladi va relay boshqariladi, ya'ni tizim avtonom ishlaydi.")
t("AP rejimda ESP32 o'zi WiFi nuqtasi bo'lib ishlaydi va SmartLight_AP nomli tarmoq yaratadi. Bu tarmoqqa ulanganida foydalanuvchi avtomatik ravishda captive portal sahifasiga yo'naltiriladi. Captive portal oddiy HTML sahifa bo'lib, unda WiFi SSID va parol kiritish maydonlari mavjud. Foydalanuvchi ma'lumotlarni kiritib saqlasa, ular NVS ga yoziladi va ESP32 qayta ishga tushadi.")
t("NVS Non-Volatile Storage ESP32 ning ichki flash xotirasida joylashgan maxsus bo'lim bo'lib, u kalit-qiymat juftliklarini saqlash uchun ishlatiladi. NVS da saqlangan ma'lumotlar qurilma o'chirilganda ham saqlanib qoladi. Bizning tizimimizda WiFi SSID va parol NVS da saqlanadi va qurilma har safar yoqilganda avval NVS dan o'qiydi. Agar NVS da ma'lumot bo'lmasa, config.h dagi standart qiymatlar ishlatiladi.")
t("WiFi signal kuchi RSSI Radio Signal Strength Indicator orqali o'lchanadi va dBm birligida ifodalanadi. Odatda minus 30 dBm juda yaxshi signal, minus 50 dBm yaxshi signal, minus 70 dBm o'rtacha signal va minus 90 dBm yomon signal hisoblanadi. Bizning tizimimiz WiFi RSSI qiymatini Firebase ga yuboradi va dashboard da ko'rsatadi. Bu foydalanuvchiga qurilmaning WiFi sifatini kuzatish imkonini beradi.")

doc.add_page_break()
h2("G' ilova. React framework va komponent arxitekturasi")
t("React Meta kompaniyasi tomonidan 2013-yilda ishlab chiqilgan JavaScript kutubxonasi bo'lib, foydalanuvchi interfeyslari yaratish uchun mo'ljallangan. React ning asosiy g'oyasi komponent asosida ishlash bo'lib, har bir UI elementi alohida komponent sifatida yaratiladi va ular bir-biri bilan props va state orqali aloqa qiladi. Bu yondashuv kodni qayta ishlatish, test qilish va boshqarishni osonlashtiradi.")
t("React ning virtual DOM texnologiyasi samaradorlikni oshiradi. Har safar state o'zgarganda React avval virtual DOM da o'zgarishlarni hisoblaydi va keyin faqat o'zgargan qismlarni haqiqiy DOM ga qo'llaydi. Bu to'g'ridan-to'g'ri DOM manipulyatsiyasidan ancha tez, chunki DOM operatsiyalari qimmat va sekin. Virtual DOM esa oddiy JavaScript ob'ekti bo'lib, u bilan ishlash tez.")
t("Bizning dashboard da quyidagi komponentlar yaratilgan. App.jsx asosiy komponent bo'lib, u routing, autentifikatsiya va global state boshqaruvini amalga oshiradi. Login.jsx autentifikatsiya sahifasi bo'lib, email va parol kiritish formasi va Firebase Auth integratsiyasini o'z ichiga oladi. Dashboard.jsx asosiy boshqaruv paneli bo'lib, power toggle, rejim tanlash va sensor qiymatlari ko'rsatiladi. Statistics.jsx statistika sahifasi bo'lib, Recharts kutubxonasi yordamida grafiklar ko'rsatiladi. MotionLog.jsx harakat logi sahifasi bo'lib, oxirgi 50 ta hodisa ro'yxatini ko'rsatadi. Settings.jsx sozlamalar sahifasi bo'lib, threshold va timeout qiymatlarini o'zgartirish imkonini beradi.")
t("React Hooks texnologiyasi funksional komponentlarda state va lifecycle boshqarish imkonini beradi. useState hook lokal state yaratish uchun ishlatiladi. useEffect hook side effect larni boshqarish uchun ishlatiladi, masalan Firebase ga ulanish va unsubscribe qilish. Bizning dashboard da useEffect Firebase onValue listener ni o'rnatish va komponent unmount bo'lganda unsubscribe qilish uchun ishlatilgan.")
t("Optimistic UI pattern foydalanuvchi tajribasini yaxshilash uchun qo'llanilgan. Bu pattern da foydalanuvchi buyruq berganda interfeys darhol yangilanadi, server javobini kutmasdan. Masalan, foydalanuvchi power toggle ni bosganda, interfeys darhol YONIQ yoki O'CHIQ holatiga o'zgaradi va pulse animatsiya ko'rsatiladi. Keyin Firebase ga so'rov yuboriladi va javob kelganda tasdiqlaydi. Agar so'rov muvaffaqiyatsiz bo'lsa, interfeys oldingi holatga qaytariladi.")
t("Responsive dizayn CSS media queries va flexbox layout yordamida amalga oshirilgan. Desktop da 768 pikseldan katta ekranlarda chap tomonda 240 piksel kenglikdagi sidebar navigatsiya ko'rinadi. Mobile da sidebar yashiriladi va pastda bottom navigation bar ko'rinadi. Bu yondashuv bitta kod bazasi bilan barcha ekran o'lchamlarida qulay interfeys yaratish imkonini beradi.")

doc.add_page_break()
h2("H ilova. Recharts kutubxonasi va ma'lumotlarni vizualizatsiya qilish")
t("Recharts React uchun mo'ljallangan ma'lumotlarni vizualizatsiya kutubxonasi bo'lib, D3.js asosida qurilgan. U deklarativ yondashuvni qo'llaydi, ya'ni dasturchi grafik turini va ma'lumotlarni belgilaydi, qolganini kutubxona o'zi bajaradi. Recharts responsive bo'lib, turli ekran o'lchamlarida to'g'ri ko'rinadi va animatsiyalarni qo'llab-quvvatlaydi.")
t("Bizning dashboard da BarChart komponenti ishlatilgan bo'lib, u haftalik energiya tejash foizini ko'rsatadi. Har bir ustun bitta kunni ifodalaydi va balandligi tejash foiziga proporsional. XAxis kunlar nomini ko'rsatadi, YAxis foiz qiymatini ko'rsatadi. Tooltip foydalanuvchi ustun ustiga hover qilganda aniq qiymatni ko'rsatadi. CartesianGrid fon chiziqlari ko'rsatadi va grafikni o'qishni osonlashtiradi.")
t("ResponsiveContainer komponenti grafikni ota elementning o'lchamiga moslaydi. U width 100 foiz va height 300 piksel qilib belgilangan. Bu grafik desktop da keng, mobile da tor ko'rinishini ta'minlaydi. Ma'lumotlar massiv ko'rinishida beriladi va har bir element date, motions_count, on_duration_min va energy_saved_percent maydonlarini o'z ichiga oladi.")
t("Live rejimda ma'lumotlar Firebase dan real vaqt rejimida olinadi. history yo'lidagi ma'lumotlar onValue listener orqali kuzatiladi va o'zgarish bo'lganda grafik avtomatik yangilanadi. Demo rejimda esa mockData.js faylidan tasodifiy generatsiya qilingan ma'lumotlar ishlatiladi. Bu internet bo'lmagan holda ham dashboard ni ko'rsatish imkonini beradi.")

doc.add_page_break()
h2("Q ilova. Captive portal va DNS server amalga oshirilishi")
t("Captive portal WiFi tarmog'iga ulangan qurilmani avtomatik ravishda veb-sahifaga yo'naltirish texnologiyasidir. U odatda mehmonxonalar, aeroportlar va kafelarda WiFi ga ulanish uchun ishlatiladi. Bizning tizimimizda captive portal ESP32 AP rejimda ishlaganda WiFi konfiguratsiya sahifasini ko'rsatish uchun ishlatiladi.")
t("Captive portal ishlash prinsipi quyidagicha. Foydalanuvchi SmartLight_AP tarmog'iga ulanganda, uning qurilmasi DNS so'rov yuboradi. Bizning DNS serverimiz barcha so'rovlarga ESP32 ning IP manzilini qaytaradi. Natijada, foydalanuvchi qaysi saytni ochishga harakat qilmasin, u ESP32 ning veb-serveriga yo'naltiriladi. Veb-server esa WiFi konfiguratsiya sahifasini ko'rsatadi.")
t("ESP32 da DNS server DNSServer kutubxonasi yordamida amalga oshirilgan. dnsServer.start funksiyasi 53-portda DNS serverni ishga tushiradi va barcha so'rovlarga ESP32 ning softAP IP manzilini qaytaradi. Bu wildcard DNS deb ataladi. Veb-server WebServer kutubxonasi yordamida amalga oshirilgan va 80-portda ishlaydi.")
t("Konfiguratsiya sahifasi oddiy HTML formadan iborat bo'lib, unda WiFi SSID va parol kiritish maydonlari mavjud. Foydalanuvchi ma'lumotlarni kiritib Save tugmasini bosganda, forma POST so'rov yuboradi. handleSave funksiyasi so'rovni qabul qiladi, SSID va parolni NVS ga saqlaydi va ESP32 ni qayta ishga tushiradi. Qayta ishga tushgandan keyin ESP32 yangi WiFi ma'lumotlari bilan ulanishga harakat qiladi.")
t("Captive portal ning afzalligi shundaki, foydalanuvchi hech qanday maxsus ilova o'rnatmasdan WiFi ma'lumotlarini o'zgartirishi mumkin. U oddiy telefon yoki kompyuterdan SmartLight_AP tarmog'iga ulanadi va brauzer avtomatik ochiladi. Bu ayniqsa qurilma yangi joyga o'rnatilganda yoki WiFi parol o'zgarganda qulay.")

doc.add_page_break()
h2("V ilova. Non-Volatile Storage va ma'lumotlarni doimiy saqlash")
t("Non-Volatile Storage ESP32 ning ichki flash xotirasida joylashgan maxsus bo'lim bo'lib, u kalit-qiymat juftliklarini saqlash uchun mo'ljallangan. NVS da saqlangan ma'lumotlar qurilma o'chirilganda, qayta ishga tushirilganda yoki firmware yangilanganda ham saqlanib qoladi. Bu xususiyat WiFi ma'lumotlari, konfiguratsiya parametrlari va boshqa doimiy ma'lumotlarni saqlash uchun ideal.")
t("NVS ning ichki tuzilishi log-structured fayl tizimiga o'xshaydi. Ma'lumotlar sahifalarga yoziladi va har bir yozish operatsiyasi yangi sahifaga yoziladi. Eski sahifalar garbage collection jarayonida tozalanadi. Bu yondashuv flash xotiraning yozish tsikllarini teng taqsimlaydi va xotiraning ishlash muddatini uzaytiradi. ESP32 ning flash xotirasi odatda 100000 yozish tsikliga ega.")
t("Bizning tizimimizda NVS quyidagi ma'lumotlarni saqlash uchun ishlatiladi. WiFi SSID va parol wifi namespace da ssid va pass kalitlari bilan saqlanadi. Bu ma'lumotlar captive portal orqali o'zgartirilishi mumkin va qurilma har safar yoqilganda NVS dan o'qiladi. Agar NVS da ma'lumot bo'lmasa, config.h dagi standart qiymatlar ishlatiladi.")
t("Preferences kutubxonasi NVS bilan ishlash uchun qulay interfeys beradi. prefs.begin funksiyasi namespace ni ochadi va ikkinchi parametr true bo'lsa faqat o'qish rejimida ochadi. prefs.getString funksiyasi string qiymatni o'qiydi va ikkinchi parametr standart qiymat bo'lib, kalit topilmasa qaytariladi. prefs.putString funksiyasi string qiymatni yozadi. prefs.end funksiyasi namespace ni yopadi va resurslarni bo'shatadi.")

doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')
print("Final pages added!")
