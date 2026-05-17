#include <Arduino.h>
#include <WiFi.h>
#include <WebServer.h>
#include <DNSServer.h>
#include "config.h"
#include "sensors.h"
#include "light_control.h"
#include "firebase_handler.h"
#include "statistics.h"

static bool wifiConnected = false;
static bool firebaseStarted = false;
static bool apMode = false;
static WebServer server(80);
static DNSServer dnsServer;
static unsigned long wifiRetryTime = 0;
static int wifiFailCount = 0;

// AP mode web sahifasi — WiFi sozlash
void handleRoot() {
  String html = "<html><head><meta name='viewport' content='width=device-width,initial-scale=1'>"
    "<style>body{font-family:sans-serif;background:#0a0e1a;color:#e8ecf4;padding:20px;max-width:400px;margin:auto}"
    "input,button{width:100%;padding:12px;margin:8px 0;border-radius:8px;border:1px solid #2a3245;background:#1c2333;color:#e8ecf4;font-size:1rem}"
    "button{background:#4f8cff;border:none;cursor:pointer}h2{text-align:center}</style></head>"
    "<body><h2>💡 Smart Street Light</h2><h3>WiFi sozlash</h3>"
    "<form action='/save' method='POST'>"
    "<input name='ssid' placeholder='WiFi nomi' required>"
    "<input name='pass' type='password' placeholder='Parol' required>"
    "<button type='submit'>Saqlash va ulash</button></form>"
    "<p style='text-align:center;color:#7a8599;font-size:0.8rem'>Hozir offline rejimda ishlayapti</p></body></html>";
  server.send(200, "text/html", html);
}

void handleSave() {
  String ssid = server.arg("ssid");
  String pass = server.arg("pass");
  server.send(200, "text/html", "<html><body style='background:#0a0e1a;color:#e8ecf4;text-align:center;padding:40px'>"
    "<h2>Saqlanmoqda...</h2><p>Qurilma qayta ishga tushadi</p></body></html>");
  delay(1000);
  // WiFi credentials ni NVS ga saqlash
  WiFi.begin(ssid.c_str(), pass.c_str());
  apMode = false;
  ESP.restart();
}

void startAP() {
  WiFi.mode(WIFI_AP_STA);
  WiFi.softAP("SmartLight-Setup", "12345678");
  // Captive portal: har qanday domen → 192.168.4.1
  dnsServer.start(53, "*", WiFi.softAPIP());
  server.on("/", handleRoot);
  server.on("/save", HTTP_POST, handleSave);
  server.onNotFound(handleRoot); // Har qanday URL → setup sahifasi
  server.begin();
  apMode = true;
  Serial.printf("AP ochildi: SmartLight-Setup (192.168.4.1)\n");
}

void setupWiFi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  Serial.print("WiFi ga ulanmoqda");

  // Non-blocking: 10s kutish
  unsigned long start = millis();
  while (WiFi.status() != WL_CONNECTED && millis() - start < 10000) {
    delay(250);
    Serial.print(".");
    // Sensorlar shu paytda ham ishlaydi
  }

  if (WiFi.status() == WL_CONNECTED) {
    wifiConnected = true;
    wifiFailCount = 0;
    Serial.printf("\nWiFi ulandi! IP: %s\n", WiFi.localIP().toString().c_str());
  } else {
    wifiConnected = false;
    wifiFailCount++;
    Serial.println("\nWiFi topilmadi. Offline ishlaydi.");
    // 3 marta urinib bo'lsa — AP ochish
    if (wifiFailCount >= 3) {
      startAP();
    }
  }
}

void checkWiFi() {
  // AP mode da server handle qilish
  if (apMode) {
    dnsServer.processNextRequest();
    server.handleClient();
  }

  // Har 60s da WiFi tekshirish
  if (millis() - wifiRetryTime < 60000) return;
  wifiRetryTime = millis();

  if (WiFi.status() == WL_CONNECTED) {
    if (!wifiConnected) {
      wifiConnected = true;
      wifiFailCount = 0;
      Serial.printf("WiFi ulandi! IP: %s\n", WiFi.localIP().toString().c_str());
      if (!firebaseStarted) {
        setupFirebase();
        setupStatistics();
        firebaseStarted = true;
      }
      // AP ni o'chirish
      if (apMode) {
        dnsServer.stop();
        server.stop();
        WiFi.softAPdisconnect(true);
        apMode = false;
        Serial.println("AP o'chirildi");
      }
    }
  } else {
    if (wifiConnected) {
      Serial.println("WiFi uzildi! Qayta ulanmoqda...");
      wifiConnected = false;
    }
    WiFi.reconnect();
    wifiFailCount++;
    if (wifiFailCount >= 3 && !apMode) {
      startAP();
    }
  }
}

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("\n=== Smart Street Light v7 ===");

  setupSensors();
  setupLightControl();
  setupWiFi();

  if (wifiConnected) {
    setupFirebase();
    setupStatistics();
    firebaseStarted = true;
  }

  Serial.println("Tizim tayyor!");
}

void loop() {
  // Sensorlar va relay DOIMO ishlaydi (offline ham)
  loopSensors();
  loopLightControl();

  // WiFi tekshirish (non-blocking)
  checkWiFi();

  // Firebase faqat online bo'lganda
  if (wifiConnected && firebaseStarted) {
    loopFirebase();
    loopStatistics();
  }
}
