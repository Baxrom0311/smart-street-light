import { useState } from 'react';

export default function Dashboard({ status, control, config, onToggleLight, onSetMode, onUpdateConfig, onUpdateControl, demoMode }) {
  const [showSettings, setShowSettings] = useState(false);
  const [tempConfig, setTempConfig] = useState(config);

  if (!status) return <div className="loading">Qurilma ulanishini kutmoqda...</div>;

  const formatTime = (seconds) => {
    const h = Math.floor(seconds / 3600);
    const m = Math.floor((seconds % 3600) / 60);
    return `${h}s ${m}d`;
  };

  const saveConfig = () => { onUpdateConfig(tempConfig); setShowSettings(false); };

  const colors = [
    { name: 'Oq', value: '#ffffff' },
    { name: 'Issiq', value: '#ffaa33' },
    { name: 'Ko\'k', value: '#3388ff' },
    { name: 'Yashil', value: '#33ff88' },
    { name: 'Qizil', value: '#ff3333' },
  ];

  return (
    <div className="dashboard">
      {/* Light Status */}
      <div className={`card light-card ${status.light_on ? 'on' : 'off'}`}>
        <div className="light-icon">{status.light_on ? '💡' : '🌑'}</div>
        <h2>{status.light_on ? 'Chiroq YONIQ' : 'Chiroq O\'CHIQ'}</h2>
        <p className="mode-badge">{control.mode === 'auto' ? '🤖 Avtomatik' : control.mode === 'schedule' ? '📅 Jadval' : '🖐 Qo\'lda'}</p>
      </div>

      {/* Control */}
      <div className="card control-card">
        <h3>Boshqaruv</h3>
        <div className="control-row">
          <span>Rejim:</span>
          <div className="mode-toggle">
            <button className={control.mode === 'auto' ? 'active' : ''} onClick={() => onSetMode('auto')}>Auto</button>
            <button className={control.mode === 'manual' ? 'active' : ''} onClick={() => onSetMode('manual')}>Manual</button>
            <button className={control.mode === 'schedule' ? 'active' : ''} onClick={() => onSetMode('schedule')}>Jadval</button>
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
        {control.mode === 'schedule' && (
          <div className="schedule-section">
            <div className="control-row">
              <span>Yoqish:</span>
              <input type="time" value={control.schedule_on || '18:00'} onChange={e => onUpdateControl({ schedule_on: e.target.value })} />
            </div>
            <div className="control-row">
              <span>O'chirish:</span>
              <input type="time" value={control.schedule_off || '06:00'} onChange={e => onUpdateControl({ schedule_off: e.target.value })} />
            </div>
          </div>
        )}
      </div>

      {/* LED Color & Brightness */}
      <div className="card">
        <h3>🎨 LED sozlamalari</h3>
        <div className="control-row">
          <span>Rang:</span>
          <div className="color-picker">
            {colors.map(c => (
              <button key={c.value} className={`color-btn ${control.led_color === c.value ? 'selected' : ''}`}
                style={{ background: c.value }} onClick={() => onUpdateControl({ led_color: c.value })} title={c.name} />
            ))}
          </div>
        </div>
        <div className="control-row">
          <span>Yorug'lik: {control.brightness || 100}%</span>
        </div>
        <input type="range" min="10" max="100" value={control.brightness || 100}
          onChange={e => onUpdateControl({ brightness: +e.target.value })} className="brightness-slider" />
      </div>

      {/* Sensors */}
      <div className="card sensor-card">
        <h3>📡 Sensorlar</h3>
        <div className="sensor-grid">
          <div className="sensor-item">
            <span className="sensor-label">Masofa</span>
            <span className="sensor-value">{status.distance_cm} cm</span>
            <span className="sensor-status">{status.motion_detected ? '🚶 Harakat' : '— Tinch'}</span>
          </div>
          <div className="sensor-item">
            <span className="sensor-label">Yorug'lik</span>
            <span className="sensor-value">{status.ambient_light}</span>
            <span className="sensor-status">{status.ambient_light < (config.light_threshold || 300) ? '🌙 Tun' : '☀️ Kunduz'}</span>
          </div>
        </div>
      </div>

      {/* Status */}
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
        <h3 onClick={() => { setTempConfig(config); setShowSettings(!showSettings); }} style={{ cursor: 'pointer' }}>
          ⚙️ Sozlamalar {showSettings ? '▲' : '▼'}
        </h3>
        {showSettings && (
          <div className="settings">
            <label>Timeout (soniya): <input type="number" value={tempConfig.timeout_sec} onChange={e => setTempConfig({ ...tempConfig, timeout_sec: +e.target.value })} /></label>
            <label>Yorug'lik chegarasi: <input type="number" value={tempConfig.light_threshold} onChange={e => setTempConfig({ ...tempConfig, light_threshold: +e.target.value })} /></label>
            <label>Masofa chegarasi (cm): <input type="number" value={tempConfig.distance_threshold} onChange={e => setTempConfig({ ...tempConfig, distance_threshold: +e.target.value })} /></label>
            <button className="save-btn" onClick={saveConfig}>Saqlash</button>
          </div>
        )}
      </div>
    </div>
  );
}
