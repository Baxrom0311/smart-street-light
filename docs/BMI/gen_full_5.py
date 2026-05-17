#!/usr/bin/env python3
"""XULOSA + ADABIYOTLAR + ILOVALAR"""
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
import os

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_full.docx')
IMG = '/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/images/'

def hc(t, sz=16):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(t); r.bold = True; r.font.size = Pt(sz); r.font.name = 'Times New Roman'
def t(x):
    p = doc.add_paragraph(x); p.paragraph_format.first_line_indent = Cm(1.25)
    for r in p.runs: r.font.name = 'Times New Roman'; r.font.size = Pt(14)
def code(x):
    p = doc.add_paragraph(); r = p.add_run(x); r.font.name = 'Courier New'; r.font.size = Pt(10)
    p.paragraph_format.left_indent = Cm(1)

# === XULOSA ===
hc("XULOSA")
doc.add_paragraph()

t("Mazkur bitiruv malakaviy ishida \"Smart Street tizimida ultratovush sensori orqali energiya tejamkorligini ta'minlovchi yoritish tizimini ishlab chiqish\" mavzusi bo'yicha tadqiqot olib borildi va to'liq ishlaydigan amaliy tizim yaratildi. Ishning asosiy natijalari quyidagilardan iborat:")
t("1. Ko'cha yoritish tizimlarining hozirgi holati chuqur tahlil qilindi. An'anaviy tizimlar tun bo'yi uzluksiz ishlashi sababli energiyaning 60-80 foizi behuda sarflanishi aniqlandi. Mavjud tijorat yechimlari (Philips CityTouch, Telensa, Tvilight) yuqori narxga ega ($100-500) ekanligi va kichik miqyosda qo'llash iqtisodiy jihatdan samarasiz ekanligi ko'rsatildi.")
t("2. ESP32 mikrokontrolleri, RCWL-9610A ultratovush sensori va TEMT6000 yorug'lik sensori asosida to'liq ishlaydigan energiya tejamkor yoritish tizimi ishlab chiqildi. Tizim bir vaqtning o'zida harakatni aniqlash (2 m masofagacha, ±1 cm aniqlik) va kunduz/tun holatini farqlash imkoniyatiga ega.")
t("3. Debounce (majority voting), hold timer (5 soniya) va hysteresis (250/350) algoritmlarini qo'llash orqali sensorlarning ishonchliligi sezilarli darajada oshirildi. Noto'g'ri natijalar (false positive) deyarli yo'q qilindi.")
t("4. Firebase Realtime Database asosida real vaqt rejimida masofadan boshqarish va monitoring tizimi yaratildi. Qurilma holati har 3 soniyada yangilanadi, dashboard buyruqlari 200-500 ms ichida qurilmaga yetib boradi.")
t("5. React 19 + Vite 8 asosida Progressive Web Application (PWA) dashboard ishlab chiqildi. U desktop va mobile da responsive ishlaydi, offline rejimni qo'llab-quvvatlaydi va native ilova sifatida o'rnatilishi mumkin. Optimistic UI pattern foydalanuvchi tajribasini yaxshilaydi.")
t("6. Non-blocking WiFi boshqaruv algoritmi va NVS + captive portal mexanizmi ishlab chiqildi. Tizim internet bo'lmasa ham avtonom ishlaydi va aloqa tiklanganda avtomatik sinxronizatsiya qiladi.")
t("7. 5 kunlik amaliy sinov o'tkazildi. Natijalar: o'rtacha 80.8% energiya tejash, kuniga 582 Wh tejamkorlik. Bitta 60W yoritgich uchun yillik tejamkorlik 212.4 kWh yoki 106,200 so'm. Tizim 6-8 oy ichida o'zini oqlaydi.")
t("8. Tizimning umumiy narxi $7-10 (50,000-70,000 so'm) bo'lib, tijorat yechimlariga nisbatan 10-50 marta arzon. Shu bilan birga, masofadan boshqarish va monitoring imkoniyati mavjud.")

doc.add_paragraph()
t("Kelajakda tizimni yanada rivojlantirish yo'nalishlari:")
t("— OTA (Over-The-Air) yangilash — firmware ni masofadan yangilash imkoniyati;")
t("— LoRa tarmoq — WiFi bo'lmagan hududlarda uzoq masofali aloqa;")
t("— Machine Learning — harakat naqshlarini o'rganish va bashorat qilish;")
t("— Quyosh paneli integratsiyasi — to'liq avtonom energiya ta'minoti;")
t("— Mesh tarmoq — bir nechta yoritgichni o'zaro bog'lash;")
t("— Edge computing — bulutga bog'liq bo'lmagan lokal qaror qabul qilish.")

