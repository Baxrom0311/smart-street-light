#!/usr/bin/env python3
"""XULOSA + ADABIYOTLAR + ILOVALAR"""
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
def ref(x):
    p = doc.add_paragraph(); p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(x); r.font.name = 'Times New Roman'; r.font.size = Pt(12)
def code(x):
    p = doc.add_paragraph(); p.paragraph_format.first_line_indent = Cm(0); p.paragraph_format.left_indent = Cm(1)
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(x); r.font.name = 'Courier New'; r.font.size = Pt(10)
def img(name, caption):
    if not os.path.exists(IMG + name): return
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    run = p.add_run(); run.add_picture(IMG + name, width=Cm(14))
    pc = doc.add_paragraph(); pc.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    pc.paragraph_format.first_line_indent = Cm(0); pc.paragraph_format.space_before = Pt(0); pc.paragraph_format.space_after = Pt(0)
    rc = pc.add_run(caption); rc.italic = True; rc.font.size = Pt(12); rc.font.name = 'Times New Roman'

# === XULOSA ===
bob("XULOSA")
t("Mazkur bitiruv malakaviy ishida Smart Street tizimida ultratovush sensori orqali energiya tejamkorligini ta'minlovchi yoritish tizimini ishlab chiqish mavzusi bo'yicha tadqiqot olib borildi va to'liq ishlaydigan amaliy tizim yaratildi. Ish davomida ko'cha yoritish tizimlarining hozirgi holati chuqur tahlil qilindi va an'anaviy tizimlar tun bo'yi uzluksiz ishlashi sababli energiyaning 60-80 foizi behuda sarflanishi aniqlandi. Mavjud tijorat yechimlari yuqori narxga ega ekanligi va kichik miqyosda qo'llash iqtisodiy jihatdan samarasiz ekanligi ko'rsatildi.")
t("ESP32 mikrokontrolleri, RCWL-9610A ultratovush sensori va TEMT6000 yorug'lik sensori asosida to'liq ishlaydigan energiya tejamkor yoritish tizimi ishlab chiqildi. Tizim bir vaqtning o'zida harakatni aniqlash va kunduz-tun holatini farqlash imkoniyatiga ega. Debounce, hold timer va hysteresis algoritmlarini qo'llash orqali sensorlarning ishonchliligi sezilarli darajada oshirildi va noto'g'ri natijalar deyarli yo'q qilindi.")
t("Firebase Realtime Database asosida real vaqt rejimida masofadan boshqarish va monitoring tizimi yaratildi. Qurilma holati har 3 soniyada yangilanadi va dashboard buyruqlari 200-500 millisekund ichida qurilmaga yetib boradi. React 19 va Vite 8 asosida Progressive Web Application dashboard ishlab chiqildi va u desktop hamda mobile da responsive ishlaydi, offline rejimni qo'llab-quvvatlaydi va native ilova sifatida o'rnatilishi mumkin.")
t("Non-blocking WiFi boshqaruv algoritmi va NVS bilan captive portal mexanizmi ishlab chiqildi. Tizim internet bo'lmasa ham avtonom ishlaydi va aloqa tiklanganda avtomatik sinxronizatsiya qiladi. 5 kunlik amaliy sinov o'tkazildi va natijalar o'rtacha 80.8 foiz energiya tejash ko'rsatkichini berdi. Bitta 60 vattli yoritgich uchun yillik tejamkorlik 212.4 kilovatt-soat yoki 106200 so'mni tashkil etadi. Tizim 6-8 oy ichida o'zini oqlaydi.")
t("Tizimning umumiy narxi 7-10 AQSh dollari bo'lib, tijorat yechimlariga nisbatan 10-50 marta arzon. Shu bilan birga masofadan boshqarish va monitoring imkoniyati mavjud. Kelajakda tizimni OTA yangilash, LoRa tarmoq, Machine Learning, quyosh paneli integratsiyasi va mesh tarmoq yo'nalishlarida rivojlantirish rejalashtirilgan.")

doc.add_page_break()

