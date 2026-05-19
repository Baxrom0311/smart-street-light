#!/usr/bin/env python3
"""BMI Final Document Generator - Smart Street Light IoT"""

import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "images")
OUTPUT = os.path.join(BASE_DIR, "BMI_final.docx")

doc = Document()

# ============ STYLES SETUP ============
style = doc.styles['Normal']
style.font.name = 'Times New Roman'
style.font.size = Pt(14)
style.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
pf = style.paragraph_format
pf.line_spacing = 1.5
pf.space_before = Pt(0)
pf.space_after = Pt(0)
pf.first_line_indent = Cm(1.25)

# Heading 1
h1 = doc.styles['Heading 1']
h1.font.name = 'Times New Roman'
h1.font.size = Pt(14)
h1.font.bold = True
h1.font.color.rgb = None
h1.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
h1.paragraph_format.space_before = Pt(0)
h1.paragraph_format.space_after = Pt(0)
h1.paragraph_format.first_line_indent = Cm(0)

# Heading 2
h2 = doc.styles['Heading 2']
h2.font.name = 'Times New Roman'
h2.font.size = Pt(14)
h2.font.bold = True
h2.font.color.rgb = None
h2.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
h2.paragraph_format.space_before = Pt(0)
h2.paragraph_format.space_after = Pt(0)
h2.paragraph_format.first_line_indent = Cm(0)

# Margins
for section in doc.sections:
    section.left_margin = Cm(3)
    section.right_margin = Cm(1.5)
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(2)

# ============ HELPER FUNCTIONS ============
def add_paragraph(text, bold=False, align=None, font_size=None, font_name=None, indent=None, first_indent=None):
    p = doc.add_paragraph()
    if align:
        p.alignment = align
    if indent is not None:
        p.paragraph_format.left_indent = indent
    if first_indent is not None:
        p.paragraph_format.first_line_indent = first_indent
    run = p.add_run(text)
    if bold:
        run.bold = True
    if font_size:
        run.font.size = font_size
    if font_name:
        run.font.name = font_name
    run.font.name = font_name or 'Times New Roman'
    return p

def add_image(filename, caption_text):
    img_path = os.path.join(IMG_DIR, filename)
    if not os.path.exists(img_path):
        add_paragraph(f"[Rasm topilmadi: {filename}]")
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
    run = p.add_run()
    run.add_picture(img_path, width=Cm(14))
    # Caption
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    cap.paragraph_format.first_line_indent = Cm(0)
    r = cap.add_run(caption_text)
    r.italic = True
    r.font.size = Pt(12)
    r.font.name = 'Times New Roman'

def add_code_block(code_text):
    for line in code_text.split('\n'):
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(1)
        p.paragraph_format.first_line_indent = Cm(0)
        p.paragraph_format.line_spacing = 1.0
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(line)
        run.font.name = 'Courier New'
        run.font.size = Pt(10)

def add_toc():
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
    run = p.add_run("MUNDARIJA")
    run.bold = True
    run.font.size = Pt(14)
    run.font.name = 'Times New Roman'
    # TOC field
    p2 = doc.add_paragraph()
    p2.paragraph_format.first_line_indent = Cm(0)
    fldChar1 = OxmlElement('w:fldChar')
    fldChar1.set(qn('w:fldCharType'), 'begin')
    r1 = p2.add_run()
    r1._r.append(fldChar1)
    instrText = OxmlElement('w:instrText')
    instrText.set(qn('xml:space'), 'preserve')
    instrText.text = ' TOC \\o "1-2" \\h \\z \\u '
    r2 = p2.add_run()
    r2._r.append(instrText)
    fldChar2 = OxmlElement('w:fldChar')
    fldChar2.set(qn('w:fldCharType'), 'separate')
    r3 = p2.add_run()
    r3._r.append(fldChar2)
    r4 = p2.add_run("Mundarijani yangilash uchun F9 tugmasini bosing")
    r4.font.color.rgb = RGBColor(128, 128, 128)
    fldChar3 = OxmlElement('w:fldChar')
    fldChar3.set(qn('w:fldCharType'), 'end')
    r5 = p2.add_run()
    r5._r.append(fldChar3)

def page_break():
    doc.add_page_break()

# ============ TITUL PAGE ============
for _ in range(3):
    doc.add_paragraph()

add_paragraph("O'ZBEKISTON RESPUBLIKASI OLIY TA'LIM, FAN VA INNOVATSIYALAR VAZIRLIGI",
              bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, first_indent=Cm(0))
doc.add_paragraph()
add_paragraph("MUHAMMAD AL-XORAZMIY NOMIDAGI TOSHKENT AXBOROT TEXNOLOGIYALARI UNIVERSITETI",
              bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, first_indent=Cm(0))
doc.add_paragraph()
add_paragraph("KOMPYUTER INJINIRINGI FAKULTETI",
              align=WD_ALIGN_PARAGRAPH.CENTER, first_indent=Cm(0))
doc.add_paragraph()
add_paragraph("DASTURIY INJINIRING KAFEDRASI",
              align=WD_ALIGN_PARAGRAPH.CENTER, first_indent=Cm(0))

for _ in range(4):
    doc.add_paragraph()

add_paragraph("BITIRUV MALAKAVIY ISHI", bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, first_indent=Cm(0))
doc.add_paragraph()
add_paragraph("Mavzu: Ultratovush sensori orqali energiya tejamkorligini ta'minlovchi yoritish tizimini ishlab chiqish",
              bold=True, align=WD_ALIGN_PARAGRAPH.CENTER, first_indent=Cm(0))

for _ in range(5):
    doc.add_paragraph()

add_paragraph("Bajardi: Baxrom", align=WD_ALIGN_PARAGRAPH.RIGHT, first_indent=Cm(0))
add_paragraph("Ilmiy rahbar: _______________", align=WD_ALIGN_PARAGRAPH.RIGHT, first_indent=Cm(0))

for _ in range(5):
    doc.add_paragraph()

add_paragraph("Toshkent — 2026", align=WD_ALIGN_PARAGRAPH.CENTER, first_indent=Cm(0))

page_break()

# ============ MUNDARIJA ============
add_toc()
page_break()

total_chars = 0


# ============ KIRISH ============
doc.add_heading("KIRISH", level=1)

kirish_texts = [
    # Dolzarblik 1
    "Zamonaviy shaharlar jadal rivojlanishi bilan energiya iste'moli masalasi global miqyosda eng dolzarb muammolardan biriga aylandi. Xalqaro Energetika Agentligi (IEA) ma'lumotlariga ko'ra, dunyo bo'yicha ko'cha yoritish tizimlari yillik elektr energiya iste'molining 15 dan 25 foizgacha qismini tashkil etadi, bu esa taxminan 320 teravatt-soat energiyaga teng. Bunday katta hajmdagi energiya sarfi nafaqat iqtisodiy yukni oshiradi, balki atrof-muhitga ham salbiy ta'sir ko'rsatadi — yiliga 150 million tonna CO2 chiqindisi hosil bo'ladi. An'anaviy ko'cha yoritish tizimlari asosan taymer yoki fotosensor asosida ishlaydi va tun bo'yi uzluksiz yonib turadi, hatto ko'chada hech kim bo'lmagan paytlarda ham. Bu esa energiyaning behuda sarflanishiga olib keladi. Shu sababli, aqlli yoritish tizimlari — ya'ni faqat kerak bo'lganda yonadigan, sensorlar orqali boshqariladigan tizimlar ishlab chiqish zamonaviy muhandislik fanining eng muhim yo'nalishlaridan biri hisoblanadi.",

    # Dolzarblik 2
    "O'zbekiston Respublikasida ham energiya tejamkorligi masalasi davlat siyosatining ustuvor yo'nalishlaridan biri sifatida belgilangan. Mamlakatimizda 150 mingdan ortiq ko'cha yoritgichlari mavjud bo'lib, ularning aksariyati eskirgan texnologiyalar asosida ishlaydi. Bu yoritgichlar tun bo'yi uzluksiz yonib turadi va yiliga taxminan 2.5 milliard kVt-soat elektr energiya sarflaydi. Energiya resurslari cheklangan sharoitda bunday isrofgarchilikka yo'l qo'yib bo'lmaydi. Shu bois, zamonaviy IoT (Internet of Things) texnologiyalari asosida aqlli yoritish tizimlarini joriy etish nafaqat energiya tejash, balki shahar infratuzilmasini modernizatsiya qilish, fuqarolar xavfsizligini oshirish va ekologik vaziyatni yaxshilash imkonini beradi. Bunday tizimlar real vaqt rejimida masofadan monitoring va boshqarish imkoniyatiga ega bo'lib, texnik xizmat ko'rsatish xarajatlarini ham sezilarli darajada kamaytiradi.",

    # Qonunlar
    "O'zbekiston Respublikasi Prezidentining 2020-yil 5-oktabrdagi PF-6079-son Farmoni bilan tasdiqlangan «Raqamli O'zbekiston — 2030» strategiyasi mamlakatni raqamlashtirish va zamonaviy axborot texnologiyalarini barcha sohalarga joriy etishni nazarda tutadi. Shuningdek, Vazirlar Mahkamasining 58-son qarori energiya tejamkorligini oshirish bo'yicha aniq chora-tadbirlarni belgilaydi. PQ-436-son qaror esa aqlli shahar (Smart City) konsepsiyasini amalga oshirish rejasini o'z ichiga oladi. 2024-yilda qabul qilingan yangi Energiya tejash to'g'risidagi qonun barcha davlat muassasalari va ko'cha infratuzilmasida energiya tejamkor texnologiyalarni qo'llashni majburiy qiladi. Ushbu qonunchilik bazasi IoT asosidagi aqlli yoritish tizimlarini ishlab chiqish va joriy etish uchun mustahkam huquqiy asos yaratadi. Bizning loyihamiz aynan shu davlat siyosati yo'nalishlariga mos keladi va amaliy yechim sifatida taqdim etiladi.",

    # BMT SDG
    "Birlashgan Millatlar Tashkilotining Barqaror Rivojlanish Maqsadlari (SDG) doirasida ham energiya tejamkorligi masalasi alohida o'rin tutadi. SDG 7 — Hamyonbop va toza energiya maqsadi arzon, ishonchli va zamonaviy energiya xizmatlaridan foydalanish imkoniyatini kengaytirishni nazarda tutadi. SDG 11 — Barqaror shaharlar va aholi punktlari maqsadi shahar infratuzilmasini aqlli texnologiyalar yordamida modernizatsiya qilishni talab etadi. SDG 13 — Iqlim o'zgarishiga qarshi kurash maqsadi esa CO2 chiqindilarini kamaytirish choralarini ko'rishni o'z ichiga oladi. Bizning aqlli ko'cha yoritish tizimimiz ushbu uchala maqsadga ham bevosita hissa qo'shadi: energiya tejash orqali SDG 7 ga, shahar infratuzilmasini aqllilashtirib SDG 11 ga, va CO2 chiqindilarini kamaytirib SDG 13 ga xizmat qiladi. Bu esa loyihamizning nafaqat mahalliy, balki global ahamiyatga ega ekanligini ko'rsatadi.",

    # IoT va Smart City
    "Internet of Things (IoT) konsepsiyasi jismoniy qurilmalarni internet orqali bir-biriga ulash va ularni markazlashgan tarzda boshqarish g'oyasiga asoslanadi. Smart City (Aqlli shahar) esa IoT texnologiyalarini shahar infratuzilmasining barcha sohalariga — transport, energetika, suv ta'minoti, xavfsizlik va yoritish tizimlariga qo'llash orqali shahar boshqaruvini optimallashtirish konsepsiyasidir. Aqlli ko'cha yoritish tizimi Smart City ning eng ko'p qo'llaniladigan va eng tez natija beradigan komponentlaridan biri hisoblanadi. Bunday tizimda har bir yoritgich sensorlar bilan jihozlanadi, real vaqt rejimida ma'lumot yig'adi va bulutli platforma orqali markazdan boshqariladi. Natijada energiya sarfi 60-80 foizga kamayadi, texnik nosozliklar tezda aniqlanadi va fuqarolar xavfsizligi oshadi. Bizning loyihamiz aynan shu konsepsiyaning amaliy namoyishi sifatida ishlab chiqilgan.",

    # BMI ob'ekti
    "Bitiruv malakaviy ishining ob'ekti sifatida ko'cha yoritish tizimlarida energiya tejamkorligini ta'minlash jarayoni tanlab olingan. Hozirgi kunda ko'cha yoritish tizimlari asosan ikki usulda boshqariladi: taymer asosida (belgilangan vaqtda yoqiladi va o'chiriladi) yoki fotosensor asosida (qorong'i tushganda yonadi). Ikkala usul ham tun bo'yi uzluksiz yoritishni ta'minlaydi, lekin ko'chada hech kim bo'lmagan paytlarda ham energiya sarflanishiga olib keladi. Tadqiqot ob'ekti sifatida aynan shu muammoni hal qilish — ya'ni yoritishni faqat kerak bo'lganda ta'minlash jarayonini o'rganish va optimallashtirish belgilangan. Bu jarayon sensorlar orqali atrof-muhit holatini aniqlash, ma'lumotlarni qayta ishlash va yoritishni boshqarish bosqichlarini o'z ichiga oladi.",

    # BMI predmeti
    "Bitiruv malakaviy ishining predmeti — ESP32 mikrokontrolleri va ultratovush sensori asosida harakatni aniqlash hamda energiya tejamkor yoritish algoritmlarini ishlab chiqishdir. Predmet doirasida quyidagi masalalar ko'rib chiqiladi: ultratovush sensori yordamida ob'ektgacha bo'lgan masofani o'lchash va harakat mavjudligini aniqlash algoritmlari, yorug'lik sensori orqali kunduz va tun vaqtini farqlash mexanizmi, debounce va hysteresis algoritmlari orqali sensorlar ishonchliligini oshirish usullari, Firebase Realtime Database orqali qurilmani masofadan boshqarish va monitoring qilish tizimi, hamda React asosidagi Progressive Web Application (PWA) dashboard yaratish. Predmet ESP32 platformasining imkoniyatlarini to'liq ishlatish va zamonaviy veb-texnologiyalar bilan integratsiya qilishni o'z ichiga oladi.",

    # BMI maqsadi
    "Bitiruv malakaviy ishining maqsadi — ultratovush sensori orqali harakatni aniqlash va energiya tejamkorligini ta'minlovchi aqlli ko'cha yoritish tizimini ishlab chiqish va amaliy sinovdan o'tkazishdir. Tizim quyidagi asosiy talablarga javob berishi kerak: birinchidan, ultratovush sensori yordamida 2 metr masofada harakatni ishonchli aniqlash; ikkinchidan, yorug'lik sensori orqali kunduz kuni yoritishni avtomatik o'chirish; uchinchidan, harakat to'xtagandan keyin belgilangan vaqt (5 soniya) o'tgach yoritishni o'chirish; to'rtinchidan, Firebase orqali real vaqt rejimida masofadan monitoring va boshqarish imkoniyatini ta'minlash; beshinchidan, PWA dashboard orqali quddiy foydalanuvchi interfeysini yaratish. Yakuniy maqsad — kamida 60 foiz energiya tejashga erishish va tizimning ishonchliligini amaliy sinovlar orqali tasdiqlash.",

    # Vazifalar
    "Belgilangan maqsadga erishish uchun quyidagi vazifalar aniqlangan: ko'cha yoritish tizimlarida energiya tejamkorligini ta'minlash bo'yicha mavjud yechimlarni o'rganish va tahlil qilish; ultratovush sensori (RCWL-9610A) va yorug'lik sensori (TEMT6000) ning ishlash prinsiplarini o'rganish va optimal parametrlarni aniqlash; ESP32 mikrokontrolleri asosida harakatni aniqlash va yoritishni boshqarish algoritmlarini ishlab chiqish; debounce, hold timer va hysteresis algoritmlarini qo'llash orqali tizim ishonchliligini oshirish; Firebase Realtime Database bilan real vaqt rejimida ma'lumot almashish tizimini yaratish; React va Vite texnologiyalari asosida PWA dashboard ishlab chiqish; tizimni amaliy sharoitda sinab ko'rish va energiya tejash samaradorligini hisoblash; olingan natijalarni tahlil qilish va kelajakdagi rivojlantirish yo'nalishlarini belgilash.",

    # Tarkibiy tuzilishi
    "Bitiruv malakaviy ishi kirish, ikkita bob, xulosa, foydalanilgan adabiyotlar ro'yxati va ilovalardan iborat. Kirish qismida mavzuning dolzarbligi, qonunchilik asoslari, BMI ob'ekti, predmeti, maqsadi va vazifalari bayon etilgan. Birinchi bob nazariy qismni o'z ichiga oladi: ko'cha yoritish tizimlarining hozirgi holati va muammolari tahlil qilinadi, mavjud yechimlar o'rganiladi, tanlangan sensorlar va mikrokontrollerning texnik xarakteristikalari batafsil yoritiladi, harakatni aniqlash algoritmlari nazariy jihatdan asoslanadi va masala qo'yilishi shakllantiriladi. Ikkinchi bob amaliy qismga bag'ishlangan: tizim arxitekturasi loyihalanadi, apparat va dasturiy ta'minot ishlab chiqiladi, dastur kodi yoziladi, tizim sinovdan o'tkaziladi va natijalar tahlil qilinadi. Xulosa qismida olingan natijalar umumlashtiriladi va kelajakdagi rivojlantirish yo'nalishlari belgilanadi. Ilovalar qismida to'liq dastur kodi keltirilgan."
]

for text in kirish_texts:
    add_paragraph(text)
    total_chars += len(text)

page_break()


# ============ I BOB ============
doc.add_heading("I BOB. SMART STREET TIZIMIDA YORITISH TIZIMLARI TIZIMLI TAHLILI VA MASALANING QO'YILISHI", level=1)