doc.add_page_break()

# === ADABIYOTLAR ===
hc("FOYDALANILGAN ADABIYOTLAR RO'YXATI")
doc.add_paragraph()

refs = [
    '1. International Energy Agency. "Energy Efficiency 2023: Lighting." IEA Publications, Paris, 2023. — 156 p.',
    '2. Statista Research Department. "Number of IoT connected devices worldwide 2019-2030." Statista, Hamburg, 2024.',
    '3. Carullo A., Parvis M. An ultrasonic sensor for distance measurement in automotive applications // IEEE Sensors Journal. — 2001. — Vol.1, No.2. — P. 143-147.',
    '4. O\'zbekiston Respublikasi Prezidentining Farmoni. "Raqamli O\'zbekiston — 2030 strategiyasi." — PF-6079. — 2020-yil 5-oktabr.',
    '5. O\'zbekiston Respublikasi Vazirlar Mahkamasi. "Energiya tejamkorligi va energiya samaradorligi to\'g\'risida." — 58-son. — 2023-yil 15-mart.',
    '6. Kostic M., Djokic L. Recommendations for energy efficient and visually acceptable street lighting // Energy. — 2009. — Vol.34, No.10. — P. 1565-1572.',
    '7. Rea M.S. The IESNA Lighting Handbook: Reference and Application. — 9th edition. — New York: IESNA, 2000. — 1000 p.',
    '8. Zanella A., Bui N., Castellani A. et al. Internet of Things for Smart Cities // IEEE Internet of Things Journal. — 2014. — Vol.1, No.1. — P. 22-32.',
    '9. Radulovic D., Skok S., Kirincic V. Energy efficiency public lighting management in the cities // Energy. — 2011. — Vol.36, No.4. — P. 1908-1915.',
    '10. Leccese F. Remote-control system of high efficiency and intelligent street lighting using a ZigBee network // IEEE Transactions on Power Delivery. — 2013. — Vol.28, No.1. — P. 21-28.',
    '11. Signify (Philips Lighting). "CityTouch: Connected street lighting management." — Technical Documentation. — Eindhoven, 2022.',
    '12. Telensa Ltd. "Smart Street Lighting Solutions: PLANet Platform." — Technical White Paper. — Cambridge, UK, 2023.',
    '13. Tvilight BV. "Dynamic Street Lighting with CitySense Motion Sensors." — Product Documentation. — Groningen, Netherlands, 2023.',
    '14. Parkash, Prabu V., Rajendra D. Internet of Things Based Intelligent Street Lighting System for Smart City // International Journal of Innovative Research in Science, Engineering and Technology. — 2016. — Vol.5, No.5. — P. 7684-7691.',
    '15. Kinsler L.E., Frey A.R., Coppens A.B., Sanders J.V. Fundamentals of Acoustics. — 4th edition. — New York: John Wiley & Sons, 2000. — 560 p.',
    '16. Borenstein J., Everett H.R., Feng L. Navigating Mobile Robots: Systems and Techniques. — Wellesley: A.K. Peters, 1996. — 226 p.',
    '17. RCWL-9610A Ultrasonic Distance Sensor Module. — Datasheet. — Shenzhen RCWL Electronics Co., 2021.',
    '18. Vishay Semiconductors. "TEMT6000 Ambient Light Sensor." — Datasheet No. 81579. — 2011.',
    '19. Elmenreich W. Sensor Fusion in Time-Triggered Systems: PhD Thesis. — Vienna University of Technology, 2002. — 178 p.',
    '20. Espressif Systems. "ESP32 Technical Reference Manual." — Version 4.8. — Shanghai, 2023. — 688 p.',
    '21. Firebase Documentation. "Realtime Database: Read and Write Data." — Google Developers, 2024. — URL: https://firebase.google.com/docs/database',
    '22. React Documentation. "React: A JavaScript library for building user interfaces." — Meta Platforms, 2024. — URL: https://react.dev',
    '23. Mobizt. "Firebase ESP32 Client Library." — GitHub Repository, 2024. — URL: https://github.com/mobizt/Firebase-ESP32',
    '24. PlatformIO. "Professional collaborative platform for embedded development." — 2024. — URL: https://platformio.org',
    '25. Vite.js. "Next Generation Frontend Tooling." — 2024. — URL: https://vitejs.dev',
]

