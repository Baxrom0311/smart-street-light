from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import copy

doc = Document()

# --- Page margins ---
for section in doc.sections:
    section.left_margin = Cm(3)
    section.right_margin = Cm(1.5)
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(2)

# --- Setup styles ---
style_normal = doc.styles['Normal']
style_normal.font.name = 'Times New Roman'
style_normal.font.size = Pt(14)
style_normal.paragraph_format.line_spacing = 1.5
style_normal.paragraph_format.space_before = Pt(0)
style_normal.paragraph_format.space_after = Pt(0)
style_normal.paragraph_format.first_line_indent = Cm(1.25)

# Heading 1
style_h1 = doc.styles['Heading 1']
style_h1.font.name = 'Times New Roman'
style_h1.font.size = Pt(14)
style_h1.font.bold = True
style_h1.font.color.rgb = None
style_h1.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
style_h1.paragraph_format.line_spacing = 1.5
style_h1.paragraph_format.space_before = Pt(0)
style_h1.paragraph_format.space_after = Pt(0)
style_h1.paragraph_format.first_line_indent = Cm(0)

# Heading 2
style_h2 = doc.styles['Heading 2']
style_h2.font.name = 'Times New Roman'
style_h2.font.size = Pt(14)
style_h2.font.bold = True
style_h2.font.color.rgb = None
style_h2.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
style_h2.paragraph_format.line_spacing = 1.5
style_h2.paragraph_format.space_before = Pt(0)
style_h2.paragraph_format.space_after = Pt(0)
style_h2.paragraph_format.first_line_indent = Cm(0)


def add_centered(text, bold=False, size=14):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
    run = p.add_run(text)
    run.bold = bold
    run.font.size = Pt(size)
    run.font.name = 'Times New Roman'
    return p


def add_body(text):
    p = doc.add_paragraph(text)
    return p


def add_empty_lines(n=1):
    for _ in range(n):
        p = doc.add_paragraph()
        p.paragraph_format.first_line_indent = Cm(0)


# ============ 1. TITUL PAGE ============
add_empty_lines(1)
add_centered("O'ZBEKISTON RESPUBLIKASI", bold=True)
add_centered("OLIY TA'LIM, FAN VA INNOVATSIYALAR VAZIRLIGI", bold=True)
add_empty_lines(1)
add_centered("MUHAMMAD AL-XORAZMIY NOMIDAGI")
add_centered("TOSHKENT AXBOROT TEXNOLOGIYALARI UNIVERSITETI", bold=True)
add_empty_lines(2)
add_centered("KOMPYUTER INJINIRINGI FAKULTETI")
add_centered("KOMPYUTER INJINIRINGI YO'NALISHI")
add_empty_lines(3)
add_centered("BITIRUV MALAKAVIY ISHI", bold=True, size=16)
add_empty_lines(1)
add_centered("Mavzu: Ultratovush sensori orqali energiya tejamkorligini", bold=True)
add_centered("ta'minlovchi yoritish tizimini ishlab chiqish", bold=True)
add_empty_lines(4)
add_centered("Bajardi: Baxrom")
add_centered("Ilmiy rahbar: ___________________")
add_empty_lines(5)
add_centered("TOSHKENT — 2026")

doc.add_page_break()

# ============ 2. MUNDARIJA (Dynamic TOC) ============
add_centered("MUNDARIJA", bold=True)
add_empty_lines(1)

# Add TOC field
p_toc = doc.add_paragraph()
p_toc.paragraph_format.first_line_indent = Cm(0)
run_toc = p_toc.add_run()
fldChar1 = OxmlElement('w:fldChar')
fldChar1.set(qn('w:fldCharType'), 'begin')
run_toc._r.append(fldChar1)

run_toc2 = p_toc.add_run()
instrText = OxmlElement('w:instrText')
instrText.set(qn('xml:space'), 'preserve')
instrText.text = ' TOC \\o "1-2" \\h \\z \\u '
run_toc2._r.append(instrText)

run_toc3 = p_toc.add_run()
fldChar2 = OxmlElement('w:fldChar')
fldChar2.set(qn('w:fldCharType'), 'separate')
run_toc3._r.append(fldChar2)

