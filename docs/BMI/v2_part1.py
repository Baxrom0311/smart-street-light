#!/usr/bin/env python3
"""BMI DOCX - to'liq qayta yozish. Formatting: 14pt, 1.5, before/after=0, no blanks"""
from docx import Document
from docx.shared import Pt, Cm, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
import os

doc = Document()
IMG = '/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/images/'

# === GLOBAL STYLE ===
style = doc.styles['Normal']
style.font.name = 'Times New Roman'
style.font.size = Pt(14)
pf = style.paragraph_format
pf.line_spacing = 1.5
pf.space_before = Pt(0)
pf.space_after = Pt(0)
pf.first_line_indent = Cm(1.25)

for s in doc.sections:
    s.top_margin = Cm(2); s.bottom_margin = Cm(2)
    s.left_margin = Cm(3); s.right_margin = Cm(1.5)

def bob(text):
    """Bob sarlavhasi - markazda, qalin, 14pt"""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text)
    r.bold = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'

def h2(text):
    """Kichik sarlavha - chapdan, qalin"""
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text)
    r.bold = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'

def t(text):
    """Oddiy paragraf - 14pt, abzats bilan"""
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'; r.font.size = Pt(14)

def img(name, caption):
    """Rasm + tagida o'ng tomondan italic izoh"""
    path = IMG + name
    if not os.path.exists(path):
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run()
    run.add_picture(path, width=Cm(14))
    # Caption - o'ng tomondan, italic
    pc = doc.add_paragraph()
    pc.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    pc.paragraph_format.first_line_indent = Cm(0)
    pc.paragraph_format.space_before = Pt(0)
    pc.paragraph_format.space_after = Pt(0)
    rc = pc.add_run(caption)
    rc.italic = True; rc.font.size = Pt(12); rc.font.name = 'Times New Roman'

def tbl(headers, rows, caption):
    """Jadval + o'ng tomondan italic izoh"""
    # Caption before table - right aligned italic
    pc = doc.add_paragraph()
    pc.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    pc.paragraph_format.first_line_indent = Cm(0)
    pc.paragraph_format.space_before = Pt(0)
    pc.paragraph_format.space_after = Pt(0)
    rc = pc.add_run(caption)
    rc.italic = True; rc.font.size = Pt(12); rc.font.name = 'Times New Roman'
    # Table
    tb = doc.add_table(rows=1+len(rows), cols=len(headers))
    tb.style = 'Table Grid'
    for i, h in enumerate(headers):
        cell = tb.rows[0].cells[i]
        cell.text = ''
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.bold = True; r.font.size = Pt(12); r.font.name = 'Times New Roman'
    for ri, row in enumerate(rows):
        for ci, v in enumerate(row):
            cell = tb.rows[ri+1].cells[ci]
            cell.text = ''
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(str(v))
            r.font.size = Pt(12); r.font.name = 'Times New Roman'

def code(text):
    """Kod bloki - Courier New 10pt"""
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.left_indent = Cm(1)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text)
    r.font.name = 'Courier New'; r.font.size = Pt(10)

# ==================== TITUL ====================
for _ in range(4):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)

bob("O'ZBEKISTON RESPUBLIKASI\nOLIY TA'LIM, FAN VA INNOVATSIYALAR VAZIRLIGI")
bob("MUHAMMAD AL-XORAZMIY NOMIDAGI\nTOSHKENT AXBOROT TEXNOLOGIYALARI UNIVERSITETI")
bob('"KOMPYUTER INJINIRINGI" FAKULTETI\n"DASTURIY INJINIRING" KAFEDRASI')

for _ in range(3):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)

bob("BITIRUV MALAKAVIY ISHI")
bob('Mavzu: "SMART STREET TIZIMIDA ULTRATOVUSH SENSORI ORQALI\nENERGIYA TEJAMKORLIGINI TA\'MINLOVCHI\nYORITISH TIZIMINI ISHLAB CHIQISH"')

for _ in range(4):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)

t("Bajardi: _______________________")
t("Ilmiy rahbar: _______________________")

for _ in range(5):
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)

bob("Toshkent — 2026")
doc.add_page_break()

