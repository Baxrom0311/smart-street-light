#!/usr/bin/env python3
"""I BOB - 1.2 section"""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_full.docx')
IMG = '/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/images/'

def h2(t):
    doc.add_paragraph()
    p = doc.add_paragraph(); r = p.add_run(t); r.bold = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'
def h3(t):
    p = doc.add_paragraph(); r = p.add_run(t); r.bold = True; r.italic = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'
def t(x):
    p = doc.add_paragraph(x); p.paragraph_format.first_line_indent = Cm(1.25)
    for r in p.runs: r.font.name = 'Times New Roman'; r.font.size = Pt(14)
def img(name, caption=""):
    if os.path.exists(IMG + name):
        doc.add_picture(IMG + name, width=Cm(14))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    if caption:
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(caption); r.font.size = Pt(12); r.italic = True; r.font.name = 'Times New Roman'
def tbl(headers, rows, caption=""):
    if caption: t(caption)
    tb = doc.add_table(rows=1+len(rows), cols=len(headers)); tb.style = 'Table Grid'
    for i, hd in enumerate(headers): tb.rows[0].cells[i].text = hd
    for ri, row in enumerate(rows):
        for ci, v in enumerate(row): tb.rows[ri+1].cells[ci].text = str(v)
    doc.add_paragraph()

# === 1.2 ===
h2("1.2. Ultratovush sensorlarning ishlash prinsipi va texnik xususiyatlari")

h3("1.2.1. Ultratovush to'lqinlarining fizik asoslari")
t("Ultratovush — bu chastotasi 20 kHz dan yuqori bo'lgan mexanik to'lqinlardir. Inson qulog'i 20 Hz dan 20 kHz gacha bo'lgan chastotadagi tovushlarni eshita oladi, ultratovush esa bu diapazondan tashqarida joylashgan. Ultratovush sensorlari odatda 40 kHz chastotada ishlaydi — bu chastota havoda yaxshi tarqaladi va qattiq jismlardan samarali aks etadi [15].")
t("Havoda ultratovush tezligi haroratga bog'liq bo'lib, quyidagi formula bilan aniqlanadi: v = 331.3 + 0.606 × T, bu yerda v — tovush tezligi (m/s), T — harorat (°C). 20°C haroratda tovush tezligi 343.4 m/s ga teng. Bu qiymat amaliy hisoblashlarda 343 m/s yoki 0.0343 cm/μs sifatida ishlatiladi. Haroratning ±10°C o'zgarishi tezlikni faqat ±2% ga o'zgartiradi, bu ko'cha yoritish uchun ahamiyatsiz xatolik hisoblanadi.")
t("Ultratovush to'lqinlarining asosiy xususiyatlari quyidagilardan iborat. Birinchidan, ular qattiq jismlardan (devorlar, odamlar, mashinalar) aks etadi — bu masofa o'lchash uchun asosiy prinsipdir. Ikkinchidan, ular ma'lum burchak ostida tarqaladi — RCWL-9610A uchun bu burchak ~30° bo'lib, bu ko'cha yoritish uchun yetarli qamrov beradi. Uchinchidan, ular ob-havo sharoitlariga (yomg'ir, tuman, qor) kam ta'sirchan — infraqizil sensorlardan farqli ravishda, ultratovush yomg'irda ham ishlaydi. To'rtinchidan, ular yorug'lik sharoitiga umuman bog'liq emas — tunda va kunduz bir xil ishlaydi.")

