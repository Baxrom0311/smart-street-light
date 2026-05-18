#!/usr/bin/env python3
"""Add ~55 more pages of content"""
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
def img(name, caption):
    if not os.path.exists(IMG + name): return
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.first_line_indent = Cm(0); p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    run = p.add_run(); run.add_picture(IMG + name, width=Cm(14))
    pc = doc.add_paragraph(); pc.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    pc.paragraph_format.first_line_indent = Cm(0); pc.paragraph_format.space_before = Pt(0); pc.paragraph_format.space_after = Pt(0)
    rc = pc.add_run(caption); rc.italic = True; rc.font.size = Pt(12); rc.font.name = 'Times New Roman'
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
def code(x):
    p = doc.add_paragraph(); p.paragraph_format.first_line_indent = Cm(0); p.paragraph_format.left_indent = Cm(1)
    p.paragraph_format.space_before = Pt(0); p.paragraph_format.space_after = Pt(0)
    r = p.add_run(x); r.font.name = 'Courier New'; r.font.size = Pt(10)

# ===== QO'SHIMCHA ILOVALAR =====
doc.add_page_break()
h2("D ilova. Firebase sinxronizatsiya moduli (firebase_handler.cpp)")

fb_code = '''#include "firebase_handler.h"
#include "config.h"
#include "sensors.h"
#include "light_control.h"
#include <Firebase_ESP_Client.h>
#include <WiFi.h>

FirebaseData fbdo;
FirebaseData stream;
FirebaseAuth auth;
FirebaseConfig config;
unsigned long lastUpdate = 0;
const unsigned long UPDATE_INTERVAL = 3000;

void setupFirebase() {
    config.api_key = FIREBASE_API_KEY;
    config.database_url = FIREBASE_DB_URL;
    auth.user.email = FIREBASE_EMAIL;
    auth.user.password = FIREBASE_PASSWORD;
    Firebase.begin(&config, &auth);
    Firebase.reconnectWiFi(true);
    if (!Firebase.RTDB.beginStream(&stream, "/device/control")) {
        Serial.println("[FB] Stream error: " + stream.errorReason());
    }
    Serial.println("[FB] Firebase initialized");
}

void readStream() {
    if (!Firebase.ready()) return;
    if (!Firebase.RTDB.readStream(&stream)) return;
    if (!stream.streamAvailable()) return;
    String path = stream.dataPath();
    if (path.indexOf("mode") >= 0) {
        if (stream.dataType() == "string") {
            currentMode = stream.stringData();
        }
    }
    if (path.indexOf("manual_light") >= 0) {
        if (stream.dataType() == "boolean") {
            manualLight = stream.boolData();
        }
    }
}

void updateStatus() {
    if (!Firebase.ready()) return;
    if (WiFi.status() != WL_CONNECTED) return;
    Firebase.RTDB.setFloat(&fbdo, "/device/status/distance_cm", currentDistance);
    Firebase.RTDB.setInt(&fbdo, "/device/status/ambient_light", currentLight);
    Firebase.RTDB.setBool(&fbdo, "/device/status/light_on", relayState);
    Firebase.RTDB.setBool(&fbdo, "/device/status/motion_detected", motionDetected);
    Firebase.RTDB.setString(&fbdo, "/device/status/mode", currentMode);
    Firebase.RTDB.setInt(&fbdo, "/device/status/uptime", (int)(millis()/1000));
    Firebase.RTDB.setInt(&fbdo, "/device/status/wifi_rssi", WiFi.RSSI());
}

void firebaseLoop() {
    if (WiFi.status() != WL_CONNECTED) return;
    readStream();
    if (millis() - lastUpdate > UPDATE_INTERVAL) {
        lastUpdate = millis();
        updateStatus();
    }
}'''
for line in fb_code.split('\n'): code(line)

doc.add_page_break()
h2("E ilova. Statistika moduli (statistics.cpp)")