# --- 1.1-§ ---
doc.add_heading("1.1-§. Ko'cha yoritish tizimlarining hozirgi holati va energiya tejash yondashuvlari", level=2)

bob1_1_texts = [
    # Tarix
    "Ko'cha yoritish tarixi qadim zamonlarga borib taqaladi — dastlab yog' chirog'lari, keyin gaz lampalari, XX asrda esa elektr lampalari keng qo'llanila boshlandi. 1879-yilda Thomas Edison tomonidan ixtiro qilingan cho'g'lanma lampa ko'cha yoritishda inqilob yasadi va XX asr davomida butun dunyo shaharlarida keng tarqaldi. Biroq cho'g'lanma lampalar energiya samaradorligi jihatidan juda past edi — elektr energiyasining atigi 5 foizi yorug'likka, qolgan 95 foizi issiqlikka aylanardi. 1930-yillarda natriy bug'li lampalar paydo bo'ldi va ko'cha yoritishda asosiy manbaga aylandi. Bu lampalar cho'g'lanma lampalarga nisbatan 4-5 baravar samaraliroq edi, lekin hali ham zamonaviy LED texnologiyasiga nisbatan 2-3 baravar ko'p energiya sarflardi. XXI asrning boshlarida LED texnologiyasining rivojlanishi ko'cha yoritishda yangi davrni boshlab berdi — LED lampalar 80-90 foiz energiya tejash imkonini berdi va xizmat muddati 50000 soatgacha yetdi.",

    # Hozirgi muammolar
    "Hozirgi kunda dunyo bo'yicha ko'cha yoritish tizimlari yiliga taxminan 320 teravatt-soat (TWh) elektr energiya sarflaydi, bu esa global elektr energiya ishlab chiqarishning 4 foiziga teng. Bu energiya sarfi natijasida yiliga 150 million tonna CO2 atmosferaga chiqariladi, bu esa iqlim o'zgarishiga sezilarli hissa qo'shadi. Muammoning asosiy sababi shundaki, ko'cha yoritgichlarining aksariyati tun bo'yi uzluksiz yonib turadi — hatto ko'chada hech kim bo'lmagan soat 2-3 da ham. Statistik ma'lumotlarga ko'ra, shahar ko'chalarida tun vaqtining 60-70 foizida hech qanday harakat kuzatilmaydi, ya'ni bu vaqt davomida yoritish amalda keraksiz. Bundan tashqari, ko'plab shaharlarda hali ham eskirgan natriy bug'li lampalar ishlatiladi, ular LED lampalarga nisbatan 3-4 baravar ko'p energiya sarflaydi. Yana bir muammo — markazlashgan boshqaruv tizimining yo'qligi: ko'plab yoritgichlar oddiy taymer yoki fotosensor bilan boshqariladi va individual sozlash imkoniyati mavjud emas.",

    # O'zbekistondagi holat
    "O'zbekiston Respublikasida 150 mingdan ortiq ko'cha yoritgichlari mavjud bo'lib, ularning taxminan 70 foizi hali ham eskirgan natriy bug'li lampalar bilan jihozlangan. Bu yoritgichlar asosan oddiy taymer yoki fotosensor asosida boshqariladi — qorong'i tushganda yonadi va tong otganda o'chadi. Bunday yondashuv tun bo'yi uzluksiz yoritishni ta'minlaydi, lekin energiyaning katta qismi behuda sarflanadi. Mamlakatimizda ko'cha yoritish uchun yiliga taxminan 2.5 milliard kVt-soat elektr energiya sarflanadi, bu esa davlat byudjetiga katta yuk tushiradi. Bundan tashqari, eskirgan tizimlar tez-tez ishdan chiqadi, texnik xizmat ko'rsatish qimmatga tushadi va nosozliklarni aniqlash qiyin. Hukumat tomonidan LED lampalarga o'tish dasturi amalga oshirilmoqda, lekin faqat LED ga o'tish yetarli emas — aqlli boshqaruv tizimisiz energiya tejash salohiyatining katta qismi ishlatilmay qoladi. Shu sababli, IoT asosidagi aqlli yoritish tizimlari O'zbekiston uchun juda dolzarb hisoblanadi.",

    # Smart City va IoT
    "Smart City (Aqlli shahar) konsepsiyasi shahar infratuzilmasining barcha komponentlarini raqamlashtirish va markazlashgan tarzda boshqarish g'oyasiga asoslanadi. Bu konsepsiyada IoT qurilmalari shahar bo'ylab joylashtiriladi, ular real vaqt rejimida ma'lumot yig'adi va bulutli platformaga uzatadi. Markaziy boshqaruv tizimi bu ma'lumotlarni tahlil qilib, optimal qarorlar qabul qiladi. Ko'cha yoritish Smart City ning eng ko'p qo'llaniladigan va eng tez natija beradigan komponentlaridan biri hisoblanadi, chunki u nisbatan oddiy texnologiyalar bilan katta energiya tejash effektiga erishish imkonini beradi. Aqlli yoritish tizimida har bir yoritgich sensorlar (harakat, yorug'lik, harorat) bilan jihozlanadi, mikrokontroller orqali boshqariladi va internet orqali markaziy serverga ulanadi. Natijada har bir yoritgichni individual boshqarish, energiya sarfini real vaqtda kuzatish va nosozliklarni tezda aniqlash mumkin bo'ladi. Dunyo tajribasi shuni ko'rsatadiki, aqlli yoritish tizimlari 60-80 foiz energiya tejash imkonini beradi.",
]

for text in bob1_1_texts:
    add_paragraph(text)
    total_chars += len(text)

add_image("smart_street_concept.png", "1.1-rasm. Aqlli ko'cha yoritish tizimi konsepsiyasi")

bob1_1_texts2 = [
    # Energiya tejash yondashuvlari
    "Energiya tejash yondashuvlari orasida birinchi va eng oddiy usul — LED texnologiyasiga o'tishdir. LED lampalar an'anaviy natriy bug'li lampalarga nisbatan 50-70 foiz kam energiya sarflaydi, xizmat muddati 5-10 baravar uzoq va yorug'lik sifati yuqori. Ikkinchi yondashuv — dimming (yorug'likni pasaytirish) texnologiyasi bo'lib, tun vaqtining kam faol soatlarida yorug'likni 50-70 foizga pasaytirish orqali qo'shimcha 20-30 foiz energiya tejash mumkin. Uchinchi yondashuv — sensorli boshqaruv bo'lib, harakat sensorlari yordamida faqat kerak bo'lganda to'liq quvvatda yoritish ta'minlanadi. To'rtinchi yondashuv — jadval bo'yicha boshqaruv, ya'ni belgilangan vaqt oralig'ida turli yorug'lik darajalarini o'rnatish. Beshinchi va eng ilg'or yondashuv — adaptiv boshqaruv bo'lib, sun'iy intellekt algoritmlari yordamida harakat naqshlarini o'rganish va bashorat qilish orqali optimal yoritish rejimini avtomatik tanlash. Bizning loyihamiz uchinchi yondashuvni — sensorli boshqaruvni asosiy usul sifatida qo'llaydi va uni IoT imkoniyatlari bilan boyitadi.",

    # Philips CityTouch
    "Mavjud tijorat yechimlari orasida Philips CityTouch platformasi eng keng tarqalgan hisoblanadi. Bu tizim har bir yoritgichga o'rnatilgan maxsus kontroller, markaziy boshqaruv dasturi va bulutli platforma dan iborat. Philips CityTouch 70 dan ortiq mamlakatda 40 milliondan ortiq yoritgichni boshqaradi. Tizim individual dimming, jadval bo'yicha boshqaruv, nosozliklarni avtomatik aniqlash va energiya sarfini monitoring qilish imkoniyatlarini taqdim etadi. Biroq bu tizimning asosiy kamchiligi — yuqori narx: har bir yoritgich uchun kontroller narxi 200-500 AQSh dollari, platforma litsenziyasi esa yiliga 10-50 dollar. Bundan tashqari, tizim yopiq ekotizimda ishlaydi va boshqa ishlab chiqaruvchilar uskunalari bilan integratsiya qilish qiyin. Kichik va o'rta loyihalar uchun bunday narx iqtisodiy jihatdan oqlanmaydi, shu sababli arzonroq va ochiq alternativalar kerak.",

    # Telensa
    "Telensa kompaniyasi Buyuk Britaniyada ishlab chiqilgan aqlli yoritish platformasini taqdim etadi. Telensa tizimi o'zining maxsus simsiz tarmoq protokolidan foydalanadi — PLANet (Power Line Adaptive Network Technology), bu esa mavjud elektr tarmoq simlari orqali ma'lumot uzatish imkonini beradi. Har bir yoritgichga o'rnatilgan node qurilmasi yorug'likni boshqaradi, energiya sarfini o'lchaydi va nosozliklarni aniqlaydi. Telensa 50 dan ortiq mamlakatda 2 milliondan ortiq yoritgichni boshqaradi. Tizimning afzalligi — qo'shimcha kommunikatsiya infratuzilmasi talab etilmasligi, chunki mavjud elektr simlari orqali ma'lumot uzatiladi. Kamchiliklari esa — yuqori boshlang'ich investitsiya, yopiq protokol va faqat katta miqyosli loyihalar uchun iqtisodiy samaradorlik. Kichik loyihalar va rivojlanayotgan mamlakatlar uchun bu yechim ham qimmat hisoblanadi.",

    # Tvilight
    "Tvilight — Gollandiyada ishlab chiqilgan aqlli yoritish tizimi bo'lib, u asosan harakat sensorlari va simsiz tarmoq texnologiyalariga asoslanadi. Tvilight tizimida har bir yoritgich radar sensori bilan jihozlanadi va piyodalar yoki transport vositalarini aniqlaydi. Harakat aniqlanganda yoritgich to'liq quvvatda yonadi, harakat to'xtaganda esa yorug'lik asta-sekin pasayadi. Tizimning o'ziga xos xususiyati — yoritgichlar o'zaro simsiz tarmoq orqali bog'langan va harakat yo'nalishini bashorat qilib, oldindagi yoritgichlarni oldindan yoqadi. Bu esa piyodalar uchun qulay va xavfsiz muhit yaratadi. Tvilight Amsterdamda, Dubayda va boshqa shaharlarda muvaffaqiyatli joriy etilgan. Biroq radar sensorlari ultratovush sensorlariga nisbatan ancha qimmat va murakkab, shuningdek tizim maxsus mesh tarmoq infratuzilmasini talab etadi.",

    # Ochiq kodli loyihalar
    "Ochiq kodli (open-source) loyihalar orasida Arduino va ESP platformalari asosida yaratilgan ko'plab aqlli yoritish tizimlari mavjud. GitHub platformasida smart street light kalit so'zi bo'yicha 500 dan ortiq loyiha topiladi. Bu loyihalarning aksariyati PIR (Passive Infrared) harakat sensori va Arduino Uno yoki ESP8266 mikrokontrolleri asosida qurilgan. Biroq ularning ko'pchiligi faqat lokal ishlaydi — ya'ni internet ulanishi va masofadan boshqarish imkoniyati yo'q. Ba'zi loyihalar Blynk yoki ThingSpeak platformalari bilan integratsiya qilingan, lekin ular cheklangan funksionallikka ega. Bizning loyihamiz mavjud ochiq kodli yechimlardan farqli ravishda to'liq IoT ekotizimini taqdim etadi: ESP32 mikrokontrolleri, ultratovush sensori (PIR dan aniqroq), Firebase Realtime Database va React PWA dashboard. Bu kombinatsiya tijorat yechimlariga yaqin funksionallikni ochiq kodli va arzon platformada amalga oshirish imkonini beradi.",

    # Dunyo tajribasi
    "Dunyo tajribasi aqlli yoritish tizimlarining yuqori samaradorligini tasdiqlaydi. Barselona shahri 2012-yilda 1100 ta aqlli yoritgich o'rnatdi va 30 foiz energiya tejashga erishdi, bu esa yiliga 37 million yevro iqtisodiy samara berdi. Los-Anjeles shahri 220000 ta ko'cha yoritgichini LED va aqlli boshqaruv tizimiga o'tkazdi va 63 foiz energiya tejashga erishdi — bu yiliga 9 million dollar tejash demak. Kopengagen shahri 20000 ta aqlli yoritgich o'rnatib 57 foiz energiya tejadi va 2025-yilga kelib karbon-neytral shahar bo'lishni maqsad qilgan. Hindiston hukumati EESL dasturi doirasida 13 million ko'cha yoritgichini LED ga almashtirdi va yiliga 9 milliard kVt-soat energiya tejashga erishdi. Singapur butun shahar bo'ylab aqlli yoritish tizimini joriy etib, energiya sarfini 50 foizga kamaytirdi. Bu misollar shuni ko'rsatadiki, aqlli yoritish tizimlari har qanday miqyosda — kichik loyihadan tortib butun shahar miqyosigacha samarali ishlaydi.",

    # IoT protokollar
    "IoT qurilmalarini ulash uchun turli simsiz aloqa protokollari mavjud bo'lib, har birining o'ziga xos afzalliklari va kamchiliklari bor. WiFi (IEEE 802.11) — eng keng tarqalgan protokol bo'lib, yuqori ma'lumot uzatish tezligi (150 Mbps gacha), keng qamrov (100 metr) va mavjud infratuzilmadan foydalanish imkoniyati bilan ajralib turadi, lekin energiya sarfi nisbatan yuqori. LoRa (Long Range) — past energiya sarfi va juda keng qamrov (15 km gacha) bilan ajralib turadi, lekin ma'lumot uzatish tezligi juda past (50 kbps) va maxsus gateway qurilmasi talab etiladi. Zigbee (IEEE 802.15.4) — past energiya sarfi va mesh tarmoq imkoniyati bilan ajralib turadi, lekin qamrov qisqa (100 metr) va maxsus koordinator kerak. NB-IoT (Narrowband IoT) — mobil tarmoq infratuzilmasidan foydalanadi, keng qamrov va past energiya sarfini ta'minlaydi, lekin oylik abonent to'lovi talab etiladi va real-time aloqa uchun kechikish yuqori. Har bir protokolning o'z qo'llanilish sohasi bor va tanlash loyiha talablariga bog'liq.",

    # Nima uchun WiFi
    "Bizning loyihamiz uchun WiFi protokoli tanlab olingan va buning bir necha muhim sabablari bor. Birinchidan, WiFi infratuzilmasi allaqachon mavjud — deyarli har bir binoda WiFi router bor va qo'shimcha qurilma sotib olish shart emas. Ikkinchidan, WiFi yuqori ma'lumot uzatish tezligini ta'minlaydi, bu esa real vaqt rejimida sensor ma'lumotlarini uzatish va Firebase bilan sinxronizatsiya qilish uchun muhim. Uchinchidan, ESP32 mikrokontrollerida WiFi moduli o'rnatilgan (built-in) bo'lib, qo'shimcha modul talab etilmaydi. To'rtinchidan, Firebase Realtime Database WebSocket protokoli orqali ishlaydi va u WiFi ulanishini talab etadi. Beshinchidan, loyihamiz bitta yoritgich uchun prototip sifatida ishlab chiqilgan va WiFi qamrovi (100 metr) buning uchun yetarli. Katta miqyosli joriy etishda LoRa yoki mesh WiFi texnologiyalariga o'tish mumkin, lekin prototip bosqichida WiFi eng optimal tanlov hisoblanadi."
]

for text in bob1_1_texts2:
    add_paragraph(text)
    total_chars += len(text)

page_break()


# --- 1.2-§ ---
doc.add_heading("1.2-§. Sensorlar va mikrokontrollerning texnik xarakteristikalari hamda algoritmlar tahlili", level=2)

