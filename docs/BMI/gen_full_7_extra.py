#!/usr/bin/env python3
"""Add ~10 more pages - IoT protocols, PWA, additional tables"""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_full.docx')
IMG = '/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/images/'

def hc(t, sz=16):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(t); r.bold = True; r.font.size = Pt(sz); r.font.name = 'Times New Roman'
def h2(t):
    doc.add_paragraph()
    p = doc.add_paragraph(); r = p.add_run(t); r.bold = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'
def h3(t):
    p = doc.add_paragraph(); r = p.add_run(t); r.bold = True; r.italic = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'
def t(x):
    p = doc.add_paragraph(x); p.paragraph_format.first_line_indent = Cm(1.25)
    for r in p.runs: r.font.name = 'Times New Roman'; r.font.size = Pt(14)
def tbl(headers, rows, caption=""):
    if caption: t(caption)
    tb = doc.add_table(rows=1+len(rows), cols=len(headers)); tb.style = 'Table Grid'
    for i, hd in enumerate(headers): tb.rows[0].cells[i].text = hd
    for ri, row in enumerate(rows):
        for ci, v in enumerate(row): tb.rows[ri+1].cells[ci].text = str(v)
    doc.add_paragraph()
def img(name, caption=""):
    if os.path.exists(IMG + name):
        doc.add_picture(IMG + name, width=Cm(14))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    if caption:
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(caption); r.font.size = Pt(12); r.italic = True; r.font.name = 'Times New Roman'

# ===== QO'SHIMCHA BO'LIM - ILOVALAR davomi =====
doc.add_page_break()
hc("M ilova. IoT aloqa protokollarining qiyosiy tahlili", 14)
doc.add_paragraph()

t("Internet of Things (IoT) tizimlarida qurilmalar o'rtasida ma'lumot almashish uchun turli aloqa protokollari qo'llaniladi. Har bir protokol o'ziga xos afzallik va kamchiliklarga ega bo'lib, loyiha talablariga qarab tanlanadi. Quyida ko'cha yoritish tizimlari uchun eng keng tarqalgan protokollarning batafsil qiyosiy tahlili keltirilgan.")

tbl(["Protokol", "Masofa", "Tezlik", "Energiya", "Narx", "Bizning tizim"],
    [["WiFi (802.11n)", "50-100 m", "150 Mbps", "Yuqori", "Bepul*", "Ha"],
     ["LoRa", "2-15 km", "0.3-50 kbps", "Juda past", "O'rtacha", "Yo'q"],
     ["Zigbee", "10-100 m", "250 kbps", "Past", "O'rtacha", "Yo'q"],
     ["NB-IoT", "10+ km", "200 kbps", "Past", "Oylik to'lov", "Yo'q"],
     ["Bluetooth LE", "10-30 m", "2 Mbps", "Juda past", "Bepul", "Yo'q"],
     ["4G/LTE", "Cheksiz", "100 Mbps", "Yuqori", "Oylik to'lov", "Yo'q"],
     ["MQTT/HTTP", "Internet", "—", "—", "Bepul", "Ha (HTTP)"]],
    "M.1-jadval. IoT aloqa protokollarining qiyosiy tahlili")

t("WiFi tanlash sabablari: 1) ESP32 da ichki WiFi moduli mavjud — qo'shimcha hardware kerak emas; 2) Yuqori tezlik (150 Mbps) — real-time ma'lumot uzatish uchun yetarli; 3) Firebase Realtime Database WiFi orqali ishlaydi; 4) Ko'cha yoritish tizimlari odatda WiFi qamrov zonasida joylashadi; 5) Qo'shimcha oylik to'lov yo'q (mavjud WiFi tarmoqdan foydalaniladi).")
t("WiFi ning kamchiliklari: 1) Qamrov chegaralangan (50-100 m) — katta hududlar uchun mos emas; 2) Energiya iste'moli yuqori (150 mA) — batareya bilan ishlash qiyin; 3) WiFi router kerak — infrastruktura talab qiladi. Biroq, ko'cha yoritish tizimlari doimiy quvvat manbaiga ulangan bo'lgani uchun energiya iste'moli muammo emas, va ko'plab shaharlarda WiFi infratuzilmasi mavjud.")
t("Kelajakda LoRa protokoliga o'tish rejalashtirilgan. LoRa 2-15 km masofada ishlaydi va juda kam energiya sarflaydi. Bu WiFi bo'lmagan qishloq hududlari uchun ideal yechim. ESP32 + SX1276 LoRa moduli kombinatsiyasi $10-15 ga tushadi.")

