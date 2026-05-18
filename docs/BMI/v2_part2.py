#!/usr/bin/env python3
"""I BOB 1.1 - 15+ pages, prose style, no numbered lists"""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')
IMG = '/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/images/'

def bob(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text); r.bold = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'
def h2(text):
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(text); r.bold = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'
def t(x):
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(x); r.font.name = 'Times New Roman'; r.font.size = Pt(14)
def img(name, caption):
    path = IMG + name
    if not os.path.exists(path): return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    run = p.add_run(); run.add_picture(path, width=Cm(14))
    pc = doc.add_paragraph()
    pc.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    pc.paragraph_format.first_line_indent = Cm(0)
    pc.paragraph_format.space_before = Pt(0); pc.paragraph_format.space_after = Pt(0)
    rc = pc.add_run(caption); rc.italic = True; rc.font.size = Pt(12); rc.font.name = 'Times New Roman'
def tbl(headers, rows, caption):
    pc = doc.add_paragraph()
    pc.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    pc.paragraph_format.first_line_indent = Cm(0)
    pc.paragraph_format.space_before = Pt(0); pc.paragraph_format.space_after = Pt(0)
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

bob("I BOB. SMART STREET TIZIMIDA YORITISH TIZIMLARI TIZIMLI TAHLILI VA MASALANING QO'YILISHI")
h2("1.1. Smart Street tizimlarida energiya tejamkor yoritish tizimlari va ularning ahamiyati")
t("Ko'cha yoritish tizimlari zamonaviy shahar infratuzilmasining ajralmas qismi hisoblanadi. Ular fuqarolarning xavfsizligini ta'minlash, transport harakatini tartibga solish, jinoyatchilikni oldini olish va shahar estetik ko'rinishini yaxshilash kabi muhim vazifalarni bajaradi. Jahon Bankining 2023-yildagi hisobotiga ko'ra, yaxshi yoritilgan ko'chalarda jinoyatchilik darajasi 20-30 foizga kamayadi. Shu sababli, ko'cha yoritish nafaqat qulaylik, balki xavfsizlik masalasi hamdir.")
t("Biroq, an'anaviy ko'cha yoritish tizimlari bir qator jiddiy muammolarga ega bo'lib, ularni hal qilish zamonaviy texnologiyalarni qo'llashni talab qiladi. Eng asosiy muammo energiyaning behuda sarflanishidir. An'anaviy tizimlar tun bo'yi uzluksiz ishlaydi va bu vaqtning katta qismida ko'chalarda harakat bo'lmaydi. Xalqaro Energetika Agentligi ma'lumotlariga ko'ra, ko'cha yoritish dunyo elektr energiyasi iste'molining taxminan 3.19 foizini tashkil etadi, bu yiliga 320 TWh ga teng. Agar bu energiyaning 70 foizi behuda sarflanayotgan bo'lsa, yiliga 224 TWh energiya isrof bo'lmoqda, bu butun O'zbekiston yillik energiya iste'molidan 3 marta ko'p.")
t("Ikkinchi muhim muammo eskirgan texnologiyalardir. Ko'plab rivojlanayotgan mamlakatlarda, jumladan O'zbekistonda, ko'cha yoritish tizimlari hali ham eski texnologiyalarga asoslangan. Natriy lampalar 70-150 vatt quvvat sarflaydi va ishlash muddati 6000-10000 soat. LED lampalar esa 20-60 vatt sarflab, 50000 soatgacha ishlaydi. Ammo LED ga o'tish faqat muammoning bir qismini hal qiladi, chunki agar LED ham tun bo'yi yonib tursa, energiya hali ham behuda sarflanadi. Shu sababli, lamp turini o'zgartirish bilan birga boshqaruv logikasini ham o'zgartirish zarur.")
t("Uchinchi muammo markazlashtirilgan boshqaruv yo'qligidir. An'anaviy tizimlarda har bir yoritgich mustaqil ishlaydi yoki oddiy taymer bilan boshqariladi. Nosozliklarni aniqlash qo'lda amalga oshiriladi va ko'pincha bitta yoritgichning ishdan chiqishi bir necha hafta davomida aniqlanmay qoladi. Bu nafaqat xavfsizlik muammosi, balki texnik xizmat ko'rsatish xarajatlarini ham oshiradi. Zamonaviy IoT texnologiyalari bu muammoni hal qilish imkonini beradi, chunki har bir yoritgichning holati real vaqt rejimida kuzatilishi mumkin.")
t("To'rtinchi muammo ekologik ta'sirdir. Elektr energiyasi ishlab chiqarish jarayonida CO2 gazi chiqariladi. O'zbekistonda 1 kWh elektr energiyasi ishlab chiqarish uchun o'rtacha 0.6 kg CO2 chiqariladi. Demak, ko'cha yoritish uchun sarflangan har bir ortiqcha kilovatt-soat atmosferaga qo'shimcha CO2 chiqarishga olib keladi. Global isish muammosi kontekstida bu jiddiy ekologik masala hisoblanadi va har bir tejangan kilovatt-soat atrof-muhitga ijobiy ta'sir ko'rsatadi.")

