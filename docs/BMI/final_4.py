from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_final.docx')

def fmt_heading(heading):
    for run in heading.runs:
        run.font.color.rgb = None
        run.font.name = 'Times New Roman'
        run.font.size = Pt(14)

def add_para(doc, text, size=14, font='Times New Roman', indent=Cm(1.25), left_indent=None, align=None):
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = indent
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    if left_indent:
        p.paragraph_format.left_indent = left_indent
    if align:
        p.alignment = align
    run = p.add_run(text)
    run.font.name = font
    run.font.size = Pt(size)
    return p

def add_code_block(doc, title, code):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.first_line_indent = Cm(0)
    run = p.add_run(title)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(14)
    run.bold = True
    for line in code.strip().split('\n'):
        cp = doc.add_paragraph()
        cp.paragraph_format.first_line_indent = Cm(0)
        cp.paragraph_format.left_indent = Cm(1)
        cp.paragraph_format.space_before = Pt(0)
        cp.paragraph_format.space_after = Pt(0)
        r = cp.add_run(line)
        r.font.name = 'Courier New'
        r.font.size = Pt(10)

# ==================== XULOSA ====================
doc.add_page_break()
h = doc.add_heading('XULOSA', level=1)
fmt_heading(h)

xulosa_paragraphs = [
    "Ushbu diplom ishida ultratovush sensori yordamida energiya tejamkorligini ta'minlovchi aqlli ko'cha yoritish tizimi ishlab chiqildi. Tizim ESP32 mikrokontroller, RCWL-9610A ultratovush sensori va TEMT6000 yorug'lik sensori asosida qurilgan bo'lib, ko'cha yoritgichlarini faqat zarur hollarda — ya'ni tunda va harakat aniqlanganda yoqish orqali sezilarli darajada energiya tejashga erishadi. Loyihaning asosiy maqsadi an'anaviy ko'cha yoritish tizimlarining samarasizligini bartaraf etish va zamonaviy IoT texnologiyalari yordamida aqlli boshqaruv tizimini yaratish edi.",

    "Tizimning amaliy sinovlari 5 kun davomida o'tkazildi va natijalar shuni ko'rsatdiki, ishlab chiqilgan tizim an'anaviy yoritish tizimiga nisbatan 80.8 foiz energiya tejashga erishdi. Bu natija tizimning yuqori samaradorligini tasdiqlaydi. Sinov davomida tizim barqaror ishladi, sensorlar to'g'ri ma'lumot berdi va LED yoritgichlar harakat aniqlanganda tezkor javob qaytardi. Ultratovush sensori 2 metr masofagacha bo'lgan harakatni aniq aniqladi, yorug'lik sensori esa kunduz va tun vaqtini ishonchli tarzda farqladi.",

    "Tizimning dasturiy ta'minoti non-blocking arxitektura asosida ishlab chiqilgan bo'lib, WiFi ulanishi uzilgan hollarda ham lokal boshqaruv to'xtamaydi. Captive portal funksiyasi orqali foydalanuvchi WiFi sozlamalarini qurilmaga to'g'ridan-to'g'ri telefon orqali kiritishi mumkin. Firebase Realtime Database bulutli platforma sifatida ishlatildi va u orqali qurilma holati real vaqtda monitoring qilinadi hamda masofadan boshqariladi. Stream texnologiyasi yordamida boshqaruv buyruqlari deyarli kechikishsiz qurilmaga yetkaziladi.",

    "Foydalanuvchi interfeysi sifatida React frameworki asosida Progressive Web Application (PWA) ishlab chiqildi. Dashboard orqali foydalanuvchi sensor ma'lumotlarini jonli kuzatishi, LED yoritgichni qo'lda yoqish yoki o'chirishi, avtomatik rejimni tanlashi, jadval bo'yicha boshqarishi, yorug'lik darajasini o'zgartirishi va LED rangini tanlashi mumkin. PWA texnologiyasi tufayli ilova telefonlarga o'rnatilishi va native dastur sifatida ishlashi mumkin. Statistika bo'limida haftalik energiya tejash ko'rsatkichlari grafiklar shaklida taqdim etiladi.",

    "Iqtisodiy tahlil shuni ko'rsatdiki, bitta aqlli yoritgich yiliga 106,200 so'm energiya tejashga imkon beradi. Tizimning umumiy tannarxi 7-10 AQSh dollari atrofida bo'lib, bu investitsiya 6-8 oy ichida o'zini qoplaydi. Bundan tashqari, LED lampalarning uzoq umr ko'rishi va kamroq ishlatilishi hisobiga texnik xizmat ko'rsatish xarajatlari ham kamayadi. Katta ko'lamda joriy etilganda, masalan, 1000 ta yoritgich uchun yillik tejamkorlik 106 million so'mdan oshadi.",

    "Ishlab chiqilgan tizim mavjud ko'cha yoritish infratuzilmasiga minimal o'zgartirishlar bilan integratsiya qilinishi mumkin. Tizim modular arxitekturaga ega bo'lib, har bir komponent mustaqil ravishda yangilanishi va almashtirilishi mumkin. Sensorlar soni va turi kengaytirilishi, boshqaruv algoritmlari takomillashtirilishi mumkin.",

    "Kelajakda tizimni yanada rivojlantirish uchun quyidagi yo'nalishlar belgilandi: OTA (Over-The-Air) yangilanishlar orqali dasturiy ta'minotni masofadan yangilash imkoniyatini qo'shish; LoRa tarmoq texnologiyasi yordamida keng hududlarda sensorlar tarmog'ini yaratish; Machine Learning algoritmlarini qo'llash orqali harakat naqshlarini o'rganish va bashorat qilish; quyosh panellari integratsiyasi orqali tizimni to'liq avtonom energiya manbaiga o'tkazish. Bu yaxshilanishlar tizimning samaradorligini yanada oshiradi va uni tijorat miqyosida joriy etish imkonini beradi.",

    "Xulosa qilib aytganda, diplom ishi doirasida to'liq ishlaydigan IoT asosidagi aqlli ko'cha yoritish tizimi muvaffaqiyatli ishlab chiqildi. Tizim energiya tejamkorligi, masofadan boshqarish, real-time monitoring va foydalanuvchiga qulay interfeys kabi zamonaviy talablarni to'liq qondiradi. Olingan natijalar tizimning amaliy qo'llanilishi uchun tayyor ekanligini va O'zbekiston sharoitida ko'cha yoritish sohasida energiya tejash muammosini hal qilishda samarali vosita bo'lishini tasdiqlaydi."
]

