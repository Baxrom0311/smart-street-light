import { useState, useEffect } from 'react';
import { db } from '../firebase';
import { ref, onValue, query, limitToLast } from 'firebase/database';

export default function MotionLog({ demoMode }) {
  const [logs, setLogs] = useState([]);

  useEffect(() => {
    if (demoMode) {
      const mockLogs = Array.from({ length: 20 }, (_, i) => ({
        time: Date.now() - i * 60000 * (Math.random() * 5 + 1),
        distance: Math.floor(Math.random() * 150) + 10,
        light: Math.floor(Math.random() * 300)
      }));
      setLogs(mockLogs);
      return;
    }
    const logsRef = query(ref(db, 'motion_log'), limitToLast(50));
    const unsub = onValue(logsRef, snap => {
      if (!snap.exists()) return;
      const data = snap.val();
      const arr = Object.values(data).sort((a, b) => b.time - a.time);
      setLogs(arr);
    });
    return () => unsub();
  }, [demoMode]);

  const formatTime = (ts) => {
    const d = new Date(ts);
    return d.toLocaleTimeString('uz', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
  };

  return (
    <div className="motion-log">
      <div className="card">
        <h3>🚶 Harakat logi</h3>
        <div className="log-list">
          {logs.length === 0 && <p className="muted">Hali harakat yo'q</p>}
          {logs.map((log, i) => (
            <div key={i} className="log-item">
              <span className="log-time">{formatTime(log.time)}</span>
              <span className="log-detail">{log.distance}cm | {log.light} lux</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