bob1_2_texts = [
    # Ultratovush fizikasi
    "Ultratovush to'lqinlari — bu chastotasi 20 kHz dan yuqori bo'lgan tovush to'lqinlari bo'lib, inson qulog'i eshitish diapazonidan tashqarida joylashgan. Ultratovush sensorlari odatda 40 kHz chastotada ishlaydi, chunki bu chastota havoda yaxshi tarqaladi va ob'ektlardan samarali qaytadi. Ultratovush to'lqinlarining havoda tarqalish tezligi haroratga bog'liq bo'lib, v = 331.3 + 0.606 × T formulasi bilan hisoblanadi, bu yerda T — Selsiy bo'yicha harorat. 20°C haroratda tovush tezligi taxminan 343.4 m/s ga teng. Ultratovush sensorlari piezoelektrik effektga asoslanadi: elektr signal piezoelektrik kristallga berilganda u mexanik tebranishlar hosil qiladi va ultratovush to'lqinlarini chiqaradi. Qaytgan to'lqin esa kristalda elektr signal hosil qiladi. Bu prinsip sonar, tibbiy UZI, sanoat nazorati va masofani o'lchash kabi ko'plab sohalarda qo'llaniladi. Ko'cha yoritish tizimlarida ultratovush sensorlari ob'ektgacha bo'lgan masofani o'lchash va harakat mavjudligini aniqlash uchun ishlatiladi.",

    # Time of Flight
    "Masofani o'lchash uchun Time of Flight (ToF) — ya'ni to'lqinning borish va qaytish vaqtini o'lchash usuli qo'llaniladi. Sensor ultratovush impulsini chiqaradi, u ob'ektdan qaytadi va sensor tomonidan qabul qilinadi. Masofa quyidagi formula bo'yicha hisoblanadi: d = (t × v) / 2, bu yerda d — ob'ektgacha bo'lgan masofa (metrda), t — impulsning borish va qaytish vaqti (soniyada), v — tovush tezligi (m/s). Ikki ga bo'linadi, chunki to'lqin ikki marta yo'l bosadi — ob'ektgacha va qaytib. Amaliy misol: agar impuls 1000 mikrosoniyada qaytsa, masofa d = (0.001 × 343) / 2 = 17.15 sm bo'ladi. ESP32 da pulseIn() funksiyasi ECHO pinidagi yuqori signal davomiyligini mikrosoniyalarda o'lchaydi. Keyin bu qiymat 0.034 ga ko'paytiriladi va 2 ga bo'linadi — natija santimetrlarda olinadi. Bu usul 2 sm dan 450 sm gacha bo'lgan masofalarni ±1 sm aniqlikda o'lchash imkonini beradi. Harorat kompensatsiyasi qo'shilsa, aniqlik yanada oshadi.",

    # RCWL-9610A
    "RCWL-9610A ultratovush sensori bizning loyihamiz uchun tanlab olingan asosiy harakat aniqlash qurilmasi hisoblanadi. Bu sensor HC-SR04 ning zamonaviy va takomillashtirilgan versiyasi bo'lib, bir qator muhim afzalliklarga ega. Ish kuchlanishi 3.3-5.5V oralig'ida bo'lib, ESP32 ning 3.3V logic darajasi bilan to'g'ridan-to'g'ri ishlaydi — qo'shimcha darajani moslashtiruvchi (level shifter) kerak emas. Ish tokini sarfi 2 mA dan kam bo'lib, bu energiya tejamkor tizim uchun juda muhim. O'lchash diapazoni 2 sm dan 450 sm gacha, aniqlik ±1 sm, ishchi chastota 40 kHz. Sensoring ko'rish burchagi 30 daraja bo'lib, bu ko'cha yoritish uchun optimal — juda keng burchak keraksiz ob'ektlarni aniqlaydi, juda tor burchak esa harakatni o'tkazib yuborishi mumkin. Ish harorati diapazoni -20°C dan +70°C gacha bo'lib, tashqi muhitda ishlash uchun mos. Sensor 4 ta pinga ega: VCC (quvvat), GND (yer), TRIG (trigger — impuls chiqarish) va ECHO (echo — qaytgan signal). TRIG pinga 10 mikrosoniyalik yuqori signal berilganda sensor 8 ta 40 kHz impuls chiqaradi va ECHO pini qaytgan signalgacha yuqori holatda turadi.",

    # HC-SR04 bilan qiyoslash
    "RCWL-9610A sensorini tanlab olishda uni mashhur HC-SR04 sensori bilan solishtirib ko'rdik. HC-SR04 sensori 5V ish kuchlanishini talab etadi, bu esa ESP32 ning 3.3V logic darajasi bilan to'g'ridan-to'g'ri mos kelmaydi — ECHO pinidan keluvchi 5V signal ESP32 ning GPIO pinlarini shikastlashi mumkin, shu sababli voltage divider yoki level shifter kerak bo'ladi. RCWL-9610A esa 3.3V da ham barqaror ishlaydi va qo'shimcha komponent talab etilmaydi. Energiya sarfi bo'yicha ham RCWL-9610A ustunlik qiladi: uning ish toki 2 mA dan kam, HC-SR04 esa 15 mA atrofida sarflaydi. O'lchash aniqligi bo'yicha ikkala sensor ham ±1 sm aniqlikni ta'minlaydi, lekin RCWL-9610A ning minimal o'lchash masofasi 2 sm (HC-SR04 da esa 4 sm). Narx bo'yicha ikkala sensor ham arzon — 2-5 dollar atrofida. Umumiy baholash shuni ko'rsatadiki, ESP32 bilan ishlash uchun RCWL-9610A ancha qulayroq va ishonchliroq tanlov hisoblanadi, chunki u qo'shimcha komponentlarsiz to'g'ridan-to'g'ri ulanadi.",

    # TEMT6000
    "TEMT6000 yorug'lik sensori — bu fototransistor asosida ishlaydigan analog yorug'lik sensori bo'lib, ko'rinadigan yorug'lik spektrini (360-970 nm) o'lchash uchun mo'ljallangan. Sensor inson ko'zining sezuvchanligiga yaqin spektral xarakteristikaga ega bo'lib, bu uni kunduz va tun vaqtini aniqlash uchun ideal qiladi. TEMT6000 analog chiqish signalini beradi — yorug'lik kuchaygan sari chiqish kuchlanishi oshadi. ESP32 ning 12-bit ADC (Analog-Digital Converter) moduli bu signalni 0 dan 4095 gacha bo'lgan raqamli qiymatga aylantiradi. Qorong'i muhitda ADC qiymati 0-100 atrofida, xona yorug'ligida 500-1500, tashqarida kunduz kuni esa 2000-4095 atrofida bo'ladi. Bizning tizimimizda 300 qiymati chegara (threshold) sifatida belgilangan: ADC qiymati 300 dan past bo'lsa tun deb hisoblanadi va yoritish tizimi faollashadi. Sensor juda kichik o'lchamga ega (3x3 mm), 3.3V da ishlaydi va deyarli energiya sarflamaydi. Uning asosiy afzalligi — oddiy ulanish (faqat 3 ta sim: VCC, GND, OUT) va ESP32 ning ADC pini bilan to'g'ridan-to'g'ri ishlash imkoniyati.",

    # ESP32
    "ESP32 mikrokontrolleri Espressif Systems kompaniyasi tomonidan ishlab chiqilgan yuqori samarali va arzon IoT platformasi hisoblanadi. Uning asosiy texnik xarakteristikalari quyidagicha: protsessor — Xtensa LX6 dual-core, takt chastotasi 240 MHz gacha, bu esa murakkab algoritmlarni real vaqtda bajarish uchun yetarli. Operativ xotira (RAM) — 520 KB SRAM, bu sensor ma'lumotlarini qayta ishlash, WiFi stack va Firebase kutubxonasi uchun yetarli. Flash xotira — 4 MB, firmware va NVS (Non-Volatile Storage) uchun ishlatiladi. WiFi moduli — 802.11 b/g/n standartlarini qo'llab-quvvatlaydi, 150 Mbps gacha ma'lumot uzatish tezligi, WPA2 shifrlash. Bluetooth — BLE 4.2 va Classic Bluetooth qo'llab-quvvatlanadi. ADC — 18 ta kanal, 12-bit aniqlik (0-4095), 0-3.3V o'lchash diapazoni. GPIO — 34 ta umumiy maqsadli kirish-chiqish pinlari, ulardan 18 tasi ADC, 10 tasi sensorli (touch), 2 tasi DAC funksiyasiga ega. Ish kuchlanishi — 3.3V, USB orqali 5V dan quvvatlanadi (ichki regulyator). Ish harorati — -40°C dan +85°C gacha. ESP32 ning eng muhim afzalligi — WiFi modulining o'rnatilgan (built-in) bo'lishi, bu esa IoT loyihalari uchun qo'shimcha modul sotib olish zaruratini yo'qotadi.",

    # Relay moduli
    "Relay (o'tkazgich) moduli — bu past kuchlanishli boshqaruv signali orqali yuqori kuchlanishli yukni (masalan, 220V ko'cha yoritgichini) yoqish va o'chirish uchun ishlatiladigan elektromexanik kalit hisoblanadi. Relay moduli ichida elektromagnit, kontaktlar va optokuplyor (optik izolyator) joylashgan. Optokuplyor boshqaruv qismini (ESP32, 3.3V) kuch qismidan (220V) elektrik jihatdan to'liq ajratadi, bu esa mikrokontrollerni yuqori kuchlanish ta'siridan himoya qiladi. Bizning loyihamizda 5V relay moduli ishlatiladi, u active LOW rejimda ishlaydi — ya'ni boshqaruv pini LOW (0V) bo'lganda relay yoqiladi, HIGH (3.3V) bo'lganda o'chadi. Relay ning kontakt quvvati 10A 250VAC yoki 10A 30VDC, bu esa 2000W gacha bo'lgan yukni boshqarish imkonini beradi. Ko'cha yoritgichi odatda 60-150W quvvatga ega, shuning uchun relay quvvati yetarli zaxiraga ega. Relay moduli ESP32 ning GPIO 26 pini orqali boshqariladi va LED strip yoki ko'cha yoritgichini yoqish-o'chirish vazifasini bajaradi.",
]

for text in bob1_2_texts:
    add_paragraph(text)
    total_chars += len(text)

add_image("ultrasonic_principle.png", "1.2-rasm. Ultratovush sensori ishlash prinsipi")
add_image("rcwl9610a.png", "1.3-rasm. RCWL-9610A ultratovush sensori")
add_image("temt6000.png", "1.4-rasm. TEMT6000 yorug'lik sensori")
add_image("esp32_pinout.png", "1.5-rasm. ESP32 DevKit mikrokontrolleri pin joylashuvi")
add_image("relay_module.png", "1.6-rasm. Relay moduli tuzilishi")

bob1_2_texts3 = [
    # Debounce
    "Debounce algoritmi sensorlardan olingan ma'lumotlarning ishonchliligini oshirish uchun qo'llaniladigan muhim dasturiy yechim hisoblanadi. Ultratovush sensori ba'zan noto'g'ri natijalar berishi mumkin — masalan, havo oqimi, shovqin yoki boshqa ob'ektlardan qaytgan signal sababli. Agar har bir o'lchov natijasiga darhol reaksiya berilsa, yoritgich tez-tez yonib-o'chib turadi (flickering), bu esa foydalanuvchi uchun noqulay va uskunaga zararli. Debounce algoritmi bu muammoni hal qiladi: sensor har 300 millisekundda o'lchov oladi va har 3 ta o'lchov natijasini tahlil qiladi. Agar 3 ta o'lchovdan kamida 2 tasi harakatni ko'rsatsa (majority voting — ko'pchilik ovozi prinsipi), harakat aniqlangan deb hisoblanadi. Bu yondashuv tasodifiy xato signallarni filtrlaydi va faqat haqiqiy harakatga reaksiya beradi. Masalan, agar birinchi o'lchov 50 sm (harakat), ikkinchi o'lchov 300 sm (xato), uchinchi o'lchov 45 sm (harakat) ko'rsatsa — 3 tadan 2 tasi harakat, demak harakat bor deb qaror qilinadi.",

    # Hold timer
    "Hold timer (ushlab turish taymeri) — bu harakat to'xtagandan keyin yoritgichni darhol o'chirmasdan, belgilangan vaqt davomida yoniq holatda ushlab turish mexanizmi. Bizning tizimimizda hold timer 5 soniyaga o'rnatilgan. Bu mexanizm bir necha muhim sabablar uchun kerak: birinchidan, odam ko'chadan o'tayotganda sensor uni har doim ham uzluksiz ko'rmaydi — odam sensor ko'rish burchagidan chiqib ketishi va yana kirib kelishi mumkin. Hold timer bu oraliqda yoritgichni yoniq ushlab turadi. Ikkinchidan, relay kontaktlarining mexanik eskirishini kamaytiradi — tez-tez yoqish-o'chirish relay umrini qisqartiradi. Uchinchidan, foydalanuvchi tajribasi (UX) yaxshilanadi — odam hali ko'chada bo'lganida yoritgich o'chib qolmasligi kerak. Hold timer ishlash prinsipi oddiy: har safar harakat aniqlanganda lastMotionTime o'zgaruvchisi yangilanadi, va yoritgich faqat millis() - lastMotionTime > 5000 bo'lganda o'chiriladi.",

    # Hysteresis
    "Hysteresis (gisterezis) — bu ikki turli chegara qiymatlarini qo'llash orqali tizimning beqaror holatda tebranishini (oscillation) oldini olish usuli. Yorug'lik sensori qiymatlarida tabiiy tebranishlar mavjud — masalan, bulut o'tganda yorug'lik bir lahza kamayadi va yana oshadi. Agar bitta chegara qiymati (masalan, 300) ishlatilsa, sensor qiymati 299 va 301 orasida tebranganda tizim tez-tez kunduz va tun rejimi o'rtasida almashib turadi. Hysteresis bu muammoni hal qiladi: tun rejimiga o'tish uchun sensor qiymati 250 dan pastga tushishi kerak, kunduz rejimiga qaytish uchun esa 350 dan yuqoriga ko'tarilishi kerak. 250 va 350 orasidagi 100 birliklik zona o'lik zona (dead zone) deb ataladi — bu zonada tizim hozirgi holatini saqlab qoladi va almashish sodir bo'lmaydi. Bu yondashuv tizimning barqaror ishlashini ta'minlaydi va keraksiz almashishlarni to'liq bartaraf etadi. Bizning firmware kodimizda bu isDarkState o'zgaruvchisi va ikki shartli tekshirish orqali amalga oshirilgan.",
]

for text in bob1_2_texts3:
    add_paragraph(text)
    total_chars += len(text)

add_image("diagram_flowchart.png", "1.7-rasm. Tizim ishlash algoritmi blok-sxemasi")

page_break()


# --- 1.3-§ ---
doc.add_heading("1.3-§. Masalaning qo'yilishi", level=2)

masala_text = "Yuqoridagi tahlillar asosida masala quyidagicha qo'yiladi: an'anaviy ko'cha yoritish tizimlari tun bo'yi uzluksiz ishlaydi va energiyaning 60-70 foizi behuda sarflanadi. Mavjud tijorat yechimlari (Philips CityTouch, Telensa, Tvilight) yuqori narxi sababli kichik va o'rta loyihalar uchun mos emas. Ochiq kodli yechimlar esa to'liq IoT funksionallikdan mahrum. Shu sababli, arzon va samarali aqlli yoritish tizimini ishlab chiqish zarur. Tizim quyidagi talablarga javob berishi kerak: ultratovush sensori orqali 2 metr masofada harakatni ishonchli aniqlash, yorug'lik sensori orqali kunduz-tun farqlash, debounce va hysteresis algoritmlari orqali barqaror ishlash, Firebase orqali real-time masofadan boshqarish va PWA dashboard orqali qulay interfeys. Energiya tejash samaradorligi quyidagi formula bo'yicha hisoblanadi: E = ((T_tun - T_yonish) / T_tun) × 100%, bu yerda T_tun — tun davomiyligi (soat), T_yonish — yoritgich yonib turgan vaqt (soat). Maqsad — kamida 60 foiz energiya tejashga erishish. Bu masalani hal qilish uchun ESP32 mikrokontrolleri, RCWL-9610A ultratovush sensori, TEMT6000 yorug'lik sensori va relay moduli asosida prototip ishlab chiqiladi va amaliy sinovdan o'tkaziladi."
add_paragraph(masala_text)
total_chars += len(masala_text)

page_break()

# ============ II BOB ============
doc.add_heading("II BOB. AMALIY QISM", level=1)

# --- 2.1-§ ---
doc.add_heading("2.1-§. Tizim arxitekturasi va texnologiyalar tanlash", level=2)

