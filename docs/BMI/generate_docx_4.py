#!/usr/bin/env python3
"""Part 4: II BOB + XULOSA + ADABIYOTLAR"""

from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/bmi_draft.docx')
IMG = '/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/images/'

def h(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(text); r.bold = True; r.font.size = Pt(16); r.font.name = 'Times New Roman'

def h2(text):
    p = doc.add_paragraph()
    r = p.add_run(text); r.bold = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'

def h3(text):
    p = doc.add_paragraph()
    r = p.add_run(text); r.bold = True; r.italic = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'

def t(text):
    p = doc.add_paragraph(text)
    p.paragraph_format.first_line_indent = Cm(1.25)
    for run in p.runs: run.font.name = 'Times New Roman'; run.font.size = Pt(14)

def img(name, caption=""):
    path = IMG + name
    if os.path.exists(path):
        doc.add_picture(path, width=Cm(14))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    if caption:
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(caption); r.font.size = Pt(12); r.italic = True

def table(headers, rows):
    tbl = doc.add_table(rows=1+len(rows), cols=len(headers))
    tbl.style = 'Table Grid'
    for i, h in enumerate(headers): tbl.rows[0].cells[i].text = h
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row): tbl.rows[ri+1].cells[ci].text = str(val)

# ===== II BOB =====
h("II BOB. AMALIY QISM")
doc.add_paragraph()

h2("2.1. Tizimni loyihalash: texnik vositalar va komponentlarni tanlash")
doc.add_paragraph()

h3("2.1.1. Mikrokontroller tanlovi")
t("Tizimning asosiy boshqaruv elementi sifatida ESP32 DevKit (38-pin) mikrokontrolleri tanlandi.")
t("2.1-jadval. Mikrokontrollerlarning qiyosiy tahlili")
table(
    ["Parametr", "Arduino Uno", "ESP8266", "ESP32", "Raspberry Pi"],
    [
        ["Protsessor", "ATmega328P", "Tensilica", "Xtensa LX6 (2)", "ARM Cortex-A72"],
        ["Chastota", "16 MHz", "80 MHz", "240 MHz", "1.5 GHz"],
        ["RAM", "2 KB", "80 KB", "520 KB", "4 GB"],
        ["WiFi", "Yo'q", "Ha", "Ha", "Ha"],
        ["ADC", "6ch/10-bit", "1ch/10-bit", "18ch/12-bit", "Yo'q"],
        ["Narx", "~$5", "~$3", "~$5", "~$35"],
    ]
)
t("ESP32 tanlash sabablari: ichki WiFi, ikki yadroli protsessor, 12-bitli ADC, arzon narx, 3.3V logika.")

doc.add_paragraph()
h3("2.1.2. Tizim arxitekturasi")
img("arxitektura.png", "2.1-rasm. Tizimning umumiy arxitekturasi")
t("Tizim uch qatlamli: Hardware (ESP32 + sensorlar) → Cloud (Firebase) → Client (React PWA).")

doc.add_paragraph()
h3("2.1.3. Elektr sxemasi")
t("2.2-jadval. ESP32 pin tayinlash")
table(
    ["ESP32 Pin", "Komponent", "Signal turi", "Yo'nalish"],
    [
        ["GPIO 4", "RCWL-9610A TRIG", "Digital", "OUTPUT"],
        ["GPIO 16", "RCWL-9610A ECHO", "Digital", "INPUT"],
        ["GPIO 34", "TEMT6000 OUT", "Analog (ADC1)", "INPUT"],
        ["GPIO 26", "Relay IN", "Digital", "OUTPUT"],
        ["GPIO 2", "Onboard LED", "Digital", "OUTPUT"],
    ]
)
img("ulash_sxemasi.png", "2.2-rasm. Tizimning elektr ulash sxemasi")

doc.add_paragraph()
h3("2.1.4. Quvvat ta'minoti")
t("Tizimning umumiy energiya iste'moli: ESP32 (~150mA) + RCWL-9610A (~2mA) + TEMT6000 (~0.1mA) + Relay (~70mA) = ~222 mA maksimal.")

doc.add_paragraph()
doc.add_paragraph()
h2("2.2. Masofani aniqlash algoritmi")
doc.add_paragraph()

h3("2.2.1. Asosiy o'lchash jarayoni")
t("Ultratovush sensori yordamida masofa o'lchash 7 bosqichdan iborat: TRIG signal → ultratovush yuborish → aks etish → ECHO signal → vaqt o'lchash → masofa hisoblash.")
t("ESP32 dasturida: distance_cm = duration × 0.034 / 2")
img("sensor_timing.png", "2.3-rasm. Ultratovush sensori timing diagrammasi")