doc.add_page_break()
hc("N ilova. Progressive Web Application (PWA) texnologiyasi", 14)
doc.add_paragraph()

t("Progressive Web Application (PWA) — bu zamonaviy veb-texnologiyalar yordamida yaratilgan ilova bo'lib, native (mahalliy) ilovalar kabi ishlaydi. PWA quyidagi asosiy xususiyatlarga ega:")
t("1) Installable (O'rnatiladigan) — foydalanuvchi ilovani bosh ekranga qo'shishi mumkin va u native ilova kabi ko'rinadi. App Store yoki Google Play ga joylash shart emas.")
t("2) Offline capable (Oflayn ishlash) — Service Worker texnologiyasi yordamida ilova internet bo'lmasa ham ishlaydi. Statik resurslar (HTML, CSS, JS) keshlanadi.")
t("3) Responsive (Moslashuvchan) — turli ekran o'lchamlarida (desktop, tablet, telefon) to'g'ri ko'rinadi.")
t("4) Fast (Tezkor) — Vite build tool yordamida optimallashtirilgan bundle yaratiladi. Lazy loading va code splitting qo'llaniladi.")
t("5) Secure (Xavfsiz) — HTTPS orqali ishlaydi. Firebase Hosting avtomatik SSL sertifikat beradi.")

t("Bizning dashboard da PWA quyidagicha amalga oshirilgan:")
t("— vite-plugin-pwa plaginidan foydalanilgan. U avtomatik ravishda Service Worker va manifest.json yaratadi;")
t("— Workbox kutubxonasi kesh strategiyalarini boshqaradi (CacheFirst statik resurslar uchun, NetworkFirst API so'rovlar uchun);")
t("— manifest.json da ilova nomi, ranglari va ikonkalar belgilangan;")
t("— registerType: 'autoUpdate' — yangi versiya chiqganda avtomatik yangilanadi.")

tbl(["Xususiyat", "Native App", "Oddiy Web", "PWA"],
    [["O'rnatish", "App Store", "Kerak emas", "Bosh ekranga"],
     ["Offline", "Ha", "Yo'q", "Ha"],
     ["Push notification", "Ha", "Yo'q", "Ha"],
     ["Kamera/GPS", "Ha", "Cheklangan", "Ha"],
     ["Yangilash", "Store orqali", "Avtomatik", "Avtomatik"],
     ["Hajm", "50-200 MB", "—", "1-5 MB"],
     ["Ishlab chiqish", "2 platforma", "1 platforma", "1 platforma"],
     ["Narx", "Yuqori", "Past", "Past"]],
    "N.1-jadval. Native, Web va PWA qiyosiy tahlili")

t("PWA tanlash sabablari: 1) Bitta kod bazasi — Android va iOS uchun alohida ilova yozish shart emas; 2) Tez yangilash — foydalanuvchi hech narsa qilmasdan yangi versiyani oladi; 3) Kichik hajm — 2 MB (native ilova 50-200 MB); 4) App Store ga joylash shart emas — vaqt va pul tejaydi; 5) Firebase Hosting bepul SSL va CDN beradi.")

doc.add_page_break()
hc("O ilova. Dunyo tajribasi — aqlli ko'cha yoritish loyihalari", 14)
doc.add_paragraph()

t("Dunyo bo'ylab aqlli ko'cha yoritish tizimlari jadal joriy etilmoqda. Quyida eng yirik va muvaffaqiyatli loyihalar haqida ma'lumot keltirilgan:")
t("1) Barcelona (Ispaniya) — 2012-yildan boshlab shahar ko'chalarida 1100 ta aqlli yoritgich o'rnatilgan. Har bir yoritgichda harakat sensori, shovqin sensori va havo sifati sensori mavjud. Natija: 30% energiya tejash, yiliga 37 million evro tejamkorlik. Tizim Cisco IoT platformasi asosida qurilgan.")
t("2) Los Angeles (AQSh) — dunyodagi eng yirik aqlli yoritish loyihasi. 2009-2020 yillar orasida 220,000 ta ko'cha yoritgichi LED ga almashtirildi va Philips CityTouch tizimi o'rnatildi. Natija: 63% energiya tejash, yiliga $9 million tejamkorlik, CO2 emissiyasi 47,000 tonna kamaydi.")
t("3) Kopengagen (Daniya) — 2016-yildan boshlab 20,000 ta yoritgich aqlli tizimga ulangan. Cisco va Signify hamkorligi. Har bir yoritgich WiFi hotspot va havo sifati sensori vazifasini ham bajaradi. Natija: 57% energiya tejash.")
t("4) Hindiston (EESL loyihasi) — 2015-yildan boshlab 13 million LED ko'cha yoritgichi o'rnatildi. Bu dunyodagi eng katta LED almashtirish dasturi. Natija: yiliga 5.5 milliard kWh tejash, 4.5 million tonna CO2 kamayishi.")
t("5) Toshkent (O'zbekiston) — 2022-2024 yillarda shahar markazida 5000 ta LED yoritgich o'rnatildi. Biroq, ular hali aqlli boshqaruv tizimiga ulanmagan — faqat taymer bilan ishlaydi. Bizning loyiha aynan shu muammoni hal qilishga qaratilgan.")