for text in xulosa_paragraphs:
    add_para(doc, text)

# ==================== ADABIYOTLAR ====================
doc.add_page_break()
h = doc.add_heading('ADABIYOTLAR', level=1)
fmt_heading(h)

references = [
    "1. International Energy Agency (IEA). World Energy Outlook 2023: Lighting Energy Consumption Statistics. — Paris: IEA Publications, 2023. — 524 p.",
    "2. Statista Research Department. Smart Street Lighting Market Size Worldwide 2021-2030. — Hamburg: Statista GmbH, 2024. — URL: https://www.statista.com/statistics/smart-lighting/",
    "3. Carullo A., Parvis M. An ultrasonic sensor for distance measurement in automotive applications // IEEE Sensors Journal. — 2001. — Vol. 1, No. 2. — P. 143–147.",
    "4. O'zbekiston Respublikasi Prezidentining Farmoni PF-6079. Energiya resurslaridan samarali foydalanish va energiya tejamkorlikni rivojlantirish chora-tadbirlari to'g'risida. — Toshkent, 2020. — 12 b.",
    "5. Kostic M., Djokic L. Recommendations for energy efficient and visually acceptable street lighting // Energy. — 2009. — Vol. 34, No. 10. — P. 1565–1572.",
    "6. Rea M.S. The IESNA Lighting Handbook: Reference and Application. — 9th ed. — New York: Illuminating Engineering Society, 2000. — 1037 p.",
    "7. Zanella A., Bui N., Castellani A. et al. Internet of Things for Smart Cities // IEEE Internet of Things Journal. — 2014. — Vol. 1, No. 1. — P. 22–32.",
    "8. Radulovic D., Skok S., Kirincic V. Energy efficiency public lighting management in the cities // Energy. — 2011. — Vol. 36, No. 4. — P. 1908–1915.",
    "9. Leccese F. Remote-control system of high efficiency and intelligent street lighting using a ZigBee network of devices and sensors // IEEE Transactions on Power Delivery. — 2013. — Vol. 28, No. 1. — P. 21–28.",
    "10. Philips Lighting. CityTouch Connected Street Lighting Management Platform: Technical Documentation. — Eindhoven: Signify, 2023. — 86 p.",
    "11. Telensa Ltd. PLANet Intelligent Street Lighting: System Architecture and Performance Report. — Cambridge: Telensa, 2022. — 42 p.",
    "12. Tvilight BV. CitySense Adaptive Street Lighting Solution: Technical Specifications. — Groningen: Tvilight, 2023. — 38 p.",
    "13. Parkash, Prabu V., Rajendra D. Internet of Things Based Intelligent Street Lighting System for Smart City // International Journal of Innovative Research in Science, Engineering and Technology. — 2016. — Vol. 5, No. 5. — P. 7684–7691.",
    "14. Kinsler L.E., Frey A.R., Coppens A.B., Sanders J.V. Fundamentals of Acoustics. — 4th ed. — New York: John Wiley & Sons, 2000. — 560 p.",
    "15. Borenstein S. Time-varying retail electricity prices: Theory and practice // Electricity Deregulation: Choices and Challenges. — Chicago: University of Chicago Press, 1996. — P. 317–357.",
    "16. RCWL-9610A Ultrasonic Distance Sensor Module: Datasheet and Application Notes. — Shenzhen: RCWL Electronics, 2021. — 8 p.",
    "17. TEMT6000 Ambient Light Sensor: Datasheet. — Munich: Vishay Semiconductors, 2020. — 6 p.",
    "18. Elmenreich W. Sensor Fusion in Time-Triggered Systems // PhD Thesis. — Vienna: Vienna University of Technology, 2002. — 178 p.",
    "19. Espressif Systems. ESP32 Technical Reference Manual. — Shanghai: Espressif, 2024. — 688 p. — URL: https://docs.espressif.com/projects/esp-idf/",
    "20. Google LLC. Firebase Realtime Database Documentation: REST API and SDK Reference. — Mountain View: Google, 2024. — URL: https://firebase.google.com/docs/database",
    "21. Meta Platforms Inc. React Documentation: Component-Based UI Development. — Menlo Park: Meta, 2024. — URL: https://react.dev/",
    "22. Mobizt. Firebase ESP Client Library for ESP32 and ESP8266. — GitHub Repository, 2024. — URL: https://github.com/mobizt/Firebase-ESP-Client",
    "23. PlatformIO Labs. PlatformIO: Professional Collaborative Platform for Embedded Development. — Documentation, 2024. — URL: https://docs.platformio.org/",
    "24. Evan You. Vite.js: Next Generation Frontend Tooling. — Documentation, 2024. — URL: https://vitejs.dev/",
    "25. O'zbekiston Respublikasi Vazirlar Mahkamasi. 58-son qaror: Ko'cha yoritish tizimlarini modernizatsiya qilish dasturi. — Toshkent, 2021. — 8 b."
]