# === ADABIYOTLAR ===
bob("FOYDALANILGAN ADABIYOTLAR RO'YXATI")
refs = [
    '1. International Energy Agency. Energy Efficiency 2023: Lighting. — IEA Publications, Paris, 2023. — 156 p.',
    '2. Statista Research Department. Number of IoT connected devices worldwide 2019-2030. — Statista, Hamburg, 2024.',
    '3. Carullo A., Parvis M. An ultrasonic sensor for distance measurement in automotive applications // IEEE Sensors Journal. — 2001. — Vol.1, No.2. — P. 143-147.',
    "4. O'zbekiston Respublikasi Prezidentining Farmoni. Raqamli O'zbekiston 2030 strategiyasi. — PF-6079. — 2020-yil 5-oktabr.",
    "5. O'zbekiston Respublikasi Vazirlar Mahkamasi. Energiya tejamkorligi va energiya samaradorligi to'g'risida. — 58-son. — 2023-yil 15-mart.",
    '6. Kostic M., Djokic L. Recommendations for energy efficient and visually acceptable street lighting // Energy. — 2009. — Vol.34, No.10. — P. 1565-1572.',
    '7. Rea M.S. The IESNA Lighting Handbook: Reference and Application. — 9th edition. — New York: IESNA, 2000. — 1000 p.',
    '8. Zanella A., Bui N., Castellani A. Internet of Things for Smart Cities // IEEE Internet of Things Journal. — 2014. — Vol.1, No.1. — P. 22-32.',
    '9. Radulovic D., Skok S., Kirincic V. Energy efficiency public lighting management in the cities // Energy. — 2011. — Vol.36, No.4. — P. 1908-1915.',
    '10. Leccese F. Remote-control system of high efficiency and intelligent street lighting // IEEE Trans. Power Delivery. — 2013. — Vol.28, No.1. — P. 21-28.',
    '11. Signify. CityTouch: Connected street lighting management. — Technical Documentation. — Eindhoven, 2022.',
    '12. Telensa Ltd. Smart Street Lighting Solutions. — Technical White Paper. — Cambridge, UK, 2023.',
    '13. Tvilight BV. Dynamic Street Lighting with CitySense. — Product Documentation. — Groningen, 2023.',
    '14. Parkash, Prabu V., Rajendra D. IoT Based Intelligent Street Lighting System // IJIRSET. — 2016. — Vol.5, No.5. — P. 7684-7691.',
    '15. Kinsler L.E. Fundamentals of Acoustics. — 4th edition. — New York: John Wiley, 2000. — 560 p.',
    '16. Borenstein J. Navigating Mobile Robots: Systems and Techniques. — Wellesley: A.K. Peters, 1996. — 226 p.',
    '17. RCWL-9610A Ultrasonic Distance Sensor Module. — Datasheet. — Shenzhen RCWL Electronics, 2021.',
    '18. Vishay Semiconductors. TEMT6000 Ambient Light Sensor. — Datasheet No. 81579. — 2011.',
    '19. Elmenreich W. Sensor Fusion in Time-Triggered Systems. — PhD Thesis. — Vienna, 2002. — 178 p.',
    '20. Espressif Systems. ESP32 Technical Reference Manual. — Version 4.8. — Shanghai, 2023. — 688 p.',
    '21. Firebase Documentation. Realtime Database. — Google Developers, 2024.',
    '22. React Documentation. — Meta Platforms, 2024. — URL: https://react.dev',
    '23. Mobizt. Firebase ESP32 Client Library. — GitHub, 2024.',
    '24. PlatformIO. Professional embedded development platform. — 2024. — URL: https://platformio.org',
    '25. Vite.js. Next Generation Frontend Tooling. — 2024. — URL: https://vitejs.dev',
]
for r in refs:
    ref(r)

doc.add_page_break()

# === ILOVALAR ===
bob("ILOVALAR")
h2("A ilova. Asosiy dastur kodi (main.cpp)")

main_code = '''#include <WiFi.h>
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
    } else { startAP(); }
}

void startAP() {
    WiFi.mode(WIFI_AP);
    WiFi.softAP("SmartLight_AP", "12345678");
    dnsServer.start(53, "*", WiFi.softAPIP());
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
}'''
for line in main_code.split('\n'): code(line)

doc.add_page_break()
h2("B ilova. Sensorlar moduli (sensors.cpp)")
sensors_code = '''#include "sensors.h"
#include "config.h"
#include <Arduino.h>

float currentDistance = 999.0;
int currentLight = 0;
bool motionDetected = false;
unsigned long lastMotionTime = 0;
bool isDark = false;

void setupSensors() {
    pinMode(TRIG_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);
    pinMode(LIGHT_PIN, INPUT);
    digitalWrite(TRIG_PIN, LOW);
}

float readDistance() {
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);
    long duration = pulseIn(ECHO_PIN, HIGH, 30000);
    if (duration == 0) return 999.0;
    float distance = duration * 0.034 / 2.0;
    if (distance < 2.0) return 2.0;
    if (distance > 450.0) return 999.0;
    return distance;
}

bool checkMotion() {
    int count = 0;
    for (int i = 0; i < 3; i++) {
        if (readDistance() < DISTANCE_THRESHOLD) count++;
        delay(50);
    }
    return count >= 2;
}

void readSensors() {
    currentLight = analogRead(LIGHT_PIN);
    if (currentLight < DARK_THRESHOLD) isDark = true;
    else if (currentLight > LIGHT_THRESHOLD) isDark = false;
    currentDistance = readDistance();
    if (checkMotion()) {
        lastMotionTime = millis();
        motionDetected = true;
    } else if (millis() - lastMotionTime > HOLD_TIME) {
        motionDetected = false;
    }
}'''
for line in sensors_code.split('\n'): code(line)

doc.add_page_break()
h2("V ilova. Yoritish boshqaruv moduli (light_control.cpp)")
light_code = '''#include "light_control.h"
#include "config.h"
#include "sensors.h"
#include <Arduino.h>

bool relayState = false;
String currentMode = "auto";
bool manualLight = false;

void setupLightControl() {
    pinMode(RELAY_PIN, OUTPUT);
    pinMode(STATUS_LED, OUTPUT);
    digitalWrite(RELAY_PIN, HIGH);
    digitalWrite(STATUS_LED, LOW);
}

void setRelay(bool state) {
    relayState = state;
    digitalWrite(RELAY_PIN, state ? LOW : HIGH);
    digitalWrite(STATUS_LED, state ? HIGH : LOW);
}

void autoMode() {
    if (!isDark) { setRelay(false); return; }
    if (motionDetected) setRelay(true);
    else setRelay(false);
}

void updateLightControl() {
    if (currentMode == "auto") autoMode();
    else if (currentMode == "manual") setRelay(manualLight);
}'''
for line in light_code.split('\n'): code(line)

doc.add_page_break()
h2("G ilova. Dashboard screenshotlari")
img("screenshot_login.png", "G.1-rasm. Login sahifasi")
img("screenshot_stats.png", "G.2-rasm. Statistika sahifasi")
img("screenshot_settings.png", "G.3-rasm. Sozlamalar sahifasi")

# SAVE
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')
print("XULOSA + ADABIYOTLAR + ILOVALAR done!")
print("=== FULL DOCX v2 COMPLETE ===")
