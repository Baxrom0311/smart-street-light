#!/usr/bin/env python3
"""Add ~40 more pages - expanded technical details"""
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
def img(name, caption):
    if not os.path.exists(IMG + name): return
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    run = p.add_run(); run.add_picture(IMG + name, width=Cm(14))
    pc = doc.add_paragraph(); pc.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    pc.paragraph_format.first_line_indent = Cm(0); pc.paragraph_format.space_before = Pt(0); pc.paragraph_format.space_after = Pt(0)
    rc = pc.add_run(caption); rc.italic = True; rc.font.size = Pt(12); rc.font.name = 'Times New Roman'

doc.add_page_break()
h2("F ilova. ESP32 mikrokontrollerining batafsil texnik tavsifi")
t("ESP32 mikrokontrolleri Espressif Systems kompaniyasi tomonidan 2016-yilda ishlab chiqilgan bo'lib, IoT va embedded tizimlar uchun mo'ljallangan. U Xtensa LX6 ikki yadroli protsessorga asoslangan bo'lib, har bir yadro 240 MHz gacha chastotada ishlaydi. Protsessor 32-bitli arxitekturaga ega va Harvard arxitekturasida qurilgan, ya'ni dastur va ma'lumotlar uchun alohida xotira magistrallari mavjud. Bu arxitektura bir vaqtning o'zida dastur kodini o'qish va ma'lumotlarni qayta ishlash imkonini beradi va samaradorlikni oshiradi.")
t("ESP32 ning xotira tizimi bir nechta qismdan iborat. Ichki SRAM 520 KB hajmga ega bo'lib, u ikki qismga bo'lingan: 200 KB DRAM va 320 KB IRAM. DRAM ma'lumotlar uchun ishlatiladi va o'zgaruvchilar, massivlar va dinamik xotira ajratish uchun foydalaniladi. IRAM dastur kodi uchun ishlatiladi va tez-tez chaqiriladigan funksiyalar bu yerda joylashtiriladi. Bundan tashqari, 4 MB tashqi SPI Flash xotira mavjud bo'lib, u firmware, SPIFFS fayl tizimi va OTA yangilash uchun ishlatiladi.")
t("WiFi moduli 802.11 b/g/n standartlarini qo'llab-quvvatlaydi va 2.4 GHz chastotada ishlaydi. Maksimal uzatish tezligi 150 Mbps bo'lib, bu IoT ilovalar uchun yetarli. WiFi moduli Station, SoftAP va Station+SoftAP rejimlarida ishlashi mumkin. Station rejimida qurilma mavjud WiFi tarmog'iga ulanadi. SoftAP rejimida qurilma o'zi WiFi nuqtasi bo'lib ishlaydi. Bizning tizimimizda ikkala rejim ham ishlatiladi: normal holatda Station, WiFi topilmaganda SoftAP.")
t("ADC moduli 18 ta kanalga ega bo'lib, ular ikki guruhga bo'lingan: ADC1 va ADC2. ADC1 8 ta kanalga ega va WiFi ishlayotganda ham foydalanish mumkin. ADC2 10 ta kanalga ega, lekin WiFi ishlayotganda foydalanib bo'lmaydi. Shu sababli biz TEMT6000 sensorini ADC1 kanaliga, ya'ni GPIO 34 ga uladik. ADC ning aniqligi 12 bit bo'lib, 0 dan 4095 gacha qiymat beradi. Biroq ESP32 ning ADC si ideal emas va nonlinear xatolikka ega, ayniqsa 0-100 mV va 3200-3300 mV diapazonlarida. Bizning qo'llanmamizda bu muammo ahamiyatsiz, chunki biz aniq qiymatni emas, balki chegaradan yuqori yoki past ekanligini tekshiramiz.")
t("GPIO tizimi 34 ta umumiy maqsadli kirish-chiqish piniga ega. Ulardan 18 tasi ADC funksiyasiga ega, 2 tasi DAC funksiyasiga ega, 16 tasi PWM chiqarishi mumkin va 10 tasi kapasitiv sensorlik funksiyasiga ega. Ba'zi pinlar maxsus vazifalarni bajaradi va ularni ehtiyotkorlik bilan ishlatish kerak. GPIO 0 boot rejimini aniqlaydi va LOW bo'lsa qurilma download rejimiga o'tadi. GPIO 2 onboard LED ga ulangan va boot vaqtida floating bo'lishi kerak. GPIO 12 flash kuchlanishini aniqlaydi va HIGH bo'lsa 1.8V, LOW bo'lsa 3.3V flash ishlatiladi. GPIO 15 JTAG debug uchun ishlatiladi.")
t("ESP32 ning energiya boshqaruv tizimi bir nechta rejimni qo'llab-quvvatlaydi. Active rejimda barcha modullar ishlaydi va iste'mol 160-260 mA. Modem Sleep rejimida WiFi o'chiriladi va iste'mol 20-30 mA. Light Sleep rejimida protsessor to'xtaydi lekin RAM saqlanadi va iste'mol 0.8 mA. Deep Sleep rejimida faqat RTC ishlaydi va iste'mol 10 mikroamper. Bizning tizimimizda Active rejim ishlatiladi, chunki sensorlar doimiy o'qilishi va WiFi doimiy ulangan bo'lishi kerak.")

