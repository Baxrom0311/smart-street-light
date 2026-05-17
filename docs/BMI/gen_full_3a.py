#!/usr/bin/env python3
"""I BOB - 1.1, 1.2, 1.3 sections (~25 pages)"""
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

hc("I BOB. SMART STREET TIZIMIDA YORITISH TIZIMLARI\nTIZIMLI TAHLILI VA MASALANING QO'YILISHI")

h2("1.1. Smart Street tizimlarida energiya tejamkor yoritish tizimlari va ularning ahamiyati")

h3("1.1.1. Ko'cha yoritish tizimlarining hozirgi holati va muammolari")
t("Ko'cha yoritish tizimlari zamonaviy shahar infratuzilmasining ajralmas qismi hisoblanadi. Ular fuqarolarning xavfsizligini ta'minlash, transport harakatini tartibga solish, jinoyatchilikni oldini olish va shahar estetik ko'rinishini yaxshilash kabi muhim vazifalarni bajaradi. Jahon Bankining 2023-yildagi hisobotiga ko'ra, yaxshi yoritilgan ko'chalarda jinoyatchilik darajasi 20-30 foizga kamayadi [1]. Biroq, an'anaviy ko'cha yoritish tizimlari bir qator jiddiy muammolarga ega bo'lib, ularni hal qilish zamonaviy texnologiyalarni qo'llashni talab qiladi.")
t("Birinchi muammo — energiyaning behuda sarflanishi. An'anaviy tizimlar tun bo'yi (o'rtacha 10-12 soat) uzluksiz ishlaydi. Kuzatishlar shuni ko'rsatadiki, tun vaqtining 60-70 foizida ko'chalarda harakat deyarli kuzatilmaydi. Xalqaro Energetika Agentligi (IEA) ma'lumotlariga ko'ra, ko'cha yoritish dunyo elektr energiyasi iste'molining taxminan 3.19 foizini tashkil etadi, bu yiliga 320 TWh ga teng [6]. Agar bu energiyaning 70 foizi behuda sarflanayotgan bo'lsa, yiliga 224 TWh energiya isrof bo'lmoqda — bu butun O'zbekiston yillik energiya iste'molidan 3 marta ko'p.")
t("Ikkinchi muammo — eskirgan texnologiyalar. Ko'plab rivojlanayotgan mamlakatlarda, jumladan O'zbekistonda, ko'cha yoritish tizimlari hali ham eski texnologiyalarga asoslangan. Natriy lampalar (HPS — High Pressure Sodium) 70-150W quvvat sarflaydi va ishlash muddati 6000-10000 soat. LED lampalar esa 20-60W sarflab, 50000 soatgacha ishlaydi [7]. Ammo LED ga o'tish faqat muammoning bir qismini hal qiladi — agar LED ham tun bo'yi yonib tursa, energiya hali ham behuda sarflanadi.")
t("Uchinchi muammo — markazlashtirilgan boshqaruv yo'qligi. An'anaviy tizimlarda har bir yoritgich mustaqil ishlaydi yoki oddiy taymer bilan boshqariladi. Nosozliklarni aniqlash qo'lda amalga oshiriladi va ko'pincha bitta yoritgichning ishdan chiqishi bir necha hafta davomida aniqlanmay qoladi. Bu nafaqat xavfsizlik muammosi, balki texnik xizmat ko'rsatish xarajatlarini ham oshiradi.")
t("To'rtinchi muammo — ekologik ta'sir. Elektr energiyasi ishlab chiqarish jarayonida CO2 gazi chiqariladi. O'zbekistonda 1 kWh elektr energiyasi ishlab chiqarish uchun o'rtacha 0.6 kg CO2 chiqariladi [5]. Demak, ko'cha yoritish uchun sarflangan har bir ortiqcha kilovatt-soat atmosferaga qo'shimcha CO2 chiqarishga olib keladi.")

