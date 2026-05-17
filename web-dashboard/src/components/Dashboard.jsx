import { useState, useEffect, useRef } from 'react';

export default function Dashboard({ status, control, onToggleLight, onSetMode, config }) {
  const [optimisticLight, setOptimisticLight] = useState(null);
  const [syncing, setSyncing] = useState(false);
  const syncTimer = useRef(null);

  // Server tasdiqlasa — optimistic holatni tozalash
  useEffect(() => {
    if (optimisticLight !== null && status?.light_on === optimisticLight) {
      setOptimisticLight(null);
      setSyncing(false);
      clearTimeout(syncTimer.current);
    }
  }, [status?.light_on, optimisticLight]);

  const handleToggle = () => {
    const newState = !displayLight;
    setOptimisticLight(newState);
    setSyncing(true);
    onToggleLight();

    // 5s ichida server javob bermasa — rollback
    syncTimer.current = setTimeout(() => {
      setOptimisticLight(null);
      setSyncing(false);
    }, 5000);
  };

  const handleMode = (mode) => {
    onSetMode(mode);
  };

  if (!status) return <div className="empty-state">Qurilma ulanishini kutmoqda...</div>;

  const displayLight = optimisticLight !== null ? optimisticLight : status.light_on;

  const formatUptime = (s) => {
    const h = Math.floor(s / 3600);
    const m = Math.floor((s % 3600) / 60);
    return h > 0 ? `${h}s ${m}d` : `${m} daqiqa`;
  };

  return (
    <div className="dashboard">
      {/* Main Power Card */}
      <div className={`power-card ${displayLight ? 'on' : 'off'}`}>
        <div className="power-visual">
          <button className={`power-btn ${syncing ? 'syncing' : ''}`} onClick={handleToggle} disabled={control.mode === 'auto'}>
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M18.36 6.64a9 9 0 1 1-12.73 0M12 2v10" strokeLinecap="round"/>
            </svg>
          </button>
        </div>
        <div className="power-status">
          <h2>{displayLight ? 'Yoniq' : 'O\'chiq'}</h2>
          <p className="power-mode">
            {syncing && <span className="sync-badge">Sinxronlanmoqda...</span>}
            {!syncing && (control.mode === 'auto' ? 'Avtomatik rejim' : control.mode === 'schedule' ? 'Jadval rejimi' : 'Qo\'lda boshqaruv')}
          </p>
        </div>
      </div>

      {/* Mode Selector */}
      <div className="card mode-card">
        <div className="mode-buttons">
          <button className={control.mode === 'auto' ? 'active' : ''} onClick={() => handleMode('auto')}>
            <span>🤖</span> Avto
          </button>
          <button className={control.mode === 'manual' ? 'active' : ''} onClick={() => handleMode('manual')}>
            <span>🖐</span> Qo'lda
          </button>
          <button className={control.mode === 'schedule' ? 'active' : ''} onClick={() => handleMode('schedule')}>
            <span>📅</span> Jadval
          </button>
        </div>
      </div>

      {/* Sensor Info */}
      <div className="card">
        <div className="info-grid">
          <div className="info-item">
            <div className="info-icon">📏</div>
            <div className="info-data">
              <span className="info-value">{status.distance_cm === 999 ? '—' : status.distance_cm + ' cm'}</span>
              <span className="info-label">{status.motion_detected ? '🚶 Harakat bor' : 'Tinch'}</span>
            </div>
          </div>
          <div className="info-item">
            <div className="info-icon">{status.ambient_light < (config.light_threshold || 300) ? '🌙' : '☀️'}</div>
            <div className="info-data">
              <span className="info-value">{status.ambient_light}</span>
              <span className="info-label">{status.ambient_light < (config.light_threshold || 300) ? 'Qorong\'u' : 'Yorug\''}</span>
            </div>
          </div>
          <div className="info-item">
            <div className="info-icon">📶</div>
            <div className="info-data">
              <span className="info-value">{status.wifi_rssi} dBm</span>
              <span className="info-label">WiFi signal</span>
            </div>
          </div>
          <div className="info-item">
            <div className="info-icon">⏱</div>
            <div className="info-data">
              <span className="info-value">{formatUptime(status.uptime)}</span>
              <span className="info-label">Ishlash vaqti</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