run_toc4 = p_toc.add_run("Mundarijani yangilash uchun shu ustiga bosing va F9 tugmasini bosing")
run_toc4.font.color.rgb = RGBColor(128, 128, 128)

run_toc5 = p_toc.add_run()
fldChar3 = OxmlElement('w:fldChar')
fldChar3.set(qn('w:fldCharType'), 'end')
run_toc5._r.append(fldChar3)

doc.add_page_break()

# ============ 3. KIRISH ============
doc.add_heading("KIRISH", level=1)
add_empty_lines(1)

# --- Paragraph 1: Raqamli O'zbekiston 2030 ---
add_body(
    "Zamonaviy axborot texnologiyalari va raqamli transformatsiya jarayonlari butun dunyo bo'ylab "
    "jadal rivojlanmoqda. O'zbekiston Respublikasi Prezidentining 2020-yil 5-oktabrdagi PF-6079-son "
    "Farmoni bilan tasdiqlangan \"Raqamli O'zbekiston — 2030\" strategiyasi mamlakatimizda raqamli "
    "iqtisodiyotni rivojlantirish, davlat boshqaruvini zamonaviylashtirish va fuqarolar hayot "
    "sifatini oshirish bo'yicha keng ko'lamli vazifalarni belgilab berdi. Ushbu strategiya doirasida "
    "Internet of Things (IoT) texnologiyalarini shahar infratuzilmasiga joriy etish, aqlli shahar "
    "konsepsiyasini amalga oshirish hamda energiya resurslaridan samarali foydalanish masalalari "
    "ustuvor yo'nalishlar sifatida ko'rsatilgan."
)

# --- Paragraph 2: Energiya tejamkorligi qarori ---
add_body(
    "O'zbekiston Respublikasi Vazirlar Mahkamasining 2023-yil 3-fevraldagi 58-son qarori \"Energiya "
    "tejamkorligi va energiya samaradorligini oshirish chora-tadbirlari to'g'risida\" mamlakatimizda "
    "energiya resurslaridan oqilona foydalanish bo'yicha aniq mexanizmlarni belgilab berdi. Qarorga "
    "muvofiq, davlat muassasalari va jamoat joylarida energiya iste'molini kamida 30 foizga "
    "kamaytirish, zamonaviy energiya tejamkor texnologiyalarni joriy etish hamda aqlli boshqaruv "
    "tizimlarini keng qo'llash ko'zda tutilgan. Ko'cha yoritish tizimlari shahar energiya "
    "iste'molining 15 dan 25 foizgacha ulushini tashkil etishi hisobga olinsa, ushbu sohada "
    "tejamkorlikni ta'minlash davlat byudjetiga sezilarli ijobiy ta'sir ko'rsatishi muqarrar."
)

# --- Paragraph 3: Energiya tejash qonuni ---
add_body(
    "O'zbekiston Respublikasining 2024-yilda qabul qilingan \"Energiya tejash va energiya "
    "samaradorligi to'g'risida\"gi Qonuni energiya resurslaridan foydalanishning huquqiy asoslarini "
    "yanada mustahkamladi. Qonunga binoan, barcha yangi qurilayotgan va rekonstruksiya qilinayotgan "
    "ob'ektlarda energiya tejamkor texnologiyalarni qo'llash majburiy hisoblanadi. Shuningdek, "
    "mavjud infratuzilmani bosqichma-bosqich zamonaviy energiya samarador tizimlarga o'tkazish "
    "rejalashtirilgan. Ko'cha yoritish sohasida an'anaviy natriy va simob lampalarini LED "
    "yoritgichlarga almashtirish, sensorli boshqaruv tizimlarini joriy etish hamda masofadan "
    "monitoring imkoniyatlarini yaratish qonun talablari doirasida amalga oshirilishi lozim."
)

# --- Paragraph 4: Aqlli shahar qarori ---
add_body(
    "O'zbekiston Respublikasi Prezidentining 2023-yildagi PQ-436-son qarori \"Aqlli shahar\" "
    "texnologiyalarini joriy etish bo'yicha qo'shimcha chora-tadbirlar haqida muhim qadam bo'ldi. "
    "Ushbu qaror doirasida Toshkent shahri va viloyat markazlarida aqlli transport, aqlli yoritish, "
    "aqlli suv ta'minoti kabi tizimlarni bosqichma-bosqich joriy etish belgilangan. Aqlli ko'cha "
    "yoritish tizimi ushbu konsepsiyaning ajralmas tarkibiy qismi sifatida e'tirof etilgan bo'lib, "
    "u nafaqat energiya tejash, balki shahar xavfsizligini oshirish, transport oqimini boshqarish "
    "va ekologik vaziyatni yaxshilash kabi ko'p qirrali vazifalarga xizmat qiladi."
)

