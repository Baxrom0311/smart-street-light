#!/usr/bin/env python3
"""II BOB 2.1"""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')
IMG = '/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/images/'

def bob(text):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text); r.bold = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'
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

bob("II BOB. AMALIY QISM")
h2("2.1. Tizimni loyihalash: texnik vositalar va komponentlarni tanlash")
t("Tizimning asosiy boshqaruv elementi sifatida ESP32 DevKit V1 38-pin mikrokontrolleri tanlandi. ESP32 Espressif Systems kompaniyasi tomonidan 2016-yilda ishlab chiqilgan ikki yadroli mikrokontroller bo'lib, IoT loyihalari uchun eng mashhur platformalardan biri hisoblanadi. Tanlash jarayonida bir nechta alternativ variantlar ko'rib chiqildi va har birining afzallik va kamchiliklari tahlil qilindi.")
t("Arduino Uno ATmega328P protsessoriga asoslangan bo'lib, 16 MHz chastotada ishlaydi va 2 KB RAM ga ega. Uning asosiy kamchiligi WiFi modulining yo'qligi bo'lib, internet ulanishi uchun qo'shimcha shield kerak. ESP8266 Tensilica protsessoriga asoslangan bo'lib, 80 MHz chastotada ishlaydi va ichki WiFi moduliga ega. Biroq uning faqat bitta ADC kanali bor va 3.3V logikada ishlaydi. STM32F103 ARM Cortex-M3 protsessoriga asoslangan bo'lib, 72 MHz chastotada ishlaydi, lekin WiFi moduli yo'q. Raspberry Pi Pico ARM Cortex-M0+ protsessoriga asoslangan bo'lib, 133 MHz chastotada ishlaydi, lekin standart versiyasida WiFi yo'q.")

tbl(["Parametr", "Arduino Uno", "ESP8266", "ESP32", "STM32"],
    [["Protsessor", "ATmega328P", "Tensilica", "Xtensa LX6 (2x)", "Cortex-M3"],
     ["Chastota", "16 MHz", "80 MHz", "240 MHz", "72 MHz"],
     ["RAM", "2 KB", "80 KB", "520 KB", "20 KB"],
     ["WiFi", "Yo'q", "Ha", "Ha", "Yo'q"],
     ["ADC", "6ch/10-bit", "1ch/10-bit", "18ch/12-bit", "10ch/12-bit"],
     ["Narx", "~$5", "~$3", "~$5", "~$3"]],
    "2.1-jadval. Mikrokontrollerlarning qiyosiy tahlili")

t("ESP32 tanlash sabablari quyidagilardan iborat. Ichki WiFi moduli tashqi WiFi shield kerakligini bartaraf etadi va bu narxni hamda murakkablikni kamaytiradi. Ikki yadroli protsessor 240 MHz chastotada ishlaydi va bitta yadro sensorlarni o'qiydi, ikkinchisi WiFi va Firebase bilan ishlaydi, bu non-blocking arxitekturani ta'minlaydi. 12-bitli ADC 18 kanalga ega bo'lib, TEMT6000 yorug'lik sensorini aniq o'qish uchun yetarli. 520 KB RAM Firebase kutubxonasi va WiFi stack uchun yetarli. 3.3V logika RCWL-9610A bilan to'g'ridan-to'g'ri ulash imkonini beradi. Arzon narxi taxminan 5 AQSh dollarini tashkil etadi va loyiha byudjetiga mos keladi.")
t("Tizim uch qatlamli arxitekturaga ega bo'lib, har bir qatlam mustaqil ishlaydi va boshqa qatlamlar bilan aniq belgilangan interfeys orqali aloqa qiladi. Hardware qatlami ESP32 mikrokontrolleri, sensorlar va relay modulidan iborat. Cloud qatlami Firebase Realtime Database, Authentication va Hosting xizmatlaridan iborat. Client qatlami React PWA Dashboard dan iborat. Bu arxitektura modulli bo'lib, har bir qatlam alohida rivojlantirilishi va almashtirilishi mumkin.")

img("diagram_architecture.png", "2.1-rasm. Tizimning umumiy arxitekturasi")

t("Yuqoridagi rasmda tizimning umumiy arxitekturasi tasvirlangan. ESP32 sensorlardan ma'lumot o'qiydi, qaror qabul qiladi va relay orqali yoritgichni boshqaradi. Har 3 soniyada status ma'lumotlarini Firebase ga yuboradi. Dashboard Firebase dan real vaqt rejimida ma'lumot oladi va foydalanuvchi buyruqlarini Firebase ga yozadi. ESP32 stream orqali buyruqlarni qabul qiladi va darhol bajaradi.")
t("ESP32 DevKit 38-pin versiyasida jami 34 ta GPIO pin mavjud, biroq ularning hammasi ham erkin ishlatilishi mumkin emas. Ba'zi pinlar strapping pins deb ataladi va boot jarayonida maxsus vazifa bajaradi. GPIO 0 boot rejimini aniqlaydi va LOW bo'lsa download rejimiga o'tadi. GPIO 2 onboard LED ga ulangan va boot vaqtida LOW bo'lishi kerak. GPIO 12 flash kuchlanishini aniqlaydi. Shu sababli pin tanlashda ehtiyotkorlik zarur va biz faqat xavfsiz pinlarni tanladik.")