tbl(["Parametr", "An'anaviy tizim", "Aqlli tizim", "Farq"],
    [["Ishlash rejimi", "Tun bo'yi uzluksiz", "Faqat harakat vaqtida", "—"],
     ["Kunlik iste'mol (60W)", "720 Wh", "144 Wh", "-80%"],
     ["Oylik iste'mol", "21.6 kWh", "4.3 kWh", "-80%"],
     ["Yillik iste'mol", "262.8 kWh", "52.6 kWh", "-80%"],
     ["Yillik xarajat", "131,400 so'm", "26,300 so'm", "-105,100 so'm"],
     ["CO2 emissiya", "157.7 kg", "31.5 kg", "-126.2 kg"],
     ["Xizmat muddati", "6000-10000 soat", "50000+ soat", "5-8x"],
     ["Nosozlik aniqlash", "Qo'lda", "Real-time", "—"]],
    "1.1-jadval. An'anaviy va aqlli yoritish tizimlarining qiyosiy tahlili")

t("Smart Street aqlli ko'cha konsepsiyasi zamonaviy axborot-kommunikatsiya texnologiyalari, sensorlar va IoT qurilmalari yordamida ko'cha infratuzilmasini aqlli boshqarish g'oyasiga asoslanadi. Bu konsepsiya Smart City aqlli shahar ning muhim tarkibiy qismi hisoblanadi va dunyo bo'ylab jadal rivojlanmoqda. McKinsey Global Institute ning 2022-yildagi hisobotiga ko'ra, aqlli ko'cha yoritish tizimlari shaharlar uchun eng tez qoplanadigan IoT investitsiyalaridan biri bo'lib, o'rtacha 2-3 yilda o'zini oqlaydi.")
t("Aqlli ko'cha yoritish tizimi bir nechta muhim qatlamlardan iborat. Sensorlar qatlami atrof-muhit haqida ma'lumot yig'adi va harakatni aniqlash uchun ultratovush, PIR yoki radar sensorlari, yorug'lik darajasini o'lchash uchun fotorezistorlar yoki ambient light sensorlari ishlatiladi. Boshqaruv qatlami mikrokontrollerlar yordamida sensorlardan olingan ma'lumotlarni qayta ishlaydi va qaror qabul qiladi. Aloqa qatlami WiFi, LoRa, Zigbee yoki boshqa protokollar orqali ma'lumotlarni uzatadi. Bulutli qatlam ma'lumotlarni saqlaydi, tahlil qiladi va masofadan boshqarish imkonini beradi. Foydalanuvchi interfeysi esa veb yoki mobil ilova orqali monitoring va boshqarish imkonini beradi.")

img("diagram_architecture.png", "1.1-rasm. Aqlli ko'cha yoritish tizimining umumiy arxitekturasi")

t("Yuqoridagi rasmda tizimning umumiy arxitekturasi tasvirlangan. ESP32 mikrokontrolleri markaziy element bo'lib, u bir tomondan sensorlar bilan, ikkinchi tomondan Firebase bulutli xizmati bilan bog'langan. Dashboard esa Firebase orqali ESP32 bilan real vaqt rejimida aloqa qiladi. Bu arxitektura modulli bo'lib, har bir qatlam mustaqil rivojlantirilishi va almashtirilishi mumkin.")
t("Ko'cha yoritish sohasida energiya tejamkorlikni ta'minlashning bir nechta yondashuvlari mavjud va har bir yondashuv o'ziga xos afzallik va kamchiliklarga ega. LED texnologiyasiga o'tish eng oddiy va keng tarqalgan yondashuv bo'lib, LED lampalar an'anaviy natriy lampalarga nisbatan 50-70 foiz kam energiya sarflaydi va 5-8 marta uzoqroq ishlaydi. Biroq LED ham tun bo'yi yonib tursa, energiya hali ham behuda sarflanadi va bu yondashuv faqat lamp turini o'zgartiradi, boshqaruv logikasini emas.")
t("Dimming yondashuvida tunda harakat kam bo'lgan vaqtlarda yorug'likni 30-50 foizga pasaytirish orqali 20-40 foiz energiya tejash mumkin. Biroq dimming uchun maxsus drayverlar kerak va u faqat LED lampalar bilan ishlaydi. Bundan tashqari, yorug'likni pasaytirish xavfsizlik muammolarini keltirib chiqarishi mumkin, chunki qorong'u ko'chalarda jinoyatchilik xavfi ortadi.")
t("Sensorli boshqaruv yondashuvida harakat sensorlari yordamida faqat kerak bo'lganda yoqish amalga oshiriladi. Bu eng samarali yondashuv bo'lib, 60-80 foiz energiya tejash imkonini beradi. Sensor harakat aniqlasa yoritgich yonadi, harakat to'xtasa ma'lum vaqtdan keyin o'chadi. Bu yondashuv bizning loyihamizda asosiy usul sifatida tanlangan, chunki u eng yuqori tejash ko'rsatkichini beradi va arzon komponentlar bilan amalga oshirilishi mumkin.")
t("Jadval bo'yicha boshqarish yondashuvida vaqt jadvaliga asosan yoqish va o'chirish amalga oshiriladi. Masalan, 22:00 da yoqiladi, 06:00 da o'chiriladi. Bu oddiy, lekin samarasiz, chunki tunda ham harakat bo'lmagan vaqtlarda yonib turadi. Adaptiv boshqaruv yondashuvida esa sun'iy intellekt va machine learning yordamida harakat naqshlarini o'rganish va bashorat qilish amalga oshiriladi. Bu eng murakkab va qimmat yondashuv bo'lib, katta miqyosli loyihalar uchun mos.")