tbl(["Parametr", "An'anaviy tizim", "Aqlli tizim", "Farq"],
    [["Ishlash rejimi", "Tun bo'yi uzluksiz (12h)", "Faqat harakat vaqtida", "—"],
     ["Kunlik iste'mol (60W)", "720 Wh", "144 Wh", "-80%"],
     ["Oylik iste'mol", "21.6 kWh", "4.3 kWh", "-80%"],
     ["Yillik iste'mol", "262.8 kWh", "52.6 kWh", "-80%"],
     ["Yillik xarajat (500 so'm/kWh)", "131,400 so'm", "26,300 so'm", "-105,100 so'm"],
     ["CO2 emissiya (yiliga)", "157.7 kg", "31.5 kg", "-126.2 kg"],
     ["Xizmat muddati", "6000-10000 soat", "50000+ soat", "5-8x"],
     ["Nosozlik aniqlash", "Qo'lda (kunlar)", "Real-time (soniyalar)", "—"]],
    "1.1-jadval. An'anaviy va aqlli yoritish tizimlarining qiyosiy tahlili")

h3("1.1.2. Smart Street (Aqlli ko'cha) konsepsiyasi va IoT texnologiyalari")
t("Smart Street — bu zamonaviy axborot-kommunikatsiya texnologiyalari, sensorlar va IoT qurilmalari yordamida ko'cha infratuzilmasini aqlli boshqarish konsepsiyasidir. Bu konsepsiya Smart City (Aqlli shahar) ning muhim tarkibiy qismi hisoblanadi va dunyo bo'ylab jadal rivojlanmoqda [8]. McKinsey Global Institute ning 2022-yildagi hisobotiga ko'ra, aqlli ko'cha yoritish tizimlari shaharlar uchun eng tez qoplanadigan IoT investitsiyalaridan biri bo'lib, o'rtacha 2-3 yilda o'zini oqlaydi.")
t("Aqlli ko'cha yoritish tizimi quyidagi asosiy komponentlardan iborat bo'lib, ularning har biri muhim vazifani bajaradi:")
t("1) Sensorlar qatlami (Perception Layer) — bu qatlam atrof-muhit haqida ma'lumot yig'adi. Harakatni aniqlash uchun ultratovush, PIR yoki radar sensorlari, yorug'lik darajasini o'lchash uchun fotorezistorlar yoki ambient light sensorlari, ob-havo sharoitlarini kuzatish uchun harorat va namlik sensorlari ishlatiladi. Bizning tizimimizda RCWL-9610A ultratovush sensori va TEMT6000 yorug'lik sensori ishlatiladi.")
t("2) Boshqaruv qatlami (Processing Layer) — mikrokontrollerlar yordamida sensorlardan olingan ma'lumotlarni qayta ishlash va qaror qabul qilish. ESP32 mikrokontrolleri bu vazifani bajaradi — u sensorlardan ma'lumot o'qiydi, algoritmlar asosida qaror qabul qiladi (yoqish/o'chirish) va natijani relay orqali amalga oshiradi.")
t("3) Aloqa qatlami (Network Layer) — WiFi, LoRa, Zigbee, NB-IoT yoki boshqa protokollar orqali ma'lumotlarni uzatish. Bizning tizimimizda WiFi (802.11 b/g/n) ishlatiladi, chunki u keng tarqalgan, tezkor va Firebase bilan integratsiya oson. ESP32 ning ichki WiFi moduli tashqi qurilma kerakligini bartaraf etadi.")
t("4) Bulutli qatlam (Cloud Layer) — ma'lumotlarni saqlash, tahlil qilish va masofadan boshqarish. Firebase Realtime Database real vaqt rejimida ma'lumot almashish imkonini beradi. Firebase ning afzalligi — u WebSocket protokoli orqali ishlaydi va ma'lumot o'zgarganda darhol barcha ulangan qurilmalarga xabar beradi (push model).")
t("5) Foydalanuvchi interfeysi (Application Layer) — veb yoki mobil ilova orqali monitoring va boshqarish. Bizning tizimimizda React asosida PWA (Progressive Web Application) yaratilgan bo'lib, u brauzerda ishlaydi, lekin native ilova kabi ko'rinadi va ishlaydi.")

