import { useState } from 'react';

export default function Dashboard({ status, control, config, onToggleLight, onSetMode, onUpdateConfig }) {
  const [showSettings, setShowSettings] = useState(false);
  const [tempConfig, setTempConfig] = useState(config);

  if (!status) return <div className="loading">Qurilma ulanishini kutmoqda...</div>;

  const formatTime = (seconds) => {
    const h = Math.floor(seconds / 3600);
    const m = Math.floor((seconds % 3600) / 60);
    return `${h}s ${m}d`;
  };

  const saveConfig = () => {
    onUpdateConfig(tempConfig);
    setShowSettings(false);
  };

  return (
    <div className="dashboard">
      {/* Light Status Card */}
      <div className={`card light-card ${status.light_on ? 'on' : 'off'}`}>
        <div className="light-icon">{status.light_on ? '💡' : '🌑'}</div>
        <h2>{status.light_on ? 'Chiroq YONIQ' : 'Chiroq O\'CHIQ'}</h2>
        <p className="mode-badge">{control.mode === 'auto' ? '🤖 Avtomatik' : '🖐 Qo\'lda'}</p>
      </div>

      {/* Control Card */}
      <div className="card control-card">
        <h3>Boshqaruv</h3>
        <div className="control-row">
          <span>Rejim:</span>
          <div className="mode-toggle">
            <button className={control.mode === 'auto' ? 'active' : ''} onClick={() => onSetMode('auto')}>Auto</button>
            <button className={control.mode === 'manual' ? 'active' : ''} onClick={() => onSetMode('manual')}>Manual</button>
          </div>
        </div>
        {control.mode === 'manual' && (
          <div className="control-row">
            <span>Chiroq:</span>
            <label className="switch">
              <input type="checkbox" checked={control.manual_light} onChange={onToggleLight} />
              <span className="slider"></span>
            </label>
          </div>
        )}
      </div>

      {/* Sensor Cards */}
      <div className="card sensor-card">
        <h3>📡 Sensorlar</h3>
        <div className="sensor-grid">
          <div className="sensor-item">
            <span className="sensor-label">Masofa</span>
            <span className="sensor-value">{status.distance_cm} cm</span>
            <span className="sensor-status">{status.motion_detected ? '🚶 Harakat bor' : '— Tinch'}</span>
          </div>
          <div className="sensor-item">
            <span className="sensor-label">Yorug'lik</span>
            <span className="sensor-value">{status.ambient_light}</span>
            <span className="sensor-status">{status.ambient_light < config.light_threshold ? '🌙 Tun' : '☀️ Kunduz'}</span>
          </div>
        </div>
      </div>

      {/* Status Card */}
      <div className="card status-card">
        <h3>📊 Holat</h3>
        <div className="status-grid">
          <div><span>WiFi:</span><span>{status.wifi_rssi} dBm</span></div>
          <div><span>Uptime:</span><span>{formatTime(status.uptime)}</span></div>
          <div><span>Oxirgi harakat:</span><span>{status.last_motion ? new Date(status.last_motion * 1000).toLocaleTimeString() : '—'}</span></div>
        </div>
      </div>

      {/* Settings */}
      <div className="card">
        <h3 onClick={() => { setTempConfig(config); setShowSettings(!showSettings); }} style={{cursor:'pointer'}}>
          ⚙️ Sozlamalar {showSettings ? '▲' : '▼'}
        </h3>
        {showSettings && (
          <div className="settings">
            <label>Timeout (soniya): <input type="number" value={tempConfig.timeout_sec} onChange={e => setTempConfig({...tempConfig, timeout_sec: +e.target.value})} /></label>
            <label>Yorug'lik chegarasi: <input type="number" value={tempConfig.light_threshold} onChange={e => setTempConfig({...tempConfig, light_threshold: +e.target.value})} /></label>
            <label>Masofa chegarasi (cm): <input type="number" value={tempConfig.distance_threshold} onChange={e => setTempConfig({...tempConfig, distance_threshold: +e.target.value})} /></label>
            <button className="save-btn" onClick={saveConfig}>Saqlash</button>
          </div>
        )}
      </div>
    </div>
  );
}
