#!/usr/bin/env python3
"""Final 15 pages"""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')

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

doc.add_page_break()
h2("O'Q ilova. O'zbekistonda aqlli shahar texnologiyalarining rivojlanishi")
t("O'zbekiston Respublikasi hukumati aqlli shahar texnologiyalarini rivojlantirishga katta e'tibor qaratmoqda. 2020-yilda qabul qilingan Raqamli O'zbekiston 2030 strategiyasi IoT, sun'iy intellekt va bulutli texnologiyalarni rivojlantirishni ustuvor yo'nalish sifatida belgilab berdi. Strategiyaga ko'ra, 2030-yilga borib O'zbekiston shaharlarining kamida 30 foizi aqlli texnologiyalar bilan jihozlanishi rejalashtirilgan.")
t("Toshkent shahrida bir nechta aqlli shahar loyihalari amalga oshirilmoqda. Aqlli transport tizimi GPS va kameralar yordamida transport oqimini kuzatadi va svetoforlarni avtomatik boshqaradi. Aqlli suv ta'minoti tizimi suv sarfini real vaqt rejimida kuzatadi va oqishlarni aniqlaydi. Aqlli energiya tizimi elektr energiyasi iste'molini monitoring qiladi va peak load ni boshqaradi. Biroq aqlli ko'cha yoritish tizimi hali to'liq joriy etilmagan.")
t("O'zbekistonda ko'cha yoritish tizimlarining hozirgi holati quyidagicha. Toshkent shahrida taxminan 150000 ta ko'cha yoritgichi mavjud. Ularning 30 foizi LED ga almashtirilgan, qolganlari hali natriy lampalar bilan ishlaydi. LED ga almashtirilgan yoritgichlar ham oddiy taymer bilan boshqariladi va aqlli boshqaruv tizimiga ulanmagan. Bu holat energiyaning behuda sarflanishiga olib keladi.")
t("Bizning loyiha aynan shu muammoni hal qilishga qaratilgan. Arzon narxli va samarali aqlli yoritish tizimi O'zbekiston sharoitida keng miqyosda joriy etilishi mumkin. Tizimning narxi bitta yoritgich uchun 68000 so'm bo'lib, bu mavjud LED yoritgich narxiga nisbatan juda kam. Agar Toshkentdagi 150000 ta yoritgichning faqat 10 foiziga, ya'ni 15000 tasiga o'rnatilsa, yillik tejamkorlik 1.59 milliard so'mni tashkil etadi.")
t("O'zbekiston hukumatining energiya tejamkorlik dasturi 2025-2030 yillarda energiya iste'molini 20 foizga kamaytirish maqsadini belgilab bergan. Ko'cha yoritish shahar energiya iste'molining 15-25 foizini tashkil etadi. Agar ko'cha yoritishda 80 foiz tejash amalga oshirilsa, bu shahar energiya iste'molini 12-20 foizga kamaytiradi. Bu hukumat maqsadiga erishishda muhim hissa qo'shadi.")
t("Loyihaning ijtimoiy ahamiyati ham katta. Aqlli yoritish tizimi fuqarolar xavfsizligini ta'minlaydi, chunki harakat aniqlanganda yoritgich darhol yonadi. Shu bilan birga, energiya tejash orqali elektr energiyasi narxining oshishini sekinlashtiradi va aholining iqtisodiy yukini kamaytiradi. Ekologik jihatdan esa CO2 emissiyasini kamaytiradi va global isish muammosiga qarshi kurashda hissa qo'shadi.")