img("diagram_architecture.png", "1.1-rasm. Aqlli ko'cha yoritish tizimining umumiy arxitekturasi")

t("1.1-rasmda tizimning umumiy arxitekturasi tasvirlangan. Ko'rinib turibdiki, ESP32 mikrokontrolleri markaziy element bo'lib, u bir tomondan sensorlar bilan, ikkinchi tomondan Firebase bulutli xizmati bilan bog'langan. Dashboard esa Firebase orqali ESP32 bilan real vaqt rejimida aloqa qiladi.")

h3("1.1.3. Energiya tejamkorlik yondashuvlari va ularning samaradorligi")
t("Ko'cha yoritish sohasida energiya tejamkorlikni ta'minlashning bir nechta yondashuvlari mavjud. Har bir yondashuv o'ziga xos afzallik va kamchiliklarga ega [9]:")
t("1) LED texnologiyasiga o'tish — eng oddiy va keng tarqalgan yondashuv. LED lampalar an'anaviy natriy lampalarga nisbatan 50-70% kam energiya sarflaydi va 5-8 marta uzoqroq ishlaydi. Biroq, LED ham tun bo'yi yonib tursa, energiya hali ham behuda sarflanadi. Bu yondashuv faqat lamp turini o'zgartiradi, boshqaruv logikasini emas.")
t("2) Dimming (yorug'lik darajasini pasaytirish) — tunda harakat kam bo'lgan vaqtlarda yorug'likni 30-50% ga pasaytirish. Bu yondashuv 20-40% energiya tejash imkonini beradi. Biroq, dimming uchun maxsus drayverlar kerak va u faqat LED lampalar bilan ishlaydi. Bundan tashqari, yorug'likni pasaytirish xavfsizlik muammolarini keltirib chiqarishi mumkin.")
t("3) Sensorli boshqaruv — harakat sensorlari yordamida faqat kerak bo'lganda yoqish. Bu eng samarali yondashuv bo'lib, 60-80% energiya tejash imkonini beradi. Sensor harakat aniqlasa — yoritgich yonadi, harakat to'xtasa — ma'lum vaqtdan keyin o'chadi. Bu yondashuv bizning loyihamizda asosiy usul sifatida tanlangan.")
t("4) Jadval bo'yicha boshqarish — vaqt jadvaliga asosan yoqish/o'chirish. Masalan, 22:00 dan 06:00 gacha yoniq, qolgan vaqtda o'chiq. Bu oddiy, lekin samarasiz — chunki tunda ham harakat bo'lmagan vaqtlarda yonib turadi.")
t("5) Adaptiv boshqaruv — sun'iy intellekt va machine learning yordamida harakat naqshlarini o'rganish va bashorat qilish. Bu eng murakkab va qimmat yondashuv bo'lib, katta miqyosli loyihalar uchun mos.")

tbl(["Yondashuv", "Tejash %", "Murakkablik", "Narx", "Bizning tizim"],
    [["LED ga o'tish", "50-70%", "Past", "O'rtacha", "Ha (LED lamp)"],
     ["Dimming", "20-40%", "O'rtacha", "O'rtacha", "Yo'q"],
     ["Sensorli boshqaruv", "60-80%", "O'rtacha", "Past", "Ha (asosiy)"],
     ["Jadval", "30-50%", "Past", "Past", "Ha (qo'shimcha)"],
     ["Adaptiv (AI)", "70-85%", "Yuqori", "Yuqori", "Yo'q"]],
    "1.2-jadval. Energiya tejamkorlik yondashuvlarining qiyosiy tahlili")

