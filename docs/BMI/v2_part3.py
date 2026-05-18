#!/usr/bin/env python3
"""I BOB 1.2 + 1.3"""
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

# === 1.2 ===
h2("1.2. Ultratovush sensorlarning ishlash prinsipi va texnik xususiyatlari")
t("Ultratovush bu chastotasi 20 kHz dan yuqori bo'lgan mexanik to'lqinlardir. Inson qulog'i 20 Hz dan 20 kHz gacha bo'lgan chastotadagi tovushlarni eshita oladi, ultratovush esa bu diapazondan tashqarida joylashgan. Ultratovush sensorlari odatda 40 kHz chastotada ishlaydi va bu chastota havoda yaxshi tarqaladi hamda qattiq jismlardan samarali aks etadi. Ultratovush to'lqinlari tibbiyotda, sanoatda, robototexnikada va xavfsizlik tizimlarida keng qo'llaniladi.")
t("Havoda ultratovush tezligi haroratga bog'liq bo'lib, v = 331.3 + 0.606 × T formulasi bilan aniqlanadi, bu yerda v tovush tezligi metr/soniyada, T esa harorat Selsiy darajasida. 20 daraja haroratda tovush tezligi 343.4 m/s ga teng. Bu qiymat amaliy hisoblashlarda 343 m/s yoki 0.0343 cm/mikrosoniya sifatida ishlatiladi. Haroratning plus-minus 10 daraja o'zgarishi tezlikni faqat plus-minus 2 foizga o'zgartiradi, bu ko'cha yoritish uchun ahamiyatsiz xatolik hisoblanadi.")
t("Ultratovush to'lqinlarining asosiy xususiyatlari quyidagilardan iborat. Ular qattiq jismlardan aks etadi va bu masofa o'lchash uchun asosiy prinsipdir. Ular ma'lum burchak ostida tarqaladi va RCWL-9610A uchun bu burchak taxminan 30 daraja bo'lib, ko'cha yoritish uchun yetarli qamrov beradi. Ular ob-havo sharoitlariga kam ta'sirchan bo'lib, infraqizil sensorlardan farqli ravishda yomg'irda ham ishlaydi. Ular yorug'lik sharoitiga umuman bog'liq emas va tunda hamda kunduz bir xil ishlaydi.")
t("Ultratovush sensori Time of Flight ya'ni uchish vaqti prinsipiga asoslanadi. Sensor ultratovush impulsini yuboradi, u ob'ektdan aks etib qaytadi va sensor qaytgan signalni qabul qiladi. Impulsning borish va qaytish vaqtini o'lchab, ob'ektgacha bo'lgan masofani hisoblash mumkin. Masofa formulasi d = (t × v) / 2 bo'lib, bu yerda d ob'ektgacha bo'lgan masofa, t to'lqinning borish va qaytish vaqti, v havoda tovush tezligi. Ikki ga bo'linadi chunki to'lqin ikki marta yo'l bosadi, ya'ni ob'ektgacha va qaytib.")
t("Amaliy misollar orqali formulani tushuntirish mumkin. Agar vaqt 580 mikrosoniya bo'lsa, masofa 580 × 0.0343 / 2 = 9.95 sm ga teng, ya'ni taxminan 10 santimetr. Agar vaqt 11600 mikrosoniya bo'lsa, masofa 11600 × 0.0343 / 2 = 198.9 sm ga teng, ya'ni taxminan 2 metr. Bizning tizimimizda 200 santimetr chegara qiymati sifatida belgilangan va agar masofa 200 santimetrdan kam bo'lsa, harakat aniqlangan deb hisoblanadi.")

img("diagram_sequence.png", "1.2-rasm. Ultratovush sensori yordamida masofa o'lchash jarayoni")