h3("1.2.2. Masofa o'lchash prinsipi (Time of Flight)")
t("Ultratovush sensori \"Time of Flight\" (ToF) — ya'ni \"uchish vaqti\" prinsipiga asoslanadi. Sensor ultratovush impulsini yuboradi, u ob'ektdan aks etib qaytadi va sensor qaytgan signalni qabul qiladi. Impulsning borish va qaytish vaqtini o'lchab, ob'ektgacha bo'lgan masofani hisoblash mumkin [16]:")
t("d = (t × v) / 2")
t("bu yerda: d — ob'ektgacha bo'lgan masofa (metr), t — to'lqinning borish va qaytish vaqti (soniya), v — havoda tovush tezligi (343 m/s). 2 ga bo'linadi, chunki to'lqin ikki marta yo'l bosadi — ob'ektgacha va qaytib.")
t("Amaliy misollar: Agar t = 580 μs bo'lsa: d = (580 × 0.0343) / 2 = 9.95 cm ≈ 10 cm. Agar t = 11600 μs bo'lsa: d = (11600 × 0.0343) / 2 = 198.9 cm ≈ 200 cm (2 metr). Bizning tizimimizda 200 cm (2 metr) chegara qiymati sifatida belgilangan — agar masofa 200 cm dan kam bo'lsa, harakat aniqlangan deb hisoblanadi.")
t("ESP32 dasturida bu hisoblash quyidagicha amalga oshiriladi: TRIG pinga 10 mikrosekundlik HIGH signal yuboriladi, sensor 8 ta 40 kHz impuls yuboradi, ECHO pin HIGH bo'ladi va ob'ektdan aks etgan signal qaytganda LOW ga tushadi. pulseIn() funksiyasi ECHO pinning HIGH bo'lgan vaqtini mikrosekundlarda qaytaradi. Keyin: distance_cm = duration * 0.034 / 2.")

img("diagram_sequence.png", "1.2-rasm. Ultratovush sensori yordamida masofa o'lchash jarayoni")

t("1.2-rasmda ultratovush sensori yordamida masofa o'lchash jarayonining ketma-ketlik diagrammasi tasvirlangan. ESP32 TRIG signalini yuboradi, sensor ultratovush impulsini chiqaradi, impuls ob'ektdan aks etadi va ECHO signal orqali vaqt o'lchanadi.")

h3("1.2.3. RCWL-9610A sensori texnik xususiyatlari va HC-SR04 bilan qiyoslash")
t("Loyiha uchun RCWL-9610A ultratovush sensori tanlandi. Bu sensor HC-SR04 ning zamonaviy va takomillashtirilgan versiyasi bo'lib, bir qator muhim afzalliklarga ega [17]:")

tbl(["Parametr", "RCWL-9610A", "HC-SR04"],
    [["Ish kuchlanishi", "3.0 - 5.5V", "5V (faqat)"],
     ["Ish toki", "< 2 mA", "15 mA"],
     ["O'lchash diapazoni", "2 - 450 cm", "2 - 400 cm"],
     ["O'lchash aniqligi", "±1 cm", "±3 mm"],
     ["Ishchi chastota", "40 kHz", "40 kHz"],
     ["Trigger signal", "10 μs HIGH", "10 μs HIGH"],
     ["O'lchash burchagi", "~30°", "~15°"],
     ["O'lcham", "21×15 mm", "45×20 mm"],
     ["3.3V mos", "Ha", "Yo'q (5V kerak)"],
     ["Narx", "~$1", "~$1.5"]],
    "1.4-jadval. RCWL-9610A va HC-SR04 qiyosiy tahlili")

t("RCWL-9610A tanlash sabablari: 1) 3.3V da ishlaydi — ESP32 ning logika darajasi 3.3V, shuning uchun qo'shimcha level shifter kerak emas; 2) Kam tok iste'mol qiladi (2 mA vs 15 mA) — energiya tejamkor tizim uchun muhim; 3) Keng burchak (30° vs 15°) — ko'cha yoritish uchun kattaroq qamrov beradi; 4) Kichik o'lcham — kompakt dizayn uchun qulay.")

h3("1.2.4. TEMT6000 yorug'lik sensori")
t("Tizimda kunduz/tun holatini aniqlash uchun TEMT6000 ambient light sensori ishlatiladi. Bu sensor Vishay kompaniyasi tomonidan ishlab chiqilgan bo'lib, inson ko'zining spektral sezgirligiga yaqin xususiyatga ega [18]. Sensor fototransistor asosida ishlaydi va yorug'lik intensivligiga proporsional analog signal chiqaradi.")

