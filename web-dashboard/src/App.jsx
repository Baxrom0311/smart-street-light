import { useState, useEffect } from 'react';
import { db, auth } from './firebase';
import { ref, onValue, set, update } from 'firebase/database';
import { onAuthStateChanged, signOut } from 'firebase/auth';
import { mockStatus, mockControl, mockConfig, mockHistory } from './mockData';
import Login from './components/Login';
import Dashboard from './components/Dashboard';
import Statistics from './components/Statistics';
import MotionLog from './components/MotionLog';
import './App.css';

const USE_MOCK = import.meta.env.VITE_USE_MOCK === 'true';

function App() {
  const [user, setUser] = useState(null);
  const [authLoading, setAuthLoading] = useState(true);
  const [status, setStatus] = useState(USE_MOCK ? mockStatus : null);
  const [control, setControl] = useState(USE_MOCK ? mockControl : { mode: 'auto', manual_light: false, brightness: 100, led_color: '#ffffff' });
  const [config, setConfig] = useState(USE_MOCK ? mockConfig : { timeout_sec: 30, light_threshold: 300, distance_threshold: 200 });
  const [history, setHistory] = useState(USE_MOCK ? mockHistory : {});
  const [tab, setTab] = useState('dashboard');
  const [demoMode, setDemoMode] = useState(USE_MOCK);

  useEffect(() => {
    const unsub = onAuthStateChanged(auth, (u) => { setUser(u); setAuthLoading(false); });
    return unsub;
  }, []);

  useEffect(() => {
    if (demoMode) return;
    if (!user) return;
    const unsub1 = onValue(ref(db, 'device/status'), snap => { if (snap.exists()) setStatus(snap.val()); });
    const unsub2 = onValue(ref(db, 'device/control'), snap => { if (snap.exists()) setControl(snap.val()); });
    const unsub3 = onValue(ref(db, 'device/config'), snap => { if (snap.exists()) setConfig(snap.val()); });
    const unsub4 = onValue(ref(db, 'history'), snap => { if (snap.exists()) setHistory(snap.val()); });
    return () => { unsub1(); unsub2(); unsub3(); unsub4(); };
  }, [demoMode, user]);

  const toggleLight = () => {
    if (demoMode) { setControl(c => ({ ...c, manual_light: !c.manual_light })); setStatus(s => ({ ...s, light_on: !s.light_on })); return; }
    set(ref(db, 'device/control/manual_light'), !control.manual_light);
  };
  const setMode = (mode) => {
    if (demoMode) { setControl(c => ({ ...c, mode })); return; }
    set(ref(db, 'device/control/mode'), mode);
  };
  const updateConfig = (newConfig) => {
    if (demoMode) { setConfig(c => ({ ...c, ...newConfig })); return; }
    update(ref(db, 'device/config'), newConfig);
  };
  const updateControl = (data) => {
    if (demoMode) { setControl(c => ({ ...c, ...data })); return; }
    update(ref(db, 'device/control'), data);
  };
  const switchMode = () => {
    const next = !demoMode;
    setDemoMode(next);
    if (next) { setStatus(mockStatus); setControl(mockControl); setConfig(mockConfig); setHistory(mockHistory); }
    else { setStatus(null); }
  };

  if (authLoading) return <div className="app"><div className="loading">Yuklanmoqda...</div></div>;
  if (!user && !demoMode) return <Login />;

  // Device online check (if uptime updated in last 10s)
  const isOnline = status && (Date.now() / 1000 - status.uptime < 30);

  return (
    <div className="app">
      <header>
        <h1>🔆 Smart Street Light</h1>
        <div className="device-status">
          <span className={`status-dot ${status && !demoMode ? 'online' : demoMode ? 'online' : 'offline'}`}></span>
          <span>{demoMode ? 'Demo' : status ? 'Online' : 'Offline'}</span>
        </div>
        <nav>
          <button className={tab === 'dashboard' ? 'active' : ''} onClick={() => setTab('dashboard')}>Boshqaruv</button>
          <button className={tab === 'stats' ? 'active' : ''} onClick={() => setTab('stats')}>Statistika</button>
          <button className={tab === 'log' ? 'active' : ''} onClick={() => setTab('log')}>Log</button>
          <button className={demoMode ? 'demo-active' : 'demo'} onClick={switchMode}>{demoMode ? '🟡 Demo' : '🟢 Live'}</button>
          {user && <button className="logout" onClick={() => signOut(auth)}>🚪</button>}
        </nav>
      </header>
      <main>
        {tab === 'dashboard' && (
          <Dashboard status={status} control={control} config={config} onToggleLight={toggleLight} onSetMode={setMode} onUpdateConfig={updateConfig} onUpdateControl={updateControl} demoMode={demoMode} />
        )}
        {tab === 'stats' && <Statistics history={history} />}
        {tab === 'log' && <MotionLog demoMode={demoMode} />}
      </main>
    </div>
  );
}

export default App;