tbl(["ESP32 Pin", "Komponent", "Signal turi", "Yo'nalish", "Izoh"],
    [["GPIO 4", "RCWL-9610A TRIG", "Digital", "OUTPUT", "Xavfsiz pin"],
     ["GPIO 16", "RCWL-9610A ECHO", "Digital", "INPUT", "UART2 RX"],
     ["GPIO 34", "TEMT6000 OUT", "Analog", "INPUT", "Faqat input"],
     ["GPIO 26", "Relay IN", "Digital", "OUTPUT", "DAC2 pin"],
     ["GPIO 2", "Onboard LED", "Digital", "OUTPUT", "Status"]],
    "2.2-jadval. ESP32 pin tayinlash")

t("Pin tanlash asoslari quyidagicha. GPIO 4 strapping pin emas va digital output uchun mos. GPIO 16 UART2 RX pini, lekin biz UART2 ishlatmaymiz va u digital input uchun mos. GPIO 34 faqat input rejimida ishlaydigan pin bo'lib, ADC1 kanalida joylashgan va WiFi bilan conflict yo'q. GPIO 26 DAC2 pini, lekin biz DAC ishlatmaymiz va digital output uchun mos. GPIO 2 onboard LED ga ulangan va debug uchun qulay.")
t("Tizimning umumiy energiya iste'moli quyidagicha hisoblanadi. ESP32 WiFi active holatda 150 milliamper, kutish holatida 20 milliamper sarflaydi. RCWL-9610A doimiy ravishda 2 milliamper sarflaydi. TEMT6000 doimiy ravishda 0.1 milliamper sarflaydi. Relay moduli faqat yoqilganda 70 milliamper sarflaydi. Jami maksimal iste'mol 222.1 milliamper bo'lib, bu 5V da 1.11 vattga teng. Kuniga tizimning o'zi sarflaydigan energiya 1.11 × 24 = 26.6 vatt-soat yoki 0.027 kWh ni tashkil etadi. Bu yoritgichning o'zi sarflaydigan energiyaga nisbatan 27 marta kam.")

tbl(["Komponent", "Ish toki", "Kutish toki", "Izoh"],
    [["ESP32 (WiFi)", "150 mA", "20 mA", "WiFi uzatish"],
     ["RCWL-9610A", "2 mA", "2 mA", "Doimiy"],
     ["TEMT6000", "0.1 mA", "0.1 mA", "Doimiy"],
     ["Relay modul", "70 mA", "0 mA", "Yoqilganda"],
     ["JAMI", "222.1 mA", "22.1 mA", ""]],
    "2.3-jadval. Tizim energiya iste'moli")

t("Firmware ishlab chiqish uchun PlatformIO IDE tanlandi. PlatformIO professional embedded development platform bo'lib, Arduino framework ni qo'llab-quvvatlaydi va VS Code bilan integratsiya qilingan. Arduino IDE dan farqli ravishda, PlatformIO kutubxonalarni avtomatik boshqaradi, multi-environment build ni qo'llab-quvvatlaydi va professional CI/CD pipeline larni sozlash imkonini beradi. Loyihada Arduino Framework ESP32 versiyasi, Firebase ESP32 Client kutubxonasi 4.4.17 versiyasi, WiFi, Preferences, DNSServer va WebServer kutubxonalari ishlatildi.")
t("Web dashboard uchun React 19 va Vite 8 tanlandi. React Meta kompaniyasi tomonidan ishlab chiqilgan UI kutubxona bo'lib, komponent asosida ishlaydi va virtual DOM texnologiyasi yordamida yuqori samaradorlikni ta'minlaydi. Vite yangi avlod build tool bo'lib, Hot Module Replacement va tezkor build ni ta'minlaydi. Firebase SDK 10 real vaqt ma'lumot almashish uchun, Recharts esa grafiklar uchun ishlatildi. vite-plugin-pwa plaginidan PWA funksionallik uchun foydalanildi.")

tbl(["Kutubxona", "Versiya", "Vazifasi"],
    [["Arduino Framework", "ESP32 v2.x", "Asosiy framework"],
     ["Firebase ESP32 Client", "v4.4.17", "Firebase RTDB"],
     ["React", "v19", "UI framework"],
     ["Vite", "v8", "Build tool"],
     ["Firebase SDK", "v10", "Web Firebase"],
     ["Recharts", "v2.x", "Grafiklar"],
     ["vite-plugin-pwa", "v0.x", "PWA support"]],
    "2.4-jadval. Ishlatilgan kutubxonalar")

doc.add_page_break()
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')
print("2.1 done (~15 pages)")