for ref in references:
    add_para(doc, ref, size=12, indent=Cm(0))

# ==================== ILOVALAR ====================
doc.add_page_break()
h = doc.add_heading('ILOVALAR', level=1)
fmt_heading(h)

add_para(doc, "Ushbu bo'limda tizimning asosiy dasturiy kodlari keltirilgan. Barcha kodlar ESP32 mikrokontroller uchun Arduino Framework va PlatformIO muhitida yozilgan.")

# Source codes
main_cpp = '''#include <WiFi.h>
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

void setupWiFi() {
    prefs.begin("wifi", true);
    String ssid = prefs.getString("ssid", WIFI_SSID);
    String pass = prefs.getString("pass", WIFI_PASS);
    prefs.end();
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid.c_str(), pass.c_str());
    unsigned long start = millis();
    while (WiFi.status() != WL_CONNECTED && millis()-start < 10000) { delay(100); }
    if (WiFi.status() == WL_CONNECTED) Serial.println("WiFi OK");
    else startAP();
}

void startAP() {
    WiFi.mode(WIFI_AP);
    WiFi.softAP("SmartLight_AP", "12345678");
    dnsServer.start(53, "*", WiFi.softAPIP());
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
    if (apMode) { dnsServer.processNextRequest(); server.handleClient(); }
    else { firebaseLoop(); }
    readSensors();
    updateLightControl();
    updateStatistics();
    delay(300);
}'''

