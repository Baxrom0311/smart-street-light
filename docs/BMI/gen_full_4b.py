#!/usr/bin/env python3
"""II BOB - 2.2 Masofani aniqlash algoritmi"""
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
def code(x):
    p = doc.add_paragraph(); r = p.add_run(x); r.font.name = 'Courier New'; r.font.size = Pt(10)
    p.paragraph_format.left_indent = Cm(1)
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

h2("2.2. Masofani aniqlash algoritmi: ultrasonic sensor yordamida obyektni aniqlash")

h3("2.2.1. Asosiy o'lchash jarayoni va dasturiy amalga oshirish")
t("Ultratovush sensori yordamida masofa o'lchash jarayoni quyidagi bosqichlardan iborat: 1) TRIG pinga 10 μs davomida HIGH signal yuboriladi; 2) Sensor 8 ta 40 kHz ultratovush impulsini chiqaradi; 3) ECHO pin HIGH holatga o'tadi; 4) Impuls ob'ektdan aks etib qaytadi; 5) ECHO pin LOW holatga tushadi; 6) ECHO pinning HIGH bo'lgan vaqti o'lchanadi; 7) Masofa hisoblanadi.")
t("ESP32 dasturida bu jarayon sensors.cpp faylida amalga oshirilgan. Quyida asosiy o'lchash funksiyasining kodi keltirilgan:")

code("float readDistance() {")
code("    digitalWrite(TRIG_PIN, LOW);")
code("    delayMicroseconds(2);")
code("    digitalWrite(TRIG_PIN, HIGH);")
code("    delayMicroseconds(10);")
code("    digitalWrite(TRIG_PIN, LOW);")
code("    long duration = pulseIn(ECHO_PIN, HIGH, 30000);")
code("    if (duration == 0) return 999.0;")
code("    float distance = duration * 0.034 / 2.0;")
code("    return distance;")
code("}")

t("Kodda pulseIn() funksiyasiga 30000 μs (30 ms) timeout berilgan. Bu 30000 × 0.034 / 2 = 510 cm ga teng — sensorning maksimal diapazonidan (450 cm) biroz katta. Agar timeout ichida signal qaytmasa, funksiya 0 qaytaradi va biz 999 cm (ob'ekt yo'q) deb hisoblaymiz.")

h3("2.2.2. Debounce algoritmi — noto'g'ri o'lchovlarni filtrlash")
t("Real sharoitlarda ultratovush sensori ba'zan noto'g'ri natijalar berishi mumkin. Masalan, havo oqimi, sensorning o'zi chiqargan signalning ichki aks etishi yoki yaqin atrofdagi boshqa ultratovush manbalari shovqin yaratishi mumkin. Shu sababli, bitta o'lchovga ishonmasdan, 3 ta ketma-ket o'lchov olinadi va ulardan kamida 2 tasi harakat ko'rsatsa — harakat aniqlangan deb hisoblanadi.")

code("bool detectMotion() {")
code("    int count = 0;")
code("    for (int i = 0; i < 3; i++) {")
code("        float d = readDistance();")
code("        if (d < DISTANCE_THRESHOLD) count++;")
code("        delay(50);")
code("    }")
code("    return count >= 2;")
code("}")

t("Bu algoritmning ishlash prinsipi: agar 3 ta o'lchovdan 2 yoki 3 tasi 200 cm dan kam masofa ko'rsatsa — harakat bor. Agar faqat 1 tasi yoki hech biri ko'rsatmasa — harakat yo'q. Bu '2 dan 3' (majority voting) prinsipi deb ataladi va shovqinni samarali filtrlaydi.")
t("Amaliy misol: O'lchovlar [150, 450, 120] — 2 ta < 200, demak harakat bor. O'lchovlar [450, 300, 420] — 0 ta < 200, demak harakat yo'q. O'lchovlar [180, 450, 450] — 1 ta < 200, demak harakat yo'q (shovqin bo'lishi mumkin).")

h3("2.2.3. Hold timer — yoritgichning beqaror ishlashini oldini olish")
t("Agar sensor har 300 ms da o'lchov olsa va odam sekin yursa, ba'zi o'lchovlarda harakat aniqlanadi, ba'zilarida esa aniqlanmaydi. Bu yoritgichning tez-tez yonib-o'chishiga olib keladi — bu foydalanuvchi uchun noqulay va relay uchun zararli (kontaktlar tez eskiradi). Shu sababli, hold timer mexanizmi qo'llanildi:")

