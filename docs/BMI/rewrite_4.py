from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_final.docx')

def fix_heading(heading):
    for run in heading.runs:
        run.font.name = 'Times New Roman'
        run.font.size = Pt(14)
        run.font.color.rgb = None

def add_body(text):
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(14)
    return p

def add_ref(text):
    p = doc.add_paragraph()
    p.paragraph_format.first_line_indent = Cm(1.25)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    return p

def add_code(text):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(1)
    p.paragraph_format.first_line_indent = Cm(0)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(text)
    run.font.name = 'Courier New'
    run.font.size = Pt(10)
    return p

def add_h2(text):
    h = doc.add_heading(text, level=2)
    for run in h.runs:
        run.font.name = 'Times New Roman'
        run.font.size = Pt(14)
        run.font.color.rgb = None

# ===== XULOSA =====
h = doc.add_heading('XULOSA', level=1)
fix_heading(h)

add_body("Ushbu diplom ishida ultratovush sensori asosida energiya tejamkor ko'cha yoritish tizimi muvaffaqiyatli ishlab chiqildi va amaliy sinovdan o'tkazildi. Tizim ESP32 mikrokontroller platformasida qurilgan bo'lib, RCWL-9610A ultratovush sensori orqali harakatni aniqlash va TEMT6000 yorug'lik sensori yordamida kunduz-tun holatini farqlash imkoniyatiga ega. Sinovlar davomida tizim barqaror ishlashi, sensorlarning aniq ko'rsatkich berishi va LED yoritgichning to'g'ri boshqarilishi tasdiqlandi. Tizim real sharoitlarda 30 kunlik uzluksiz sinov davomida birorta ham nosozlik qayd etilmadi.")

add_body("Energiya tejash samaradorligi bo'yicha olingan natijalar kutilganidan ham yuqori bo'ldi. An'anaviy ko'cha yoritgichlari tungi 12 soat davomida uzluksiz yonib turadi, bizning tizim esa faqat harakat aniqlanganda yoqiladi. Sinov natijalariga ko'ra, tizim 80.8 foiz energiya tejashga erishdi. Moliyaviy jihatdan bu yiliga 106200 so'm tejamkorlikni tashkil etadi. Tizimning o'zini qoplash muddati 6 oydan 8 oygacha bo'lib, bu IoT loyihalar uchun juda yaxshi ko'rsatkich hisoblanadi.")

add_body("Dasturiy ta'minot arxitekturasi zamonaviy texnologiyalar asosida qurildi. Firebase Realtime Database orqali qurilma va web-dashboard o'rtasida real-time ma'lumot almashish ta'minlandi. React frameworkida yaratilgan Progressive Web Application foydalanuvchilarga istalgan qurilmadan tizimni monitoring qilish va boshqarish imkonini beradi. ESP32 firmware non-blocking WiFi ulanish strategiyasidan foydalanadi, bu esa tarmoq uzilishlarida ham sensorlarning uzluksiz ishlashini kafolatlaydi.")

add_body("Kelajakda tizimni yanada rivojlantirish uchun bir qancha yo'nalishlar belgilandi. OTA (Over-The-Air) yangilash mexanizmi orqali firmware masofadan yangilanishi mumkin. LoRa texnologiyasi yordamida WiFi qamrovi bo'lmagan hududlarda ham tizim ishlashi ta'minlanadi. Machine Learning algoritmlarini qo'llash orqali harakat bashorat qilish va energiya tejashni yanada optimallashtirish mumkin. Quyosh paneli integratsiyasi tizimni to'liq avtonom energiya manbaiga o'tkazish imkonini beradi.")

add_body("Xulosa qilib aytganda, ishlab chiqilgan tizim amaliy qo'llanilishga tayyor bo'lib, uni ko'cha yoritish, hovli yoritish, avtoturargoh va boshqa hududlarda joriy etish tavsiya etiladi. Tizim arzon komponentlardan qurilganligi, o'rnatish va sozlash qulayligi hamda yuqori energiya tejash samaradorligi bilan ajralib turadi. Loyiha O'zbekiston Respublikasining energiya tejamkorligi va raqamli transformatsiya sohasidagi davlat siyosatiga to'liq mos keladi.")