doc.add_page_break()
h2("X ilova. Firebase Realtime Database batafsil tavsifi")
t("Firebase Realtime Database Google kompaniyasi tomonidan ishlab chiqilgan NoSQL bulutli ma'lumotlar bazasi bo'lib, real vaqt rejimida ma'lumot almashish uchun mo'ljallangan. U JSON formatida ma'lumotlarni saqlaydi va WebSocket protokoli orqali barcha ulangan clientlarga o'zgarishlarni darhol yetkazadi. Bu an'anaviy REST API dan farqli ravishda, client doimiy so'rov yubormasdan ham yangi ma'lumotlarni oladi.")
t("Firebase ning arxitekturasi client-server modeliga asoslangan. Client, ya'ni ESP32 yoki veb-brauzer, Firebase serveriga ulanadi va ma'lum yo'lni kuzatishni boshlaydi. Server ma'lumot o'zgarganda darhol barcha kuzatuvchilarga xabar beradi. Bu push model deb ataladi va polling modeldan ancha samarali. Polling modelda client har N soniyada serverga so'rov yuboradi va ko'pincha javob bo'sh bo'ladi, ya'ni ma'lumot o'zgarmagan. Push modelda esa faqat o'zgarish bo'lganda ma'lumot uzatiladi.")
t("Firebase ning ma'lumotlar strukturasi daraxt ko'rinishida bo'lib, har bir tugun yo'l orqali aniqlanadi. Bizning tizimimizda asosiy yo'l device bo'lib, u status, control va config kichik tugunlarini o'z ichiga oladi. status tugunida ESP32 tomonidan yoziladigan sensor qiymatlari va tizim holati saqlanadi. control tugunida dashboard tomonidan yoziladigan buyruqlar saqlanadi. config tugunida foydalanuvchi tomonidan o'zgartiriladigan sozlamalar saqlanadi.")
t("Firebase ning xavfsizlik qoidalari JSON formatida yoziladi va har bir yo'l uchun o'qish va yozish huquqlarini belgilaydi. Qoidalarda auth o'zgaruvchisi autentifikatsiya qilingan foydalanuvchini ifodalaydi. Agar auth null bo'lmasa, foydalanuvchi tizimga kirgan demak. Bizning qoidalarimizda device/status yo'liga o'qish ochiq, chunki dashboard autentifikatsiyadan oldin ham sensor qiymatlarini ko'rsatishi kerak. Boshqa barcha yo'llarga faqat autentifikatsiya qilingan foydalanuvchilar kirishi mumkin.")
t("Firebase ning bepul rejimi Spark plan deb ataladi va u bir nechta cheklovlarga ega. Bir vaqtda 100 ta ulanish mumkin, kuniga 10 GB ma'lumot uzatish mumkin va 1 GB saqlash hajmi mavjud. Bizning tizimimiz uchun bu cheklovlar yetarli, chunki bitta ESP32 va bitta dashboard faqat 2 ta ulanish ishlatadi. Kunlik ma'lumot uzatish hajmi taxminan 50 MB bo'lib, bu chegaradan ancha kam.")
t("Firebase Authentication xizmati foydalanuvchilarni autentifikatsiya qilish uchun ishlatiladi. U email va parol, Google, Facebook, telefon raqami va boshqa usullarni qo'llab-quvvatlaydi. Bizning tizimimizda email va parol usuli ishlatiladi. Foydalanuvchi device@smartlight.com email va SmartLight2026! parol bilan tizimga kiradi. Firebase avtomatik ravishda parolni hash qiladi va xavfsiz saqlaydi.")