t("Yuqoridagi rasmda ultratovush sensori yordamida masofa o'lchash jarayonining ketma-ketlik diagrammasi tasvirlangan. ESP32 TRIG signalini yuboradi, sensor ultratovush impulsini chiqaradi, impuls ob'ektdan aks etadi va ECHO signal orqali vaqt o'lchanadi. Bu jarayon har 300 millisekundda takrorlanadi.")
t("ESP32 dasturida bu hisoblash quyidagicha amalga oshiriladi. TRIG pinga 10 mikrosekundlik HIGH signal yuboriladi va sensor 8 ta 40 kHz impuls yuboradi. ECHO pin HIGH bo'ladi va ob'ektdan aks etgan signal qaytganda LOW ga tushadi. pulseIn funksiyasi ECHO pinning HIGH bo'lgan vaqtini mikrosekundlarda qaytaradi. Keyin distance_cm = duration * 0.034 / 2 formulasi bilan masofa hisoblanadi.")
t("Loyiha uchun RCWL-9610A ultratovush sensori tanlandi. Bu sensor HC-SR04 ning zamonaviy va takomillashtirilgan versiyasi bo'lib, bir qator muhim afzalliklarga ega. Eng muhimi, u 3.3V da ishlaydi va ESP32 ning logika darajasi ham 3.3V bo'lgani uchun qo'shimcha level shifter kerak emas. Bundan tashqari, u kam tok iste'mol qiladi, ya'ni 2 milliamper, HC-SR04 esa 15 milliamper sarflaydi. Keng burchagi 30 daraga teng bo'lib, HC-SR04 ning 15 darajasiga nisbatan ko'cha yoritish uchun kattaroq qamrov beradi.")

tbl(["Parametr", "RCWL-9610A", "HC-SR04"],
    [["Ish kuchlanishi", "3.0-5.5V", "5V (faqat)"],
     ["Ish toki", "< 2 mA", "15 mA"],
     ["O'lchash diapazoni", "2-450 cm", "2-400 cm"],
     ["O'lchash aniqligi", "±1 cm", "±3 mm"],
     ["Ishchi chastota", "40 kHz", "40 kHz"],
     ["O'lchash burchagi", "~30°", "~15°"],
     ["O'lcham", "21×15 mm", "45×20 mm"],
     ["3.3V mos", "Ha", "Yo'q"]],
    "1.5-jadval. RCWL-9610A va HC-SR04 qiyosiy tahlili")

t("Tizimda kunduz va tun holatini aniqlash uchun TEMT6000 ambient light sensori ishlatiladi. Bu sensor Vishay kompaniyasi tomonidan ishlab chiqilgan bo'lib, inson ko'zining spektral sezgirligiga yaqin xususiyatga ega. Sensor fototransistor asosida ishlaydi va yorug'lik intensivligiga proporsional analog signal chiqaradi. Uning spektral diapazoni 360 dan 970 nanometrgacha bo'lib, ko'rinadigan yorug'lik diapazonini to'liq qamrab oladi. Maksimal sezgirligi 570 nanometrda, ya'ni yashil rang diapazonida joylashgan.")
t("ESP32 ning 12-bitli ADC yordamida sensor signali 0 dan 4095 gacha bo'lgan raqamli qiymatga o'giriladi. Bizning tizimimizda quyidagi chegaralar belgilangan. 0 dan 250 gacha qorong'u holat bo'lib, yoritgich yonishi kerak. 250 dan 350 gacha oraliq zona bo'lib, holat o'zgarmaydi. 350 dan yuqori yorug' holat bo'lib, yoritgich o'chiq bo'lishi kerak. Bu ikki chegarali tizim hysteresis deb ataladi va u yorug'lik chegarasida tebranishni bartaraf etadi.")
t("Real sharoitlarda ultratovush sensorlari ba'zan noto'g'ri natijalar berishi mumkin. Bu shovqin deb ataladi va uning sabablari havo oqimi, harorat o'zgarishi, sensorning o'zi chiqargan signalning ichki aks etishi va yaqin atrofdagi boshqa ultratovush manbalari bo'lishi mumkin. Shovqinni bartaraf etish uchun maxsus algoritmlar ishlab chiqildi.")
t("Debounce algoritmi 3 ta ketma-ket o'lchov oladi va kamida 2 tasi harakat ko'rsatsa harakat aniqlangan deb hisoblanadi. Bu bitta noto'g'ri o'lchovning ta'sirini yo'q qiladi. Masalan, agar 3 ta o'lchov 150, 450 va 120 santimetr bo'lsa, 2 tasi 200 santimetrdan kam, demak harakat bor. Bu majority voting prinsipi deb ataladi va shovqinni samarali filtrlaydi.")
t("Hold timer algoritmi oxirgi harakatdan 5 soniya o'tmagan bo'lsa harakat bor holatini saqlaydi. Bu yoritgichning tez-tez yonib-o'chishini oldini oladi. Masalan, odam sekin yursa va sensor uni har doim aniqlay olmasa ham, 5 soniya ichida yoritgich o'chmaydi. Bu foydalanuvchi tajribasini yaxshilaydi va relay kontaktlarining erta eskirishini oldini oladi.")
t("Hysteresis algoritmi yorug'lik sensori uchun ikki chegarali tizim bo'lib, pastki chegara 250 va yuqori chegara 350 qilib belgilangan. Sensor qiymati 250 dan pastga tushsa qorong'u holati o'rnatiladi, 350 dan oshsa yorug' holati o'rnatiladi, 250 va 350 orasida esa holat o'zgarmaydi. Bu 100 birlik o'lik zona yaratadi va bulutli ob-havoda yoritgichning beqaror ishlashini oldini oladi.")