# --- Paragraph 5: BMT SDG ---
add_body(
    "Birlashgan Millatlar Tashkilotining Barqaror rivojlanish maqsadlari (SDG) kontekstida ham "
    "energiya tejamkor yoritish tizimlari muhim ahamiyat kasb etadi. Xususan, SDG 7 — \"Arzon va "
    "toza energiya\" maqsadi energiya samaradorligini oshirish va qayta tiklanuvchi energiya "
    "manbalaridan foydalanishni kengaytirishni nazarda tutadi. SDG 11 — \"Barqaror shaharlar va "
    "aholi punktlari\" maqsadi shahar infratuzilmasini zamonaviylashtirish va atrof-muhitga salbiy "
    "ta'sirni kamaytirishga qaratilgan. SDG 13 — \"Iqlim o'zgarishiga qarshi kurash\" maqsadi esa "
    "karbonat angidrid chiqindilarini kamaytirish orqali global isishning oldini olishni ko'zda "
    "tutadi. Aqlli ko'cha yoritish tizimi ushbu uchala maqsadga bir vaqtning o'zida hissa qo'shadi."
)

# --- Paragraph 6: Dolzarblik statistika ---
add_body(
    "Jahon miqyosida ko'cha yoritish tizimlari yiliga taxminan 320 TWh elektr energiya iste'mol "
    "qiladi, bu esa global elektr energiya ishlab chiqarishning 3-4 foizini tashkil etadi. Shahar "
    "darajasida esa ko'cha yoritish umumiy energiya iste'molining 15 dan 25 foizgacha ulushini "
    "egallaydi. An'anaviy ko'cha yoritish tizimlari tun bo'yi uzluksiz ishlaydi, vaholanki "
    "ko'chalardan foydalanish intensivligi vaqt oralig'iga qarab sezilarli farq qiladi. Tadqiqotlar "
    "shuni ko'rsatadiki, tunda soat 23:00 dan 05:00 gacha bo'lgan davrda piyodalar va transport "
    "harakati kunduzi nisbatan 70-85 foizga kamayadi. Shunga qaramay, an'anaviy tizimlar to'liq "
    "quvvatda ishlashda davom etadi, bu esa katta miqdorda energiya isrof bo'lishiga olib keladi."
)

# --- Paragraph 7: Dolzarblik davomi ---
add_body(
    "Mamlakatimizda 2025-yil holatiga ko'ra 2,5 milliondan ortiq ko'cha yoritgichlari mavjud bo'lib, "
    "ularning aksariyati an'anaviy boshqaruv tizimlariga asoslangan. Har bir yoritgichning o'rtacha "
    "quvvati 150-250 Vt ni tashkil etishini hisobga olsak, faqat keraksiz yonish tufayli yiliga "
    "milliardlab so'mlik energiya isrof bo'lmoqda. Sensorli aqlli boshqaruv tizimlarini joriy etish "
    "orqali ushbu isrofgarchilikni 60-80 foizga kamaytirish mumkin. Bu nafaqat iqtisodiy tejamkorlik, "
    "balki ekologik barqarorlik nuqtai nazaridan ham muhim ahamiyatga ega, chunki kamroq energiya "
    "iste'moli kamroq karbonat angidrid chiqindisi demakdir."
)