# ==================== MUNDARIJA ====================
bob("MUNDARIJA")
items = [
    ("KIRISH", "4"),
    ("I BOB. SMART STREET TIZIMIDA YORITISH TIZIMLARI TIZIMLI TAHLILI VA MASALANING QO'YILISHI", "10"),
    ("1.1. Smart Street tizimlarida energiya tejamkor yoritish tizimlari va ularning ahamiyati", "10"),
    ("1.2. Ultratovush sensorlarning ishlash prinsipi va texnik xususiyatlari", "26"),
    ("1.3. Masalaning qo'yilishi", "40"),
    ("II BOB. AMALIY QISM", "46"),
    ("2.1. Tizimni loyihalash: texnik vositalar va komponentlarni tanlash", "46"),
    ("2.2. Masofani aniqlash algoritmi: ultrasonic sensor yordamida obyektni aniqlash", "60"),
    ("2.3. Yoritish tizimini boshqarish dasturi va tizimning ishlash jarayoni va natijalar tahlili", "72"),
    ("XULOSA", "88"),
    ("FOYDALANILGAN ADABIYOTLAR RO'YXATI", "91"),
    ("ILOVALAR", "93"),
]
for title, page in items:
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    r = p.add_run(f"{title} {'.'*(70-len(title))} {page}")
    r.font.name = 'Times New Roman'; r.font.size = Pt(14)

doc.add_page_break()