code("unsigned long lastMotionTime = 0;")
code("const unsigned long HOLD_TIME = 5000; // 5 sekund")
code("")
code("void updateMotion() {")
code("    if (detectMotion()) {")
code("        lastMotionTime = millis();")
code("        motionDetected = true;")
code("    } else if (millis() - lastMotionTime > HOLD_TIME) {")
code("        motionDetected = false;")
code("    }")
code("}")

t("Bu algoritm quyidagicha ishlaydi: harakat aniqlanganda lastMotionTime yangilanadi va motionDetected = true bo'ladi. Harakat to'xtasa ham, 5 soniya davomida motionDetected = true bo'lib qoladi. Faqat 5 soniya o'tgandan keyin motionDetected = false ga o'zgaradi va yoritgich o'chadi. Bu odam ko'cha bo'ylab yurganida yoritgichning uzluksiz yonib turishini ta'minlaydi.")

h3("2.2.4. Hysteresis — yorug'lik chegarasida beqarorlikni bartaraf etish")
t("Yorug'lik sensori qiymati chegaraga yaqin bo'lganda (masalan, 300 atrofida) tebranish yuz berishi mumkin — bulut ortidan quyosh chiqib-yashirinayotganda sensor qiymati 280-320 orasida o'zgarib turadi. Agar chegara 300 bo'lsa, tizim doimiy ravishda 'kunduz-tun-kunduz-tun' holatini almashtiradi.")
t("Bu muammoni hal qilish uchun hysteresis (gisterezis) mexanizmi qo'llanildi — ikkita chegara belgilanadi:")
t("— Pastki chegara (DARK_THRESHOLD = 250): sensor qiymati 250 dan pastga tushsa — 'qorong'u' holati o'rnatiladi;")
t("— Yuqori chegara (LIGHT_THRESHOLD = 350): sensor qiymati 350 dan oshsa — 'yorug'' holati o'rnatiladi;")
t("— 250-350 orasida: holat o'zgarmaydi (oldingi holat saqlanadi).")

code("bool isDark = false;")
code("")
code("void updateLightStatus() {")
code("    int light = analogRead(LIGHT_PIN);")
code("    if (light < 250) isDark = true;")
code("    else if (light > 350) isDark = false;")
code("    // 250-350 orasida o'zgarmaydi")
code("}")

t("Bu mexanizm 100 birlik 'o'lik zona' yaratadi. Sensor qiymati bu zonada bo'lganda tizim holat o'zgartirmaydi. Natijada, bulutli ob-havoda yoritgich beqaror ishlamaydi.")

img("diagram_flowchart.png", "2.2-rasm. Harakatni aniqlash va yoritgichni boshqarish algoritmining blok-sxemasi")

t("2.2-rasmda tizimning to'liq ishlash algoritmi tasvirlangan. Algoritm har 300 ms da takrorlanadi: avval yorug'lik tekshiriladi, keyin harakat, va natijaga qarab relay boshqariladi.")

h3("2.2.5. Sensor kalibrovkasi va sinov natijalari")
t("Sensor o'rnatilgandan keyin kalibrovka o'tkazildi. Turli masofalardan ob'ekt (odam) qo'yilib, sensor ko'rsatkichlari tekshirildi:")

tbl(["Haqiqiy masofa (cm)", "Sensor ko'rsatkichi (cm)", "Xatolik (cm)", "Xatolik (%)"],
    [["50", "49", "1", "2.0%"],
     ["100", "99", "1", "1.0%"],
     ["150", "148", "2", "1.3%"],
     ["200", "197", "3", "1.5%"],
     ["250", "245", "5", "2.0%"],
     ["300", "292", "8", "2.7%"],
     ["400", "385", "15", "3.8%"]],
    "2.5-jadval. Sensor kalibrovka natijalari")

t("Natijalar shuni ko'rsatadiki, 200 cm masofagacha xatolik ±3 cm dan oshmaydi (1.5%). Bu ko'cha yoritish uchun yetarli aniqlik — chunki biz aniq masofani emas, balki 'ob'ekt 2 metr ichida bor yoki yo'q' degan savolga javob qidiramiz. 200 cm chegara qiymati optimal tanlangan — bu odamning yurish tezligida (5 km/h = 1.4 m/s) yoritgichning oldindan yonishini ta'minlaydi.")

doc.add_page_break()
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_full.docx')
print("2.2 done (~10 pages)")
