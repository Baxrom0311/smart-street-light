#!/usr/bin/env python3
"""Part 3: I BOB"""

from docx import Document
from docx.shared import Pt, Cm, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/bmi_draft.docx')
IMG = '/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/images/'

def h(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text)
    r.bold = True; r.font.size = Pt(16); r.font.name = 'Times New Roman'

def h2(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'

def h3(text):
    p = doc.add_paragraph()
    r = p.add_run(text)
    r.bold = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'
    r.italic = True

def t(text):
    p = doc.add_paragraph(text)
    p.paragraph_format.first_line_indent = Cm(1.25)
    for run in p.runs:
        run.font.name = 'Times New Roman'; run.font.size = Pt(14)

def img(name, caption=""):
    path = IMG + name
    if os.path.exists(path):
        doc.add_picture(path, width=Cm(14))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    if caption:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(caption)
        r.font.size = Pt(12); r.font.name = 'Times New Roman'; r.italic = True

def table(headers, rows):
    tbl = doc.add_table(rows=1+len(rows), cols=len(headers))
    tbl.style = 'Table Grid'
    for i, h in enumerate(headers):
        tbl.rows[0].cells[i].text = h
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            tbl.rows[ri+1].cells[ci].text = str(val)

# ===== I BOB =====
h("I BOB. SMART STREET TIZIMIDA YORITISH TIZIMLARI\nTIZIMLI TAHLILI VA MASALANING QO'YILISHI")
doc.add_paragraph()

h2("1.1. Smart Street tizimlarida energiya tejamkor yoritish tizimlari va ularning ahamiyati")
doc.add_paragraph()

h3("1.1.1. Ko'cha yoritish tizimlarining hozirgi holati")
t("Ko'cha yoritish tizimlari zamonaviy shahar infratuzilmasining ajralmas qismi hisoblanadi. Ular fuqarolarning xavfsizligini ta'minlash, transport harakatini tartibga solish va shahar estetik ko'rinishini yaxshilash kabi muhim vazifalarni bajaradi. Biroq, an'anaviy ko'cha yoritish tizimlari bir qator jiddiy muammolarga ega [1].")
t("Birinchidan, an'anaviy tizimlar tun bo'yi (o'rtacha 10-12 soat) uzluksiz ishlaydi. Bu vaqtning katta qismida — ayniqsa tunda soat 00:00 dan 05:00 gacha — ko'chalarda harakat deyarli bo'lmaydi, ammo yoritgichlar to'liq quvvatda yonib turadi. Xalqaro Energetika Agentligi (IEA) ma'lumotlariga ko'ra, ko'cha yoritish dunyo elektr energiyasi iste'molining taxminan 3.19 foizini tashkil etadi, bu yiliga 320 TWh ga teng [6].")
t("Ikkinchidan, ko'plab rivojlanayotgan mamlakatlarda, jumladan O'zbekistonda, ko'cha yoritish tizimlari hali ham eski texnologiyalarga — natriy lampalar va lyuminessent lampalar — asoslangan. Bu lampalar nafaqat ko'p energiya sarflaydi, balki ularning ishlash muddati ham qisqa (o'rtacha 6000-10000 soat) [7].")
t("Uchinchidan, markazlashtirilgan boshqaruv tizimlarining yo'qligi sababli nosozliklarni aniqlash va bartaraf etish uzoq vaqt talab qiladi. Ko'pincha bitta yoritgichning ishdan chiqishi bir necha hafta davomida aniqlanmay qoladi.")

doc.add_paragraph()
t("1.1-jadval. An'anaviy va aqlli yoritish tizimlarining qiyosiy tahlili")
table(
    ["Parametr", "An'anaviy tizim", "Aqlli tizim"],
    [
        ["Ishlash rejimi", "Tun bo'yi uzluksiz", "Faqat kerak bo'lganda"],
        ["Energiya iste'moli", "100% (12 soat)", "20-40%"],
        ["Boshqaruv", "Qo'lda / taymer", "Avtomatik / masofadan"],
        ["Nosozlik aniqlash", "Qo'lda tekshirish", "Real-time monitoring"],
        ["Energiya tejash", "0%", "60-80%"],
        ["Xizmat muddati", "6000-10000 soat", "50000+ soat (LED)"],
    ]
)

doc.add_paragraph()
h3("1.1.2. Smart Street (Aqlli ko'cha) konsepsiyasi")
t("Smart Street — bu zamonaviy axborot-kommunikatsiya texnologiyalari, sensorlar va IoT qurilmalari yordamida ko'cha infratuzilmasini aqlli boshqarish konsepsiyasidir. Bu konsepsiya Smart City (Aqlli shahar) ning muhim tarkibiy qismi hisoblanadi [8].")
t("Aqlli ko'cha yoritish tizimi quyidagi asosiy komponentlardan iborat: 1) Sensorlar qatlami — harakatni aniqlash, yorug'lik darajasini o'lchash; 2) Boshqaruv qatlami — mikrokontrollerlar yordamida qaror qabul qilish; 3) Aloqa qatlami — WiFi orqali ma'lumotlarni uzatish; 4) Bulutli qatlam — Firebase da saqlash va tahlil; 5) Foydalanuvchi interfeysi — PWA dashboard.")

img("diagram_architecture.png", "1.1-rasm. Aqlli ko'cha yoritish tizimining umumiy arxitekturasi")

doc.add_paragraph()
h3("1.1.3. Energiya tejamkorlik muammosi va yechimlar")
t("Energiya tejamkorlik — bu bir xil natijaga erishish uchun kamroq energiya sarflash demakdir. Ko'cha yoritish sohasida energiya tejamkorlikni ta'minlashning bir nechta yondashuvlari mavjud [9]:")
t("1) LED texnologiyasiga o'tish — LED lampalar an'anaviy lampalarga nisbatan 50-70% kam energiya sarflaydi;")
t("2) Dimming — tunda yorug'likni 30-50% ga pasaytirish;")
t("3) Sensorli boshqaruv — harakat sensorlari yordamida faqat kerak bo'lganda yoqish;")
t("4) Jadval bo'yicha boshqarish — vaqt jadvaliga asosan yoqish/o'chirish;")
t("5) Adaptiv boshqaruv — ob-havo va harakat intensivligiga qarab moslashish.")
t("Mazkur ishda uchinchi yondashuv — sensorli boshqaruv — asosiy usul sifatida tanlandi. Ultratovush sensori yordamida harakatni aniqlash eng aniq va ishonchli natija beradi [10].")

doc.add_paragraph()
h3("1.1.4. Mavjud yechimlarning tahlili")
t("Dunyo miqyosida ko'cha yoritishni aqlli boshqarish bo'yicha bir qator loyihalar amalga oshirilgan:")
t("1) Philips CityTouch — markazlashtirilgan boshqaruv, 30-40% tejash [11];")
t("2) Telensa — LoRa tarmoq, 50-60% tejash [12];")
t("3) Tvilight — radar sensori, 60-70% tejash [13];")
t("4) Arduino/ESP ochiq kodli loyihalar — 50-80% tejash [14].")

t("1.2-jadval. Mavjud yechimlarning qiyosiy tahlili")
table(
    ["Tizim", "Sensor", "Aloqa", "Tejash", "Narx"],
    [
        ["Philips CityTouch", "PIR + Light", "4G/LTE", "30-40%", "Yuqori"],
        ["Telensa", "PIR + Light", "LoRa", "50-60%", "O'rtacha"],
        ["Tvilight", "Radar", "WiFi", "60-70%", "Yuqori"],
        ["Bizning tizim", "Ultrasonic+Light", "WiFi/Firebase", "60-80%", "Past"],
    ]
)

doc.add_paragraph()
doc.add_paragraph()
h2("1.2. Ultratovush sensorlarning ishlash prinsipi va texnik xususiyatlari")
doc.add_paragraph()

h3("1.2.1. Ultratovush to'lqinlarining fizik asoslari")
t("Ultratovush — bu chastotasi 20 kHz dan yuqori bo'lgan tovush to'lqinlaridir. Havoda ultratovush tezligi taxminan 343 m/s (20°C da). Bu qiymat haroratga bog'liq: v = 331.3 + 0.606 × T, bu yerda T — harorat (°C) [15].")
t("Ultratovush to'lqinlarining asosiy xususiyatlari: 1) Qattiq jismlardan aks etadi — masofa o'lchash uchun asosiy prinsip; 2) Ma'lum burchak ostida tarqaladi (RCWL-9610A uchun ~30°); 3) Ob-havo sharoitlariga kam ta'sirchan.")

doc.add_paragraph()
h3("1.2.2. Masofa o'lchash prinsipi")
t("Ultratovush sensori \"Time of Flight\" (ToF) prinsipiga asoslanadi [16]:")
t("d = (t × v) / 2")
t("bu yerda: d — masofa (m), t — to'lqinning borish va qaytish vaqti (s), v — tovush tezligi (343 m/s). 2 ga bo'linadi, chunki to'lqin ikki marta yo'l bosadi.")

img("diagram_sequence.png", "1.2-rasm. Ultratovush sensori timing diagrammasi")

t("ESP32 dasturida: distance_cm = duration × 0.034 / 2, bu yerda duration — pulseIn() qaytargan mikrosekundlardagi qiymat.")

doc.add_paragraph()
h3("1.2.3. RCWL-9610A sensori texnik xususiyatlari")
t("1.3-jadval. RCWL-9610A texnik xususiyatlari")
table(
    ["Parametr", "Qiymat"],
    [
        ["Ish kuchlanishi", "3.0 - 5.5V"],
        ["Ish toki", "< 2mA"],
        ["O'lchash diapazoni", "2 cm - 450 cm"],
        ["O'lchash aniqligi", "±1 cm"],
        ["Ishchi chastota", "40 kHz"],
        ["Trigger signal", "10 μs HIGH pulse"],
        ["O'lchash burchagi", "~30°"],
        ["Ishlash harorati", "-20°C dan +70°C"],
    ]
)

doc.add_paragraph()
h3("1.2.4. TEMT6000 yorug'lik sensori")
t("1.4-jadval. TEMT6000 texnik xususiyatlari")
table(
    ["Parametr", "Qiymat"],
    [
        ["Ish kuchlanishi", "3.3 - 5V"],
        ["Chiqish signali", "Analog (0 - VCC)"],
        ["Spektral diapazoni", "360 - 970 nm"],
        ["Ko'rish burchagi", "±60°"],
    ]
)
t("ESP32 ning 12-bitli ADC yordamida 0-4095 qiymatga o'giriladi. 0-250: qorong'u, 250-350: oraliq, 350+: yorug' [18].")

doc.add_paragraph()
h3("1.2.5. Harakatni aniqlash algoritmi")
t("Sensorning shovqinini bartaraf etish uchun maxsus algoritm ishlab chiqildi [19]:")
t("1) Debounce — 3 ta o'lchov ichida 2 tasi harakat ko'rsatsa, harakat aniqlangan;")
t("2) Hold timer — 5 soniya davomida 'harakat bor' holati saqlanadi;")
t("3) Hysteresis — yorug'lik chegarasida tebranishni bartaraf etadi (250/350).")

img("diagram_flowchart.png", "1.3-rasm. Harakatni aniqlash algoritmining blok-sxemasi")

doc.add_paragraph()
doc.add_paragraph()
h2("1.3. Masalaning qo'yilishi")
doc.add_paragraph()
t("Yuqorida keltirilgan tahlillar asosida quyidagi masala qo'yiladi:")
t("ESP32 mikrokontrolleri, RCWL-9610A ultratovush sensori va TEMT6000 yorug'lik sensori asosida energiya tejamkor ko'cha yoritish tizimini ishlab chiqish zarur.")
doc.add_paragraph()
t("Funksional talablar:")
t("1) Harakatni 2 metr masofagacha aniqlash;")
t("2) Kunduz/tun holatini avtomatik farqlash;")
t("3) Qorong'uda harakat aniqlanganda yoritgichni yoqish;")
t("4) Harakat to'xtagandan 5 soniya keyin o'chirish;")
t("5) Masofadan boshqarish (Auto/Manual/Schedule);")
t("6) Real-time monitoring;")
t("7) Energiya tejash statistikasi.")
doc.add_paragraph()
t("Energiya tejash formulasi:")
t("E_tejash = ((T_tun - T_yonish) / T_tun) × 100%")
t("Misol: T_tun=12 soat, T_yonish=2.5 soat → E_tejash = 79.2%")

doc.add_page_break()
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/bmi_draft.docx')
print("Part 3 done: I BOB")
