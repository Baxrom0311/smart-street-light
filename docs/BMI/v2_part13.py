#!/usr/bin/env python3
"""Final 10+ pages to reach 100"""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')
IMG = '/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/images/'

def h2(t_):
    p = doc.add_paragraph(); p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(t_); r.bold = True; r.font.size = Pt(14); r.font.name = 'Times New Roman'
def t(x):
    p = doc.add_paragraph(); p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(x); r.font.name = 'Times New Roman'; r.font.size = Pt(14)
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
def img(name, caption):
    if not os.path.exists(IMG + name): return
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    run = p.add_run(); run.add_picture(IMG + name, width=Cm(14))
    pc = doc.add_paragraph(); pc.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    pc.paragraph_format.first_line_indent = Cm(0); pc.paragraph_format.space_before = Pt(0); pc.paragraph_format.space_after = Pt(0)
    rc = pc.add_run(caption); rc.italic = True; rc.font.size = Pt(12); rc.font.name = 'Times New Roman'

doc.add_page_break()
h2("YA ilova. Tizimning real sharoitlarda ishlash tajribasi")
t("Tizim ishlab chiqilgandan keyin bir nechta muhim muammolar yuzaga keldi va ular iterativ ravishda hal qilindi. Bu tajriba kelajakda shunga o'xshash loyihalar uchun foydali bo'lishi mumkin. Birinchi muammo ESP32 ning GPIO pinlarini tanlash bilan bog'liq bo'ldi. Dastlab relay uchun GPIO 27 tanlangan edi, chunki u ADC2 kanalida joylashgan va WiFi bilan conflict bo'lishi mumkin edi. Sinov davomida relay ishlamadi va GPIO 26 ga o'tish muammoni hal qildi. Bu tajriba shuni ko'rsatadiki, ESP32 da pin tanlashda nazariy bilim yetarli emas va amaliy sinov zarur.")
t("Ikkinchi muammo Firebase kutubxonasining stream callback funksiyasi bilan bog'liq bo'ldi. Dastlab streamCallback funksiyasi ishlatilgan edi, lekin u ESP32 da barqaror ishlamadi va ba'zan crash ga olib keldi. Bu muammo readStream usulga o'tish orqali hal qilindi. readStream usulda loop ichida har tsiklda stream tekshiriladi va yangi ma'lumot bo'lsa o'qiladi. Bu usul callback dan ko'ra barqarorroq ishladi, chunki u asosiy loop kontekstida ishlaydi va stack overflow xavfi yo'q.")
t("Uchinchi muammo WiFi ulanish jarayonining blocking xususiyati bilan bog'liq bo'ldi. Standart WiFi.begin funksiyasi ulanish tugaguncha dasturni to'xtatadi va bu vaqtda sensorlar o'qilmaydi va relay boshqarilmaydi. Bu muammo non-blocking WiFi algoritmiga o'tish orqali hal qilindi. Algoritmda WiFi.begin chaqirilgandan keyin 10 soniya davomida har 100 millisekundda WiFi.status tekshiriladi va bu vaqt davomida sensorlar o'qiladi.")
t("To'rtinchi muammo firmware hajmining flash xotiraga sig'masligi bilan bog'liq bo'ldi. Firebase ESP32 Client kutubxonasi juda katta bo'lib, standart partition sxemasida dastur uchun ajratilgan 1.2 MB yetarli emas edi. Bu muammo huge_app.csv partition sxemasiga o'tish orqali hal qilindi. Bu sxemada dastur uchun 3 MB ajratilgan va Firebase kutubxonasi bilan birga firmware 2.1 MB hajmni egalladi.")
t("Beshinchi muammo serial monitor va firmware yuklash o'rtasidagi conflict bilan bog'liq bo'ldi. ESP32 ning USB-UART chipi bitta portdan foydalanadi va serial monitor ochiq bo'lganda firmware yuklab bo'lmaydi. Bu muammo serial monitorni yopib, keyin firmware yuklash orqali hal qilindi. Bundan tashqari, sensor simlarini firmware yuklash vaqtida ajratish kerak bo'ldi, chunki GPIO 4 va GPIO 16 boot jarayonida ta'sir qilishi mumkin.")
t("Oltinchi muammo dashboard da Live va Demo rejimlar o'rtasida almashishda holat yo'qolishi bilan bog'liq bo'ldi. Foydalanuvchi Demo rejimga o'tganda va keyin sahifani yangilaganda, tizim yana Live rejimga qaytardi. Bu muammo localStorage ga isLive holatini saqlash orqali hal qilindi. Endi foydalanuvchi tanlagan rejim brauzer yopilganda ham saqlanib qoladi.")

