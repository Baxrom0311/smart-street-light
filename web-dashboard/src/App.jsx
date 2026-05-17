import { useState, useEffect } from 'react';
import { db, auth } from './firebase';
import { ref, onValue, set, update } from 'firebase/database';
import { onAuthStateChanged, signInWithEmailAndPassword, signOut } from 'firebase/auth';
import { mockStatus, mockControl, mockConfig, mockHistory } from './mockData';
import Dashboard from './components/Dashboard';
import Statistics from './components/Statistics';
import MotionLog from './components/MotionLog';
import './App.css';

function App() {
  const [user, setUser] = useState(null);
  const [authLoading, setAuthLoading] = useState(true);
  const [status, setStatus] = useState(mockStatus);
  const [control, setControl] = useState(mockControl);
  const [config, setConfig] = useState(mockConfig);
  const [history, setHistory] = useState(mockHistory);
  const [tab, setTab] = useState('home');
  const [isLive, setIsLive] = useState(false);

  useEffect(() => {
    const unsub = onAuthStateChanged(auth, u => { setUser(u); setAuthLoading(false); });
    return unsub;
  }, []);

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

  if (authLoading) return <div className="app center"><div className="spinner"></div></div>;
  if (!user) return <Login />;

  return (
    <div className="app">
      <aside className="sidebar">
        <div className="sidebar-brand">
          <span className="brand-icon">💡</span>
          <span className="brand-text">Smart Light</span>
        </div>
        <nav className="sidebar-nav">
          <button className={tab === 'home' ? 'active' : ''} onClick={() => setTab('home')}>
            <span className="nav-icon">🏠</span><span className="nav-text">Boshqaruv</span>
          </button>
          <button className={tab === 'stats' ? 'active' : ''} onClick={() => setTab('stats')}>
            <span className="nav-icon">📊</span><span className="nav-text">Statistika</span>
          </button>
          <button className={tab === 'log' ? 'active' : ''} onClick={() => setTab('log')}>
            <span className="nav-icon">📋</span><span className="nav-text">Log</span>
          </button>
          <button className={tab === 'settings' ? 'active' : ''} onClick={() => setTab('settings')}>
            <span className="nav-icon">⚙️</span><span className="nav-text">Sozlama</span>
          </button>
        </nav>
        <div className="sidebar-footer">
          <div className="user-info">
            <div className="user-avatar">{user.email?.[0]?.toUpperCase()}</div>
            <span className="user-email">{user.email}</span>
          </div>
          <button className="logout-btn" onClick={() => signOut(auth)}>Chiqish</button>
        </div>
      </aside>

      <div className="main-area">
        <header className="topbar">
          <h1>{tab === 'home' ? 'Boshqaruv paneli' : tab === 'stats' ? 'Statistika' : tab === 'log' ? 'Harakat logi' : 'Sozlamalar'}</h1>
          <button className={`live-toggle ${isLive ? 'live' : 'demo'}`} onClick={() => setIsLive(!isLive)}>
            <span className="live-dot"></span>
            {isLive ? 'Live' : 'Demo'}
          </button>
        </header>

        <main className="content">
          {tab === 'home' && <Dashboard status={status} control={control} config={config} onToggleLight={toggleLight} onSetMode={setMode} />}
          {tab === 'stats' && <Statistics history={history} />}
          {tab === 'log' && <MotionLog demoMode={!isLive} />}
          {tab === 'settings' && <Settings config={config} control={control} onUpdateConfig={updateConfig} onUpdateControl={updateControl} />}
        </main>
      </div>

      {/* Mobile bottom nav */}
      <nav className="bottom-nav">
        <button className={tab === 'home' ? 'active' : ''} onClick={() => setTab('home')}>
          <span className="nav-icon">🏠</span><span className="nav-label">Bosh</span>
        </button>
        <button className={tab === 'stats' ? 'active' : ''} onClick={() => setTab('stats')}>
          <span className="nav-icon">📊</span><span className="nav-label">Statistika</span>
        </button>
        <button className={tab === 'log' ? 'active' : ''} onClick={() => setTab('log')}>
          <span className="nav-icon">📋</span><span className="nav-label">Log</span>
        </button>
        <button className={tab === 'settings' ? 'active' : ''} onClick={() => setTab('settings')}>
          <span className="nav-icon">⚙️</span><span className="nav-label">Sozlama</span>
        </button>
      </nav>
    </div>
  );
}

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      await signInWithEmailAndPassword(auth, email, password);
    } catch (err) {
      setError(err.code === 'auth/invalid-credential' ? 'Email yoki parol noto\'g\'ri' : 'Xatolik yuz berdi');
    }
    setLoading(false);
  };

  return (
    <div className="login-page">
      <div className="login-container">
        <div className="login-hero">
          <div className="hero-icon">💡</div>
          <h1>Smart Street Light</h1>
          <p>IoT energiya tejamkor yoritish tizimi</p>
        </div>
        <form className="login-form" onSubmit={handleLogin}>
          <h2>Tizimga kirish</h2>
          <div className="input-group">
            <label>Email</label>
            <input type="email" value={email} onChange={e => setEmail(e.target.value)} placeholder="email@example.com" required />
          </div>
          <div className="input-group">
            <label>Parol</label>
            <input type="password" value={password} onChange={e => setPassword(e.target.value)} placeholder="••••••••" required />
          </div>
          {error && <p className="error-msg">{error}</p>}
          <button type="submit" className="btn-primary" disabled={loading}>{loading ? 'Kirmoqda...' : 'Kirish'}</button>
        </form>
      </div>
    </div>
  );
}