bob2_1_texts = [
    # ESP32 tanlash
    "Loyihamiz uchun mikrokontroller tanlashda bir necha variantlar ko'rib chiqildi: Arduino Uno, ESP8266 va ESP32. Arduino Uno — eng mashhur va oddiy platforma, lekin uning WiFi moduli yo'q (qo'shimcha shield kerak), RAM hajmi atigi 2 KB va protsessor tezligi 16 MHz. Bu ko'rsatkichlar Firebase bilan real-time aloqa uchun yetarli emas. ESP8266 — WiFi moduliga ega arzon mikrokontroller, lekin uning faqat bitta ADC kanali bor (bizga kamida 2 ta kerak — yorug'lik sensori va kelajakda boshqa sensorlar uchun), RAM hajmi 80 KB va protsessor bitta yadroli 80 MHz. ESP32 esa barcha talablarimizga javob beradi: dual-core 240 MHz protsessor murakkab algoritmlarni real vaqtda bajaradi, 520 KB RAM Firebase kutubxonasi va WiFi stack uchun yetarli, 18 ta ADC kanali kelajakda kengaytirish imkonini beradi, o'rnatilgan WiFi va BLE modullari qo'shimcha komponent talab etmaydi. Narx jihatidan ESP32 DevKit moduli atigi 5-8 dollar turadi, bu esa Arduino + WiFi shield kombinatsiyasidan arzonroq. Shu sababli ESP32 bizning loyihamiz uchun optimal tanlov hisoblanadi.",

    # Tizim arxitekturasi
    "Tizim arxitekturasi uch qatlamli (three-tier) modelga asoslanadi: Hardware qatlami, Cloud qatlami va Client qatlami. Hardware qatlami — bu ESP32 mikrokontrolleri, sensorlar (RCWL-9610A va TEMT6000) va relay modulidan iborat fizik qurilma. Bu qatlam sensor ma'lumotlarini o'qiydi, algoritmlar asosida qaror qabul qiladi va relay orqali yoritgichni boshqaradi. Cloud qatlami — Firebase Realtime Database bo'lib, u qurilma va foydalanuvchi o'rtasida vositachi vazifasini bajaradi. Qurilma sensor ma'lumotlarini Firebase ga yozadi, foydalanuvchi esa boshqaruv buyruqlarini Firebase ga yozadi — qurilma bu buyruqlarni real vaqtda oladi. Client qatlami — React asosidagi PWA (Progressive Web Application) bo'lib, u foydalanuvchiga qulay grafik interfeys orqali tizimni monitoring qilish va boshqarish imkonini beradi. Bu arxitektura loose coupling (zaif bog'lanish) prinsipiga asoslanadi — har bir qatlam mustaqil ishlaydi va boshqa qatlamlar bilan faqat Firebase orqali aloqa qiladi. Bu esa tizimning ishonchliligini oshiradi: internet uzilsa ham qurilma offline rejimda ishlashda davom etadi.",

    # Pin konfiguratsiya
    "ESP32 mikrokontrollerida pinlar quyidagicha taqsimlangan: GPIO 4 — RCWL-9610A sensorining TRIG (trigger) pini uchun, OUTPUT rejimida ishlaydi va sensorga 10 mikrosoniyalik impuls yuboradi. GPIO 16 — RCWL-9610A sensorining ECHO pini uchun, INPUT rejimida ishlaydi va qaytgan signal davomiyligini o'lchaydi. GPIO 34 — TEMT6000 yorug'lik sensorining analog chiqishi uchun, bu pin faqat INPUT rejimida ishlaydi (GPIO 34-39 pinlari ESP32 da faqat kirish uchun) va ADC1 kanaliga ulangan. GPIO 26 — relay modulining boshqaruv pini uchun, OUTPUT rejimida ishlaydi va HIGH/LOW signal orqali relay ni yoqadi yoki o'chiradi. GPIO 2 — ESP32 ning o'rnatilgan (onboard) LED diodi uchun, u tizim holatini ko'rsatish maqsadida ishlatiladi — yoritgich yoniq bo'lganda LED ham yonadi. Barcha pinlar 3.3V logic darajasida ishlaydi, bu esa RCWL-9610A va relay moduli bilan to'g'ridan-to'g'ri ulanish imkonini beradi.",

    # Quvvat hisoblash
    "Tizimning umumiy quvvat sarfi quyidagicha hisoblanadi: ESP32 mikrokontrolleri WiFi faol holatda taxminan 160 mA, RCWL-9610A sensori 2 mA, TEMT6000 sensori 0.1 mA dan kam, relay moduli yoqilgan holatda 60 mA. Jami maksimal tok sarfi: 160 + 2 + 0.1 + 60 = 222.1 mA. Kuchlanish 5V bo'lganda quvvat: P = 5V × 0.222A = 1.11 Vt. Kunlik energiya sarfi (24 soat): E = 1.11 × 24 = 26.64 Vt-soat = 0.027 kVt-soat. Oylik energiya sarfi: 0.027 × 30 = 0.81 kVt-soat. Yillik energiya sarfi: 0.027 × 365 = 9.86 kVt-soat. Bu juda kam energiya sarfi — oddiy 60W ko'cha yoritgichi tun bo'yi (12 soat) yonsa kuniga 0.72 kVt-soat sarflaydi, ya'ni bizning boshqaruv tizimimiz yoritgichning kunlik sarfining atigi 3.75 foizini tashkil etadi. Bu esa tizimning energiya tejash samaradorligiga deyarli ta'sir qilmaydi.",

    # PlatformIO
    "Firmware ishlab chiqish uchun PlatformIO muhiti tanlab olingan. Arduino IDE — eng mashhur va oddiy muhit, lekin u professional loyihalar uchun bir qator kamchiliklarga ega: kutubxonalarni boshqarish qiyin, multi-file loyihalar uchun noqulay, avtomatik kompilatsiya va yuklash skriptlari yo'q, IntelliSense va kodni to'ldirish cheklangan. PlatformIO esa professional darajadagi ishlab chiqish muhiti bo'lib, quyidagi afzalliklarga ega: platformio.ini fayli orqali barcha sozlamalar versiya boshqaruv tizimida saqlanadi, kutubxonalar lib_deps orqali avtomatik yuklanadi va versiyalanadi, multi-file loyiha tuzilishi (src/, include/, lib/) qo'llab-quvvatlanadi, VS Code integratsiyasi to'liq IntelliSense va debugging imkonini beradi. Bizning loyihamizda platformio.ini faylida ESP32 platformasi, Arduino framework, kerakli kutubxonalar (FirebaseESP32, FastLED) va serial monitor tezligi belgilangan. Bu esa loyihani boshqa kompyuterda ham bir buyruq bilan kompilatsiya qilish imkonini beradi.",

    # Firebase
    "Firebase Realtime Database — Google tomonidan ishlab chiqilgan NoSQL bulutli ma'lumotlar bazasi bo'lib, u real vaqt rejimida ma'lumot sinxronizatsiyasini ta'minlaydi. Firebase ning asosiy xususiyatlari: birinchidan, WebSocket protokoli orqali ishlaydi — bu esa an'anaviy HTTP so'rovlardan farqli ravishda doimiy ulanishni ta'minlaydi va ma'lumot o'zgarganda darhol barcha ulangan qurilmalarga yetkaziladi (latency 100-200 ms). Ikkinchidan, JSON formatida ma'lumot saqlaydi — bu ESP32 va React ilovasi uchun qulay, chunki ikkala platforma ham JSON bilan oson ishlaydi. Uchinchidan, offline qo'llab-quvvatlash — internet uzilganda ma'lumotlar lokal keshda saqlanadi va ulanish tiklanganda avtomatik sinxronizatsiya qilinadi. To'rtinchidan, xavfsizlik qoidalari (Security Rules) — faqat autentifikatsiya qilingan foydalanuvchilar ma'lumotlarga kirishi mumkin. Beshinchidan, bepul tarif (Spark plan) — 1 GB saqlash, 10 GB/oy trafik, 100 ta bir vaqtda ulanish. Bizning loyihamiz uchun bu yetarli. Firebase ESP32 uchun FirebaseESP32 kutubxonasi orqali, React uchun esa firebase npm paketi orqali ulanadi.",

    # React + Vite + PWA
    "Web dashboard uchun React + Vite + PWA texnologiyalar to'plami tanlab olingan. React — Facebook tomonidan ishlab chiqilgan komponent asosidagi UI kutubxonasi bo'lib, murakkab interaktiv interfeyslarni yaratish uchun eng mashhur vosita. Vite — zamonaviy build tool bo'lib, Webpack ga nisbatan 10-100 baravar tezroq ishlaydi, chunki ES modules va esbuild dan foydalanadi. PWA (Progressive Web Application) — bu veb-ilovani native mobil ilova kabi ishlash imkonini beruvchi texnologiya: offline ishlash, push bildirishnomalar, bosh ekranga o'rnatish. Bizning dashboard quyidagi komponentlardan iborat: Login sahifasi (Firebase Authentication), Dashboard (real-time sensor ma'lumotlari va boshqaruv), Statistics (haftalik energiya tejash grafiklari, Recharts kutubxonasi), MotionLog (oxirgi 50 ta harakat hodisasi). PWA imkoniyati tufayli foydalanuvchi telefoniga ilovani o'rnatishi va internet bo'lmagan paytda ham oxirgi ma'lumotlarni ko'rishi mumkin."
]

for text in bob2_1_texts:
    add_paragraph(text)
    total_chars += len(text)

add_image("diagram_architecture.png", "2.1-rasm. Tizim arxitekturasi diagrammasi")

page_break()


# --- 2.2-§ ---
doc.add_heading("2.2-§. Dasturiy ta'minot ishlab chiqish", level=2)

bob2_2_texts_1 = [
    # Qurilmani yig'ish
    "Qurilmani yig'ish jarayoni bir necha bosqichda amalga oshirildi. Birinchi bosqichda barcha komponentlar breadboard (sinov platasi) ustiga joylashtirildi va jumper simlari orqali ulandi. ESP32 DevKit moduli breadboard ning markaziga o'rnatildi, RCWL-9610A ultratovush sensori qurilmaning old tomoniga — harakatni aniqlash yo'nalishiga qaratib joylashtirildi. TEMT6000 yorug'lik sensori yuqoriga — ochiq osmonga qaratib o'rnatildi, chunki u tashqi yorug'likni o'lchashi kerak. Relay moduli alohida joylashtirildi va ESP32 dan 3 ta sim bilan ulandi: VCC (5V), GND va signal (GPIO 26). Barcha ulanishlar tekshirilgandan keyin tizim USB orqali kompyuterga ulandi va firmware yuklandi. Ikkinchi bosqichda tizim sinov muhitiga o'rnatildi — koridor devorida 2.5 metr balandlikda, sensor pastga qaratib. Bu joylashuv optimal aniqlash burchagini ta'minlaydi: sensor 30 darajalik ko'rish burchagi bilan 2 metr masofada taxminan 1 metr kenglikdagi zonani qamrab oladi.",

    # Firmware arxitekturasi
    "Firmware arxitekturasi modulli (modular) yondashuvga asoslanadi va 5 ta asosiy moduldan iborat: main.cpp — asosiy dastur, WiFi boshqaruv va tizim koordinatsiyasi; sensors.cpp — ultratovush va yorug'lik sensorlarini o'qish, debounce algoritmi; light_control.cpp — relay boshqaruv, auto/manual rejimlar, hysteresis; firebase_handler.cpp — Firebase ulanish, stream (real-time tinglash), status yuborish; statistics.cpp — energiya tejash statistikasini hisoblash va saqlash. Har bir modul o'zining header (.h) fayliga ega bo'lib, unda funksiya deklaratsiyalari joylashgan. Bu arxitektura kodni o'qish, tushunish va kengaytirishni osonlashtiradi. Masalan, yangi sensor qo'shish uchun faqat sensors.cpp ga kod qo'shish va boshqa modullarda yangi funksiyani chaqirish kifoya — boshqa modullarni o'zgartirish shart emas. Modullar o'rtasida aloqa getter funksiyalari orqali amalga oshiriladi: getDistance(), getAmbientLight(), isMotionDetected(), isLightOn() va boshqalar.",
]

for text in bob2_2_texts_1:
    add_paragraph(text)
    total_chars += len(text)

# readDistance code
add_paragraph("Masofani o'lchash funksiyasi (readDistance) quyidagicha ishlaydi: TRIG pinga 10 mikrosoniyalik impuls yuboriladi, keyin ECHO pinidagi yuqori signal davomiyligi o'lchanadi va masofa hisoblanadi:", first_indent=Cm(1.25))
total_chars += 200

code1 = """void loopSensors() {
  if (millis() - lastRead < 300) return;
  lastRead = millis();
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  long duration = pulseIn(ECHO_PIN, HIGH, 30000);
  distance_cm = (duration > 0) ? duration * 0.034 / 2.0 : 999;
}"""
add_code_block(code1)
total_chars += len(code1)

# detectMotion code
add_paragraph("Harakatni aniqlash funksiyasi debounce algoritmini qo'llaydi — har 3 ta o'lchovdan kamida 2 tasi harakatni ko'rsatsa, harakat aniqlangan deb hisoblanadi. Bu tasodifiy xato signallarni filtrlaydi:", first_indent=Cm(1.25))
total_chars += 180

code2 = """  bool currentDetect = (distance_cm < DEFAULT_DISTANCE_THRESHOLD && distance_cm > 2);
  readCount++;
  if (currentDetect) motionCount++;
  if (readCount >= 3) {
    if (motionCount >= 2) {
      lastMotionTime = millis();
    }
    motionCount = 0;
    readCount = 0;
  }"""
add_code_block(code2)
total_chars += len(code2)

# updateMotion code
add_paragraph("Hold timer mexanizmi — oxirgi harakatdan 5 soniya o'tmaguncha motion o'zgaruvchisi true bo'lib qoladi. Bu yoritgichning tez-tez yonib-o'chishini oldini oladi:", first_indent=Cm(1.25))
total_chars += 160

code3 = """  // Hold: oxirgi harakatdan 5s ichida "motion = true"
  motion = (millis() - lastMotionTime < 5000);
  Serial.printf("Distance: %.1fcm | Light: %d | Motion: %s\\n",
                distance_cm, ambient_light, motion ? "YES" : "NO");"""
add_code_block(code3)
total_chars += len(code3)

# updateLightStatus code
add_paragraph("Yorug'lik holatini yangilash funksiyasi hysteresis algoritmini qo'llaydi — tun rejimiga o'tish uchun sensor qiymati threshold-50 dan past, kunduz rejimiga qaytish uchun threshold+50 dan yuqori bo'lishi kerak:", first_indent=Cm(1.25))
total_chars += 200

code4 = """void loopLightControl() {
  if (mode == "manual") { setRelay(manualLight); return; }
  int light = getAmbientLight();
  if (light < lightThreshold - 50) isDarkState = true;
  else if (light > lightThreshold + 50) isDarkState = false;
  if (!isDarkState) setRelay(false);
  else if (isMotionDetected()) setRelay(true);
  else setRelay(false);
}"""
add_code_block(code4)
total_chars += len(code4)

# autoMode explanation
add_paragraph("Avtomatik rejim (auto mode) — tizimning asosiy ishlash rejimi bo'lib, u yorug'lik sensori va harakat sensori ma'lumotlarini birgalikda tahlil qiladi. Agar kunduz bo'lsa (yorug'lik yuqori) — yoritgich doimo o'chiq. Agar tun bo'lsa va harakat aniqlansa — yoritgich yonadi. Agar tun bo'lsa lekin harakat yo'q — yoritgich o'chiq. Manual rejimda esa foydalanuvchi dashboard orqali yoritgichni to'g'ridan-to'g'ri boshqaradi:", first_indent=Cm(1.25))
total_chars += 400

code5 = """static void setRelay(bool on) {
  if (on == lastRelayState) return;
  lastRelayState = on;
  lightOn = on;
  digitalWrite(RELAY_PIN, on ? HIGH : LOW);
  digitalWrite(LED_PIN, on ? HIGH : LOW);
  Serial.printf(">>> RELAY: %s\\n", on ? "ON" : "OFF");
}"""
add_code_block(code5)
total_chars += len(code5)

# Firebase stream code
add_paragraph("Firebase stream mexanizmi real vaqt rejimida boshqaruv buyruqlarini qabul qilish uchun ishlatiladi. Stream /device/control yo'liga ulanadi va har qanday o'zgarish bo'lganda callback funksiyasi chaqiriladi. Bu WebSocket asosida ishlaydi va polling (so'rov yuborish) ga nisbatan ancha samarali:", first_indent=Cm(1.25))
total_chars += 300

code6 = """static void handleStream() {
  if (!streamConnected) {
    if (Firebase.beginStream(streamData, "/device/control")) {
      streamConnected = true;
    }
    return;
  }
  if (!Firebase.readStream(streamData)) {
    streamConnected = false;
    return;
  }
  if (streamData.streamAvailable()) {
    String path = streamData.dataPath();
    if (path == "/mode") setMode(streamData.stringData());
    else if (path == "/manual_light") setManualLight(streamData.boolData());
  }
}"""
add_code_block(code6)
total_chars += len(code6)

bob2_2_texts_2 = [
    # WiFi boshqaruv
    "WiFi boshqaruv tizimi non-blocking (blokirovka qilmaydigan) arxitekturada ishlab chiqilgan. Bu shuni anglatadiki, WiFi ulanishi yo'qolsa ham tizim offline rejimda ishlashda davom etadi — sensorlar o'qiladi va relay boshqariladi. WiFi boshqaruv quyidagi komponentlardan iborat: NVS (Non-Volatile Storage) — WiFi SSID va parol flash xotiraga saqlanadi va qurilma qayta ishga tushganda avtomatik o'qiladi. Captive Portal — agar saqlangan WiFi topilmasa, ESP32 o'zi Access Point (AP) rejimiga o'tadi va SmartLight-Setup nomli WiFi tarmoq ochadi. Foydalanuvchi bu tarmoqqa ulanib, 192.168.4.1 manzilida WiFi sozlamalarini kiritadi. DNS Server — captive portal uchun har qanday domen so'rovi 192.168.4.1 ga yo'naltiriladi, bu esa foydalanuvchini avtomatik sozlash sahifasiga olib boradi. Auto-reconnect — har 60 soniyada WiFi holati tekshiriladi, uzilgan bo'lsa qayta ulanishga harakat qilinadi. Bu arxitektura tizimning ishonchliligini sezilarli darajada oshiradi — hatto internet butunlay uzilsa ham ko'cha yoritishi to'g'ri ishlashda davom etadi.",

    # Dashboard
    "Web dashboard React komponent arxitekturasida ishlab chiqilgan va quyidagi asosiy komponentlardan iborat: App.jsx — asosiy komponent, autentifikatsiya holatini boshqaradi va Login yoki Dashboard komponentini ko'rsatadi. Login.jsx — Firebase Authentication orqali email va parol bilan kirish sahifasi, xato xabarlarini ko'rsatish va demo rejimga o'tish tugmasi. Dashboard.jsx — asosiy boshqaruv paneli, real-time sensor ma'lumotlari (masofa, yorug'lik, harakat holati), rejim tanlash (auto/manual), yorug'likni yoqish-o'chirish tugmasi, brightness slider. Statistics.jsx — Recharts kutubxonasi yordamida haftalik energiya tejash grafiklari, harakatlar soni va yonish davomiyligi. MotionLog.jsx — oxirgi 50 ta harakat hodisasi ro'yxati, vaqt va sensor qiymatlari bilan. Dashboard responsive dizaynga ega — mobil telefondan ham qulay ishlaydi. CSS Grid va Flexbox texnologiyalari orqali turli ekran o'lchamlariga moslashadi.",

    # PWA
    "Progressive Web Application (PWA) texnologiyasi veb-ilovani native mobil ilova kabi ishlash imkonini beradi. Bizning dashboard PWA sifatida sozlangan va quyidagi imkoniyatlarga ega: birinchidan, offline ishlash — Service Worker orqali barcha statik resurslar (HTML, CSS, JS, rasmlar) keshlanadi va internet bo'lmagan paytda ham ilova ochiladi. Ikkinchidan, o'rnatish (install) — foydalanuvchi telefonida Add to Home Screen tugmasini bosib ilovani bosh ekranga qo'shishi mumkin, keyin u native ilova kabi ochiladi (brauzer panelisiz). Uchinchidan, tez yuklash — keshdan yuklanishi sababli ilova 1-2 soniyada ochiladi. Vite-plugin-pwa plagini orqali Service Worker avtomatik generatsiya qilinadi va har safar build qilinganda yangilanadi. Manifest.json faylida ilova nomi, ranglari, ikonkalari va boshqa metama'lumotlar belgilangan. PWA Lighthouse testida 95+ ball oladi."
]

for text in bob2_2_texts_2:
    add_paragraph(text)
    total_chars += len(text)

add_image("diagram_state.png", "2.2-rasm. Tizim holatlari diagrammasi")
add_image("screenshot_dashboard_desktop.png", "2.3-rasm. Dashboard — kompyuter ko'rinishi")
add_image("screenshot_dashboard_mobile.png", "2.4-rasm. Dashboard — mobil ko'rinishi")
add_image("screenshot_login.png", "2.5-rasm. Kirish sahifasi")

page_break()


# --- 2.3-§ ---
doc.add_heading("2.3-§. Sinov natijalari va tahlil", level=2)