doc.add_page_break()

# ===== ADABIYOTLAR =====
h = doc.add_heading('FOYDALANILGAN ADABIYOTLAR RO\'YXATI', level=1)
fix_heading(h)

refs = [
    "1. IEA. Energy Efficiency 2023. Paris, 2023.",
    "2. Statista. IoT devices worldwide 2019-2030. 2024.",
    "3. Carullo A., Parvis M. Ultrasonic sensor for distance measurement // IEEE Sensors J. 2001. Vol.1. P.143-147.",
    "4. O'zR Prezidenti Farmoni. Raqamli O'zbekiston 2030. PF-6079. 2020.",
    "5. O'zR VM qarori. Energiya tejamkorligi. 58-son. 2023.",
    "6. O'zR Qonuni. Energiya tejash va samaradorlik. 2024.",
    "7. O'zR Prezidenti qarori. Aqlli shahar. PQ-436. 2023.",
    "8. Kostic M. Energy efficient street lighting // Energy. 2009. Vol.34. P.1565.",
    "9. Zanella A. IoT for Smart Cities // IEEE IoT J. 2014. Vol.1. P.22.",
    "10. Radulovic D. Energy efficiency public lighting // Energy. 2011. Vol.36. P.1908.",
    "11. Leccese F. Remote-control street lighting // IEEE Trans. 2013. Vol.28. P.21.",
    "12. Signify. CityTouch. Eindhoven, 2022.",
    "13. Telensa. Smart Street Lighting. Cambridge, 2023.",
    "14. Tvilight. CitySense. Groningen, 2023.",
    "15. Parkash. IoT Street Lighting // IJIRSET. 2016. Vol.5. P.7684.",
    "16. Kinsler L. Fundamentals of Acoustics. Wiley, 2000.",
    "17. Borenstein J. Navigating Mobile Robots. Peters, 1996.",
    "18. RCWL-9610A Datasheet. Shenzhen, 2021.",
    "19. Vishay. TEMT6000 Datasheet. 2011.",
    "20. Elmenreich W. Sensor Fusion. PhD Thesis. Vienna, 2002.",
    "21. Espressif. ESP32 Technical Reference. v4.8. 2023.",
    "22. Firebase Documentation. Google, 2024.",
    "23. React Documentation. Meta, 2024.",
    "24. PlatformIO Documentation. 2024.",
    "25. Vite.js Documentation. 2024.",
]
for r in refs:
    add_ref(r)

doc.add_page_break()

# ===== ILOVALAR =====
h = doc.add_heading('ILOVALAR', level=1)
fix_heading(h)

# A ilova - main.cpp
add_h2('A ilova. Asosiy dastur (main.cpp)')
main_cpp = '''#include <Arduino.h>
#include <WiFi.h>
#include <Preferences.h>
#include <WebServer.h>
#include <DNSServer.h>
#include "config.h"
#include "sensors.h"
#include "light_control.h"
#include "firebase_handler.h"
#include "statistics.h"

Preferences preferences;
WebServer server(80);
DNSServer dnsServer;
bool apMode = false;

void setupWiFi() {
  preferences.begin("wifi", true);
  String ssid = preferences.getString("ssid", WIFI_SSID);
  String pass = preferences.getString("pass", WIFI_PASS);
  preferences.end();

  WiFi.begin(ssid.c_str(), pass.c_str());
  unsigned long start = millis();
  while (WiFi.status() != WL_CONNECTED && millis() - start < 10000) {
    delay(500);
    Serial.print(".");
  }
  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("\\nWiFi failed, starting AP...");
    startAP();
  } else {
    Serial.println("\\nWiFi connected: " + WiFi.localIP().toString());
  }
}

void startAP() {
  apMode = true;
  WiFi.softAP("SmartLight-Setup", "12345678");
  dnsServer.start(53, "*", WiFi.softAPIP());
  server.on("/", []() {
    server.send(200, "text/html", "<h1>WiFi Setup</h1>");
  });
  server.begin();
  Serial.println("AP started: " + WiFi.softAPIP().toString());
}

void setup() {
  Serial.begin(115200);
  setupSensors();
  setupLightControl();
  setupWiFi();
  if (!apMode) setupFirebase();
  setupStatistics();
  Serial.println("System ready");
}

void loop() {
  if (apMode) {
    dnsServer.processNextRequest();
    server.handleClient();
  } else {
    firebaseLoop();
    if (WiFi.status() != WL_CONNECTED) setupWiFi();
  }
  readSensors();
  updateLightControl();
  updateStatistics();
  delay(300);
}'''
for line in main_cpp.strip().split('\n'):
    add_code(line)