function Settings({ config, control, onUpdateConfig, onUpdateControl }) {
  const [tempConfig, setTempConfig] = useState(config);
  const [saved, setSaved] = useState(false);

  useEffect(() => { setTempConfig(config); }, [config]);

  const handleSave = () => {
    onUpdateConfig(tempConfig);
    setSaved(true);
    setTimeout(() => setSaved(false), 2000);
  };

  return (
    <div className="settings-page">
      <div className="settings-section">
        <h3>Qurilma sozlamalari</h3>
        <div className="setting-item"><label>Harakat timeout</label><div className="setting-value"><input type="number" value={tempConfig.timeout_sec} onChange={e => setTempConfig({ ...tempConfig, timeout_sec: +e.target.value })} /><span>s</span></div></div>
        <div className="setting-item"><label>Yorug'lik chegarasi</label><div className="setting-value"><input type="number" value={tempConfig.light_threshold} onChange={e => setTempConfig({ ...tempConfig, light_threshold: +e.target.value })} /><span>lux</span></div></div>
        <div className="setting-item"><label>Aniqlash masofasi</label><div className="setting-value"><input type="number" value={tempConfig.distance_threshold} onChange={e => setTempConfig({ ...tempConfig, distance_threshold: +e.target.value })} /><span>cm</span></div></div>
        <button className="btn-primary" onClick={handleSave}>{saved ? '✓ Saqlandi!' : 'Saqlash'}</button>
      </div>
      <div className="settings-section">
        <h3>Jadval rejimi</h3>
        <div className="setting-item"><label>Yoqish</label><input type="time" value={control.schedule_on || '18:00'} onChange={e => onUpdateControl({ schedule_on: e.target.value })} /></div>
        <div className="setting-item"><label>O'chirish</label><input type="time" value={control.schedule_off || '06:00'} onChange={e => onUpdateControl({ schedule_off: e.target.value })} /></div>
      </div>
      <div className="settings-section">
        <h3>Haqida</h3>
        <p className="about-text">Smart Street Light IoT v6.0</p>
        <p className="about-text">Diplom ishi — Baxrom, 2026</p>
      </div>
    </div>
  );
}

export default App;