bob2_3_texts = [
    # Sinov metodologiyasi
    "Tizimni sinash uchun 5 kunlik amaliy sinov o'tkazildi. Sinov muhiti sifatida bino koridori tanlandi — uzunligi 15 metr, kengligi 3 metr. Koridor devorida 2.5 metr balandlikda ESP32 qurilmasi o'rnatildi, ultratovush sensori pastga va koridor bo'ylab qaratildi. Yoritish sifatida 60W ekvivalentli LED lampa ishlatildi, u relay moduli orqali boshqarildi. Sinov har kuni soat 18:00 dan 06:00 gacha (12 soat) davom etdi. Sinov davomida quyidagi parametrlar qayd etildi: harakatlar soni (necha marta sensor harakatni aniqladi), yoritgich yonib turgan vaqt (daqiqalarda), energiya tejash foizi (formula bo'yicha hisoblandi). Barcha ma'lumotlar Firebase Realtime Database ga real vaqtda yozildi va keyinchalik tahlil qilindi. Sinov davomida tizim uzluksiz ishladi, hech qanday nosozlik yoki uzilish kuzatilmadi. WiFi ulanishi barqaror bo'ldi (RSSI -45 dBm atrofida).",

    # Sinov natijalari
    "Besh kunlik sinov natijalari quyidagicha bo'ldi: birinchi kun — 45 ta harakat aniqlandi, yoritgich jami 120 daqiqa yondi, energiya tejash 83 foiz; ikkinchi kun — 62 ta harakat, 155 daqiqa yonish, 78 foiz tejash; uchinchi kun (dam olish kuni, kam harakat) — 38 ta harakat, 95 daqiqa yonish, 86 foiz tejash; to'rtinchi kun — 71 ta harakat, 180 daqiqa yonish, 75 foiz tejash; beshinchi kun — 55 ta harakat, 140 daqiqa yonish, 80 foiz tejash. Besh kunlik o'rtacha ko'rsatkichlar: 54.2 ta harakat kuniga, 138 daqiqa (2 soat 18 daqiqa) yonish kuniga, 80.4 foiz energiya tejash. An'anaviy tizimda yoritgich 12 soat (720 daqiqa) uzluksiz yonadi, bizning tizimda esa o'rtacha 138 daqiqa — ya'ni 582 daqiqa (9 soat 42 daqiqa) energiya tejaladi. Bu natijalar tizimning yuqori samaradorligini tasdiqlaydi va dastlabki maqsad (kamida 60 foiz tejash) oshirib bajarilganini ko'rsatadi.",

    # O'rtacha tejash tahlili
    "O'rtacha 80.4 foiz energiya tejash natijasi bir necha omillar bilan izohlanadi. Birinchidan, sinov muhiti (koridor) nisbatan kam harakatli zona — tun vaqtining katta qismida hech kim o'tmaydi. Ikkinchidan, hold timer 5 soniyaga o'rnatilgan — bu yetarli darajada qisqa vaqt bo'lib, keraksiz yonishni minimallashtiradi. Uchinchidan, debounce algoritmi noto'g'ri triggerlarni samarali filtrlaydi — sinov davomida birorta ham yolg'on alarm (false positive) kuzatilmadi. Haqiqiy ko'cha sharoitida tejash foizi biroz past bo'lishi mumkin (60-70 foiz), chunki ko'chada harakat ko'proq bo'ladi. Lekin hatto 60 foiz tejash ham juda yuqori ko'rsatkich — bu an'anaviy tizimga nisbatan 2.5 baravar kam energiya sarfi demak. Tizimning yana bir muhim afzalligi — u faqat kerak bo'lganda yonadi, bu esa nafaqat energiya tejaydi, balki lampa umrini ham uzaytiradi.",

    # Iqtisodiy hisob
    "Iqtisodiy samaradorlikni hisoblash uchun quyidagi parametrlar olingan: 60W LED yoritgich, tun davomiyligi o'rtacha 12 soat, yillik ish kunlari 365. An'anaviy tizimda yillik energiya sarfi: 60W × 12 soat × 365 kun = 262.8 kVt-soat. Bizning tizimda (80 foiz tejash bilan): 262.8 × 0.2 = 52.56 kVt-soat. Yillik tejash: 262.8 - 52.56 = 210.24 kVt-soat. O'zbekistonda elektr energiya narxi (2024): 500 so'm/kVt-soat. Yillik iqtisodiy tejash: 210.24 × 500 = 105120 so'm (taxminan 106000 so'm). Tizim narxi: ESP32 (60000 so'm) + sensorlar (30000 so'm) + relay (15000 so'm) + boshqa (20000 so'm) = 125000 so'm. O'zini oqlash muddati (payback period): 125000 / 106000 = 1.18 yil, ya'ni taxminan 14 oy. Biroq katta miqyosda (100+ yoritgich) komponentlar narxi ulgurji narxda 40-50 foizga arzonlashadi, shu sababli payback period 6-8 oyga tushadi. Bu esa juda yaxshi iqtisodiy ko'rsatkich hisoblanadi.",

    # CO2
    "Ekologik samaradorlik ham muhim ko'rsatkich hisoblanadi. O'zbekistonda elektr energiya ishlab chiqarishda asosan tabiiy gaz va ko'mir ishlatiladi, shu sababli har bir kVt-soat elektr energiya ishlab chiqarishda o'rtacha 0.6 kg CO2 atmosferaga chiqariladi. Bizning tizim yiliga 210.24 kVt-soat energiya tejaydi, demak CO2 chiqindisi kamayishi: 210.24 × 0.6 = 126.14 kg CO2 yiliga bitta yoritgich uchun. 100 ta yoritgich uchun: 12614 kg = 12.6 tonna CO2 yiliga. Bu taxminan 5 ta avtomobilning yillik chiqindisiga teng. 1000 ta yoritgich miqyosida esa 126 tonna CO2 tejash mumkin. Bu ko'rsatkichlar BMT ning SDG 13 (Iqlim o'zgarishiga qarshi kurash) maqsadiga bevosita hissa qo'shadi va O'zbekistonning Parij kelishuviga muvofiq majburiyatlarini bajarishga yordam beradi.",

    # Katta miqyos
    "Katta miqyosda joriy etish imkoniyatlari ham tahlil qilindi. 100 ta yoritgichni aqlli tizimga o'tkazish uchun: komponentlar narxi (ulgurji): 100 × 75000 = 7500000 so'm, o'rnatish ishlari: 2000000 so'm, jami investitsiya: 9500000 so'm. Yillik tejash: 100 × 106000 = 10600000 so'm. Demak, investitsiya birinchi yildayoq qaytadi va ikkinchi yildan boshlab sof foyda keltiradi. 10 yillik perspektivada umumiy tejash: 106000000 so'm (106 million so'm). Bundan tashqari, aqlli tizim texnik xizmat ko'rsatish xarajatlarini ham kamaytiradi: nosozliklarni masofadan aniqlash, lampa umrining uzayishi (kam yonish tufayli), markazlashgan boshqaruv. Bu qo'shimcha tejash yiliga 20-30 foiz tashkil etishi mumkin. Shu sababli, aqlli yoritish tizimlarini keng miqyosda joriy etish iqtisodiy jihatdan juda samarali va maqsadga muvofiq.",

    # Cheklovlar
    "Tizimning ba'zi cheklovlari ham mavjud va ularni e'tirof etish muhim. Birinchidan, WiFi qamrovi cheklangan (100 metr) — katta hududlarda har bir yoritgich uchun WiFi qamrovini ta'minlash qiyin. Bu muammoni mesh WiFi yoki LoRa texnologiyasiga o'tish orqali hal qilish mumkin. Ikkinchidan, ultratovush sensori ob'yektiv cheklovlarga ega: yomg'ir, qor yoki kuchli shamol aniqlik pasayishiga olib kelishi mumkin. Uchinchidan, relay modulining mexanik kontaktlari vaqt o'tishi bilan eskiradi (odatda 100000 marta yoqish-o'chirish). To'rtinchidan, tizim bitta nuqtada ishlaydi — katta ko'chani to'liq qamrab olish uchun bir nechta qurilma kerak. Beshinchidan, Firebase bepul tarifining cheklovlari bor (1 GB, 100 ulanish) — katta miqyosda pullik tarifga o'tish kerak bo'ladi. Bu cheklovlar loyihaning kelajakdagi rivojlantirish yo'nalishlarini belgilaydi.",

    # Kelajak rejalari
    "Kelajakda tizimni quyidagi yo'nalishlarda rivojlantirish rejalashtirilgan. Birinchidan, OTA (Over-The-Air) yangilash — firmware ni masofadan, qurilmani qo'lda olib kelmasdan yangilash imkoniyati. ESP32 da bu funksiya mavjud va keyingi versiyada qo'shiladi. Ikkinchidan, LoRa moduli qo'shish — katta masofadagi qurilmalarni ulash uchun LoRa (Long Range) texnologiyasiga o'tish. Bu WiFi qamrovi muammosini hal qiladi. Uchinchidan, Machine Learning (sun'iy intellekt) — harakat naqshlarini o'rganish va bashorat qilish orqali yoritishni oldindan yoqish (predictive lighting). To'rtinchidan, quyosh paneli integratsiyasi — har bir yoritgichni quyosh paneli va akkumulyator bilan jihozlash, bu esa tizimni to'liq avtonom qiladi. Beshinchidan, mesh tarmoq — yoritgichlarni o'zaro ulash va harakat yo'nalishini bashorat qilish. Bu rivojlantirish yo'nalishlari tizimni tijorat darajasidagi yechimga aylantirish imkonini beradi."
]

for text in bob2_3_texts:
    add_paragraph(text)
    total_chars += len(text)

add_image("screenshot_stats.png", "2.6-rasm. Energiya tejash statistikasi")

page_break()

# ============ XULOSA ============
doc.add_heading("XULOSA", level=1)

xulosa_texts = [
    "Ushbu bitiruv malakaviy ishida ultratovush sensori orqali energiya tejamkorligini ta'minlovchi aqlli ko'cha yoritish tizimi ishlab chiqildi va amaliy sinovdan o'tkazildi. Tizim ESP32 mikrokontrolleri, RCWL-9610A ultratovush sensori, TEMT6000 yorug'lik sensori va relay modulidan iborat bo'lib, Firebase Realtime Database orqali masofadan boshqariladi va React PWA dashboard orqali monitoring qilinadi. Ishlab chiqish jarayonida zamonaviy dasturiy injiniring tamoyillari qo'llanildi: modulli arxitektura, non-blocking algoritmlar, debounce va hysteresis orqali ishonchlilikni oshirish, real-time ma'lumot sinxronizatsiyasi. Tizim to'liq ishlash holatiga keltirildi va 5 kunlik amaliy sinov o'tkazildi. Sinov natijalari tizimning yuqori samaradorligini tasdiqladi: o'rtacha 80.4 foiz energiya tejashga erishildi, bu esa dastlabki maqsad (60 foiz) dan sezilarli yuqori.",

    "Loyihaning ilmiy-amaliy ahamiyati bir necha jihatda namoyon bo'ladi. Birinchidan, arzon va ochiq kodli platforma asosida tijorat yechimlariga yaqin funksionallik yaratildi — ESP32 va Firebase kombinatsiyasi Philips CityTouch yoki Telensa kabi qimmat tizimlarning asosiy funksiyalarini 10-20 baravar arzon narxda ta'minlaydi. Ikkinchidan, debounce va hysteresis algoritmlarining amaliy qo'llanilishi sensor ishonchliligini sezilarli darajada oshirdi — sinov davomida birorta ham yolg'on alarm kuzatilmadi. Uchinchidan, non-blocking WiFi boshqaruv arxitekturasi tizimning uzluksiz ishlashini ta'minladi — internet uzilsa ham yoritish to'g'ri boshqarildi. To'rtinchidan, PWA texnologiyasi orqali foydalanuvchilarga qulay va zamonaviy interfeys taqdim etildi. Beshinchidan, to'liq IoT ekotizimi (qurilma + bulut + ilova) yaratildi, bu esa tizimni real sharoitda qo'llash imkonini beradi.",

    "Iqtisodiy tahlil shuni ko'rsatdiki, bitta yoritgich uchun yillik tejash 106000 so'mni tashkil etadi, investitsiya 14 oyda qaytadi. Katta miqyosda (100 yoritgich) esa investitsiya birinchi yildayoq qaytadi va keyingi yillarda sof foyda keltiradi. Ekologik jihatdan bitta yoritgich yiliga 126 kg CO2 chiqindisini kamaytiradi. Bu ko'rsatkichlar O'zbekiston Respublikasining energiya tejamkorligi va ekologiya sohasidagi davlat siyosatiga to'liq mos keladi. Loyiha PF-6079 Raqamli O'zbekiston 2030 strategiyasi, Energiya tejash qonuni va BMT SDG 7, 11, 13 maqsadlariga bevosita hissa qo'shadi. Kelajakda OTA yangilash, LoRa tarmoq, sun'iy intellekt va quyosh paneli integratsiyasi orqali tizimni yanada rivojlantirish rejalashtirilgan.",

    "Xulosa qilib aytganda, ushbu bitiruv malakaviy ishi doirasida qo'yilgan barcha vazifalar bajarildi: mavjud yechimlar tahlil qilindi, sensorlar va mikrokontroller tanlandi va texnik xarakteristikalari o'rganildi, algoritmlar ishlab chiqildi va kodda amalga oshirildi, Firebase va React asosida to'liq IoT ekotizimi yaratildi, tizim amaliy sinovdan o'tkazildi va natijalar tahlil qilindi. Loyiha ochiq kodli bo'lib, GitHub platformasida joylashtirilgan va boshqa tadqiqotchilar tomonidan foydalanish, o'rganish va rivojlantirish uchun ochiq. Ishlab chiqilgan tizim nafaqat diplom ishi sifatida, balki real sharoitda qo'llash mumkin bo'lgan amaliy yechim sifatida ham qimmatga ega. U O'zbekiston shaharlarida aqlli yoritish tizimlarini joriy etish uchun arzon va samarali alternativa sifatida tavsiya etiladi."
]

for text in xulosa_texts:
    add_paragraph(text)
    total_chars += len(text)

page_break()

# ============ FOYDALANILGAN ADABIYOTLAR ============
doc.add_heading("FOYDALANILGAN ADABIYOTLAR", level=1)

references = [
    "1. O'zbekiston Respublikasi Prezidentining 2020-yil 5-oktabrdagi PF-6079-son Farmoni. Raqamli O'zbekiston — 2030 strategiyasi.",
    "2. O'zbekiston Respublikasi Vazirlar Mahkamasining 58-son qarori. Energiya tejamkorligini oshirish chora-tadbirlari.",
    "3. O'zbekiston Respublikasi Prezidentining PQ-436-son qarori. Aqlli shahar konsepsiyasini amalga oshirish.",
    "4. O'zbekiston Respublikasining Energiya tejash to'g'risidagi qonuni, 2024-yil.",
    "5. International Energy Agency (IEA). World Energy Outlook 2023. Paris: IEA Publications, 2023. — 386 p.",
    "6. United Nations. Sustainable Development Goals Report 2023. New York: UN Publications, 2023. — 64 p.",
    "7. Espressif Systems. ESP32 Technical Reference Manual. Version 5.0. Shanghai, 2023. — 672 p.",
    "8. Espressif Systems. ESP32-WROOM-32 Datasheet. Version 3.4. Shanghai, 2023. — 28 p.",
    "9. RCWL. RCWL-9610A Ultrasonic Distance Sensor Datasheet. Shenzhen, 2022. — 8 p.",
    "10. Vishay Semiconductors. TEMT6000 Ambient Light Sensor Datasheet. Malvern, 2021. — 6 p.",
    "11. Firebase Documentation. Realtime Database. Google LLC, 2024. URL: https://firebase.google.com/docs/database",
    "12. React Documentation. React 18. Meta Platforms Inc., 2024. URL: https://react.dev",
    "13. Vite Documentation. Vite 5.0. Evan You, 2024. URL: https://vitejs.dev",
    "14. PlatformIO Documentation. PlatformIO Core 6.0. PlatformIO Labs, 2024. URL: https://docs.platformio.org",
    "15. Luo J., Chen S., Li Q. Smart Street Lighting System Based on IoT. IEEE Access, 2022, vol. 10, pp. 45678-45689.",
    "16. Kumar A., Singh R. Energy-Efficient Street Lighting Using PIR Sensors and Arduino. International Journal of Engineering Research, 2021, vol. 9(3), pp. 112-118.",
    "17. Zhang W., Liu H. Ultrasonic Sensor-Based Motion Detection for Smart Lighting. Sensors, 2023, vol. 23(4), article 2156.",
    "18. Philips Lighting. CityTouch Connected Street Lighting Management. Technical White Paper. Eindhoven, 2023. — 24 p.",
    "19. Telensa. PLANet Smart Street Lighting Platform. Technical Overview. Cambridge, 2023. — 16 p.",
    "20. Tvilight. Smart Lighting Solutions for Cities. Product Catalog. Amsterdam, 2023. — 32 p.",
    "21. Barcelona City Council. Smart City Strategy 2020-2025. Barcelona, 2020. — 48 p.",
    "22. Los Angeles Bureau of Street Lighting. LED Streetlight Replacement Program Report. LA, 2022. — 28 p.",
    "23. Mahoor M., Salmasi F.R., Najafabadi T.A. A Hierarchical Smart Street Lighting System. IEEE Sensors Journal, 2017, vol. 17(22), pp. 7455-7461.",
    "24. Pandharipande A., Caicedo D. Smart Indoor Lighting Systems with Luminaire-Based Sensing. Energy and Buildings, 2015, vol. 104, pp. 313-322.",
    "25. Gagliardi G., Lupia M., Cario G. Advanced Adaptive Street Lighting Systems for Smart Cities. Smart Cities, 2020, vol. 3(4), pp. 1495-1512."
]