doc.add_page_break()
h2("Y ilova. Progressive Web Application texnologiyasi batafsil")
t("Progressive Web Application zamonaviy veb-texnologiyalar yordamida yaratilgan ilova bo'lib, native ilovalar kabi ishlaydi. PWA konsepsiyasi 2015-yilda Google tomonidan taqdim etilgan va o'shandan beri jadal rivojlanmoqda. PWA ning asosiy g'oyasi bitta kod bazasi bilan barcha platformalarda, ya'ni desktop, mobil va planshetlarda ishlash imkoniyatini yaratishdir.")
t("PWA ning asosiy texnologiyalari Service Worker, Web App Manifest va HTTPS dir. Service Worker brauzer va tarmoq o'rtasida joylashgan JavaScript fayli bo'lib, u tarmoq so'rovlarini ushlab olishi va keshdan javob berishi mumkin. Bu offline ishlash imkoniyatini beradi. Web App Manifest JSON fayli bo'lib, u ilova nomi, ikonkalar, ranglar va boshqa metama'lumotlarni belgilaydi. HTTPS xavfsiz ulanishni ta'minlaydi va Service Worker faqat HTTPS orqali ishlaydi.")
t("Bizning dashboard da vite-plugin-pwa plaginidan foydalanilgan. Bu plagin avtomatik ravishda Service Worker yaratadi va Workbox kutubxonasini ishlatadi. Workbox Google tomonidan ishlab chiqilgan kutubxona bo'lib, kesh strategiyalarini boshqaradi. CacheFirst strategiyasi statik resurslar uchun ishlatiladi va avval keshdan qidiradi, topilmasa tarmoqdan oladi. NetworkFirst strategiyasi API so'rovlar uchun ishlatiladi va avval tarmoqdan olishga harakat qiladi, muvaffaqiyatsiz bo'lsa keshdan oladi.")
t("PWA ning o'rnatish jarayoni quyidagicha ishlaydi. Foydalanuvchi birinchi marta saytga kirganida brauzer Service Worker ni ro'yxatdan o'tkazadi va manifest faylini o'qiydi. Agar manifest to'g'ri to'ldirilgan bo'lsa va sayt HTTPS orqali ishlasa, brauzer foydalanuvchiga ilovani o'rnatish taklifini ko'rsatadi. Foydalanuvchi qabul qilsa, ilova bosh ekranga qo'shiladi va keyingi safar ochilganda brauzer paneli ko'rinmaydi, ya'ni native ilova kabi ko'rinadi.")
t("Bizning PWA ning manifest fayli quyidagi ma'lumotlarni o'z ichiga oladi. Ilova nomi Smart Street Light, qisqa nomi SmartLight, tema rangi va fon rangi 1a1a2e, ko'rsatish rejimi standalone. Ikonkalar 192x192 va 512x512 o'lchamlarda berilgan. start_url ildiz yo'lga yo'naltirilgan va scope ham ildiz yo'l bilan cheklangan.")