for ref in refs:
    p = doc.add_paragraph(ref)
    p.paragraph_format.first_line_indent = Cm(1.25)
    for r in p.runs: r.font.name = 'Times New Roman'; r.font.size = Pt(12)

doc.add_page_break()

# === ILOVALAR ===
hc("ILOVALAR")
doc.add_paragraph()
hc("A ilova. ESP32 firmware asosiy kodi (main.cpp)", 14)
doc.add_paragraph()

main_code = """#include <WiFi.h>
#include <Preferences.h>
#include <WebServer.h>
#include <DNSServer.h>
#include "config.h"
#include "sensors.h"
#include "light_control.h"
#include "firebase_handler.h"
#include "statistics.h"

Preferences prefs;
WebServer server(80);
DNSServer dnsServer;
bool apMode = false;
unsigned long lastWiFiCheck = 0;

void setupWiFi() {
    prefs.begin("wifi", true);
    String ssid = prefs.getString("ssid", WIFI_SSID);
    String pass = prefs.getString("pass", WIFI_PASS);
    prefs.end();
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid.c_str(), pass.c_str());
    unsigned long start = millis();
    while (WiFi.status() != WL_CONNECTED && millis()-start < 10000) {
        delay(100);
    }
    if (WiFi.status() == WL_CONNECTED) {
        Serial.println("WiFi connected: " + WiFi.localIP().toString());
    } else {
        startAP();
    }
}

void startAP() {
    WiFi.mode(WIFI_AP);
    WiFi.softAP("SmartLight_AP", "12345678");
    dnsServer.start(53, "*", WiFi.softAPIP());
    // Captive portal web server
    server.on("/save", HTTP_POST, handleSave);
    server.onNotFound(handlePortal);
    server.begin();
    apMode = true;
}

void setup() {
    Serial.begin(115200);
    setupSensors();
    setupLightControl();
    setupWiFi();
    if (!apMode) setupFirebase();
}

void loop() {
    if (apMode) {
        dnsServer.processNextRequest();
        server.handleClient();
    } else {
        firebaseLoop();
        checkWiFi();
    }
    readSensors();
    updateLightControl();
    updateStatistics();
    delay(300);
}"""

for line in main_code.strip().split('\n'):
    code(line)

doc.add_page_break()
hc("B ilova. Firebase ma'lumotlar strukturasi", 14)
doc.add_paragraph()

fb_code = """{
  "device": {
    "status": {
      "light_on": false,
      "motion_detected": false,
      "distance_cm": 150,
      "ambient_light": 820,
      "mode": "auto",
      "last_motion": 1716000000,
      "uptime": 3600,
      "wifi_rssi": -45
    },
    "control": {
      "mode": "auto",
      "manual_light": false,
      "brightness": 100,
      "schedule_on": "18:00",
      "schedule_off": "06:00"
    },
    "config": {
      "timeout_sec": 5,
      "light_threshold": 300,
      "distance_threshold": 200
    }
  },
  "history": {
    "2026-05-15": {
      "motions_count": 45,
      "on_duration_min": 120,
      "energy_saved_percent": 75
    }
  }
}"""

for line in fb_code.strip().split('\n'):
    code(line)

doc.add_page_break()
hc("V ilova. Dashboard screenshotlari", 14)
doc.add_paragraph()

if os.path.exists(IMG + 'screenshot_stats.png'):
    doc.add_picture(IMG + 'screenshot_stats.png', width=Cm(14))
    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("V.1-rasm. Statistika sahifasi"); r.font.size = Pt(12); r.italic = True

if os.path.exists(IMG + 'screenshot_settings.png'):
    doc.add_picture(IMG + 'screenshot_settings.png', width=Cm(14))
    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("V.2-rasm. Sozlamalar sahifasi"); r.font.size = Pt(12); r.italic = True

if os.path.exists(IMG + 'screenshot_log.png'):
    doc.add_picture(IMG + 'screenshot_log.png', width=Cm(14))
    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("V.3-rasm. Harakat logi sahifasi"); r.font.size = Pt(12); r.italic = True

# SAVE FINAL
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_full.docx')
print("XULOSA + ADABIYOTLAR + ILOVALAR done!")
print("FULL DOCX COMPLETE!")