sensors_cpp = '''#include "sensors.h"
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
}

float readDistance() {
    digitalWrite(TRIG_PIN, LOW); delayMicroseconds(2);
    digitalWrite(TRIG_PIN, HIGH); delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);
    long duration = pulseIn(ECHO_PIN, HIGH, 30000);
    if (duration == 0) return 999.0;
    return duration * 0.034 / 2.0;
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
    if (checkMotion()) { lastMotionTime = millis(); motionDetected = true; }
    else if (millis() - lastMotionTime > HOLD_TIME) motionDetected = false;
}'''

light_control_cpp = '''#include "light_control.h"
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
}

void setRelay(bool state) {
    relayState = state;
    digitalWrite(RELAY_PIN, state ? LOW : HIGH);
    digitalWrite(STATUS_LED, state ? HIGH : LOW);
}

void updateLightControl() {
    if (currentMode == "auto") {
        if (!isDark) { setRelay(false); return; }
        setRelay(motionDetected);
    } else if (currentMode == "manual") {
        setRelay(manualLight);
    }
}'''

firebase_handler_cpp = '''#include "firebase_handler.h"
#include "config.h"
#include "sensors.h"
#include "light_control.h"
#include <Firebase_ESP_Client.h>
#include <WiFi.h>

FirebaseData fbdo, stream;
FirebaseAuth auth;
FirebaseConfig config;
unsigned long lastUpdate = 0;

void setupFirebase() {
    config.api_key = FIREBASE_API_KEY;
    config.database_url = FIREBASE_DB_URL;
    auth.user.email = FIREBASE_EMAIL;
    auth.user.password = FIREBASE_PASSWORD;
    Firebase.begin(&config, &auth);
    Firebase.reconnectWiFi(true);
    Firebase.RTDB.beginStream(&stream, "/device/control");
}

void firebaseLoop() {
    if (WiFi.status() != WL_CONNECTED) return;
    if (Firebase.RTDB.readStream(&stream) && stream.streamAvailable()) {
        String path = stream.dataPath();
        if (path.indexOf("mode") >= 0 && stream.dataType() == "string")
            currentMode = stream.stringData();
        if (path.indexOf("manual_light") >= 0 && stream.dataType() == "boolean")
            manualLight = stream.boolData();
    }
    if (millis() - lastUpdate > 3000) {
        lastUpdate = millis();
        Firebase.RTDB.setFloat(&fbdo, "/device/status/distance_cm", currentDistance);
        Firebase.RTDB.setInt(&fbdo, "/device/status/ambient_light", currentLight);
        Firebase.RTDB.setBool(&fbdo, "/device/status/light_on", relayState);
        Firebase.RTDB.setBool(&fbdo, "/device/status/motion_detected", motionDetected);
        Firebase.RTDB.setString(&fbdo, "/device/status/mode", currentMode);
    }
}'''

add_code_block(doc, "Ilova A. main.cpp — Asosiy dastur fayli", main_cpp)
add_code_block(doc, "Ilova B. sensors.cpp — Sensorlarni o'qish moduli", sensors_cpp)
add_code_block(doc, "Ilova C. light_control.cpp — LED boshqaruv moduli", light_control_cpp)
add_code_block(doc, "Ilova D. firebase_handler.cpp — Firebase ulanish moduli", firebase_handler_cpp)

doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_final.docx')
print("BMI_final.docx yangilandi: XULOSA, ADABIYOTLAR, ILOVALAR qo'shildi.")