stats_code = '''#include "statistics.h"
#include "config.h"
#include "sensors.h"
#include "light_control.h"
#include <Firebase_ESP_Client.h>
#include <WiFi.h>

extern FirebaseData fbdo;
unsigned long onDuration = 0;
unsigned long lastOnTime = 0;
int motionsCount = 0;
unsigned long lastStatsUpdate = 0;
const unsigned long STATS_INTERVAL = 60000;
bool wasOn = false;

void setupStatistics() {
    onDuration = 0;
    motionsCount = 0;
    lastStatsUpdate = millis();
}

void updateStatistics() {
    if (relayState && !wasOn) {
        lastOnTime = millis();
        wasOn = true;
    } else if (!relayState && wasOn) {
        onDuration += millis() - lastOnTime;
        wasOn = false;
    }
    static bool lastMotion = false;
    if (motionDetected && !lastMotion) motionsCount++;
    lastMotion = motionDetected;
    if (millis() - lastStatsUpdate > STATS_INTERVAL) {
        lastStatsUpdate = millis();
        saveStats();
    }
}

void saveStats() {
    if (WiFi.status() != WL_CONNECTED) return;
    if (!Firebase.ready()) return;
    unsigned long onMin = onDuration / 60000;
    int savedPercent = (onMin < 720) ? ((720 - onMin) * 100) / 720 : 0;
    String path = "/history/today";
    Firebase.RTDB.setInt(&fbdo, path + "/motions_count", motionsCount);
    Firebase.RTDB.setInt(&fbdo, path + "/on_duration_min", (int)onMin);
    Firebase.RTDB.setInt(&fbdo, path + "/energy_saved_percent", savedPercent);
}'''
for line in stats_code.split('\n'): code(line)

doc.add_page_break()
h2("J ilova. Konfiguratsiya fayli (config.h)")

config_code = '''#ifndef CONFIG_H
#define CONFIG_H

#define TRIG_PIN        4
#define ECHO_PIN        16
#define LIGHT_PIN       34
#define RELAY_PIN       26
#define STATUS_LED      2

#define DISTANCE_THRESHOLD  200
#define DARK_THRESHOLD      250
#define LIGHT_THRESHOLD     350
#define HOLD_TIME           5000

#define WIFI_SSID       "baxrom0311"
#define WIFI_PASS       "12345678"

#define FIREBASE_API_KEY    "AIzaSyDTGp-CAQmfuhuc4bGYXEaWoEhXnWMpPrU"
#define FIREBASE_DB_URL     "https://smart-street-light-iot-default-rtdb.firebaseio.com"
#define FIREBASE_EMAIL      "device@smartlight.com"
#define FIREBASE_PASSWORD   "SmartLight2026!"

#endif'''
for line in config_code.split('\n'): code(line)

doc.add_page_break()
h2("Z ilova. React Dashboard (App.jsx)")

react_code = '''import { useState, useEffect } from 'react';
import { ref, onValue, set } from 'firebase/database';
import { signInWithEmailAndPassword, signOut } from 'firebase/auth';
import { db, auth } from './firebase';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import Statistics from './components/Statistics';
import MotionLog from './components/MotionLog';
import Settings from './components/Settings';
import { getMockData } from './mockData';
import './App.css';

function App() {
  const [user, setUser] = useState(null);
  const [page, setPage] = useState('dashboard');
  const [data, setData] = useState(null);
  const [isLive, setIsLive] = useState(() => {
    return localStorage.getItem('isLive') !== 'false';
  });

  useEffect(() => {
    const unsub = auth.onAuthStateChanged(setUser);
    return unsub;
  }, []);

  useEffect(() => {
    if (!user || !isLive) return;
    const statusRef = ref(db, 'device/status');
    const unsub = onValue(statusRef, (snap) => {
      if (snap.exists()) setData(snap.val());
    });
    return unsub;
  }, [user, isLive]);

  useEffect(() => {
    if (!isLive) setData(getMockData());
  }, [isLive]);

  const handleLogin = async (email, pass) => {
    await signInWithEmailAndPassword(auth, email, pass);
  };

  const togglePower = async () => {
    const newState = !data?.light_on;
    setData(prev => ({...prev, light_on: newState}));
    if (isLive) {
      await set(ref(db, 'device/control/manual_light'), newState);
    }
  };

  const setMode = async (mode) => {
    setData(prev => ({...prev, mode}));
    if (isLive) {
      await set(ref(db, 'device/control/mode'), mode);
    }
  };

  if (!user) return <Login onLogin={handleLogin} />;

  return (
    <div className="app">
      <nav className="sidebar">
        <h2>Smart Light</h2>
        <button onClick={() => setPage('dashboard')}>Dashboard</button>
        <button onClick={() => setPage('stats')}>Statistika</button>
        <button onClick={() => setPage('log')}>Log</button>
        <button onClick={() => setPage('settings')}>Sozlamalar</button>
        <div className="mode-toggle">
          <span>{isLive ? "LIVE" : "DEMO"}</span>
          <button onClick={() => {
            const next = !isLive;
            setIsLive(next);
            localStorage.setItem('isLive', next);
          }}>Toggle</button>
        </div>
      </nav>
      <main>
        {page === 'dashboard' && <Dashboard data={data} onToggle={togglePower} onSetMode={setMode} />}
        {page === 'stats' && <Statistics isLive={isLive}/>}
        {page === 'log' && <MotionLog isLive={isLive}/>}
        {page === 'settings' && <Settings isLive={isLive}/>}
      </main>
    </div>
  );
}
export default App;'''
for line in react_code.split('\n'): code(line)