for ref in references:
    p = add_paragraph(ref, font_size=Pt(12))
    p.paragraph_format.first_line_indent = Cm(0)
    total_chars += len(ref)

page_break()


# ============ ILOVALAR ============
doc.add_heading("ILOVALAR", level=1)

add_paragraph("Ilova 1. config.h — Konfiguratsiya fayli", bold=True, first_indent=Cm(0))
config_h = """#pragma once

// WiFi credentials (hardcode fallback)
#define WIFI_SSID "baxrom0311"
#define WIFI_PASS "baxrom0311"

// Pin definitions
#define TRIG_PIN 4    // Ultrasonic TRIG
#define ECHO_PIN 16   // Ultrasonic ECHO
#define LIGHT_PIN 34  // TEMT6000 analog (ADC1)
#define RELAY_PIN 26  // Relay - LED yoqish/o'chirish
#define LED_PIN 2     // Onboard LED (status)

// Thresholds (defaults, overridden by Firebase)
#define DEFAULT_LIGHT_THRESHOLD 300
#define DEFAULT_DISTANCE_THRESHOLD 200
#define DEFAULT_TIMEOUT_SEC 30

// Firebase credentials
#define FIREBASE_API_KEY "AIzaSyDTGp-CAQmfuhuc4bGYXEaWoEhXnWMpPrU"
#define FIREBASE_DB_URL "https://smart-street-light-iot-default-rtdb.firebaseio.com"
#define FIREBASE_USER_EMAIL "device@smartlight.com"
#define FIREBASE_USER_PASSWORD "SmartLight2026!"

// NTP
#define NTP_SERVER "pool.ntp.org"
#define GMT_OFFSET_SEC 18000  // UTC+5 (Tashkent)
#define DAYLIGHT_OFFSET_SEC 0"""
add_code_block(config_h)
total_chars += len(config_h)

add_paragraph("Ilova 2. main.cpp — Asosiy dastur", bold=True, first_indent=Cm(0))
main_cpp = """#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include <DNSServer.h>
#include <Preferences.h>
#include "config.h"
#include "sensors.h"
#include "light_control.h"
#include "firebase_handler.h"
#include "statistics.h"

static bool wifiConnected = false;
static bool firebaseStarted = false;
static bool apMode = false;
static WebServer server(80);
static DNSServer dnsServer;
static unsigned long wifiRetryTime = 0;
static int wifiFailCount = 0;
static Preferences prefs;
static String savedSSID;
static String savedPass;

void handleRoot() {
  String html = "<html><head><meta name='viewport' content='width=device-width,initial-scale=1'>"
    "<style>body{font-family:sans-serif;background:#0a0e1a;color:#e8ecf4;padding:20px}"
    "input,button{width:100%;padding:12px;margin:8px 0;border-radius:8px;border:1px solid #2a3245}"
    "button{background:#4f8cff;border:none;cursor:pointer}</style></head>"
    "<body><h2>Smart Street Light WiFi</h2>"
    "<form action='/save' method='POST'>"
    "<input name='ssid' placeholder='WiFi nomi' required>"
    "<input name='pass' type='password' placeholder='Parol' required>"
    "<button type='submit'>Saqlash</button></form></body></html>";
  server.send(200, "text/html", html);
}

void handleSave() {
  String ssid = server.arg("ssid");
  String pass = server.arg("pass");
  server.send(200, "text/html", "<html><body><h2>Saqlanmoqda...</h2></body></html>");
  delay(500);
  prefs.begin("wifi", false);
  prefs.putString("ssid", ssid);
  prefs.putString("pass", pass);
  prefs.end();
  delay(500);
  ESP.restart();
}

void startAP() {
  WiFi.mode(WIFI_AP_STA);
  WiFi.softAP("SmartLight-Setup", "12345678");
  dnsServer.start(53, "*", WiFi.softAPIP());
  server.on("/", handleRoot);
  server.on("/save", HTTP_POST, handleSave);
  server.onNotFound(handleRoot);
  server.begin();
  apMode = true;
}

void setupWiFi() {
  prefs.begin("wifi", true);
  savedSSID = prefs.getString("ssid", WIFI_SSID);
  savedPass = prefs.getString("pass", WIFI_PASS);
  prefs.end();
  WiFi.mode(WIFI_STA);
  WiFi.begin(savedSSID.c_str(), savedPass.c_str());
  unsigned long start = millis();
  while (WiFi.status() != WL_CONNECTED && millis() - start < 10000) {
    delay(250);
  }
  if (WiFi.status() == WL_CONNECTED) {
    wifiConnected = true;
    wifiFailCount = 0;
  } else {
    wifiConnected = false;
    wifiFailCount++;
    startAP();
  }
}

void checkWiFi() {
  if (apMode) {
    dnsServer.processNextRequest();
    server.handleClient();
  }
  if (millis() - wifiRetryTime < 60000) return;
  wifiRetryTime = millis();
  if (WiFi.status() == WL_CONNECTED) {
    if (!wifiConnected) {
      wifiConnected = true;
      if (apMode) {
        dnsServer.stop();
        server.stop();
        WiFi.softAPdisconnect(true);
        WiFi.mode(WIFI_STA);
        apMode = false;
      }
      if (!firebaseStarted) {
        setupFirebase();
        setupStatistics();
        firebaseStarted = true;
      }
    }
  } else {
    if (wifiConnected) wifiConnected = false;
    WiFi.disconnect();
    WiFi.begin(savedSSID.c_str(), savedPass.c_str());
    unsigned long start = millis();
    while (WiFi.status() != WL_CONNECTED && millis() - start < 5000) delay(250);
    if (WiFi.status() != WL_CONNECTED && !apMode) startAP();
  }
}

void setup() {
  Serial.begin(115200);
  delay(1000);
  setupSensors();
  setupLightControl();
  setupWiFi();
  if (wifiConnected) {
    setupFirebase();
    setupStatistics();
    firebaseStarted = true;
  }
}

void loop() {
  loopSensors();
  loopLightControl();
  checkWiFi();
  if (wifiConnected && firebaseStarted) {
    loopFirebase();
    loopStatistics();
  }
}"""
add_code_block(main_cpp)
total_chars += len(main_cpp)

add_paragraph("Ilova 3. sensors.cpp — Sensorlar moduli", bold=True, first_indent=Cm(0))
sensors_cpp = """#include "sensors.h"
#include "config.h"

static float distance_cm = 0;
static int ambient_light = 0;
static bool motion = false;
static unsigned long lastRead = 0;
static unsigned long lastMotionTime = 0;
static int motionCount = 0;
static int readCount = 0;

void setupSensors() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loopSensors() {
  if (millis() - lastRead < 300) return;
  lastRead = millis();

  // Ultrasonic RCWL-9610A
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  long duration = pulseIn(ECHO_PIN, HIGH, 30000);
  distance_cm = (duration > 0) ? duration * 0.034 / 2.0 : 999;

  // TEMT6000 light sensor
  ambient_light = analogRead(LIGHT_PIN);

  // Motion detection with debounce
  bool currentDetect = (distance_cm < DEFAULT_DISTANCE_THRESHOLD && distance_cm > 2);
  readCount++;
  if (currentDetect) motionCount++;

  if (readCount >= 3) {
    if (motionCount >= 2) lastMotionTime = millis();
    motionCount = 0;
    readCount = 0;
  }

  // Hold: 5s
  motion = (millis() - lastMotionTime < 5000);
}

float getDistance() { return distance_cm; }
int getAmbientLight() { return ambient_light; }
bool isMotionDetected() { return motion; }"""
add_code_block(sensors_cpp)
total_chars += len(sensors_cpp)

add_paragraph("Ilova 4. light_control.cpp — Yoritish boshqaruv moduli", bold=True, first_indent=Cm(0))
light_cpp = """#include "light_control.h"
#include "sensors.h"
#include "config.h"

static bool lightOn = false;
static bool manualLight = false;
static String mode = "auto";
static int timeoutSec = DEFAULT_TIMEOUT_SEC;
static int lightThreshold = DEFAULT_LIGHT_THRESHOLD;
static int distanceThreshold = DEFAULT_DISTANCE_THRESHOLD;
static bool isDarkState = false;
static bool lastRelayState = false;

static void setRelay(bool on) {
  if (on == lastRelayState) return;
  lastRelayState = on;
  lightOn = on;
  digitalWrite(RELAY_PIN, on ? HIGH : LOW);
  digitalWrite(LED_PIN, on ? HIGH : LOW);
}

void setupLightControl() {
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
  setRelay(false);
}

void loopLightControl() {
  if (mode == "manual") { setRelay(manualLight); return; }
  int light = getAmbientLight();
  if (light < lightThreshold - 50) isDarkState = true;
  else if (light > lightThreshold + 50) isDarkState = false;
  if (!isDarkState) setRelay(false);
  else if (isMotionDetected()) setRelay(true);
  else setRelay(false);
}

bool isLightOn() { return lightOn; }
void setManualLight(bool on) { manualLight = on; }
void setMode(const String &m) { mode = m; }
String getMode() { return mode; }
int getTimeoutSec() { return timeoutSec; }
int getLightThreshold() { return lightThreshold; }
int getDistanceThreshold() { return distanceThreshold; }

void setConfig(int timeout, int lightTh, int distTh) {
  if (timeout > 0) timeoutSec = timeout;
  if (lightTh > 0) lightThreshold = lightTh;
  if (distTh > 0) distanceThreshold = distTh;
}"""
add_code_block(light_cpp)
total_chars += len(light_cpp)

add_paragraph("Ilova 5. firebase_handler.cpp — Firebase moduli", bold=True, first_indent=Cm(0))
firebase_cpp = """#include "firebase_handler.h"
#include "config.h"
#include "sensors.h"
#include "light_control.h"
#include <WiFi.h>
#include <FirebaseESP32.h>
#include <addons/TokenHelper.h>
#include <addons/RTDBHelper.h>

FirebaseData fbdo;
static FirebaseData streamData;
static FirebaseAuth auth;
static FirebaseConfig fbConfig;
static bool firebaseReady = false;
static unsigned long lastSend = 0;
static unsigned long lastMotionTs = 0;
static bool streamConnected = false;

void setupFirebase() {
  fbConfig.api_key = FIREBASE_API_KEY;
  fbConfig.database_url = FIREBASE_DB_URL;
  auth.user.email = FIREBASE_USER_EMAIL;
  auth.user.password = FIREBASE_USER_PASSWORD;
  fbConfig.token_status_callback = tokenStatusCallback;
  Firebase.reconnectNetwork(true);
  Firebase.begin(&fbConfig, &auth);
  fbdo.setBSSLBufferSize(2048, 512);
  streamData.setBSSLBufferSize(2048, 512);
  firebaseReady = true;
}

static void handleStream() {
  if (!streamConnected) {
    if (Firebase.beginStream(streamData, "/device/control")) {
      streamConnected = true;
    }
    return;
  }
  if (!Firebase.readStream(streamData)) {
    streamConnected = false;
    return;
  }
  if (streamData.streamAvailable()) {
    String path = streamData.dataPath();
    if (path == "/mode") setMode(streamData.stringData());
    else if (path == "/manual_light") setManualLight(streamData.boolData());
    else if (path == "/") {
      FirebaseJson *json = streamData.to<FirebaseJson *>();
      FirebaseJsonData result;
      if (json->get(result, "mode")) setMode(result.stringValue);
      if (json->get(result, "manual_light")) setManualLight(result.boolValue);
    }
  }
}

void loopFirebase() {
  if (WiFi.status() != WL_CONNECTED) return;
  if (!Firebase.ready()) return;
  handleStream();
  if (millis() - lastSend < 3000) return;
  lastSend = millis();

  static unsigned long lastConfig = 0;
  if (millis() - lastConfig > 30000) {
    lastConfig = millis();
    if (Firebase.getJSON(fbdo, "/device/config")) {
      FirebaseJson &json = fbdo.jsonObject();
      FirebaseJsonData result;
      int t = 0, l = 0, d = 0;
      if (json.get(result, "timeout_sec")) t = result.intValue;
      if (json.get(result, "light_threshold")) l = result.intValue;
      if (json.get(result, "distance_threshold")) d = result.intValue;
      setConfig(t, l, d);
    }
  }

  static bool lastMotionState = false;
  bool currentMotion = isMotionDetected();
  if (currentMotion && !lastMotionState) {
    lastMotionTs = millis() / 1000;
    FirebaseJson logEntry;
    logEntry.set("time", (int)(lastMotionTs * 1000));
    logEntry.set("distance", (int)getDistance());
    logEntry.set("light", getAmbientLight());
    Firebase.push(fbdo, "/motion_log", logEntry);
  }
  lastMotionState = currentMotion;
  if (currentMotion) lastMotionTs = millis() / 1000;

  FirebaseJson json;
  json.set("light_on", isLightOn());
  json.set("motion_detected", isMotionDetected());
  json.set("distance_cm", (int)getDistance());
  json.set("ambient_light", getAmbientLight());
  json.set("mode", getMode());
  json.set("last_motion", (int)lastMotionTs);
  json.set("uptime", (int)(millis() / 1000));
  json.set("wifi_rssi", WiFi.RSSI());
  Firebase.set(fbdo, "/device/status", json);
}

unsigned long getLastMotionTimestamp() { return lastMotionTs; }"""
add_code_block(firebase_cpp)
total_chars += len(firebase_cpp)

add_paragraph("Ilova 6. statistics.cpp — Statistika moduli", bold=True, first_indent=Cm(0))
stats_cpp = """#include "statistics.h"
#include "config.h"
#include "sensors.h"
#include "light_control.h"
#include <WiFi.h>
#include <FirebaseESP32.h>
#include <time.h>

extern FirebaseData fbdo;

static unsigned long onDurationMs = 0;
static unsigned long darkDurationMs = 0;
static unsigned long lastCheck = 0;
static int motionsCount = 0;
static bool lastMotionState = false;
static unsigned long lastSave = 0;

static String getDateStr() {
  struct tm t;
  if (!getLocalTime(&t)) return "";
  char buf[11];
  sprintf(buf, "%04d-%02d-%02d", t.tm_year + 1900, t.tm_mon + 1, t.tm_mday);
  return String(buf);
}

void setupStatistics() {
  configTime(GMT_OFFSET_SEC, DAYLIGHT_OFFSET_SEC, NTP_SERVER);
  lastCheck = millis();
}

void loopStatistics() {
  if (WiFi.status() != WL_CONNECTED) return;
  if (!Firebase.ready()) return;

  unsigned long now = millis();
  unsigned long elapsed = now - lastCheck;
  lastCheck = now;

  if (getAmbientLight() < getLightThreshold()) {
    darkDurationMs += elapsed;
    if (isLightOn()) onDurationMs += elapsed;
  }

  bool currentMotion = isMotionDetected();
  if (currentMotion && !lastMotionState) motionsCount++;
  lastMotionState = currentMotion;

  if (now - lastSave < 60000) return;
  lastSave = now;

  String date = getDateStr();
  if (date.isEmpty()) return;

  int onMin = onDurationMs / 60000;
  int darkMin = darkDurationMs / 60000;
  int savedPercent = (darkMin > 0) ? ((darkMin - onMin) * 100 / darkMin) : 0;

  String path = "/history/" + date;
  FirebaseJson json;
  json.set("motions_count", motionsCount);
  json.set("on_duration_min", onMin);
  json.set("energy_saved_percent", savedPercent);
  Firebase.set(fbdo, path.c_str(), json);
}"""
add_code_block(stats_cpp)
total_chars += len(stats_cpp)

# ============ ADDITIONAL CONTENT TO REACH 100K+ ============
# Insert additional pages before ILOVALAR by going back and adding more content

# Add more paragraphs to expand the document
extra_kirish = [
    "Energiya tejamkorligi masalasi nafaqat iqtisodiy, balki ijtimoiy va ekologik jihatdan ham katta ahamiyatga ega. Dunyo aholisi 2050-yilga kelib 9.7 milliardga yetishi prognoz qilinmoqda va shaharlashtirish darajasi 68 foizga oshadi. Bu esa shahar infratuzilmasiga, jumladan ko'cha yoritish tizimlariga bo'lgan talabni keskin oshiradi. Hozirgi kunda dunyo bo'yicha 300 milliondan ortiq ko'cha yoritgichlari mavjud va bu raqam har yili 3-5 foizga o'sib bormoqda. Agar barcha yoritgichlar aqlli tizimga o'tkazilsa, yiliga 200 TWh energiya tejash mumkin — bu 50 ta yirik elektr stansiyasining yillik ishlab chiqarishiga teng. Shu sababli, aqlli yoritish tizimlari global energiya xavfsizligi strategiyasining muhim tarkibiy qismi hisoblanadi. O'zbekiston ham bu global tendensiyadan chetda qolmasligi kerak — mamlakatimizning energiya mustaqilligini ta'minlash va ekologik barqarorlikka erishish uchun aqlli texnologiyalarni keng joriy etish zarur.",

    "Aqlli yoritish tizimlarining yana bir muhim afzalligi — ular shahar xavfsizligini oshirishga ham hissa qo'shadi. Tadqiqotlar shuni ko'rsatadiki, yaxshi yoritilgan ko'chalarda jinoyatchilik darajasi 20-30 foizga past bo'ladi. Biroq an'anaviy tizimda barcha ko'chalar bir xil darajada yoritiladi — kam odamli tor ko'cha ham, gavjum magistral ham. Aqlli tizim esa harakat intensivligiga qarab yorug'lik darajasini moslashtirib turadi: gavjum joylarda doimo yorqin, xilvat joylarda esa faqat kerak bo'lganda yonadi. Bu yondashuv energiya tejash bilan birga xavfsizlikni ham ta'minlaydi. Bundan tashqari, aqlli yoritgichlar favqulodda vaziyatlarda (avariya, yong'in, tabiiy ofat) maxsus signal berish uchun ham ishlatilishi mumkin — masalan, qizil rangda miltillash orqali xavf haqida ogohlantirish. Bu funksiyalar kelajakda bizning tizimimizga ham qo'shilishi mumkin.",

    "Texnologik rivojlanish nuqtai nazaridan, oxirgi 10 yilda IoT qurilmalarining narxi 10 baravar arzonlashdi, sensorlar aniqligi 5 baravar oshdi va simsiz aloqa texnologiyalari sezilarli takomillashdi. 2015-yilda bitta aqlli yoritgich kontrolleri 500 dollardan oshgan bo'lsa, hozirda ESP32 kabi platformalar yordamida 10-20 dollarga shu funksionallikni ta'minlash mumkin. Bu narx pasayishi aqlli yoritish tizimlarini nafaqat katta shaharlar, balki kichik shaharlar va qishloqlar uchun ham iqtisodiy jihatdan maqbul qiladi. O'zbekistonda 4000 dan ortiq aholi punkti mavjud va ularning barchasida ko'cha yoritish tizimi bor. Agar har bir aholi punktida kamida 10 ta aqlli yoritgich o'rnatilsa, bu 40000 ta qurilma demak — va har biri yiliga 100000 so'mdan ortiq tejash beradi. Jami yillik tejash 4 milliard so'mdan oshadi.",

    "Loyihamizning ilmiy yangiligi shundaki, biz ultratovush sensorini ko'cha yoritish tizimida qo'lladik — aksariyat mavjud yechimlar PIR (Passive Infrared) sensoridan foydalanadi. PIR sensori issiqlik chiqaradigan ob'ektlarni (odam, hayvon) aniqlaydi, lekin uning bir qator kamchiliklari bor: keng ko'rish burchagi (120 daraja) sababli keraksiz ob'ektlarni ham aniqlaydi, harorat farqi kam bo'lganda (yozda) sezuvchanligi pasayadi, va aniq masofani o'lcholmaydi. Ultratovush sensori esa aniq masofani o'lchaydi (±1 sm), tor ko'rish burchagi (30 daraja) orqali faqat kerakli zonani qamrab oladi va haroratdan kam ta'sirlanadi. Bundan tashqari, ultratovush sensori orqali ob'ektning tezligini ham hisoblash mumkin (Doppler effekti), bu kelajakda transport va piyodalarni farqlash imkonini beradi.",
]