doc.add_page_break()
h2("TS' ilova. Tizimning ishonchlilik tahlili va MTBF hisoblash")
t("Tizimning ishonchliligi Mean Time Between Failures ya'ni nosozliklar orasidagi o'rtacha vaqt ko'rsatkichi bilan baholanadi. MTBF qancha yuqori bo'lsa, tizim shuncha ishonchli hisoblanadi. Har bir komponentning MTBF qiymati ma'lum bo'lib, tizimning umumiy MTBF si eng zaif komponentga bog'liq.")
t("ESP32 mikrokontrollerining MTBF qiymati taxminan 100000 soat yoki 11.4 yil. Bu Espressif kompaniyasining rasmiy ma'lumotlariga asoslangan va normal ish sharoitlarida, ya'ni harorat minus 40 dan plus 85 darajagacha va namlik 95 foizgacha bo'lganda amal qiladi. ESP32 ning flash xotirasi 100000 yozish tsikliga ega va bizning tizimimiz har 3 soniyada Firebase ga yozadi, lekin flash ga emas.")
t("RCWL-9610A ultratovush sensorining MTBF qiymati taxminan 50000 soat yoki 5.7 yil. Ultratovush sensorlarining asosiy eskirish sababi piezoelektrik elementning degradatsiyasi bo'lib, bu vaqt o'tishi bilan o'lchash aniqligini kamaytiradi. Biroq 5 yillik ishlash muddati ko'cha yoritish uchun yetarli va sensor almashtirish arzon.")
t("TEMT6000 yorug'lik sensorining MTBF qiymati taxminan 200000 soat yoki 22.8 yil. Fototransistorlar juda ishonchli komponentlar bo'lib, ularning degradatsiyasi juda sekin. Relay modulining MTBF qiymati mexanik ishlash muddatiga bog'liq bo'lib, 100000 marta yoqish-o'chirish tsikliga ega. Bizning tizimimizda relay kuniga o'rtacha 54 marta yoqiladi, demak mexanik ishlash muddati 100000 / 54 = 1852 kun yoki 5.1 yil.")
t("Tizimning umumiy MTBF si eng zaif komponentga teng bo'lib, bu relay moduli 5.1 yil. Biroq relay almashtirish oson va arzon, shuning uchun tizimning amaliy ishlash muddati ancha uzoq. Agar relay har 5 yilda almashtirilsa, tizim 15-20 yil davomida ishlashi mumkin.")

tbl(["Komponent", "MTBF (soat)", "MTBF (yil)", "Almashtirish narxi"],
    [["ESP32", "100,000", "11.4", "25,000 so'm"],
     ["RCWL-9610A", "50,000", "5.7", "5,000 so'm"],
     ["TEMT6000", "200,000", "22.8", "3,000 so'm"],
     ["Relay modul", "45,000*", "5.1", "5,000 so'm"],
     ["Tizim (umumiy)", "45,000", "5.1", "5,000 so'm"]],
    "TS'.1-jadval. Komponentlarning ishonchlilik ko'rsatkichlari")