h3("1.1.4. Mavjud tijorat va akademik yechimlarning tahlili")
t("Dunyo miqyosida ko'cha yoritishni aqlli boshqarish bo'yicha bir qator tijorat va akademik loyihalar amalga oshirilgan. Ularni tahlil qilish bizning tizimimizning o'rnini aniqlash va afzalliklarini ko'rsatish uchun muhimdir.")
t("Philips CityTouch — Niderlandiyada Signify (avvalgi Philips Lighting) kompaniyasi tomonidan ishlab chiqilgan markazlashtirilgan boshqaruv tizimi. Har bir yoritgichga o'rnatilgan kontroller 4G/LTE tarmoq orqali markaziy serverga ulanadi. Tizim 30-40% energiya tejash imkonini beradi va 1000+ yoritgichni bir vaqtda boshqarish mumkin. Biroq, tizimning narxi juda yuqori — bitta yoritgich uchun $200-500 [11].")
t("Telensa — Buyuk Britaniyada ishlab chiqilgan tizim bo'lib, LoRa (Long Range) tarmoq protokoli orqali ishlaydi. Har bir yoritgichda PIR harakat sensori va yorug'lik sensori mavjud. Tizim 50-60% energiya tejashni ta'minlaydi va 10 km masofagacha aloqa qilish mumkin. Narxi o'rtacha — bitta yoritgich uchun $100-200 [12].")
t("Tvilight — Niderlandiyada ishlab chiqilgan tizim bo'lib, 24 GHz radar sensori yordamida harakatni aniqlaydi. Radar sensorining afzalligi — u piyodalar va transport vositalarini farqlash imkoniyatiga ega. Tizim 60-70% energiya tejash ko'rsatkichiga erishgan. Biroq, radar sensorining narxi yuqori ($50-100) [13].")
t("Arduino/ESP asosidagi ochiq kodli loyihalar — akademik va tadqiqot maqsadlarida yaratilgan turli prototiplar. Ular odatda PIR yoki ultratovush sensorlari bilan ishlaydi. Parkash va boshqalar (2016) tomonidan ishlab chiqilgan tizim HC-SR04 ultratovush sensori va Arduino Uno asosida qurilgan va 50-80% energiya tejash imkonini bergan [14]. Biroq, bu loyihalar odatda masofadan boshqarish va monitoring imkoniyatiga ega emas.")

tbl(["Tizim", "Sensor", "Aloqa", "Tejash", "Narx (1 ta)", "Masofadan boshqarish"],
    [["Philips CityTouch", "PIR + Light", "4G/LTE", "30-40%", "$200-500", "Ha"],
     ["Telensa", "PIR + Light", "LoRa", "50-60%", "$100-200", "Ha"],
     ["Tvilight", "Radar 24GHz", "WiFi", "60-70%", "$150-300", "Ha"],
     ["Parkash (2016)", "HC-SR04", "Yo'q", "50-80%", "$10-20", "Yo'q"],
     ["Bizning tizim", "RCWL-9610A+TEMT6000", "WiFi/Firebase", "60-80%", "$7-10", "Ha (PWA)"]],
    "1.3-jadval. Mavjud yechimlarning qiyosiy tahlili")

t("Yuqoridagi tahlildan ko'rinib turibdiki, mavjud tijorat yechimlari yuqori narxga ega va ularni kichik miqyosda qo'llash iqtisodiy jihatdan samarasiz. Bizning tizimimiz esa arzon komponentlar (ESP32 ~$5, RCWL-9610A ~$1, TEMT6000 ~$0.5, Relay ~$1) asosida qurilgan bo'lib, jami narxi $7-10 ni tashkil etadi. Shu bilan birga, Firebase va PWA orqali masofadan boshqarish imkoniyati mavjud — bu tijorat yechimlaridek funksionallikni arzon narxda ta'minlaydi.")

doc.add_page_break()
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_full.docx')
print("I BOB 1.1 done (~12 pages)")