doc.add_page_break()
h2("I ilova. Firebase konfiguratsiya (firebase.js)")
fb_js = '''import { initializeApp } from 'firebase/app';
import { getDatabase } from 'firebase/database';
import { getAuth } from 'firebase/auth';

const firebaseConfig = {
  apiKey: "AIzaSyDTGp-CAQmfuhuc4bGYXEaWoEhXnWMpPrU",
  authDomain: "smart-street-light-iot.firebaseapp.com",
  databaseURL: "https://smart-street-light-iot-default-rtdb.firebaseio.com",
  projectId: "smart-street-light-iot",
  storageBucket: "smart-street-light-iot.appspot.com",
  messagingSenderId: "123456789",
  appId: "1:123456789:web:abc123"
};

const app = initializeApp(firebaseConfig);
export const db = getDatabase(app);
export const auth = getAuth(app);'''
for line in fb_js.split('\n'): code(line)

doc.add_page_break()
h2("K ilova. PlatformIO konfiguratsiya (platformio.ini)")
pio = '''[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
monitor_speed = 115200
upload_speed = 921600
upload_port = /dev/cu.usbserial-0001
board_build.partitions = huge_app.csv
lib_deps =
    mobizt/Firebase ESP32 Client@^4.4.17
build_flags =
    -DCORE_DEBUG_LEVEL=0'''
for line in pio.split('\n'): code(line)

h2("L ilova. Vite konfiguratsiya (vite.config.js)")
vite = '''import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { VitePWA } from 'vite-plugin-pwa';

export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      manifest: {
        name: 'Smart Street Light',
        short_name: 'SmartLight',
        theme_color: '#1a1a2e',
        background_color: '#1a1a2e',
        display: 'standalone',
        icons: [{ src: '/icon-192.png', sizes: '192x192', type: 'image/png' }]
      }
    })
  ]
});'''
for line in vite.split('\n'): code(line)

doc.add_page_break()
h2("M ilova. Dashboard komponenti (Dashboard.jsx)")
dash = '''import { useState } from 'react';

export default function Dashboard({ data, onToggle, onSetMode }) {
  const [syncing, setSyncing] = useState(false);

  const handleToggle = async () => {
    setSyncing(true);
    await onToggle();
    setTimeout(() => setSyncing(false), 500);
  };

  if (!data) return <div className="loading">Yuklanmoqda...</div>;

  return (
    <div className="dashboard">
      <div className="status-card">
        <h3>Yoritgich holati</h3>
        <button
          className={`power-btn ${data.light_on ? 'on' : 'off'} ${syncing ? 'syncing' : ''}`}
          onClick={handleToggle}
        >
          {data.light_on ? 'YONIQ' : 'O\\'CHIQ'}
        </button>
      </div>
      <div className="mode-selector">
        <h3>Rejim</h3>
        <div className="modes">
          {['auto', 'manual', 'schedule'].map(mode => (
            <button
              key={mode}
              className={data.mode === mode ? 'active' : ''}
              onClick={() => onSetMode(mode)}
            >
              {mode === 'auto' ? 'Avtomatik' : mode === 'manual' ? 'Qo\\'lda' : 'Jadval'}
            </button>
          ))}
        </div>
      </div>
      <div className="sensors-grid">
        <div className="sensor-card">
          <span className="label">Masofa</span>
          <span className="value">{data.distance_cm} cm</span>
        </div>
        <div className="sensor-card">
          <span className="label">Yorug\\'lik</span>
          <span className="value">{data.ambient_light}</span>
        </div>
        <div className="sensor-card">
          <span className="label">Harakat</span>
          <span className="value">{data.motion_detected ? 'Ha' : 'Yo\\'q'}</span>
        </div>
        <div className="sensor-card">
          <span className="label">WiFi</span>
          <span className="value">{data.wifi_rssi} dBm</span>
        </div>
      </div>
    </div>
  );
}'''
for line in dash.split('\n'): code(line)