# ==================== KIRISH ====================
bob("KIRISH")
t("Hozirgi kunda dunyo miqyosida energiya iste'moli keskin o'sib bormoqda va bu jarayon atrof-muhitga salbiy ta'sir ko'rsatmoqda. Birlashgan Millatlar Tashkilotining ma'lumotlariga ko'ra, ko'cha yoritish tizimlari shahar elektr energiyasi iste'molining 15-25 foizini tashkil etadi. Dunyo bo'ylab ko'cha yoritish uchun yiliga taxminan 320 teravatt-soat elektr energiyasi sarflanadi, bu esa 150 million tonna CO2 emissiyasiga teng keladi. Bu ko'rsatkich ayniqsa rivojlanayotgan mamlakatlar uchun jiddiy muammo hisoblanadi, chunki ularning energiya infratuzilmasi cheklangan va har bir kilovatt-soat tejash katta iqtisodiy samara beradi.")
t("An'anaviy ko'cha yoritish tizimlari tun bo'yi uzluksiz ishlaydi, ya'ni o'rtacha 10-12 soat davomida to'liq quvvatda yonib turadi. Biroq, kuzatishlar shuni ko'rsatadiki, tun vaqtining 60-70 foizida ko'chalarda harakat deyarli kuzatilmaydi. Masalan, shahar ko'chalarida soat 00:00 dan 05:00 gacha bo'lgan vaqt oralig'ida piyodalar va transport vositalari harakati kunduzi vaqtiga nisbatan 90 foizga kamayadi. Shunga qaramay, yoritgichlar to'liq quvvatda yonib turadi va bu energiyaning behuda sarflanishiga olib keladi. Xalqaro Energetika Agentligi ma'lumotlariga ko'ra, agar bu energiyaning 70 foizi behuda sarflanayotgan bo'lsa, yiliga 224 TWh energiya isrof bo'lmoqda.")
t("Internet of Things texnologiyasining jadal rivojlanishi aqlli shahar konsepsiyasini amalga oshirish imkonini yaratmoqda. Statista tahliliy kompaniyasining 2024-yildagi hisobotiga ko'ra, dunyo bo'ylab IoT qurilmalari soni 2025-yilga kelib 30 milliarddan oshgan bo'lib, 2030-yilga borib bu ko'rsatkich 75 milliardga yetishi prognoz qilinmoqda. IoT texnologiyalari yordamida ko'cha yoritish tizimlarini aqlli boshqarish energiya tejashning eng samarali usullaridan biri hisoblanadi. Sensorlar yordamida harakatni aniqlash va faqat kerak bo'lganda yoritgichni yoqish orqali 60-80 foiz energiya tejash mumkin.")
t("Ultratovush sensorlari harakatni aniqlash uchun eng ishonchli va arzon vositalardan biri bo'lib, ular bir qator muhim afzalliklarga ega. Ular ob-havo sharoitlariga kam ta'sirchan bo'lib, yomg'ir, tuman va changda ham barqaror ishlaydi. Keng burchak ostida ishlash qobiliyatiga ega bo'lib, 30-40 gradus qamrov beradi. Past energiya iste'mol qiladi, ya'ni 2 milliamperdan kam tok sarflaydi. Narxi arzon bo'lib, 1-3 AQSh dollarini tashkil etadi. Infraqizil sensorlardan farqli ravishda, ultratovush sensorlari harorat o'zgarishlariga sezgir emas va aniqroq masofa ma'lumotini beradi.")
t("Ushbu sensorlarni ESP32 mikrokontrolleri bilan birgalikda qo'llash orqali energiya tejamkor yoritish tizimini yaratish mumkin. ESP32 Espressif Systems kompaniyasi tomonidan ishlab chiqilgan ikki yadroli mikrokontroller bo'lib, ichki WiFi va Bluetooth modullariga ega. Bu xususiyatlar tizimni internet orqali masofadan boshqarish va monitoring qilish imkonini beradi. Tizim faqat harakat aniqlanganda yoritgichni yoqadi va ma'lum vaqt o'tgach avtomatik o'chiradi, shu bilan birga kunduz kuni yoritgichni umuman yoqmaydi.")
t("O'zbekiston Respublikasi Prezidentining 2020-yil 5-oktabrdagi PF-6079-sonli Farmoni asosida qabul qilingan Raqamli O'zbekiston 2030 strategiyasi IoT va aqlli shahar texnologiyalarini rivojlantirishni ustuvor yo'nalish sifatida belgilab beradi. Strategiyada ko'rsatilishicha, 2030-yilga borib O'zbekiston shaharlarining kamida 30 foizi aqlli texnologiyalar bilan jihozlanishi rejalashtirilgan. Shuningdek, O'zbekiston Respublikasi Vazirlar Mahkamasining 2023-yil 15-martdagi 58-sonli qarori bilan tasdiqlangan Energiya tejamkorligi va energiya samaradorligi to'g'risidagi dastur energiya resurslaridan oqilona foydalanish zarurligini ta'kidlaydi. Ushbu dasturga ko'ra, 2025-2030 yillarda energiya iste'molini 20 foizga kamaytirish maqsad qilib qo'yilgan.")
t("Yuqoridagilarni hisobga olgan holda, ultratovush sensori asosida energiya tejamkor ko'cha yoritish tizimini ishlab chiqish nafaqat ilmiy, balki amaliy jihatdan ham dolzarb masala hisoblanadi. Bunday tizim O'zbekiston shahar va qishloqlarida energiya tejash, ekologik vaziyatni yaxshilash va fuqarolar xavfsizligini ta'minlash uchun muhim hissa qo'shishi mumkin.")
h2("Ishning ilmiy yangiligi")
t("Mazkur bitiruv malakaviy ishida ishlab chiqilgan tizim quyidagi ilmiy va amaliy yangiliklarga ega. ESP32 mikrokontrolleri asosida ultratovush sensori va yorug'lik sensori birgalikda qo'llanilgan energiya tejamkor yoritish tizimi ishlab chiqildi. Mavjud yechimlardan farqli ravishda, tizim bir vaqtning o'zida harakatni aniqlash va kunduz-tun holatini farqlash imkoniyatiga ega. Bu ikki sensorning birgalikda ishlashi tizimning energiya samaradorligini sezilarli darajada oshiradi.")
t("Firebase Realtime Database asosida real vaqt rejimida masofadan boshqarish va monitoring tizimi yaratildi. Bu tizim qurilmaning holatini har 3 soniyada yangilab turadi va foydalanuvchiga veb-interfeys orqali boshqarish imkonini beradi. Non-blocking WiFi boshqaruv algoritmi ishlab chiqildi va tizim internet aloqasi uzilgan holda ham avtonom ravishda ishlashda davom etadi. Progressive Web Application texnologiyasi asosida cross-platform dashboard yaratildi va u desktop va mobil qurilmalarda bir xil samarali ishlaydi.")
h2("Ishning maqsadi")
t("Bitiruv malakaviy ishining asosiy maqsadi ultratovush sensori yordamida harakatni aniqlash va yorug'lik sensori orqali kunduz-tun holatini farqlash asosida energiya tejamkor ko'cha yoritish tizimini ishlab chiqish, uni masofadan boshqarish imkoniyatini yaratish va energiya tejash samaradorligini amaliy tajribalar orqali isbotlashdan iborat. Tizim real sharoitlarda sinovdan o'tkazilishi va uning samaradorligi raqamlar bilan isbotlanishi kerak.")
h2("Ishning vazifalari")
t("Yuqorida belgilangan maqsadga erishish uchun quyidagi vazifalar amalga oshirildi. Ko'cha yoritish tizimlarining hozirgi holati, mavjud muammolar va energiya tejamkorlik yondashuvlari chuqur o'rganildi. Ultratovush sensorlarining ishlash prinsipini, fizik asoslarini va texnik xususiyatlari tadqiq qilindi. ESP32 mikrokontrolleri asosida hardware platforma loyihalandi va komponentlar tanlandi. Harakatni aniqlash algoritmi ishlab chiqildi va debounce, hold timer hamda hysteresis mexanizmlari qo'llanildi. Firebase Realtime Database bilan real vaqt sinxronizatsiya tizimi yaratildi. React framework asosida Progressive Web Application dashboard ishlab chiqildi. Tizimning energiya tejash samaradorligi hisoblandi va amaliy tajribalar o'tkazildi. Tizim real sharoitlarda sinab ko'rildi va natijalar tahlil qilindi.")
h2("Tadqiqot obyekti va predmeti")
t("Tadqiqot obyekti ko'cha yoritish tizimlari va ularda energiya tejamkorlikni ta'minlash uchun ishlatiladigan sensorli boshqaruv tizimlari hisoblanadi. Tadqiqot predmeti esa ultratovush sensori yordamida harakatni aniqlash algoritmlari, IoT texnologiyalari asosida masofadan boshqarish tizimlari va ularning energiya tejamkorlikka ta'siridir. Tadqiqot davomida ESP32 mikrokontrolleri, RCWL-9610A ultratovush sensori, TEMT6000 yorug'lik sensori va relay moduli asosida amaliy prototip yaratildi va real sharoitlarda sinovdan o'tkazildi.")
h2("Tadqiqot usullari")
t("Bitiruv ishi davomida quyidagi tadqiqot usullaridan foydalanildi. Ilmiy adabiyotlarni tahlil va sintez qilish usuli mavjud tadqiqotlar, patentlar va texnik hujjatlarni o'rganish uchun qo'llanildi. Sistemali yondashuv tizimni qatlamlar bo'yicha loyihalash imkonini berdi. Eksperimental tadqiqotlar prototipni yaratish va real sharoitlarda sinash uchun o'tkazildi. Qiyosiy tahlil mavjud yechimlar bilan solishtirib baholash uchun ishlatildi. Matematik modellashtirish energiya tejash formulalarini ishlab chiqish va hisoblash uchun qo'llanildi. Prototiplash va iterativ ishlab chiqish metodologiyasi har bir komponentni alohida sinab, keyin birlashtirish imkonini berdi.")
h2("Ishning amaliy ahamiyati")
t("Ishlab chiqilgan tizim shahar va qishloq ko'chalarida energiya tejamkor yoritish tizimini joriy etish uchun foydalanish mumkin. Bitta yoritgich uchun yillik tejamkorlik 212 kWh yoki 106 ming so'mni tashkil etadi. Tizim bog'lar, parkovkalar va yopiq hududlarda avtomatik yoritish, sanoat korxonalari va omborxonalarda energiya sarfini kamaytirish, aqlli shahar loyihalarida yoritish infratuzilmasini modernizatsiya qilish va ta'lim muassasalarida IoT bo'yicha amaliy o'quv materiali sifatida qo'llanilishi mumkin.")
h2("Bitiruv malakaviy ishining tarkibi")
t("Bitiruv malakaviy ishi kirish, ikkita asosiy bob, xulosa, foydalanilgan adabiyotlar ro'yxati va ilovalardan iborat. Birinchi bobda ko'cha yoritish tizimlari, ultratovush sensorlari va IoT texnologiyalari nazariy jihatdan tahlil qilingan, mavjud yechimlar qiyosiy o'rganilgan va masala qo'yilishi shakllantirilgan. Ikkinchi bobda esa tizim arxitekturasi, hardware va software qismlarini amalda ishlab chiqish, dasturlash jarayoni va sinov natijalari batafsil bayon etilgan. Ishning umumiy hajmi 100 sahifani tashkil etadi, matn ichida rasmlar, sxemalar, jadvallar va dastur kodi fragmentlari keltirilgan. Foydalanilgan adabiyotlar ro'yxati 25 manbadan iborat.")

doc.add_page_break()
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')
print("Part 1 done: Titul + Mundarija + KIRISH")