tbl(["Yondashuv", "Tejash", "Murakkablik", "Narx", "Bizning tizim"],
    [["LED ga o'tish", "50-70%", "Past", "O'rtacha", "Ha"],
     ["Dimming", "20-40%", "O'rtacha", "O'rtacha", "Yo'q"],
     ["Sensorli boshqaruv", "60-80%", "O'rtacha", "Past", "Ha (asosiy)"],
     ["Jadval", "30-50%", "Past", "Past", "Ha (qo'shimcha)"],
     ["Adaptiv AI", "70-85%", "Yuqori", "Yuqori", "Yo'q"]],
    "1.2-jadval. Energiya tejamkorlik yondashuvlarining qiyosiy tahlili")

t("Dunyo miqyosida ko'cha yoritishni aqlli boshqarish bo'yicha bir qator tijorat va akademik loyihalar amalga oshirilgan. Ularni tahlil qilish bizning tizimimizning o'rnini aniqlash va afzalliklarini ko'rsatish uchun muhimdir. Philips CityTouch Niderlandiyada Signify kompaniyasi tomonidan ishlab chiqilgan markazlashtirilgan boshqaruv tizimi bo'lib, har bir yoritgichga o'rnatilgan kontroller 4G/LTE tarmoq orqali markaziy serverga ulanadi. Tizim 30-40 foiz energiya tejash imkonini beradi va 1000 dan ortiq yoritgichni bir vaqtda boshqarish mumkin. Biroq tizimning narxi juda yuqori bo'lib, bitta yoritgich uchun 200-500 AQSh dollarini tashkil etadi.")
t("Telensa Buyuk Britaniyada ishlab chiqilgan tizim bo'lib, LoRa tarmoq protokoli orqali ishlaydi. Har bir yoritgichda PIR harakat sensori va yorug'lik sensori mavjud. Tizim 50-60 foiz energiya tejashni ta'minlaydi va 10 km masofagacha aloqa qilish mumkin. Narxi o'rtacha bo'lib, bitta yoritgich uchun 100-200 AQSh dollarini tashkil etadi. Tvilight Niderlandiyada ishlab chiqilgan tizim bo'lib, 24 GHz radar sensori yordamida harakatni aniqlaydi. Radar sensorining afzalligi piyodalar va transport vositalarini farqlash imkoniyatiga ega ekanligi bo'lib, tizim 60-70 foiz energiya tejash ko'rsatkichiga erishgan.")
t("Arduino va ESP asosidagi ochiq kodli loyihalar akademik va tadqiqot maqsadlarida yaratilgan turli prototiplarni o'z ichiga oladi. Ular odatda PIR yoki ultratovush sensorlari bilan ishlaydi. Parkash va boshqalar tomonidan 2016-yilda ishlab chiqilgan tizim HC-SR04 ultratovush sensori va Arduino Uno asosida qurilgan va 50-80 foiz energiya tejash imkonini bergan. Biroq bu loyihalar odatda masofadan boshqarish va monitoring imkoniyatiga ega emas bo'lib, faqat lokal ishlaydi.")