# --- Paragraph 8: Muammo va yechim ---
add_body(
    "Mavjud ko'cha yoritish tizimlarining asosiy kamchiliklari quyidagilardan iborat: birinchidan, "
    "ular harakatni aniqlay olmaydi va doimo bir xil rejimda ishlaydi; ikkinchidan, masofadan "
    "boshqarish va monitoring imkoniyati mavjud emas; uchinchidan, energiya iste'moli haqida "
    "statistik ma'lumotlar to'planmaydi; to'rtinchidan, nosozliklarni aniqlash faqat vizual "
    "tekshirish orqali amalga oshiriladi. Ushbu muammolarni hal qilish uchun IoT texnologiyalariga "
    "asoslangan aqlli boshqaruv tizimini ishlab chiqish zarur. Bunday tizim real vaqt rejimida "
    "harakatni aniqlash, atrof-muhit yorug'ligini o'lchash va olingan ma'lumotlar asosida yoritishni "
    "avtomatik boshqarish imkoniyatini beradi."
)

# --- Paragraph 9: Ilmiy yangilik ---
add_body(
    "Ushbu tadqiqotning ilmiy yangiligi shundaki, ultratovush sensori va yorug'lik sensori "
    "ma'lumotlarini birgalikda qayta ishlash asosida ko'p bosqichli qaror qabul qilish algoritmi "
    "ishlab chiqilgan. An'anaviy PIR (passiv infraqizil) sensorlardan farqli o'laroq, ultratovush "
    "sensori aniq masofani o'lchash imkonini beradi, bu esa yoritish intensivligini ob'ektning "
    "yaqinlashish masofasiga qarab bosqichma-bosqich oshirish imkoniyatini yaratadi. Bundan tashqari, "
    "tizim bulutli platformaga ulangan holda ishlaydi, bu esa masofadan boshqarish, statistik "
    "tahlil va prediktiv texnik xizmat ko'rsatish kabi qo'shimcha funksiyalarni amalga oshirish "
    "imkonini beradi."
)

# --- Paragraph 10: Maqsad ---
add_body(
    "Tadqiqotning asosiy maqsadi — ESP32 mikrokontrolleri, ultratovush sensori va bulutli "
    "texnologiyalar asosida energiya tejamkor aqlli ko'cha yoritish tizimini ishlab chiqish va "
    "amaliy sinovdan o'tkazishdir. Tizim harakatni aniqlash, atrof-muhit yorug'ligini baholash, "
    "LED yoritgichlarni avtomatik boshqarish hamda barcha ma'lumotlarni real vaqt rejimida bulutli "
    "platformaga uzatish funksiyalarini bajarishi kerak. Shuningdek, foydalanuvchilarga qulay veb "
    "interfeys orqali tizimni masofadan monitoring qilish va boshqarish imkoniyatini yaratish ham "
    "maqsad qilib qo'yilgan."
)

# --- Paragraph 11: Vazifalar ---
add_body(
    "Belgilangan maqsadga erishish uchun quyidagi vazifalar hal qilinishi lozim: mavjud ko'cha "
    "yoritish tizimlarini tahlil qilish va ularning kamchiliklarini aniqlash; ultratovush sensori "
    "yordamida harakatni aniqlash algoritmini ishlab chiqish va optimallashtirish; yorug'lik sensori "
    "ma'lumotlari asosida kunduz va tun rejimlarini avtomatik aniqlash mexanizmini yaratish; ESP32 "
    "mikrokontrolleri uchun dasturiy ta'minotni ishlab chiqish; Firebase Realtime Database bilan "
    "integratsiyani amalga oshirish; React texnologiyasi asosida Progressive Web Application "
    "ko'rinishidagi boshqaruv panelini yaratish; tizimning energiya tejash samaradorligini "
    "eksperimental sinovlar orqali baholash."
)

# --- Paragraph 12: Obyekt va predmet ---
add_body(
    "Tadqiqot ob'ekti sifatida ko'cha yoritish tizimlarini avtomatlashtirish va aqlli boshqarish "
    "jarayonlari tanlab olingan. Tadqiqot predmeti esa ultratovush sensori va IoT texnologiyalari "
    "asosida energiya tejamkor yoritish tizimini loyihalash, ishlab chiqish va sinovdan o'tkazish "
    "jarayonidir. Tadqiqotda eksperimental, qiyosiy tahlil va modellashtirish usullari qo'llanilgan. "
    "Eksperimental usul orqali tizimning real sharoitlarda ishlash ko'rsatkichlari o'lchangan, "
    "qiyosiy tahlil usuli orqali an'anaviy va aqlli tizimlar samaradorligi solishtirilgan, "
    "modellashtirish usuli esa tizim arxitekturasini optimallashtirish uchun ishlatilgan."
)