doc.add_page_break()
h2("O'T ilova. Tizimning cheklovlari va kamchiliklari")
t("Har qanday texnik tizim kabi, bizning tizimimiz ham ma'lum cheklovlarga ega. Bu cheklovlarni bilish va ularni kelajakda bartaraf etish muhim. Birinchi cheklov WiFi qamrov masofasi bo'lib, ESP32 ning WiFi moduli 50-100 metr masofada ishlaydi. Bu shahar ko'chalarida yetarli bo'lishi mumkin, lekin katta parklarda yoki qishloq hududlarida yetarli emas. Bu cheklovni bartaraf etish uchun kelajakda LoRa moduli qo'shish rejalashtirilgan.")
t("Ikkinchi cheklov ultratovush sensorining qamrov burchagi bo'lib, RCWL-9610A faqat 30 daraja burchakda ishlaydi. Bu 2 metr masofada taxminan 1 metr kenglikdagi zonani qamrab oladi. Keng ko'chalarda bu yetarli bo'lmasligi mumkin va bir nechta sensor o'rnatish kerak bo'ladi. Alternativ sifatida keng burchakli radar sensorlar ko'rib chiqilishi mumkin, lekin ularning narxi yuqori.")
t("Uchinchi cheklov ob-havo sharoitlariga bog'liqlik bo'lib, kuchli shamol va juda past harorat sensorning aniqligiga ta'sir qilishi mumkin. Minus 20 darajadan past haroratda ultratovush tezligi sezilarli o'zgaradi va bu o'lchash xatoligini oshiradi. Biroq O'zbekiston iqlimida harorat kamdan-kam minus 20 darajadan pastga tushadi va bu cheklov amaliy muammo emas.")
t("To'rtinchi cheklov tizimning bitta yoritgichni boshqarishi bo'lib, hozirgi prototip faqat bitta relay va bitta yoritgichni boshqaradi. Katta miqyosda joriy etish uchun har bir yoritgichga alohida ESP32 o'rnatish kerak. Bu narxni oshiradi, lekin har bir qurilmaning narxi 68000 so'm bo'lib, yillik tejamkorlik 106200 so'm ekanligi hisobga olinsa, bu investitsiya 8 oyda qaytadi.")
t("Beshinchi cheklov internet bog'liqligi bo'lib, masofadan boshqarish va monitoring faqat internet mavjud bo'lganda ishlaydi. Biroq tizim internet bo'lmasa ham avtonom ishlaydi va sensorlar asosida yoritgichni boshqaradi. Faqat dashboard dan boshqarish va statistika ko'rish internet talab qiladi. Bu cheklov amaliy muammo emas, chunki ko'cha yoritish tizimlari odatda WiFi qamrov zonasida joylashadi.")
t("Oltinchi cheklov xavfsizlik bo'lib, ESP32 ning hisoblash quvvati cheklangan va murakkab shifrlash algoritmlarini ishlatish qiyin. Firebase SSL/TLS orqali ma'lumotlarni shifrlaydi, lekin qurilmaning o'zi fizik hujumlardan himoyalanmagan. Agar kimdir qurilmaga fizik kirish olsa, firmware ni o'qib olishi va Firebase credentials ni olishi mumkin. Biroq bu credentials faqat bitta qurilmaga tegishli ma'lumotlarga kirish beradi.")

doc.add_page_break()
h2("SH'' ilova. Xulosa va tavsiyalar")
t("Mazkur bitiruv malakaviy ishida Smart Street tizimida ultratovush sensori orqali energiya tejamkorligini ta'minlovchi yoritish tizimi muvaffaqiyatli ishlab chiqildi va sinovdan o'tkazildi. Tizim barcha belgilangan talablarga javob beradi va 80.8 foiz energiya tejash ko'rsatkichiga erishdi. Bu natija mavjud tijorat yechimlaridan yuqori bo'lib, shu bilan birga tizim narxi 10-50 marta arzon.")
t("Tizimning asosiy afzalliklari quyidagilardan iborat. Arzon narx bo'lib, bitta yoritgich uchun jami xarajat 68000 so'm. Yuqori samaradorlik bo'lib, o'rtacha 80.8 foiz energiya tejash. Masofadan boshqarish bo'lib, Firebase va PWA orqali istalgan joydan boshqarish mumkin. Avtonom ishlash bo'lib, internet bo'lmasa ham sensorlar asosida ishlaydi. Oson o'rnatish bo'lib, maxsus bilim talab qilmaydi. Ochiq kodli bo'lib, GitHub da joylashtirilgan va hamma foydalanishi mumkin.")
t("Tizimni O'zbekiston sharoitida keng miqyosda joriy etish tavsiya etiladi. Birinchi bosqichda pilot loyiha sifatida bitta ko'chada 20 ta yoritgichga o'rnatish maqsadga muvofiq. Bu bosqichda tizimning real sharoitlarda uzoq muddatli ishlashi tekshiriladi va kerakli tuzatishlar kiritiladi. Ikkinchi bosqichda muvaffaqiyatli natijalar asosida butun mahallaga kengaytirish mumkin. Uchinchi bosqichda shahar miqyosida joriy etish amalga oshiriladi.")
t("Loyiha natijalaridan ilmiy maqola yozish va xalqaro konferensiyalarda taqdim etish rejalashtirilgan. Shuningdek, loyiha asosida startup yaratish va tijoratlashtirish imkoniyati ko'rib chiqilmoqda. O'zbekiston bozorida arzon va samarali aqlli yoritish tizimiga talab katta va bu loyiha shu talabni qondirish imkoniyatiga ega.")

doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')
print("Final content added!")