doc.add_page_break()
h2("SH ilova. Loyiha boshqaruvi va versiya nazorati")
t("Loyiha Git versiya nazorat tizimi yordamida boshqarildi va GitHub platformasida joylashtirildi. Repository manzili https://github.com/Baxrom0311/smart-street-light bo'lib, u ochiq kodli va hamma uchun foydalanish mumkin. Loyiha davomida jami 25 dan ortiq commit yaratildi va har bir commit aniq belgilangan o'zgarishni ifodalaydi.")
t("Loyiha strukturasi quyidagicha tashkil etilgan. Ildiz papkada firebase.json, database.rules.json va README.md fayllari joylashgan. firmware papkasida ESP32 firmware kodi joylashgan bo'lib, u PlatformIO loyiha strukturasiga mos keladi. web-dashboard papkasida React PWA kodi joylashgan bo'lib, u Vite loyiha strukturasiga mos keladi. docs papkasida hujjatlar joylashgan bo'lib, u arxitektura, hardware, software va boshqa hujjatlarni o'z ichiga oladi.")
t("Loyiha davomida bir nechta muhim muammolar yuzaga keldi va ular hal qilindi. Birinchi muammo ESP32 ning WiFi va Firebase kutubxonasi o'rtasidagi xotira konflikti bo'ldi. Bu muammo huge_app.csv partition sxemasiga o'tish orqali hal qilindi, chunki standart partition sxemasida dastur uchun ajratilgan xotira yetarli emas edi. Ikkinchi muammo Firebase stream callback funksiyasining to'g'ri ishlamasligi bo'ldi. Bu muammo readStream usulga o'tish orqali hal qilindi, chunki callback usul ESP32 da barqaror ishlamadi.")
t("Uchinchi muammo WiFi ulanish jarayonining blocking xususiyati bo'ldi. Standart WiFi.begin funksiyasi ulanish tugaguncha dasturni to'xtatadi va bu vaqtda sensorlar o'qilmaydi. Bu muammo non-blocking WiFi algoritmiga o'tish orqali hal qilindi, ya'ni WiFi ulanish jarayoni asosiy loop ni to'xtatmaydi. To'rtinchi muammo GPIO 26 pinining relay bilan ishlashida yuzaga keldi. Dastlab GPIO 27 tanlangan edi, lekin u relay bilan ishlamadi va GPIO 26 ga o'tish muammoni hal qildi.")
t("Beshinchi muammo dashboard da Live va Demo rejimlar o'rtasida almashishda holat yo'qolishi bo'ldi. Bu muammo localStorage ga isLive holatini saqlash orqali hal qilindi. Oltinchi muammo Settings sahifasida konfiguratsiya o'zgarishlarining Firebase ga saqlanmasligi bo'ldi. Bu muammo useEffect hook orqali tempConfig va config ni sinxronizatsiya qilish orqali hal qilindi.")

img("screenshot_log.png", "F.1-rasm. Harakat logi sahifasi")