tbl(["Parametr", "Qiymat", "Izoh"],
    [["Ish kuchlanishi", "3.3 - 5V", "ESP32 bilan mos"],
     ["Chiqish signali", "Analog (0 - VCC)", "ADC bilan o'qiladi"],
     ["Spektral diapazoni", "360 - 970 nm", "Ko'rinadigan yorug'lik"],
     ["Maksimal sezgirlik", "570 nm", "Yashil rang"],
     ["Ko'rish burchagi", "±60°", "Keng qamrov"],
     ["Javob vaqti", "< 1 ms", "Tezkor"],
     ["Ish harorati", "-40°C dan +85°C", "Tashqi muhit uchun mos"]],
    "1.5-jadval. TEMT6000 texnik xususiyatlari")

t("ESP32 ning 12-bitli ADC (Analog-to-Digital Converter) yordamida sensor signali 0-4095 oralig'idagi raqamli qiymatga o'giriladi. Bizning tizimimizda quyidagi chegaralar belgilangan: 0-250: qorong'u (tun) — yoritgich yonishi kerak; 250-350: oraliq zona (hysteresis) — holat o'zgarmaydi; 350+: yorug' (kunduz) — yoritgich o'chiq bo'lishi kerak. Hysteresis mexanizmi yorug'lik chegarasida tebranishni bartaraf etadi — masalan, bulut ortidan quyosh chiqib-yashirinayotganda yoritgich tez-tez yonib-o'chmasligini ta'minlaydi.")

h3("1.2.5. Harakatni aniqlash algoritmi va shovqinni filtrlash")
t("Ultratovush sensorlari ba'zan noto'g'ri natijalar berishi mumkin — bu shovqin (noise) deb ataladi. Shovqin sabablari: havo oqimi, harorat o'zgarishi, sensorning o'zi chiqargan signalning ichki aks etishi, yaqin atrofdagi boshqa ultratovush manbalari. Shovqinni bartaraf etish uchun maxsus algoritmlar ishlab chiqildi [19]:")
t("1) Debounce (tebranishni bartaraf etish) — 3 ta ketma-ket o'lchov olinadi, kamida 2 tasi harakat ko'rsatsa — harakat aniqlangan deb hisoblanadi. Bu bitta noto'g'ri o'lchovning ta'sirini yo'q qiladi. Masalan, agar 3 ta o'lchov [150cm, 450cm, 120cm] bo'lsa — 2 tasi 200cm dan kam, demak harakat bor.")
t("2) Hold timer (ushlab turish) — oxirgi harakatdan 5 soniya o'tmagan bo'lsa, 'harakat bor' holati saqlanadi. Bu yoritgichning tez-tez yonib-o'chishini oldini oladi. Masalan, odam sekin yursa va sensor uni har doim aniqlay olmasa ham, 5 soniya ichida yoritgich o'chmaydi.")
t("3) Hysteresis (gisterezis) — yorug'lik sensori uchun ikki chegarali tizim: Light < 250 → qorong'u, Light > 350 → yorug'. 250-350 orasida holat o'zgarmaydi. Bu bulutli ob-havoda yoritgichning beqaror ishlashini oldini oladi.")

img("diagram_flowchart.png", "1.3-rasm. Harakatni aniqlash va yoritgichni boshqarish algoritmining blok-sxemasi")

t("1.3-rasmda tizimning asosiy ishlash algoritmi tasvirlangan. Algoritm avval yorug'lik darajasini tekshiradi — agar kunduz bo'lsa, yoritgich o'chiq qoladi. Agar tun bo'lsa, harakat sensorini tekshiradi — harakat aniqlansa yoritgich yonadi, aks holda 5 soniya kutib o'chiradi.")

doc.add_page_break()
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_full.docx')
print("1.2 done (~10 pages)")