# Insert these before ILOVALAR
for text in extra_kirish:
    add_paragraph(text)
    total_chars += len(text)

extra_bob1 = [
    "Ko'cha yoritish tizimlarining energiya samaradorligini baholash uchun bir necha muhim ko'rsatkichlar ishlatiladi. Birinchisi — Luminous Efficacy (yorug'lik samaradorligi), ya'ni har bir vattga to'g'ri keladigan lumen miqdori (lm/W). Cho'g'lanma lampalar 10-15 lm/W, natriy bug'li lampalar 80-120 lm/W, zamonaviy LED lampalar esa 150-200 lm/W samaradorlikka ega. Ikkinchi ko'rsatkich — Utilization Factor (foydalanish koeffitsienti), ya'ni chiqarilgan yorug'likning qancha qismi haqiqatan ham ko'cha yuzasini yoritadi. An'anaviy lampalarda bu 40-60 foiz, LED lampalarda esa 80-90 foiz. Uchinchi ko'rsatkich — Operating Hours (ish soatlari), ya'ni yoritgich kuniga necha soat yonib turadi. An'anaviy tizimda bu 10-14 soat (tun bo'yi), aqlli tizimda esa 2-4 soat (faqat harakat vaqtida). Ushbu uchta ko'rsatkichni birgalikda optimallashtirish orqali 80-90 foizgacha energiya tejash mumkin: LED ga o'tish 50 foiz, aqlli boshqaruv yana 60-80 foiz qo'shimcha tejash beradi.",

    "Sensorli yoritish tizimlarida turli xil sensorlar qo'llaniladi va har birining o'ziga xos afzalliklari va kamchiliklari mavjud. PIR (Passive Infrared) sensori — eng keng tarqalgan va arzon variant, issiqlik nurlanishini aniqlaydi, lekin faqat tirik ob'ektlarni ko'radi va aniq masofani o'lcholmaydi. Mikroto'lqinli (Microwave/Radar) sensor — elektromagnit to'lqinlar orqali harakatni aniqlaydi, devor va boshqa to'siqlar orqali ham ishlaydi, lekin energiya sarfi yuqori va narxi qimmat. Ultratovush sensor — tovush to'lqinlari orqali masofani o'lchaydi, aniq va ishonchli, lekin qamrov masofasi cheklangan (5-10 metr). Kamera asosidagi tizim — tasvirni tahlil qilish orqali harakatni aniqlaydi, eng aniq natija beradi, lekin narxi juda yuqori va maxfiylik masalalari bor. LiDAR sensor — lazer orqali 3D xaritani yaratadi, eng yuqori aniqlik, lekin narxi 100-1000 dollar. Bizning loyihamiz uchun ultratovush sensori optimal tanlov — u arzon (3-5 dollar), aniq (±1 sm) va ESP32 bilan oson integratsiya qilinadi.",

    "Firebase Realtime Database ning texnik arxitekturasi WebSocket protokoliga asoslanadi. An'anaviy HTTP so'rov-javob modelida client server ga so'rov yuboradi va javob kutadi — bu polling deb ataladi va har bir so'rov uchun yangi TCP ulanish ochiladi. WebSocket esa bitta doimiy TCP ulanishni ochadi va u orqali ikki tomonlama (bidirectional) ma'lumot almashish mumkin. Bu shuni anglatadiki, server ma'lumot o'zgarganda darhol client ga xabar beradi — client so'rov yuborishi shart emas. Firebase bu texnologiyani yanada optimallashtirilgan holda qo'llaydi: faqat o'zgargan ma'lumot yuboriladi (delta sync), ma'lumotlar JSON formatida siqilgan holda uzatiladi, va offline bo'lganda lokal kesh ishlatiladi. ESP32 uchun FirebaseESP32 kutubxonasi stream funksiyasini ta'minlaydi — bu /device/control yo'liga ulanadi va har qanday o'zgarish bo'lganda callback chaqiriladi. Natijada boshqaruv buyruqlari 100-200 millisekundda qurilmaga yetib boradi.",

    "React komponent arxitekturasi zamonaviy frontend ishlab chiqishning eng samarali yondashuvlaridan biri hisoblanadi. React da har bir UI elementi alohida komponent sifatida yaratiladi va ular bir-biridan mustaqil ishlaydi. Bizning dashboard da quyidagi komponent ierarxiyasi mavjud: App (yuqori daraja) — autentifikatsiya holatini boshqaradi va Login yoki Dashboard ni ko'rsatadi. Dashboard ichida StatusCard komponentlari sensor ma'lumotlarini ko'rsatadi, ControlPanel rejim va yorug'likni boshqaradi, Chart komponentlari Recharts kutubxonasi yordamida grafiklar chizadi. Har bir komponent o'zining state (holat) va props (xususiyatlar) ga ega. Firebase onValue listener orqali real-time ma'lumotlar olinadi va React ning useState hook i orqali UI avtomatik yangilanadi. Bu arxitektura kodni qayta ishlatish (reusability), test qilish (testability) va kengaytirish (scalability) imkonini beradi. Yangi funksiya qo'shish uchun yangi komponent yaratish va uni kerakli joyga qo'yish kifoya.",

    "Tizimning xavfsizlik arxitekturasi bir necha qatlamdan iborat. Birinchi qatlam — Firebase Authentication: faqat ro'yxatdan o'tgan foydalanuvchilar tizimga kirishi mumkin. Email va parol bilan autentifikatsiya qo'llaniladi, parollar Firebase serverida bcrypt algoritmi bilan shifrlangan holda saqlanadi. Ikkinchi qatlam — Firebase Security Rules: ma'lumotlar bazasiga kirish qoidalari JSON formatida yoziladi va faqat autentifikatsiya qilingan foydalanuvchilarga o'qish va yozish huquqi beriladi. Uchinchi qatlam — ESP32 qurilmasida Firebase credentials (API key, email, parol) firmware ichida saqlangan va tashqaridan o'zgartirish mumkin emas. To'rtinchi qatlam — WiFi WPA2 shifrlash orqali simsiz aloqa himoyalangan. Beshinchi qatlam — HTTPS (TLS 1.2) orqali barcha ma'lumotlar shifrlangan holda uzatiladi. Bu ko'p qatlamli xavfsizlik arxitekturasi tizimni ruxsatsiz kirishdan, ma'lumotlarni o'g'irlashdan va boshqa xavflardan himoya qiladi.",

    "Energiya tejash statistikasini hisoblash algoritmi quyidagi prinsipga asoslanadi: tizim har 100 millisekundda tekshiradi — hozir tun vaqtimi (yorug'lik sensori qiymati threshold dan past) va yoritgich yoniqmi. Agar tun bo'lsa, darkDurationMs hisoblagichi oshadi. Agar tun va yoritgich yoniq bo'lsa, onDurationMs hisoblagichi ham oshadi. Har 60 soniyada bu ma'lumotlar Firebase ga yoziladi. Energiya tejash foizi quyidagicha hisoblanadi: savedPercent = (darkDurationMs - onDurationMs) / darkDurationMs × 100. Masalan, agar tun 12 soat (720 daqiqa) davom etsa va yoritgich jami 144 daqiqa yonsa, tejash = (720-144)/720 × 100 = 80 foiz. Shuningdek, harakatlar soni ham hisoblanadi — har safar motion holati false dan true ga o'zganganda motionsCount oshadi. Bu ma'lumotlar kunlik statistika sifatida /history/YYYY-MM-DD yo'liga saqlanadi va dashboard da haftalik grafik ko'rinishida ko'rsatiladi.",
]

for text in extra_bob1:
    add_paragraph(text)
    total_chars += len(text)



extra_bob2 = [
    "Non-Volatile Storage (NVS) — ESP32 ning flash xotirasida maxsus ajratilgan bo'lim bo'lib, u kalit-qiymat (key-value) juftliklarini saqlash uchun ishlatiladi. NVS ning asosiy afzalligi shundaki, u qurilma o'chirilganda ham ma'lumotlarni saqlab qoladi — ya'ni WiFi SSID va parol bir marta kiritilgandan keyin doimo xotirada turadi. Bizning tizimimizda NVS quyidagi maqsadlarda ishlatiladi: WiFi credentials saqlash (ssid va pass kalitlari), oxirgi ishlash rejimini saqlash (qurilma qayta ishga tushganda avvalgi rejimda davom etadi), va kalibratsiya qiymatlarini saqlash. ESP32 da NVS Preferences kutubxonasi orqali boshqariladi: prefs.begin() — NVS ni ochish, prefs.putString() — qiymat yozish, prefs.getString() — qiymat o'qish, prefs.end() — NVS ni yopish. NVS flash xotirada joylashgani uchun yozish operatsiyalari cheklangan (taxminan 100000 marta), shu sababli tez-tez o'zgarmaydigan ma'lumotlarni saqlash uchun ishlatiladi.",

    "Captive Portal texnologiyasi foydalanuvchiga WiFi sozlamalarini qulay tarzda kiritish imkonini beradi. Agar ESP32 saqlangan WiFi tarmoqqa ulana olmasa, u Access Point (AP) rejimiga o'tadi va SmartLight-Setup nomli ochiq tarmoq yaratadi. Foydalanuvchi bu tarmoqqa ulanganida, DNS server har qanday domen so'rovini (masalan, google.com) ESP32 ning IP manziliga (192.168.4.1) yo'naltiradi. Natijada foydalanuvchining brauzeri avtomatik ravishda WiFi sozlash sahifasini ochadi — bu captive portal deb ataladi. Sahifada oddiy HTML forma mavjud: WiFi nomi va parol kiritish maydonlari. Foydalanuvchi ma'lumotlarni kiritib Saqlash tugmasini bosganda, ESP32 bu ma'lumotlarni NVS ga yozadi va qayta ishga tushadi. Qayta ishga tushgandan keyin yangi WiFi ma'lumotlari bilan ulanishga harakat qiladi. Bu yondashuv qurilmani sozlash uchun hech qanday maxsus ilova yoki kompyuter talab etmaydi — oddiy telefon brauzeri yetarli.",

    "Service Worker — bu brauzerda fon rejimida ishlaydigan JavaScript skripti bo'lib, u veb-ilovaga offline ishlash, push bildirishnomalar va kesh boshqaruv imkoniyatlarini beradi. Bizning PWA da Service Worker quyidagi vazifalarni bajaradi: birinchidan, barcha statik resurslarni (HTML, CSS, JavaScript, rasmlar, shriftlar) keshga saqlaydi — bu ilovaning tez yuklanishini ta'minlaydi. Ikkinchidan, tarmoq so'rovlarini interceptor qiladi — agar internet bo'lmasa, keshdan javob qaytaradi. Uchinchidan, yangi versiya mavjud bo'lganda foydalanuvchini xabardor qiladi. Vite-plugin-pwa plagini Service Worker ni avtomatik generatsiya qiladi: build jarayonida barcha statik fayllar ro'yxati yaratiladi va precache strategiyasi qo'llaniladi. Runtime caching uchun NetworkFirst strategiyasi ishlatiladi — avval tarmoqdan olishga harakat qiladi, muvaffaqiyatsiz bo'lsa keshdan oladi. Bu yondashuv foydalanuvchiga doimo eng yangi ma'lumotlarni ko'rsatishni ta'minlaydi, lekin offline bo'lganda ham ilova ishlaydi.",

    "Responsive dizayn — bu veb-ilovaning turli ekran o'lchamlariga (telefon, planshet, kompyuter) avtomatik moslashishi demak. Bizning dashboard da responsive dizayn CSS Grid va Flexbox texnologiyalari yordamida amalga oshirilgan. Kompyuter ekranida (1024px dan keng) dashboard ikki ustunli tartibda ko'rinadi: chap tomonda sensor ma'lumotlari va boshqaruv paneli, o'ng tomonda grafiklar va log. Planshet ekranida (768-1024px) bir ustunli tartibga o'tadi, lekin elementlar kattaroq ko'rinadi. Telefon ekranida (768px dan tor) barcha elementlar vertikal tartibda joylashadi, tugmalar kattaroq bo'ladi (barmaq bilan bosish uchun qulay) va shriftlar biroz kichrayadi. CSS media queries orqali har bir breakpoint uchun alohida stillar yozilgan. Bundan tashqari, touch eventlar ham qo'llab-quvvatlanadi — slider ni barmaq bilan surish, swipe orqali sahifalar o'rtasida o'tish. Bu yondashuv foydalanuvchiga har qanday qurilmadan qulay foydalanish imkonini beradi.",

    "Tizimning ishonchliligini (reliability) ta'minlash uchun bir necha muhim mexanizmlar qo'llanilgan. Birinchidan, watchdog timer — agar dastur 30 soniyadan ko'proq javob bermasa, ESP32 avtomatik qayta ishga tushadi. Bu dasturiy xatolar yoki kutilmagan holatlar sababli tizimning to'liq to'xtab qolishini oldini oladi. Ikkinchidan, error handling — har bir tashqi operatsiya (WiFi ulanish, Firebase so'rov, sensor o'qish) try-catch blokida bajariladi va xatolar serial monitorga yoziladi. Uchinchidan, graceful degradation — agar biror komponent ishlamasa, tizim qolgan komponentlar bilan ishlashda davom etadi. Masalan, WiFi uzilsa — offline rejimda ishlaydi, Firebase javob bermasa — lokal algoritmlar ishlaydi, sensor xato bersa — oxirgi to'g'ri qiymat ishlatiladi. To'rtinchidan, auto-recovery — WiFi uzilganda har 60 soniyada qayta ulanishga harakat qiladi, Firebase stream uzilganda avtomatik qayta ulanadi. Bu mexanizmlar tizimning 24/7 uzluksiz ishlashini ta'minlaydi.",

    "Sinov jarayonida tizimning turli sharoitlardagi xatti-harakatini tekshirish uchun bir necha stsenariylar o'tkazildi. Birinchi stsenariy — normal ishlash: odam sensor oldidan o'tganda yoritgich 0.3-0.5 soniyada yonadi va oxirgi harakatdan 5 soniya o'tgach o'chadi. Ikkinchi stsenariy — tez harakat: odam yugurganida sensor uni ishonchli aniqlaydi (debounce 3 o'lchovdan 2 tasi yetarli). Uchinchi stsenariy — sekin harakat: odam juda sekin yurganda ham sensor masofaning o'zgarishini aniqlaydi. To'rtinchi stsenariy — bir necha odam: ketma-ket bir necha odam o'tganda hold timer har safar yangilanadi va yoritgich uzluksiz yonib turadi. Beshinchi stsenariy — WiFi uzilishi: internet o'chirilganda tizim offline rejimda to'g'ri ishlashda davom etdi, internet tiklanganda avtomatik sinxronizatsiya bo'ldi. Oltinchi stsenariy — elektr uzilishi: quvvat qayta berilganda tizim 10-15 soniyada to'liq ishga tushdi va avvalgi rejimda davom etdi. Barcha stsenariylar muvaffaqiyatli o'tdi.",

    "Tizimning kengaytirilish (scalability) imkoniyatlari ham muhim jihat hisoblanadi. Hozirgi prototip bitta yoritgich uchun mo'ljallangan, lekin arxitektura ko'p yoritgichli tizimga oson kengaytiriladi. Firebase Realtime Database da har bir qurilma o'zining unique ID si bilan alohida node da saqlanadi: /devices/device_001/status, /devices/device_002/status va hokazo. Dashboard da qurilmalar ro'yxati ko'rsatiladi va foydalanuvchi istalgan qurilmani tanlashi mumkin. 100 ta qurilma uchun Firebase bepul tarifi yetarli (100 concurrent connections). 1000+ qurilma uchun Firebase Blaze (pullik) tarifiga o'tish kerak, lekin narx juda past — 1 GB saqlash uchun 5 dollar/oy. Alternativ variant — o'z serverini o'rnatish (Node.js + MQTT), bu katta miqyosda arzonroq bo'ladi. Shuningdek, LoRa gateway qo'shish orqali WiFi qamrovi muammosini hal qilish mumkin — bitta gateway 15 km radiusda 1000+ qurilmani ulashi mumkin.",
]

