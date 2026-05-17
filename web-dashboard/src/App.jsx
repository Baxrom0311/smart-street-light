import { useState, useEffect } from 'react';
import { db } from './firebase';
import { ref, onValue, set, update } from 'firebase/database';
import { mockStatus, mockControl, mockConfig, mockHistory } from './mockData';
import Dashboard from './components/Dashboard';
import Statistics from './components/Statistics';
import MotionLog from './components/MotionLog';
import './App.css';

function App() {
  const [status, setStatus] = useState(mockStatus);
  const [control, setControl] = useState(mockControl);
  const [config, setConfig] = useState(mockConfig);
  const [history, setHistory] = useState(mockHistory);
  const [tab, setTab] = useState('home');
  const [isLive, setIsLive] = useState(false);

  useEffect(() => {
    if (!isLive) return;
    const unsub1 = onValue(ref(db, 'device/status'), s => { if (s.exists()) setStatus(s.val()); });
    const unsub2 = onValue(ref(db, 'device/control'), s => { if (s.exists()) setControl(s.val()); });
    const unsub3 = onValue(ref(db, 'device/config'), s => { if (s.exists()) setConfig(s.val()); });
    const unsub4 = onValue(ref(db, 'history'), s => { if (s.exists()) setHistory(s.val()); });
    return () => { unsub1(); unsub2(); unsub3(); unsub4(); };
  }, [isLive]);

  const toggleLight = () => {
    if (!isLive) { setControl(c => ({ ...c, manual_light: !c.manual_light })); setStatus(s => ({ ...s, light_on: !s.light_on })); return; }
    set(ref(db, 'device/control/manual_light'), !control.manual_light);
  };
  const setMode = (mode) => {
    if (!isLive) { setControl(c => ({ ...c, mode })); return; }
    set(ref(db, 'device/control/mode'), mode);
  };
  const updateConfig = (data) => {
    if (!isLive) { setConfig(c => ({ ...c, ...data })); return; }
    update(ref(db, 'device/config'), data);
  };
  const updateControl = (data) => {
    if (!isLive) { setControl(c => ({ ...c, ...data })); return; }
    update(ref(db, 'device/control'), data);
  };

  return (
    <div className="app">
      {/* Top bar */}
      <header className="topbar">
        <div className="topbar-left">
          <h1>Smart Light</h1>
        </div>
        <button className={`live-toggle ${isLive ? 'live' : 'demo'}`} onClick={() => setIsLive(!isLive)}>
          <span className="live-dot"></span>
          {isLive ? 'Live' : 'Demo'}
        </button>
      </header>

      {/* Content */}
      <main className="content">
        {tab === 'home' && <Dashboard status={status} control={control} config={config} onToggleLight={toggleLight} onSetMode={setMode} onUpdateConfig={updateConfig} onUpdateControl={updateControl} />}
        {tab === 'stats' && <Statistics history={history} />}
        {tab === 'log' && <MotionLog demoMode={!isLive} />}
        {tab === 'settings' && (
          <Settings config={config} control={control} onUpdateConfig={updateConfig} onUpdateControl={updateControl} />
        )}
      </main>

      {/* Bottom Navigation */}
      <nav className="bottom-nav">
        <button className={tab === 'home' ? 'active' : ''} onClick={() => setTab('home')}>
          <span className="nav-icon">🏠</span>
          <span className="nav-label">Bosh sahifa</span>
        </button>
        <button className={tab === 'stats' ? 'active' : ''} onClick={() => setTab('stats')}>
          <span className="nav-icon">📊</span>
          <span className="nav-label">Statistika</span>
        </button>
        <button className={tab === 'log' ? 'active' : ''} onClick={() => setTab('log')}>
          <span className="nav-icon">📋</span>
          <span className="nav-label">Log</span>
        </button>
        <button className={tab === 'settings' ? 'active' : ''} onClick={() => setTab('settings')}>
          <span className="nav-icon">⚙️</span>
          <span className="nav-label">Sozlama</span>
        </button>
      </nav>
    </div>
  );
}

function Settings({ config, control, onUpdateConfig, onUpdateControl }) {
  const [tempConfig, setTempConfig] = useState(config);

  const save = () => onUpdateConfig(tempConfig);

  return (
    <div className="settings-page">
      <div className="settings-section">
        <h3>Qurilma sozlamalari</h3>
        <div className="setting-item">
          <label>Harakat timeout</label>
          <div className="setting-value">
            <input type="number" value={tempConfig.timeout_sec} onChange={e => setTempConfig({ ...tempConfig, timeout_sec: +e.target.value })} />
            <span>soniya</span>
          </div>
        </div>
        <div className="setting-item">
          <label>Yorug'lik chegarasi</label>
          <div className="setting-value">
            <input type="number" value={tempConfig.light_threshold} onChange={e => setTempConfig({ ...tempConfig, light_threshold: +e.target.value })} />
            <span>lux</span>
          </div>
        </div>
        <div className="setting-item">
          <label>Aniqlash masofasi</label>
          <div className="setting-value">
            <input type="number" value={tempConfig.distance_threshold} onChange={e => setTempConfig({ ...tempConfig, distance_threshold: +e.target.value })} />
            <span>cm</span>
          </div>
        </div>
        <button className="btn-primary" onClick={save}>Saqlash</button>
      </div>

      <div className="settings-section">
        <h3>Jadval rejimi</h3>
        <div className="setting-item">
          <label>Yoqish vaqti</label>
          <input type="time" value={control.schedule_on || '18:00'} onChange={e => onUpdateControl({ schedule_on: e.target.value })} />
        </div>
        <div className="setting-item">
          <label>O'chirish vaqti</label>
          <input type="time" value={control.schedule_off || '06:00'} onChange={e => onUpdateControl({ schedule_off: e.target.value })} />
        </div>
      </div>

      <div className="settings-section">
        <h3>Haqida</h3>
        <p className="about-text">Smart Street Light IoT v5.0</p>
        <p className="about-text">Diplom ishi — Baxrom, 2026</p>
      </div>
    </div>
  );
}

export default App;
