const mockStatus = {
  light_on: true,
  motion_detected: true,
  distance_cm: 85,
  ambient_light: 120,
  mode: 'auto',
  last_motion: Math.floor(Date.now() / 1000) - 15,
  uptime: 7265,
  wifi_rssi: -42
};

const mockControl = { mode: 'auto', manual_light: false };
const mockConfig = { timeout_sec: 30, light_threshold: 300, distance_threshold: 200 };

const today = new Date();
const mockHistory = {};
for (let i = 6; i >= 0; i--) {
  const d = new Date(today);
  d.setDate(d.getDate() - i);
  const key = d.toISOString().slice(0, 10);
  mockHistory[key] = {
    motions_count: Math.floor(Math.random() * 80) + 20,
    on_duration_min: Math.floor(Math.random() * 180) + 60,
    energy_saved_percent: Math.floor(Math.random() * 30) + 55
  };
}

export { mockStatus, mockControl, mockConfig, mockHistory };