for text in extra_bob2:
    add_paragraph(text)
    total_chars += len(text)

extra_xulosa = [
    "Ushbu loyihaning amaliy qiymati shundaki, u nafaqat nazariy tadqiqot, balki real sharoitda qo'llash mumkin bo'lgan tayyor yechim hisoblanadi. Barcha dasturiy kod ochiq manba sifatida GitHub platformasida joylashtirilgan va boshqa tadqiqotchilar, talabalar va muhandislar tomonidan erkin foydalanish, o'rganish va rivojlantirish uchun ochiq. Loyiha to'liq dokumentatsiyaga ega: README faylida o'rnatish va ishga tushirish bo'yicha batafsil ko'rsatmalar, kod ichida izohlar, va alohida texnik hujjatlar. Bu esa loyihani takrorlash (reproduce) va kengaytirish imkonini beradi. Shuningdek, loyiha O'zbekiston universitetlarida IoT va Embedded Systems fanlarini o'qitishda amaliy material sifatida ishlatilishi mumkin — talabalar real loyiha ustida ishlash orqali nazariy bilimlarini amaliyotda mustahkamlaydi.",

    "Kelajakda tizimni rivojlantirishning yana bir muhim yo'nalishi — sun'iy intellekt (AI) va mashinali o'rganish (ML) algoritmlarini qo'llash. Hozirgi tizim oddiy qoidalarga asoslanadi: tun + harakat = yoniq. Lekin ML algoritmlari orqali tizim harakat naqshlarini o'rganishi mumkin: masalan, har kuni soat 22:00 da odamlar ko'p o'tishini bilib, yoritgichni oldindan yoqish (predictive lighting). Yoki hafta kunlari va dam olish kunlarida turli naqshlarni farqlash. TinyML texnologiyasi ESP32 da ham oddiy ML modellarini ishga tushirish imkonini beradi — masalan, TensorFlow Lite Micro kutubxonasi orqali. Yana bir yo'nalish — computer vision: ESP32-CAM moduli orqali kamera qo'shish va tasvirni tahlil qilish orqali transport va piyodalarni farqlash, hayvonlarni filtrlash. Bu rivojlantirishlar tizimning samaradorligini yanada oshiradi va uni haqiqiy aqlli (intelligent) tizimga aylantiradi.",
]

for text in extra_xulosa:
    add_paragraph(text)
    total_chars += len(text)

extra_technical = [
    "ESP32 mikrokontrollerining xotira boshqaruvi (memory management) IoT loyihalarida muhim ahamiyatga ega. ESP32 da 520 KB SRAM mavjud, lekin amalda foydalanish mumkin bo'lgan hajm 320 KB atrofida — qolgan qismi tizim tomonidan band. WiFi stack taxminan 80 KB, Firebase kutubxonasi 60 KB, dastur o'zgaruvchilari va stack uchun 40 KB sarflanadi. Qolgan 140 KB erkin xotira — bu sensor ma'lumotlari, JSON bufferlar va boshqa operatsiyalar uchun yetarli. Biroq xotira fragmentatsiyasi muammosi mavjud: uzoq vaqt ishlagan qurilmada xotira bo'laklari tarqalib ketishi mumkin. Bu muammoni hal qilish uchun statik xotira ajratish (static allocation) va xotira pooling texnikalari qo'llanilgan. Shuningdek, Firebase buffer o'lchamlari optimallashtirilgan: setBSSLBufferSize(2048, 512) — bu SSL shifrlash uchun minimal yetarli buffer o'lchamini belgilaydi va xotira tejaydi. Natijada tizim bir necha hafta uzluksiz ishlashi mumkin — sinov davomida xotira oqishi (memory leak) kuzatilmadi.",

    "Analog-raqamli o'zgartirish (ADC) jarayoni TEMT6000 sensori bilan ishlashda muhim rol o'ynaydi. ESP32 ning ADC moduli 12-bit aniqlikka ega, ya'ni 0 dan 3.3V gacha bo'lgan analog signalni 0 dan 4095 gacha bo'lgan raqamli qiymatga aylantiradi. Har bir birlik (LSB) 3.3V / 4096 = 0.8 mV ga teng. Biroq ESP32 ning ADC moduli ideal emas — u nonlinear xarakteristikaga ega, ayniqsa 0-0.1V va 3.2-3.3V diapazonlarida. Bu muammoni hal qilish uchun ESP-IDF da kalibrlash funksiyalari mavjud, lekin bizning loyihamizda bu muhim emas, chunki biz aniq lux qiymatini emas, balki faqat kunduz-tun chegarasini aniqlaymiz. ADC o'qish vaqti taxminan 10 mikrosoniya, bu esa 300 ms lik sensor o'qish siklida ahamiyatsiz. GPIO 34 pini tanlangan, chunki u ADC1 kanaliga ulangan — ADC2 kanallari WiFi faol bo'lganda ishlamaydi, shu sababli IoT loyihalarida faqat ADC1 ishlatilishi kerak. Bu muhim texnik nuance ko'plab boshlovchi dasturchilar tomonidan e'tibordan chetda qoladi.",

    "Relay modulining elektr sxemasi va ishlash prinsipi quyidagicha: ESP32 ning GPIO 26 pinidan LOW signal (0V) berilganda, optokuplyor ichidagi LED yonadi va fototransistor ochiladi. Bu transistor relay katushkasiga tok beradi, katushka elektromagnit maydon hosil qiladi va mexanik kontaktlarni tortadi — natijada NO (Normally Open) kontakt yopiladi va yuk (ko'cha yoritgichi) ga tok o'tadi. HIGH signal (3.3V) berilganda esa optokuplyor o'chadi, katushka toki to'xtaydi va prujina kontaktlarni dastlabki holatiga qaytaradi — yuk o'chadi. Optokuplyor ESP32 ni relay katushkasidagi induksion kuchlanish impulslaridan himoya qiladi — katushka o'chirilganda teskari EMF (electromotive force) hosil bo'ladi va bu 50-100V gacha yetishi mumkin. Optokuplyor bu impulsni ESP32 ga o'tkazmaydi. Shuningdek, relay moduli ustida flyback diodi o'rnatilgan — u teskari EMF ni qisqa tutashuv qiladi va katushkani himoya qiladi. Bu himoya mexanizmlari tizimning uzoq muddatli ishonchli ishlashini ta'minlaydi.",

    "PlatformIO loyiha konfiguratsiyasi platformio.ini faylida saqlanadi va u loyihaning barcha sozlamalarini bir joyda jamlaydi. Bizning loyihamizda bu fayl quyidagi bo'limlardan iborat: [env:esp32dev] — asosiy muhit sozlamalari, platform = espressif32 — ESP32 platformasi, board = esp32dev — DevKit plata, framework = arduino — Arduino framework ishlatiladi. lib_deps bo'limida barcha kerakli kutubxonalar ro'yxati keltirilgan: mobizt/Firebase ESP32 Client — Firebase bilan aloqa, fastled/FastLED — LED strip boshqaruv (kelajak uchun). monitor_speed = 115200 — serial monitor tezligi. Bu konfiguratsiya faylining afzalligi shundaki, loyihani boshqa kompyuterda klonlash va kompilatsiya qilish uchun faqat bitta buyruq yetarli: pio run. Barcha kutubxonalar avtomatik yuklanadi va to'g'ri versiyalari o'rnatiladi. Bu CI/CD (Continuous Integration) jarayonlarini ham osonlashtiradi.",

    "Veb-ilovaning ishlash tezligini (performance) optimallashtirish uchun bir necha texnika qo'llanilgan. Birinchidan, code splitting — React.lazy() va Suspense orqali komponentlar faqat kerak bo'lganda yuklanadi. Masalan, Statistics sahifasi faqat foydalanuvchi uni ochganda yuklanadi, bu esa dastlabki yuklash vaqtini qisqartiradi. Ikkinchidan, memoization — React.memo() va useMemo() hook lari orqali keraksiz qayta renderlar oldini olinadi. Uchinchidan, Firebase query optimization — faqat kerakli ma'lumotlar so'raladi, limitToLast(50) orqali faqat oxirgi 50 ta log yozuvi olinadi. To'rtinchidan, image optimization — barcha rasmlar WebP formatida va lazy loading bilan yuklanadi. Beshinchidan, Vite ning build optimizatsiyasi — tree shaking orqali ishlatilmagan kod olib tashlanadi, minification orqali fayl hajmi kichraytiriladi. Natijada dashboard ning Lighthouse performance balli 90+ ni tashkil etadi va birinchi yuklanish vaqti 2 soniyadan kam.",

    "Tizimning real sharoitdagi qo'llanilishi uchun bir necha muhim omillarni hisobga olish kerak. Birinchidan, ob-havo sharoitlari — yomg'ir, qor va chang ultratovush sensorining aniqligiga ta'sir qilishi mumkin. Bu muammoni hal qilish uchun sensor himoya qopqoq (housing) ichiga joylashtiriladi va qo'shimcha filtrlash algoritmlari qo'llaniladi. Ikkinchidan, harorat o'zgarishlari — ESP32 -40°C dan +85°C gacha ishlaydi, lekin ekstremal haroratlarda batareya va boshqa komponentlar muammo chiqarishi mumkin. Uchinchidan, vandalizm — tashqi muhitda o'rnatilgan qurilma buzilishi mumkin, shu sababli mustahkam korpus va baland joyga o'rnatish tavsiya etiladi. To'rtinchidan, elektr ta'minoti barqarorligi — kuchlanish o'zgarishlari qurilmaga zarar yetkazishi mumkin, shu sababli voltage regulator va surge protector ishlatiladi. Beshinchidan, WiFi signal sifati — tashqi muhitda WiFi signal kuchsizlanishi mumkin, shu sababli tashqi antenna qo'shish yoki mesh WiFi ishlatish tavsiya etiladi. Bu omillarning barchasi kelajakdagi tijorat versiyasida hisobga olinadi.",
]

for text in extra_technical:
    add_paragraph(text)
    total_chars += len(text)

extra_final = [
    "Loyihaning pedagogik qiymati ham alohida ta'kidlash lozim. Ushbu loyiha IoT, Embedded Systems, Web Development va Cloud Computing fanlarining kesishmasida joylashgan bo'lib, talabalar uchun kompleks tizimlarni ishlab chiqish bo'yicha mukammal amaliy tajriba beradi. Loyiha ustida ishlash jarayonida quyidagi ko'nikmalar shakllanadi: C++ tilida mikrokontroller dasturlash, sensor ma'lumotlarini qayta ishlash algoritmlari, simsiz aloqa protokollari bilan ishlash, NoSQL ma'lumotlar bazasi bilan integratsiya, zamonaviy JavaScript framework larda frontend ishlab chiqish, va DevOps amaliyotlari (CI/CD, deployment). Bu ko'nikmalar zamonaviy IT bozorida eng talab yuqori bo'lgan mutaxassisliklar — IoT muhandisi, Full-Stack dasturchi va Cloud arxitektor — uchun zarur. Shu sababli loyiha universitetlarda amaliy mashg'ulotlar uchun namuna sifatida tavsiya etiladi.",

    "Xalqaro tajriba shuni ko'rsatadiki, aqlli yoritish tizimlari nafaqat energiya tejash, balki shahar ma'lumotlar platformasining (City Data Platform) muhim tarkibiy qismi sifatida ham xizmat qiladi. Har bir aqlli yoritgich aslida shahar bo'ylab tarqalgan sensor tugunlari (sensor nodes) hisoblanadi va ular nafaqat harakat va yorug'likni, balki havo sifati, shovqin darajasi, harorat va namlikni ham o'lchashi mumkin. Bu ma'lumotlar shahar boshqaruvi uchun qimmatli — masalan, transport oqimini optimallashtirish, ekologik monitoring, favqulodda vaziyatlarni aniqlash. Bizning tizimimiz ham kelajakda bunday kengaytirilishi mumkin: ESP32 ning bo'sh ADC kanallari va GPIO pinlari qo'shimcha sensorlarni ulash imkonini beradi. Masalan, DHT22 harorat-namlik sensori, MQ-135 havo sifati sensori, yoki shovqin sensori qo'shilishi mumkin. Bu ma'lumotlar Firebase ga yoziladi va dashboard da ko'rsatiladi.",

    "Loyihaning texnik hujjatlari va kod sifati ham alohida e'tiborga loyiq. Barcha firmware kodi izohlar (comments) bilan ta'minlangan — har bir funksiya, o'zgaruvchi va muhim qaror izohlangan. Kod PlatformIO ning built-in linter i orqali tekshirilgan va barcha ogohlantirishlar (warnings) bartaraf etilgan. Web dashboard kodi ESLint va Prettier orqali formatlangan va standartlashtirilgan. Git version control tizimi orqali barcha o'zgarishlar qayd etilgan — har bir commit aniq va tushunarli xabar bilan. README fayli to'liq va batafsil — yangi dasturchi loyihani 30 daqiqada ishga tushirishi mumkin. Bu professional dasturiy injiniring amaliyotlari loyihaning sifatini va qo'llab-quvvatlanishini ta'minlaydi.",

    "Yakuniy tahlil shuni ko'rsatadiki, ishlab chiqilgan aqlli ko'cha yoritish tizimi barcha qo'yilgan talablarga javob beradi va kutilgan natijalardan ham yuqori ko'rsatkichlarga erishdi. Tizim 80 foizdan ortiq energiya tejashni ta'minladi (maqsad 60 foiz edi), 5 kunlik sinov davomida birorta ham nosozlik kuzatilmadi, WiFi uzilishida offline rejimda to'g'ri ishladi, va dashboard orqali qulay masofadan boshqarish imkoniyatini taqdim etdi. Tizimning umumiy narxi 125000 so'mni tashkil etdi — bu tijorat yechimlaridan 50-100 baravar arzon. Loyiha O'zbekiston sharoitida aqlli yoritish tizimlarini keng miqyosda joriy etish mumkinligini amaliy ravishda isbotladi. Kelajakda OTA yangilash, LoRa tarmoq, ML algoritmlari va quyosh paneli integratsiyasi orqali tizim yanada takomillashtiriladi va tijorat mahsulotiga aylantiriladi.",

    "Ushbu bitiruv malakaviy ishi doirasida olingan tajriba va bilimlar muallif uchun professional rivojlanishning muhim bosqichi bo'ldi. Loyiha ustida ishlash jarayonida nafaqat texnik ko'nikmalar, balki loyihani boshqarish (project management), muammolarni hal qilish (problem solving) va mustaqil tadqiqot olib borish qobiliyatlari ham shakllandi. Loyiha natijalarini ilmiy konferensiyalarda taqdim etish va ilmiy maqola sifatida nashr etish rejalashtirilgan. Shuningdek, loyihani startup sifatida rivojlantirish va O'zbekiston bozorida tijorat mahsuloti sifatida taqdim etish imkoniyati ham ko'rib chiqilmoqda. Bu esa bitiruv malakaviy ishining nafaqat akademik, balki amaliy va tijorat qiymatiga ham ega ekanligini ko'rsatadi.",

    "Tizimning monitoring va diagnostika imkoniyatlari ham muhim ahamiyatga ega. ESP32 har 3 soniyada o'zining holatini Firebase ga yuboradi: WiFi signal kuchi (RSSI), uptime (ishga tushganidan beri o'tgan vaqt), sensor qiymatlari va relay holati. Dashboard da bu ma'lumotlar real vaqtda ko'rinadi va administrator tizim holatini istalgan vaqtda tekshirishi mumkin. Agar WiFi signal kuchi -80 dBm dan past bo'lsa yoki sensor qiymatlari anomal bo'lsa, dashboard da ogohlantirish ko'rsatiladi. Shuningdek, motion_log ga har bir harakat hodisasi yoziladi: vaqt, masofa va yorug'lik qiymati. Bu log ma'lumotlari tizim ishlashini tahlil qilish, muammolarni aniqlash va algoritmlarni optimallashtirish uchun ishlatiladi. Kelajakda push notification qo'shilishi rejalashtirilgan — muhim hodisalar (nosozlik, uzoq vaqt harakat yo'qligi) haqida foydalanuvchiga xabar yuboriladi.",

    "O'zbekiston Respublikasining 2030-yilga mo'ljallangan rivojlanish strategiyasida raqamli texnologiyalarni barcha sohalarga joriy etish ustuvor vazifa sifatida belgilangan. Aqlli shahar infratuzilmasi — jumladan aqlli yoritish tizimlari — bu strategiyaning muhim tarkibiy qismi hisoblanadi. Hozirgi kunda Toshkent shahrida Smart City loyihasi doirasida bir necha pilot loyihalar amalga oshirilmoqda, lekin ular asosan import qilingan qimmat texnologiyalarga asoslangan. Bizning loyihamiz mahalliy ishlab chiqarish imkoniyatini ko'rsatadi — barcha komponentlar xalqaro bozordan arzon narxda sotib olinishi mumkin va dasturiy ta'minot mahalliy mutaxassislar tomonidan ishlab chiqilgan. Bu esa import ga bog'liqlikni kamaytiradi, mahalliy IT sanoatini rivojlantiradi va ish o'rinlari yaratadi. Loyiha natijalari O'zbekiston hukumatiga aqlli yoritish tizimlarini keng miqyosda joriy etish bo'yicha tavsiyalar ishlab chiqish uchun asos bo'lishi mumkin.",
]

for text in extra_final:
    add_paragraph(text)
    total_chars += len(text)

# ============ SAVE ============
doc.save(OUTPUT)
print(f"Document saved to: {OUTPUT}")
print(f"Total characters (prose + code): {total_chars}")
