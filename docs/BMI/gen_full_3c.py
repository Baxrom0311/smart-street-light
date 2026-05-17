#!/usr/bin/env python3
"""I BOB - 1.3 Masalaning qo'yilishi"""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_full.docx')

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

h2("1.3. Masalaning qo'yilishi")

h3("1.3.1. Muammoning rasmiy ta'rifi")
t("Yuqorida keltirilgan tahlillar asosida quyidagi muammo aniqlanadi: an'anaviy ko'cha yoritish tizimlari tun bo'yi uzluksiz ishlaydi va energiyaning 60-80 foizi behuda sarflanadi. Mavjud tijorat yechimlari (Philips CityTouch, Telensa) yuqori narxga ega ($100-500 bitta yoritgich uchun) va kichik miqyosda qo'llash iqtisodiy jihatdan samarasiz. Akademik loyihalar esa masofadan boshqarish va monitoring imkoniyatiga ega emas.")
t("Shu sababli, quyidagi masala qo'yiladi: ESP32 mikrokontrolleri, RCWL-9610A ultratovush sensori va TEMT6000 yorug'lik sensori asosida arzon narxli, masofadan boshqariladigan, energiya tejamkor ko'cha yoritish tizimini ishlab chiqish zarur. Tizim real vaqt rejimida monitoring qilinishi va 60-80% energiya tejash ko'rsatkichiga erishishi kerak.")

h3("1.3.2. Funksional talablar")
t("Ishlab chiqiladigan tizim quyidagi funksional talablarga javob berishi kerak:")
t("1) Harakatni aniqlash — ultratovush sensori yordamida 2 metr masofagacha bo'lgan ob'ektlarni (piyodalar, transport vositalari) aniqlash. Aniqlash aniqligi ±1 cm, javob vaqti < 100 ms;")
t("2) Kunduz/tun farqlash — yorug'lik sensori yordamida avtomatik ravishda kunduz va tun holatini aniqlash. Kunduz kuni yoritgich umuman yonmasligi kerak;")
t("3) Avtomatik boshqarish — qorong'uda harakat aniqlanganda yoritgichni yoqish, harakat to'xtagandan 5 soniya keyin o'chirish;")
t("4) Masofadan boshqarish — veb-interfeys orqali yoritgichni qo'lda yoqish/o'chirish, rejimni o'zgartirish (Auto/Manual/Schedule);")
t("5) Real-time monitoring — sensor qiymatlari, yoritgich holati va statistikani jonli ko'rsatish;")
t("6) Energiya statistikasi — kunlik, haftalik va oylik energiya tejash ko'rsatkichlarini hisoblash va saqlash;")
t("7) Offline ishlash — internet bo'lmagan holda ham avtonom ishlash, aloqa tiklanganda sinxronizatsiya;")
t("8) WiFi konfiguratsiya — captive portal orqali WiFi ma'lumotlarini o'zgartirish imkoniyati.")

h3("1.3.3. Nofunksional talablar")
t("Tizim quyidagi nofunksional talablarga ham javob berishi kerak:")
t("— Ishonchlilik: tizim 24/7 uzluksiz ishlashi kerak, xotira oqishi (memory leak) bo'lmasligi kerak;")
t("— Javob vaqti: sensor o'qishdan relay yoqishgacha < 100 ms, dashboard buyrug'idan qurilma javobigacha < 500 ms;")
t("— Energiya samaradorligi: tizimning o'zi kam energiya iste'mol qilishi kerak (< 250 mA);")
t("— Xavfsizlik: Firebase Authentication orqali faqat vakolatli foydalanuvchilar boshqarishi mumkin;")
t("— Kengayuvchanlik: bir nechta yoritgichni bitta dashboard dan boshqarish imkoniyati;")
t("— Foydalanish qulayligi: oddiy va tushunarli interfeys, mobil qurilmalarda ham qulay ishlash.")

h3("1.3.4. Energiya tejash formulasi")
t("Tizimning energiya tejash samaradorligini baholash uchun quyidagi matematik model ishlab chiqildi:")
t("E_tejash = ((T_tun - T_yonish) / T_tun) × 100%")
t("bu yerda: E_tejash — energiya tejash foizi, T_tun — tun davomiyligi (soat), T_yonish — yoritgichning haqiqiy yonish vaqti (soat).")
t("Misol: T_tun = 12 soat, T_yonish = 2.5 soat bo'lsa: E_tejash = ((12 - 2.5) / 12) × 100% = 79.2%")
t("Kunlik energiya tejash (kWh): E_kunlik = P × (T_tun - T_yonish) / 1000, bu yerda P — yoritgich quvvati (Vt).")
t("Misol: P = 60W, T_tun = 12h, T_yonish = 2.5h: E_kunlik = 60 × 9.5 / 1000 = 0.57 kWh/kun = 17.1 kWh/oy = 208 kWh/yil")
t("Pul hisobida (500 so'm/kWh): 208 × 500 = 104,000 so'm/yil tejash bitta yoritgich uchun.")

h3("1.3.5. I Bob xulosasi")
t("Birinchi bobda ko'cha yoritish tizimlarining hozirgi holati tahlil qilindi, mavjud muammolar aniqlandi va ularni hal qilish yo'llari ko'rib chiqildi. Ultratovush sensorlarining ishlash prinsipi, fizik asoslari va texnik xususiyatlari batafsil o'rganildi. Mavjud tijorat va akademik yechimlar qiyosiy tahlil qilindi va ularning kamchiliklari aniqlandi. Natijada, ESP32 + RCWL-9610A + TEMT6000 + Firebase + React PWA asosida arzon, samarali va masofadan boshqariladigan energiya tejamkor yoritish tizimini ishlab chiqish masalasi qo'yildi. Keyingi bobda ushbu masalaning amaliy yechimi — tizimni loyihalash, dasturlash va sinov natijalari — batafsil bayon etiladi.")

doc.add_page_break()
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_full.docx')
print("1.3 done (~5 pages)")