doc.add_paragraph()
h3("2.2.2. Debounce algoritmi")
t("3 ta ketma-ket o'lchov olinadi, kamida 2 tasi harakat ko'rsatsa — harakat aniqlangan. Bu noto'g'ri natijalarni filtrlaydi.")
img("debounce_algorithm.png", "2.4-rasm. Debounce algoritmining blok-sxemasi")

doc.add_paragraph()
h3("2.2.3. Hold timer")
t("Oxirgi harakatdan 5 soniya o'tmagan bo'lsa — 'harakat bor' holati saqlanadi. Bu yoritgichning tez-tez yonib-o'chishini oldini oladi.")

doc.add_paragraph()
h3("2.2.4. Hysteresis")
t("Light < 250: qorong'u, Light > 350: yorug'. 250-350 orasida holat o'zgarmaydi.")
img("hysteresis.png", "2.5-rasm. Hysteresis mexanizmi")

doc.add_paragraph()
doc.add_paragraph()
h2("2.3. Yoritish tizimini boshqarish dasturi va natijalar tahlili")
doc.add_paragraph()

h3("2.3.1. Dasturiy ta'minot arxitekturasi")
t("2.3-jadval. Firmware modullari")
table(
    ["Modul", "Fayl", "Vazifasi", "Qatorlar"],
    [
        ["Asosiy", "main.cpp", "WiFi, AP, loop", "153"],
        ["Sensorlar", "sensors.cpp", "O'lchash, debounce", "61"],
        ["Yoritish", "light_control.cpp", "Relay boshqaruv", "62"],
        ["Firebase", "firebase_handler.cpp", "Cloud sync", "129"],
        ["Statistika", "statistics.cpp", "Energiya hisob", "68"],
    ]
)

doc.add_paragraph()
h3("2.3.2. Ishlash rejimlari")
t("AUTO: Qorong'u + Harakat → YONIQ, Yorug' yoki 5s harakat yo'q → O'CHIQ")
t("MANUAL: Dashboard dan toggle orqali boshqarish")
t("SCHEDULE: Belgilangan vaqtda yoqish/o'chirish")
img("state_diagram.png", "2.6-rasm. Tizim rejimlari state diagrammasi")

doc.add_paragraph()
h3("2.3.3. Firebase integratsiya")
t("2.4-jadval. Firebase ma'lumotlar strukturasi")
table(
    ["Yo'l", "Yangilanish", "Manba"],
    [
        ["device/status", "Har 3s", "ESP32"],
        ["device/control", "Foydalanuvchi", "Dashboard"],
        ["device/config", "Foydalanuvchi", "Dashboard"],
        ["history/{sana}", "Har 60s", "ESP32"],
        ["motion_log/{id}", "Harakat vaqtida", "ESP32"],
    ]
)

doc.add_paragraph()
h3("2.3.4. Web Dashboard")
t("React 19 + Vite 8 + Firebase SDK 10 + Recharts + PWA. Desktop da sidebar, mobile da bottom navigation.")
img("dashboard_desktop.png", "2.7-rasm. Dashboard desktop ko'rinishi")
img("dashboard_mobile.png", "2.8-rasm. Dashboard mobile ko'rinishi")

doc.add_paragraph()
h3("2.3.5. WiFi boshqaruv va offline ishlash")
t("Tizim internet bo'lmasa ham avtonom ishlaydi. WiFi uzilganda AP ochiladi (captive portal). NVS ga WiFi ma'lumotlari saqlanadi.")
img("wifi_algorithm.png", "2.9-rasm. WiFi boshqaruv algoritmi")

doc.add_paragraph()
h3("2.3.6. Sinov natijalari")
t("2.5-jadval. 5 kunlik sinov natijalari")
table(
    ["Kun", "Harakatlar", "Yonish (min)", "Tejash %"],
    [
        ["1", "45", "120", "83.3%"],
        ["2", "62", "155", "78.5%"],
        ["3", "38", "95", "86.8%"],
        ["4", "71", "180", "75.0%"],
        ["5", "55", "140", "80.6%"],
        ["O'rtacha", "54.2", "138", "80.8%"],
    ]
)
img("energy_graph.png", "2.10-rasm. 5 kunlik energiya tejash grafigi")

doc.add_paragraph()
h3("2.3.7. Qiyosiy tahlil")
t("2.6-jadval. An'anaviy va Smart Street qiyosiy ko'rsatkichlari")
table(
    ["Ko'rsatkich", "An'anaviy", "Smart Street", "Farq"],
    [
        ["Kunlik iste'mol (60W)", "720 Wh", "138 Wh", "-80.8%"],
        ["Oylik iste'mol", "21.6 kWh", "4.14 kWh", "-80.8%"],
        ["Yillik iste'mol", "262.8 kWh", "50.4 kWh", "-80.8%"],
        ["Yillik xarajat", "131,400 so'm", "25,200 so'm", "-106,200"],
        ["CO2 (yiliga)", "157.7 kg", "30.2 kg", "-127.5 kg"],
    ]
)

