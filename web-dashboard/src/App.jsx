import { useState, useEffect } from 'react';
import { db } from './firebase';
import { ref, onValue, set, update } from 'firebase/database';
import { mockStatus, mockControl, mockConfig, mockHistory } from './mockData';
import Dashboard from './components/Dashboard';
import Statistics from './components/Statistics';
import './App.css';

const USE_MOCK = import.meta.env.VITE_USE_MOCK === 'true';

function App() {
  const [status, setStatus] = useState(USE_MOCK ? mockStatus : null);
  const [control, setControl] = useState(USE_MOCK ? mockControl : { mode: 'auto', manual_light: false });
  const [config, setConfig] = useState(USE_MOCK ? mockConfig : { timeout_sec: 30, light_threshold: 300, distance_threshold: 200 });
  const [history, setHistory] = useState(USE_MOCK ? mockHistory : {});
  const [tab, setTab] = useState('dashboard');
  const [demoMode, setDemoMode] = useState(USE_MOCK);

  useEffect(() => {
    if (demoMode) return;
    const unsub1 = onValue(ref(db, 'device/status'), snap => { if (snap.exists()) setStatus(snap.val()); });
    const unsub2 = onValue(ref(db, 'device/control'), snap => { if (snap.exists()) setControl(snap.val()); });
    const unsub3 = onValue(ref(db, 'device/config'), snap => { if (snap.exists()) setConfig(snap.val()); });
    const unsub4 = onValue(ref(db, 'history'), snap => { if (snap.exists()) setHistory(snap.val()); });
    return () => { unsub1(); unsub2(); unsub3(); unsub4(); };
  }, [demoMode]);

  const toggleLight = () => {
    if (demoMode) { setControl(c => ({ ...c, manual_light: !c.manual_light })); setStatus(s => ({ ...s, light_on: !s.light_on })); return; }
    set(ref(db, 'device/control/manual_light'), !control.manual_light);
  };
  const setMode = (mode) => {
    if (demoMode) { setControl(c => ({ ...c, mode })); setStatus(s => ({ ...s, mode })); return; }
    set(ref(db, 'device/control/mode'), mode);
  };
  const updateConfig = (newConfig) => {
    if (demoMode) { setConfig(c => ({ ...c, ...newConfig })); return; }
    update(ref(db, 'device/config'), newConfig);
  };
  const switchMode = () => {
    const next = !demoMode;
    setDemoMode(next);
    if (next) { setStatus(mockStatus); setControl(mockControl); setConfig(mockConfig); setHistory(mockHistory); }
    else { setStatus(null); }
  };

  return (
    <div className="app">
      <header>
        <h1>🔆 Smart Street Light</h1>
        <nav>
          <button className={tab === 'dashboard' ? 'active' : ''} onClick={() => setTab('dashboard')}>Boshqaruv</button>
          <button className={tab === 'stats' ? 'active' : ''} onClick={() => setTab('stats')}>Statistika</button>
          <button className={demoMode ? 'demo-active' : 'demo'} onClick={switchMode}>{demoMode ? '🟡 Demo' : '🟢 Live'}</button>
        </nav>
      </header>
      <main>
        {tab === 'dashboard' ? (
          <Dashboard status={status} control={control} config={config} onToggleLight={toggleLight} onSetMode={setMode} onUpdateConfig={updateConfig} />
        ) : (
          <Statistics history={history} />
        )}
      </main>
    </div>
  );
}

export default App;