# --- Paragraph 13: Usullar ---
add_body(
    "Tadqiqotda qo'llanilgan asosiy usullar orasida prototiplash, iterativ loyihalash va empirik "
    "sinovlar alohida o'rin tutadi. Prototiplash usuli orqali tizimning dastlabki namunasi yaratilgan "
    "va uning ishlash prinsipi tekshirilgan. Iterativ loyihalash jarayonida har bir bosqichda "
    "olingan natijalar tahlil qilingan va tizimga tegishli yaxshilanishlar kiritilgan. Empirik "
    "sinovlar davomida tizimning turli sharoitlardagi ishlash ko'rsatkichlari o'lchangan va "
    "statistik qayta ishlangan. Dasturiy ta'minotni ishlab chiqishda Agile metodologiyasi, "
    "xususan Scrum freymvorki qo'llanilgan bo'lib, bu loyihani bosqichma-bosqich rivojlantirish "
    "va doimiy yaxshilash imkonini bergan."
)

# --- Paragraph 14: Amaliy ahamiyat ---
add_body(
    "Tadqiqotning amaliy ahamiyati shundaki, ishlab chiqilgan tizim real sharoitlarda qo'llanilishi "
    "mumkin bo'lgan tayyor yechim hisoblanadi. Tizim arzon va keng tarqalgan komponentlar asosida "
    "qurilgan bo'lib, uni mavjud ko'cha yoritish infratuzilmasiga minimal xarajatlar bilan "
    "integratsiya qilish mumkin. Bitta yoritish nuqtasi uchun tizim narxi taxminan 50-70 ming "
    "so'mni tashkil etadi, vaholanki yillik energiya tejamkorligi 200-300 ming so'mga yetishi "
    "mumkin. Demak, tizim o'zini 3-4 oy ichida oqlab beradi. Bundan tashqari, veb-interfeys "
    "orqali masofadan boshqarish imkoniyati texnik xizmat ko'rsatish xarajatlarini ham sezilarli "
    "darajada kamaytiradi."
)

# --- Paragraph 15: BMI tuzilishi ---
add_body(
    "Bitiruv malakaviy ishi kirish, uchta bob, xulosa va foydalanilgan adabiyotlar ro'yxatidan "
    "iborat. Birinchi bobda ko'cha yoritish tizimlarining rivojlanish tarixi, mavjud yechimlar "
    "tahlili, IoT texnologiyalarining nazariy asoslari va tizim arxitekturasi batafsil yoritilgan. "
    "Ikkinchi bobda tizimning apparat va dasturiy ta'minoti, sensorlar ishlash prinsipi, "
    "mikrokontroller dasturlash va bulutli platforma integratsiyasi tavsiflangan. Uchinchi bobda "
    "tizimni sinovdan o'tkazish natijalari, energiya tejash ko'rsatkichlari va iqtisodiy "
    "samaradorlik tahlili keltirilgan. Xulosa qismida olingan natijalar umumlashtirilgan va "
    "kelgusida tizimni rivojlantirish bo'yicha takliflar berilgan."
)

# --- Paragraph 16: Xulosa kirish ---
add_body(
    "Shunday qilib, ushbu tadqiqot O'zbekiston Respublikasining raqamli transformatsiya "
    "strategiyasi, energiya tejamkorligi siyosati va aqlli shahar konsepsiyasi doirasida amalga "
    "oshirilgan bo'lib, u nazariy bilimlarni amaliy tatbiq etish orqali real muammoni hal qilishga "
    "qaratilgan. Ishlab chiqilgan tizim nafaqat energiya tejash, balki shahar infratuzilmasini "
    "zamonaviylashtirish, xavfsizlikni oshirish va ekologik barqarorlikni ta'minlash kabi ko'p "
    "qirrali vazifalarga xizmat qiladi. Tadqiqot natijalari ko'cha yoritish sohasida IoT "
    "texnologiyalarini qo'llashning samaradorligini isbotlaydi va ushbu yo'nalishda keyingi "
    "ilmiy izlanishlar uchun poydevor yaratadi."
)

# Page break after KIRISH
doc.add_page_break()

# --- Save ---
output_path = "/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_final.docx"
doc.save(output_path)
print("Done")