doc.add_page_break()
h2("YO ilova. Tizimning boshqa IoT loyihalar bilan integratsiya imkoniyatlari")
t("Ishlab chiqilgan tizim mustaqil ishlash bilan birga, boshqa IoT loyihalar bilan integratsiya qilish imkoniyatiga ham ega. Firebase Realtime Database ochiq API ga ega bo'lib, istalgan dastur undan ma'lumot o'qishi va yozishi mumkin. Bu tizimni boshqa aqlli shahar komponentlari bilan bog'lash imkonini beradi.")
t("Aqlli transport tizimi bilan integratsiya quyidagicha amalga oshirilishi mumkin. Transport sensori mashinaning yaqinlashishini aniqlaydi va Firebase ga signal yuboradi. Ko'cha yoritish tizimi bu signalni qabul qiladi va mashina yo'nalishi bo'yicha yoritgichlarni oldindan yoqadi. Mashina o'tgandan keyin yoritgichlar o'chadi. Bu yondashuv energiya tejashni yanada oshiradi, chunki faqat mashina yo'nalishi bo'yicha yoritgichlar yonadi.")
t("Aqlli xavfsizlik tizimi bilan integratsiya ham mumkin. Agar ko'cha yoritish tizimi tunda g'ayrioddiy harakat aniqlasa, masalan bir joyda uzoq vaqt turish yoki tez-tez harakat, u xavfsizlik tizimiga signal yuborishi mumkin. Xavfsizlik tizimi kamerani yoqishi yoki qo'riqchiga xabar berishi mumkin. Bu fuqarolar xavfsizligini oshiradi.")
t("Ob-havo monitoring tizimi bilan integratsiya ham foydali bo'lishi mumkin. Agar ob-havo tizimi kuchli shamol yoki yomg'ir haqida xabar bersa, ko'cha yoritish tizimi sensorlarning aniqligini tekshirishi va kerak bo'lsa kalibrovka qilishi mumkin. Bundan tashqari, ob-havo ma'lumotlari energiya tejash statistikasini aniqroq hisoblash uchun ishlatilishi mumkin.")
t("Aqlli energiya tizimi bilan integratsiya eng muhim integratsiya hisoblanadi. Agar shahar energiya tizimi peak load vaqtida ko'cha yoritish iste'molini kamaytirish kerak bo'lsa, u Firebase orqali barcha yoritgichlarga signal yuborishi mumkin. Yoritgichlar yorug'likni 50 foizga pasaytirishi yoki faqat harakat aniqlanganda yonishi mumkin. Bu demand response deb ataladi va energiya tizimining barqarorligini ta'minlaydi.")

doc.add_page_break()
h2("YU ilova. Foydalanuvchi qo'llanmasi")
t("Tizimni o'rnatish va ishga tushirish uchun quyidagi qadamlarni bajarish kerak. Avval barcha komponentlarni ulash sxemasiga muvofiq ulang. ESP32 ning GPIO 4 pinini RCWL-9610A ning TRIG piniga, GPIO 16 ni ECHO piniga, GPIO 34 ni TEMT6000 ning OUT piniga va GPIO 26 ni relay modulining IN piniga ulang. Barcha komponentlarning GND pinlarini ESP32 ning GND piniga ulang. RCWL-9610A va TEMT6000 ning VCC pinlarini ESP32 ning 3.3V piniga ulang. Relay modulining VCC pinini ESP32 ning 5V piniga ulang.")
t("Firmware yuklash uchun ESP32 ni USB kabel orqali kompyuterga ulang. PlatformIO o'rnatilgan bo'lishi kerak. Terminal da firmware papkasiga o'ting va pio run --target upload buyrug'ini bajaring. Firmware yuklash vaqtida sensor simlarini ajrating va serial monitorni yoping. Firmware muvaffaqiyatli yuklangandan keyin sensor simlarini qayta ulang.")
t("Birinchi ishga tushirishda ESP32 WiFi ga ulanishga harakat qiladi. Agar config.h dagi WiFi ma'lumotlari to'g'ri bo'lsa, qurilma avtomatik ulanadi. Agar ulanish muvaffaqiyatsiz bo'lsa, qurilma SmartLight_AP nomli WiFi nuqtasi yaratadi. Telefoningiz yoki kompyuteringiz bilan bu tarmoqqa ulaning va parol sifatida 12345678 kiriting. Brauzer avtomatik ochiladi va WiFi konfiguratsiya sahifasi ko'rinadi. WiFi SSID va parolni kiriting va Save tugmasini bosing.")
t("Dashboard ga kirish uchun https://smart-street-light-iot.web.app manzilini oching. Login sahifasida email sifatida device@smartlight.com va parol sifatida SmartLight2026! kiriting. Muvaffaqiyatli kirgandan keyin Dashboard sahifasi ochiladi va sensor qiymatlari ko'rinadi. Power toggle orqali yoritgichni qo'lda yoqish va o'chirish mumkin. Rejim tugmalari orqali Auto, Manual yoki Schedule rejimini tanlash mumkin.")
t("Dashboard ni telefonga o'rnatish uchun brauzerda sahifani oching va Add to Home Screen yoki Bosh ekranga qo'shish tugmasini bosing. Ilova bosh ekranga qo'shiladi va keyingi safar ochilganda brauzer paneli ko'rinmaydi. Ilova native ilova kabi ishlaydi va internet bo'lmasa ham Demo rejimda ishlaydi.")
t("Sozlamalar sahifasida quyidagi parametrlarni o'zgartirish mumkin. Distance threshold harakat aniqlash masofasini belgilaydi va standart qiymati 200 santimetr. Light threshold yorug'lik chegarasini belgilaydi va standart qiymati 300. Timeout yoritgichning o'chish vaqtini belgilaydi va standart qiymati 5 soniya. Schedule on va Schedule off jadval rejimida yoqish va o'chirish vaqtlarini belgilaydi.")

img("screenshot_settings.png", "YU.1-rasm. Sozlamalar sahifasi")

t("Muammolarni bartaraf etish uchun quyidagi qadamlarni bajaring. Agar sensor qiymatlari ko'rinmasa, ESP32 ning serial monitorini oching va xato xabarlarini tekshiring. Agar WiFi ulanmasa, SmartLight_AP tarmog'iga ulaning va yangi WiFi ma'lumotlarini kiriting. Agar relay ishlamasa, GPIO 26 pinini va relay modulining ulanishini tekshiring. Agar dashboard yangilanmasa, brauzer keshini tozalang va sahifani qayta yuklang.")

doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')
print("Done! Final pages added.")