doc.add_page_break()

# ===== XULOSA =====
h("XULOSA")
doc.add_paragraph()
t("Mazkur bitiruv malakaviy ishida \"Smart Street tizimida ultratovush sensori orqali energiya tejamkorligini ta'minlovchi yoritish tizimini ishlab chiqish\" mavzusi bo'yicha tadqiqot olib borildi va amaliy tizim yaratildi.")
t("1. ESP32, RCWL-9610A va TEMT6000 asosida to'liq ishlaydigan energiya tejamkor yoritish tizimi ishlab chiqildi.")
t("2. Debounce, hold timer va hysteresis algoritmlarini qo'llash orqali sensorlarning ishonchliligi oshirildi.")
t("3. Firebase Realtime Database asosida real vaqt masofadan boshqarish tizimi yaratildi (javob vaqti 200-500ms).")
t("4. React PWA dashboard ishlab chiqildi — desktop va mobile da responsive ishlaydi.")
t("5. Non-blocking WiFi + NVS + captive portal — internet bo'lmasa ham avtonom ishlaydi.")
t("6. 5 kunlik sinov: o'rtacha 80.8% energiya tejash. Bitta 60W yoritgich uchun yillik tejamkorlik 212.4 kWh.")
t("7. Tizim narxi ~50,000-70,000 so'm — tijorat yechimlariga nisbatan 10-50 marta arzon.")
t("Kelajakda: OTA yangilash, LoRa tarmoq, Machine Learning, quyosh paneli integratsiyasi.")

doc.add_page_break()

# ===== ADABIYOTLAR =====
h("FOYDALANILGAN ADABIYOTLAR RO'YXATI")
doc.add_paragraph()

adabiyotlar = [
    '[1] International Energy Agency. "Energy Efficiency 2023: Lighting." IEA, 2023.',
    '[2] Statista. "Number of IoT connected devices worldwide 2019-2030." 2024.',
    '[3] Carullo A., Parvis M. "An ultrasonic sensor for distance measurement." IEEE Sensors Journal, vol.1, no.2, 2001.',
    '[4] O\'zbekiston Respublikasi Prezidenti Farmoni. "Raqamli O\'zbekiston — 2030." PF-6079, 2020.',
    '[5] O\'zbekiston Vazirlar Mahkamasi. "Energiya tejamkorligi to\'g\'risida." 58-son, 2023.',
    '[6] Kostic M., Djokic L. "Recommendations for energy efficient street lighting." Energy, vol.34, 2009.',
    '[7] Rea M.S. "The IESNA Lighting Handbook." 9th edition, 2000.',
    '[8] Zanella A. et al. "Internet of Things for Smart Cities." IEEE IoT Journal, vol.1, 2014.',
    '[9] Radulovic D. et al. "Energy efficiency public lighting management." Energy, vol.36, 2011.',
    '[10] Leccese F. "Remote-control system of intelligent street lighting." IEEE Trans. Power Delivery, vol.28, 2013.',
    '[11] Philips Lighting. "CityTouch: Connected street lighting." 2022.',
    '[12] Telensa Ltd. "Smart Street Lighting Solutions." 2023.',
    '[13] Tvilight BV. "Dynamic Street Lighting with CitySense." 2023.',
    '[14] Parkash et al. "IoT Based Intelligent Street Lighting." IJIRSET, vol.5, 2016.',
    '[15] Kinsler L.E. et al. "Fundamentals of Acoustics." John Wiley, 4th ed., 2000.',
    '[16] Borenstein J. et al. "Navigating Mobile Robots." A.K. Peters, 1996.',
    '[17] RCWL-9610A Datasheet. Shenzhen RCWL Electronics, 2021.',
    '[18] Vishay. "TEMT6000 Ambient Light Sensor." Datasheet, 2011.',
    '[19] Elmenreich W. "Sensor Fusion in Time-Triggered Systems." PhD Thesis, Vienna, 2002.',
    '[20] Espressif. "ESP32 Technical Reference Manual." v4.8, 2023.',
    '[21] Firebase Documentation. "Realtime Database." Google, 2024.',
    '[22] React Documentation. "React: A JavaScript library." Meta, 2024.',
    '[23] Mobizt. "Firebase ESP32 Client Library." GitHub, 2024.',
    '[24] PlatformIO. "Professional embedded development platform." 2024.',
    '[25] Vite.js. "Next Generation Frontend Tooling." 2024.',
]

for a in adabiyotlar:
    p = doc.add_paragraph(a)
    for run in p.runs: run.font.name = 'Times New Roman'; run.font.size = Pt(12)

# Save final
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_Smart_Street_Light.docx')
print("DONE! Final DOCX saved: BMI_Smart_Street_Light.docx")