doc.add_page_break()
h2("N ilova. Statistika komponenti (Statistics.jsx)")
stats_jsx = '''import { useState, useEffect } from 'react';
import { ref, onValue } from 'firebase/database';
import { db } from '../firebase';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { getMockHistory } from '../mockData';

export default function Statistics({ isLive }) {
  const [data, setData] = useState([]);
  const [view, setView] = useState('weekly');

  useEffect(() => {
    if (!isLive) {
      setData(getMockHistory());
      return;
    }
    const histRef = ref(db, 'history');
    const unsub = onValue(histRef, (snap) => {
      if (snap.exists()) {
        const val = snap.val();
        const arr = Object.entries(val).map(([date, v]) => ({
          date, ...v
        }));
        setData(arr.slice(-7));
      }
    });
    return unsub;
  }, [isLive]);

  return (
    <div className="statistics">
      <h2>Energiya tejash statistikasi</h2>
      <div className="view-toggle">
        <button className={view === 'weekly' ? 'active' : ''} onClick={() => setView('weekly')}>
          Haftalik
        </button>
        <button className={view === 'daily' ? 'active' : ''} onClick={() => setView('daily')}>
          Kunlik
        </button>
      </div>
      <div className="chart-container">
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="date" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="energy_saved_percent" fill="#4ade80" name="Tejash %" />
          </BarChart>
        </ResponsiveContainer>
      </div>
      <div className="stats-summary">
        <div className="stat">
          <span>O'rtacha tejash</span>
          <span>{data.length ? Math.round(data.reduce((s,d) => s + d.energy_saved_percent, 0) / data.length) : 0}%</span>
        </div>
        <div className="stat">
          <span>Jami harakatlar</span>
          <span>{data.reduce((s,d) => s + d.motions_count, 0)}</span>
        </div>
      </div>
    </div>
  );
}'''
for line in stats_jsx.split('\n'): code(line)

doc.add_page_break()
h2("O ilova. CSS stillar (App.css) - asosiy qism")
css = '''* { margin: 0; padding: 0; box-sizing: border-box; }

.app {
  display: flex;
  min-height: 100vh;
  background: #0f0f23;
  color: #e0e0e0;
}

.sidebar {
  width: 240px;
  background: #1a1a2e;
  padding: 20px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.sidebar h2 {
  color: #4ade80;
  margin-bottom: 20px;
  font-size: 1.2rem;
}

.sidebar button {
  background: transparent;
  border: 1px solid #333;
  color: #e0e0e0;
  padding: 12px 16px;
  border-radius: 8px;
  cursor: pointer;
  text-align: left;
}

.sidebar button:hover { background: #252540; }
.sidebar button.active { background: #4ade80; color: #000; }

main {
  flex: 1;
  padding: 24px;
  overflow-y: auto;
}

.power-btn {
  width: 120px; height: 120px;
  border-radius: 50%;
  border: 3px solid #333;
  font-size: 1rem; font-weight: bold;
  cursor: pointer;
  transition: all 0.3s;
}

.power-btn.on { background: #4ade80; color: #000; border-color: #4ade80; }
.power-btn.off { background: #333; color: #999; }
.power-btn.syncing { animation: pulse 0.5s ease; }

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

.sensors-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 12px;
  margin-top: 20px;
}

.sensor-card {
  background: #1a1a2e;
  padding: 16px;
  border-radius: 12px;
  text-align: center;
}

@media (max-width: 768px) {
  .sidebar { display: none; }
  .bottom-nav {
    position: fixed; bottom: 0; left: 0; right: 0;
    display: flex; background: #1a1a2e;
    padding: 8px; justify-content: space-around;
  }
}'''
for line in css.split('\n'): code(line)

doc.add_page_break()
h2("P ilova. Firebase ma'lumotlar bazasi qoidalari (database.rules.json)")
rules = '''{
  "rules": {
    "device": {
      "status": {
        ".read": true,
        ".write": "auth != null"
      },
      "control": {
        ".read": true,
        ".write": "auth != null"
      },
      "config": {
        ".read": true,
        ".write": "auth != null"
      }
    },
    "history": {
      ".read": "auth != null",
      ".write": "auth != null"
    },
    "motion_log": {
      ".read": "auth != null",
      ".write": "auth != null"
    }
  }
}'''
for line in rules.split('\n'): code(line)

h2("R ilova. Mock data (mockData.js)")
mock = '''export function getMockData() {
  return {
    light_on: false,
    motion_detected: false,
    distance_cm: 250,
    ambient_light: 820,
    mode: "auto",
    last_motion: Date.now() - 60000,
    uptime: 3600,
    wifi_rssi: -45
  };
}

export function getMockHistory() {
  const days = ['Dush', 'Sesh', 'Chor', 'Pay', 'Jum', 'Shan', 'Yak'];
  return days.map((d, i) => ({
    date: d,
    motions_count: 30 + Math.floor(Math.random() * 40),
    on_duration_min: 80 + Math.floor(Math.random() * 100),
    energy_saved_percent: 70 + Math.floor(Math.random() * 20)
  }));
}'''
for line in mock.split('\n'): code(line)

# Save
doc.save('/Users/baxrom/ish_full/dimlom_ishi/smart_street_light/docs/BMI/BMI_v2.docx')
print("Additional appendices added!")