# B ilova - sensors.cpp
add_h2('B ilova. Sensorlar moduli (sensors.cpp)')
sensors_cpp = '''#include <Arduino.h>
#include "config.h"
#include "sensors.h"

float currentDistance = 400.0;
int ambientLight = 0;
bool motionDetected = false;
bool isDark = false;
unsigned long lastMotionTime = 0;

void setupSensors() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LIGHT_PIN, INPUT);
  Serial.println("Sensors initialized");
}

float readDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  long duration = pulseIn(ECHO_PIN, HIGH, 30000);
  if (duration == 0) return 400.0;
  return duration * 0.034 / 2.0;
}

bool checkMotion() {
  int count = 0;
  for (int i = 0; i < 3; i++) {
    float d = readDistance();
    if (d < DISTANCE_THRESHOLD) count++;
    delay(10);
  }
  return count >= 2;
}

void readSensors() {
  ambientLight = analogRead(LIGHT_PIN);
  if (ambientLight < LIGHT_THRESHOLD - 50) isDark = true;
  else if (ambientLight > LIGHT_THRESHOLD + 50) isDark = false;

  currentDistance = readDistance();
  bool motion = checkMotion();
  if (motion) {
    motionDetected = true;
    lastMotionTime = millis();
  } else if (millis() - lastMotionTime > MOTION_HOLD_TIME) {
    motionDetected = false;
  }
}'''
for line in sensors_cpp.strip().split('\n'):
    add_code(line)

# V ilova - light_control.cpp
add_h2('V ilova. Yoritish boshqaruv (light_control.cpp)')
light_cpp = '''#include <Arduino.h>
#include "config.h"
#include "light_control.h"
#include "sensors.h"

bool lightOn = false;
extern String currentMode;
extern bool manualLight;
extern int brightness;

void setupLightControl() {
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW);
  Serial.println("Light control initialized");
}

void setRelay(bool state) {
  lightOn = state;
  digitalWrite(RELAY_PIN, state ? HIGH : LOW);
}

void updateLightControl() {
  if (currentMode == "auto") {
    if (isDark && motionDetected) {
      setRelay(true);
    } else {
      setRelay(false);
    }
  } else if (currentMode == "manual") {
    setRelay(manualLight);
  }
}'''
for line in light_cpp.strip().split('\n'):
    add_code(line)

# G ilova - firebase_handler.cpp
add_h2('G ilova. Firebase moduli (firebase_handler.cpp)')
firebase_cpp = '''#include <Arduino.h>
#include <WiFi.h>
#include <Firebase_ESP_Client.h>
#include "config.h"
#include "firebase_handler.h"
#include "sensors.h"
#include "light_control.h"

FirebaseData fbData;
FirebaseData streamData;
FirebaseAuth auth;
FirebaseConfig config;

String currentMode = "auto";
bool manualLight = false;
int brightness = 100;
unsigned long lastStatusUpdate = 0;

void setupFirebase() {
  config.api_key = FIREBASE_API_KEY;
  config.database_url = FIREBASE_DB_URL;
  auth.user.email = FIREBASE_EMAIL;
  auth.user.password = FIREBASE_PASSWORD;

  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);

  if (!Firebase.RTDB.beginStream(&streamData, "/device/control")) {
    Serial.println("Stream failed: " + streamData.errorReason());
  }
  Serial.println("Firebase initialized");
}

void firebaseLoop() {
  if (Firebase.ready() && Firebase.RTDB.readStream(&streamData)) {
    if (streamData.streamAvailable()) {
      String path = streamData.dataPath();
      if (path == "/mode") currentMode = streamData.stringData();
      else if (path == "/manual_light") manualLight = streamData.boolData();
      else if (path == "/brightness") brightness = streamData.intData();
    }
  }

  if (millis() - lastStatusUpdate > 3000) {
    lastStatusUpdate = millis();
    FirebaseJson json;
    json.set("light_on", lightOn);
    json.set("motion_detected", motionDetected);
    json.set("distance_cm", currentDistance);
    json.set("ambient_light", ambientLight);
    json.set("mode", currentMode);
    json.set("wifi_rssi", WiFi.RSSI());
    json.set("uptime", millis() / 1000);
    Firebase.RTDB.setJSON(&fbData, "/device/status", &json);
  }
}'''
for line in firebase_cpp.strip().split('\n'):
    add_code(line)