img("diagram_flowchart.png", "1.3-rasm. Harakatni aniqlash algoritmining blok-sxemasi")

t("Yuqoridagi rasmda tizimning asosiy ishlash algoritmi tasvirlangan. Algoritm avval yorug'lik darajasini tekshiradi va agar kunduz bo'lsa yoritgich o'chiq qoladi. Agar tun bo'lsa harakat sensorini tekshiradi va harakat aniqlansa yoritgich yonadi, aks holda 5 soniya kutib o'chiradi. Bu algoritm har 300 millisekundda takrorlanadi va tizimning asosiy ishlash logikasini tashkil etadi.")

doc.add_page_break()

# === 1.3 ===
h2("1.3. Masalaning qo'yilishi")
t("Yuqorida keltirilgan tahlillar asosida quyidagi muammo aniqlanadi. An'anaviy ko'cha yoritish tizimlari tun bo'yi uzluksiz ishlaydi va energiyaning 60-80 foizi behuda sarflanadi. Mavjud tijorat yechimlari yuqori narxga ega bo'lib, bitta yoritgich uchun 100-500 AQSh dollari talab qilinadi va kichik miqyosda qo'llash iqtisodiy jihatdan samarasiz. Akademik loyihalar esa masofadan boshqarish va monitoring imkoniyatiga ega emas bo'lib, faqat lokal ishlaydi.")
t("Shu sababli quyidagi masala qo'yiladi. ESP32 mikrokontrolleri, RCWL-9610A ultratovush sensori va TEMT6000 yorug'lik sensori asosida arzon narxli, masofadan boshqariladigan, energiya tejamkor ko'cha yoritish tizimini ishlab chiqish zarur. Tizim real vaqt rejimida monitoring qilinishi va 60-80 foiz energiya tejash ko'rsatkichiga erishishi kerak. Tizim internet bo'lmagan holda ham avtonom ishlashi va aloqa tiklanganda avtomatik sinxronizatsiya qilishi kerak.")
t("Ishlab chiqiladigan tizim quyidagi funksional talablarga javob berishi kerak. Harakatni aniqlash ultratovush sensori yordamida 2 metr masofagacha bo'lgan ob'ektlarni aniqlashi kerak va aniqlash aniqligi plus-minus 1 santimetr, javob vaqti 100 millisekunddan kam bo'lishi kerak. Kunduz va tun farqlash yorug'lik sensori yordamida avtomatik ravishda amalga oshirilishi va kunduz kuni yoritgich umuman yonmasligi kerak. Avtomatik boshqarish qorong'uda harakat aniqlanganda yoritgichni yoqishi va harakat to'xtagandan 5 soniya keyin o'chirishi kerak.")
t("Masofadan boshqarish veb-interfeys orqali yoritgichni qo'lda yoqish va o'chirish, rejimni o'zgartirish imkonini berishi kerak. Real-time monitoring sensor qiymatlari, yoritgich holati va statistikani jonli ko'rsatishi kerak. Energiya statistikasi kunlik, haftalik va oylik energiya tejash ko'rsatkichlarini hisoblashi va saqlashi kerak. Offline ishlash internet bo'lmagan holda ham avtonom ishlashni ta'minlashi va aloqa tiklanganda sinxronizatsiya qilishi kerak. WiFi konfiguratsiya captive portal orqali WiFi ma'lumotlarini o'zgartirish imkoniyatini berishi kerak.")
t("Tizim quyidagi nofunksional talablarga ham javob berishi kerak. Ishonchlilik jihatidan tizim 24 soat 7 kun uzluksiz ishlashi va xotira oqishi bo'lmasligi kerak. Javob vaqti jihatidan sensor o'qishdan relay yoqishgacha 100 millisekunddan kam, dashboard buyrug'idan qurilma javobigacha 500 millisekunddan kam bo'lishi kerak. Energiya samaradorligi jihatidan tizimning o'zi 250 milliamperdan kam tok iste'mol qilishi kerak. Xavfsizlik jihatidan Firebase Authentication orqali faqat vakolatli foydalanuvchilar boshqarishi mumkin bo'lishi kerak.")
t("Tizimning energiya tejash samaradorligini baholash uchun quyidagi matematik model ishlab chiqildi. Energiya tejash foizi E_tejash = ((T_tun - T_yonish) / T_tun) × 100 formulasi bilan hisoblanadi, bu yerda T_tun tun davomiyligi soatlarda, T_yonish yoritgichning haqiqiy yonish vaqti soatlarda. Misol uchun, agar tun davomiyligi 12 soat va yoritgichning yonish vaqti 2.5 soat bo'lsa, energiya tejash foizi ((12 - 2.5) / 12) × 100 = 79.2 foizni tashkil etadi.")
t("Kunlik energiya tejash kilovatt-soatlarda E_kunlik = P × (T_tun - T_yonish) / 1000 formulasi bilan hisoblanadi, bu yerda P yoritgich quvvati vattlarda. Misol uchun, agar yoritgich quvvati 60 vatt, tun davomiyligi 12 soat va yonish vaqti 2.5 soat bo'lsa, kunlik tejash 60 × 9.5 / 1000 = 0.57 kWh ni tashkil etadi. Bu oyiga 17.1 kWh va yiliga 208 kWh ga teng. Pul hisobida 500 so'm/kWh narxda yillik tejamkorlik 104 ming so'mni tashkil etadi.")
t("Birinchi bobda ko'cha yoritish tizimlarining hozirgi holati tahlil qilindi, mavjud muammolar aniqlandi va ularni hal qilish yo'llari ko'rib chiqildi. Ultratovush sensorlarining ishlash prinsipi, fizik asoslari va texnik xususiyatlari batafsil o'rganildi. Mavjud tijorat va akademik yechimlar qiyosiy tahlil qilindi va ularning kamchiliklari aniqlandi. Natijada ESP32, RCWL-9610A, TEMT6000 va Firebase asosida arzon, samarali va masofadan boshqariladigan energiya tejamkor yoritish tizimini ishlab chiqish masalasi qo'yildi. Keyingi bobda ushbu masalaning amaliy yechimi batafsil bayon etiladi.")

doc.add_page_break()
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')
print("1.2 + 1.3 done (~18 pages)")