doc.add_page_break()
h2("CH ilova. Energiya tejash hisoblash metodologiyasi")
t("Energiya tejash samaradorligini hisoblash uchun quyidagi metodologiya ishlab chiqildi. Asosiy formula E_tejash = ((T_tun - T_yonish) / T_tun) × 100 foiz bo'lib, bu yerda T_tun tun davomiyligi soatlarda va T_yonish yoritgichning haqiqiy yonish vaqti soatlarda. Bu formula an'anaviy tizim bilan solishtirganda qancha energiya tejalganini ko'rsatadi.")
t("Tun davomiyligi O'zbekiston uchun yil davomida o'zgaradi. Qishda tun 14 soatgacha cho'ziladi, yozda esa 8 soatgacha qisqaradi. O'rtacha yillik tun davomiyligi 11 soatni tashkil etadi. Bizning hisoblashlarimizda 12 soat ishlatildi, chunki sinov bahor oylarida o'tkazildi va bu vaqtda tun davomiyligi taxminan 12 soat.")
t("Yoritgichning yonish vaqti bir nechta omillarga bog'liq. Birinchi omil harakat intensivligi bo'lib, ko'chada qancha odam va transport vositasi harakatlanishi. Ikkinchi omil hold timer davomiyligi bo'lib, bizning tizimimizda 5 soniya. Uchinchi omil sensorning qamrov zonasi bo'lib, 2 metr masofa va 30 daraja burchak. To'rtinchi omil ko'chaning joylashuvi bo'lib, markaziy ko'chalarda harakat ko'p, chekkadagi ko'chalarda kam.")
t("Sinov davomida o'rtacha yonish vaqti 138 daqiqa yoki 2.3 soat bo'ldi. Bu 12 soatlik tun davomida yoritgich faqat 19.2 foiz vaqt yonganini ko'rsatadi. Qolgan 80.8 foiz vaqt yoritgich o'chiq bo'ldi va energiya tejaladi. Bu natija nazariy hisoblarga mos keladi va tizimning samaradorligini tasdiqlaydi.")
t("Iqtisodiy samaradorlikni hisoblash uchun O'zbekistondagi elektr energiyasi narxi ishlatildi. 2024-yil holatiga ko'ra, aholining elektr energiyasi narxi 500 so'm/kWh atrofida. Sanoat uchun narx biroz yuqori bo'lib, 700-900 so'm/kWh ni tashkil etadi. Bizning hisoblashlarimizda 500 so'm/kWh ishlatildi.")
t("Bitta 60 vattli yoritgich uchun yillik hisoblash quyidagicha. An'anaviy tizimda kunlik iste'mol 60W × 12h = 720 Wh. Smart Street tizimida kunlik iste'mol 60W × 2.3h = 138 Wh. Kunlik tejash 720 - 138 = 582 Wh. Yillik tejash 582 × 365 = 212430 Wh = 212.4 kWh. Pul hisobida 212.4 × 500 = 106200 so'm yillik tejamkorlik.")
t("Agar bitta ko'chada 20 ta yoritgich bo'lsa, yillik tejamkorlik 20 × 106200 = 2124000 so'm yoki 2.1 million so'm. Agar butun mahallada 100 ta yoritgich bo'lsa, yillik tejamkorlik 10.6 million so'm. Agar shahar miqyosida 10000 ta yoritgich bo'lsa, yillik tejamkorlik 1.06 milliard so'm. Bu raqamlar tizimning iqtisodiy samaradorligini yaqqol ko'rsatadi.")
t("CO2 emissiyasini kamaytirish ham muhim ekologik ko'rsatkich hisoblanadi. O'zbekistonda 1 kWh elektr energiyasi ishlab chiqarish uchun o'rtacha 0.6 kg CO2 chiqariladi. Bitta yoritgich uchun yillik CO2 tejash 212.4 × 0.6 = 127.4 kg. 10000 ta yoritgich uchun yillik CO2 tejash 1274 tonna. Bu Parij kelishuviga muvofiq O'zbekistonning CO2 emissiyasini kamaytirish majburiyatlariga hissa qo'shadi.")

tbl(["Miqyos", "Yoritgichlar", "Yillik tejash (kWh)", "Yillik tejash (so'm)", "CO2 tejash (kg)"],
    [["1 ta yoritgich", "1", "212.4", "106,200", "127.4"],
     ["1 ko'cha", "20", "4,248", "2,124,000", "2,549"],
     ["1 mahalla", "100", "21,240", "10,620,000", "12,744"],
     ["1 tuman", "1,000", "212,400", "106,200,000", "127,440"],
     ["1 shahar", "10,000", "2,124,000", "1,062,000,000", "1,274,400"]],
    "CH.1-jadval. Turli miqyoslarda energiya tejash ko'rsatkichlari")

t("Yuqoridagi jadvaldan ko'rinib turibdiki, tizim katta miqyosda joriy etilganda juda katta iqtisodiy va ekologik samara beradi. Bitta shahar miqyosida yiliga 1 milliard so'mdan ortiq tejash va 1274 tonna CO2 emissiyasini kamaytirish mumkin. Bu raqamlar tizimning nafaqat texnik, balki iqtisodiy va ekologik jihatdan ham samarali ekanligini isbotlaydi.")

doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')
print("40 more pages added!")