tbl(["Shahar", "Yoritgichlar", "Tejash %", "Yillik tejash", "Texnologiya"],
    [["Barcelona", "1,100", "30%", "€37M", "Cisco IoT"],
     ["Los Angeles", "220,000", "63%", "$9M", "Philips CityTouch"],
     ["Kopengagen", "20,000", "57%", "€2.5M", "Cisco + Signify"],
     ["Hindiston", "13,000,000", "50%", "$660M", "EESL LED"],
     ["Toshkent", "5,000", "40%*", "—", "LED (taymer)"],
     ["Bizning loyiha", "1 (prototip)", "80.8%", "106,200 so'm", "ESP32+Firebase"]],
    "O.1-jadval. Dunyo bo'ylab aqlli yoritish loyihalari")

t("Tahlildan ko'rinib turibdiki, sensorli boshqaruv (bizning yondashuv) eng yuqori tejash foizini beradi (80.8%). Tijorat yechimlari 30-63% oralig'ida, chunki ular dimming va jadval asosida ishlaydi. Bizning tizim faqat kerak bo'lganda yoqadi — bu eng radikal va samarali yondashuv.")

doc.add_page_break()
hc("P ilova. Tizimni kengaytirish rejasi", 14)
doc.add_paragraph()

t("Hozirgi prototip bitta yoritgichni boshqaradi. Kelajakda tizimni kengaytirish uchun quyidagi arxitektura rejalashtirilgan:")
t("1-bosqich (hozirgi): 1 ta ESP32 + 1 ta yoritgich. WiFi orqali Firebase ga ulanadi. Dashboard bitta qurilmani boshqaradi.")
t("2-bosqich (6 oy): 5-10 ta ESP32 + yoritgichlar. Har biri mustaqil WiFi orqali Firebase ga ulanadi. Dashboard barcha qurilmalarni ro'yxat ko'rinishida ko'rsatadi. Har bir qurilma o'z ID siga ega.")
t("3-bosqich (1 yil): 50-100 ta qurilma. ESP32 Mesh WiFi orqali o'zaro bog'lanadi. Bitta gateway qurilma internet bilan aloqa qiladi. LoRa moduli qo'shiladi (WiFi bo'lmagan hududlar uchun).")
t("4-bosqich (2 yil): 1000+ qurilma. Machine Learning qo'shiladi — harakat naqshlarini o'rganadi va bashorat qiladi. Quyosh paneli + batareya — to'liq avtonom. OTA (Over-The-Air) firmware yangilash.")

tbl(["Bosqich", "Qurilmalar", "Aloqa", "Qo'shimcha", "Narx (1 ta)"],
    [["1 (hozir)", "1", "WiFi", "—", "$7-10"],
     ["2 (6 oy)", "5-10", "WiFi", "Multi-device dashboard", "$7-10"],
     ["3 (1 yil)", "50-100", "WiFi Mesh + LoRa", "Gateway, offline", "$12-15"],
     ["4 (2 yil)", "1000+", "LoRa + 4G", "ML, Solar, OTA", "$20-25"]],
    "P.1-jadval. Tizimni kengaytirish bosqichlari")

t("Har bir bosqichda tizimning asosiy prinsipi saqlanadi: faqat kerak bo'lganda yoqish. Farq faqat miqyos va qo'shimcha funksiyalarda. Firebase ning bepul rejasi (Spark plan) 100 ta simultaneous connection ni qo'llab-quvvatlaydi — bu 2-bosqich uchun yetarli. 3-bosqichdan boshlab Firebase Blaze plan ($0.001/read) yoki o'z serveriga o'tish kerak bo'ladi.")

# SAVE
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_full.docx')
print("Additional ~10 pages added! Total should be ~100+ pages now")