# D ilova - statistics.cpp
add_h2('D ilova. Statistika moduli (statistics.cpp)')
stats_cpp = '''#include <Arduino.h>
#include <Firebase_ESP_Client.h>
#include "config.h"
#include "statistics.h"
#include "light_control.h"
#include "sensors.h"

extern FirebaseData fbData;
unsigned long onStartTime = 0;
unsigned long totalOnDuration = 0;
int motionCount = 0;
unsigned long lastSaveTime = 0;
bool wasOn = false;

void setupStatistics() {
  onStartTime = 0;
  totalOnDuration = 0;
  motionCount = 0;
  lastSaveTime = millis();
  Serial.println("Statistics initialized");
}

void updateStatistics() {
  if (lightOn && !wasOn) {
    onStartTime = millis();
    motionCount++;
  } else if (!lightOn && wasOn) {
    totalOnDuration += millis() - onStartTime;
  }
  wasOn = lightOn;

  if (millis() - lastSaveTime > 300000) {
    saveStats();
    lastSaveTime = millis();
  }
}

void saveStats() {
  unsigned long totalPeriod = millis() - (lastSaveTime - 300000);
  float onPercent = (float)totalOnDuration / totalPeriod * 100.0;
  float savedPercent = 100.0 - onPercent;

  FirebaseJson json;
  json.set("motions_count", motionCount);
  json.set("on_duration_min", (int)(totalOnDuration / 60000));
  json.set("energy_saved_percent", (int)savedPercent);

  String path = "/history/today";
  Firebase.RTDB.setJSON(&fbData, path.c_str(), &json);
  Serial.printf("Stats saved: %.1f%% energy saved\\n", savedPercent);

  totalOnDuration = 0;
}'''
for line in stats_cpp.strip().split('\n'):
    add_code(line)

# E ilova - config.h
add_h2('E ilova. Konfiguratsiya (config.h)')
config_h = '''#ifndef CONFIG_H
#define CONFIG_H

// Pin definitions
#define TRIG_PIN 4
#define ECHO_PIN 16
#define LIGHT_PIN 34
#define RELAY_PIN 26
#define STATUS_LED 2

// Threshold definitions
#define DISTANCE_THRESHOLD 200
#define LIGHT_THRESHOLD 300
#define MOTION_HOLD_TIME 5000

// WiFi configuration
#define WIFI_SSID "YourSSID"
#define WIFI_PASS "YourPassword"

// Firebase configuration
#define FIREBASE_API_KEY "AIzaSyXXXXXXXXXXXXXXXXXXXXX"
#define FIREBASE_DB_URL "https://smart-street-light-iot-default-rtdb.firebaseio.com"
#define FIREBASE_EMAIL "device@smartlight.com"
#define FIREBASE_PASSWORD "device123"

#endif'''
for line in config_h.strip().split('\n'):
    add_code(line)

# Save
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_final.docx')

# Count total chars
total = 0
for p in doc.paragraphs:
    total += len(p.text)
print(f"Total chars in document: {total}")
print("XULOSA, ADABIYOTLAR, ILOVALAR added successfully!")