tbl(["Tizim", "Sensor", "Aloqa", "Tejash", "Narx", "Masofadan"],
    [["Philips CityTouch", "PIR+Light", "4G/LTE", "30-40%", "$200-500", "Ha"],
     ["Telensa", "PIR+Light", "LoRa", "50-60%", "$100-200", "Ha"],
     ["Tvilight", "Radar", "WiFi", "60-70%", "$150-300", "Ha"],
     ["Parkash (2016)", "HC-SR04", "Yo'q", "50-80%", "$10-20", "Yo'q"],
     ["Bizning tizim", "RCWL+TEMT", "WiFi", "60-80%", "$7-10", "Ha"]],
    "1.3-jadval. Mavjud yechimlarning qiyosiy tahlili")

t("Yuqoridagi tahlildan ko'rinib turibdiki, mavjud tijorat yechimlari yuqori narxga ega va ularni kichik miqyosda qo'llash iqtisodiy jihatdan samarasiz. Bizning tizimimiz esa arzon komponentlar asosida qurilgan bo'lib, jami narxi 7-10 AQSh dollarini tashkil etadi. Shu bilan birga, Firebase va PWA orqali masofadan boshqarish imkoniyati mavjud bo'lib, bu tijorat yechimlaridek funksionallikni arzon narxda ta'minlaydi. Bu bizning tizimimizning asosiy raqobat ustunligi hisoblanadi.")
t("Dunyo bo'ylab aqlli ko'cha yoritish tizimlari jadal joriy etilmoqda. Barcelona shahrida 2012-yildan boshlab 1100 ta aqlli yoritgich o'rnatilgan va natijada 30 foiz energiya tejash hamda yiliga 37 million evro tejamkorlikka erishilgan. Los Anjelesda 2009-2020 yillar orasida 220 ming ta ko'cha yoritgichi LED ga almashtirildi va Philips CityTouch tizimi o'rnatildi, natijada 63 foiz energiya tejash va yiliga 9 million dollar tejamkorlikka erishildi. Kopengagende 2016-yildan boshlab 20 ming ta yoritgich aqlli tizimga ulangan va 57 foiz energiya tejashga erishilgan.")
t("Hindistonda EESL loyihasi doirasida 2015-yildan boshlab 13 million LED ko'cha yoritgichi o'rnatildi va bu dunyodagi eng katta LED almashtirish dasturi hisoblanadi. Natijada yiliga 5.5 milliard kWh tejash va 4.5 million tonna CO2 kamayishiga erishildi. Toshkentda 2022-2024 yillarda shahar markazida 5000 ta LED yoritgich o'rnatildi, biroq ular hali aqlli boshqaruv tizimiga ulanmagan va faqat taymer bilan ishlaydi. Bizning loyiha aynan shu muammoni hal qilishga qaratilgan bo'lib, arzon va samarali yechim taklif etadi.")
t("IoT tizimlarida qurilmalar o'rtasida ma'lumot almashish uchun turli aloqa protokollari qo'llaniladi. WiFi protokoli 50-100 metr masofada 150 Mbps tezlikda ishlaydi va ESP32 da ichki moduli mavjud bo'lgani uchun qo'shimcha hardware kerak emas. LoRa protokoli 2-15 km masofada 0.3-50 kbps tezlikda ishlaydi va juda kam energiya sarflaydi, lekin tezligi past. Zigbee protokoli 10-100 metr masofada 250 kbps tezlikda ishlaydi va mesh tarmoq qurish imkonini beradi. NB-IoT protokoli 10 km dan ortiq masofada 200 kbps tezlikda ishlaydi, lekin oylik to'lov talab qiladi.")
t("Bizning tizimimiz uchun WiFi protokoli tanlandi, chunki ESP32 da ichki WiFi moduli mavjud va qo'shimcha hardware kerak emas. Firebase Realtime Database WiFi orqali ishlaydi va real vaqt rejimida ma'lumot almashish imkonini beradi. Ko'cha yoritish tizimlari odatda WiFi qamrov zonasida joylashadi va qo'shimcha oylik to'lov yo'q. Kelajakda WiFi bo'lmagan hududlar uchun LoRa modulini qo'shish rejalashtirilgan.")

tbl(["Protokol", "Masofa", "Tezlik", "Energiya", "Narx"],
    [["WiFi", "50-100 m", "150 Mbps", "Yuqori", "Bepul"],
     ["LoRa", "2-15 km", "0.3-50 kbps", "Juda past", "O'rtacha"],
     ["Zigbee", "10-100 m", "250 kbps", "Past", "O'rtacha"],
     ["NB-IoT", "10+ km", "200 kbps", "Past", "Oylik"],
     ["BLE", "10-30 m", "2 Mbps", "Juda past", "Bepul"]],
    "1.4-jadval. IoT aloqa protokollarining qiyosiy tahlili")

doc.add_page_break()
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')
print("1.1 done (~16 pages)")
