import { useState } from 'react';
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

export default function Statistics({ history }) {
  const [period, setPeriod] = useState('week');

  const allData = Object.entries(history || {})
    .sort(([a], [b]) => a.localeCompare(b))
    .map(([date, val]) => ({
      date: date.slice(5),
      energy_saved: val.energy_saved_percent || 0,
      motions: val.motions_count || 0,
      on_minutes: val.on_duration_min || 0
    }));

  const data = period === 'week' ? allData.slice(-7) : allData.slice(-1);

  if (allData.length === 0) {
    return <div className="card"><h3>📈 Statistika</h3><p className="muted">Ma'lumot hali yo'q. Qurilma ishlagandan keyin bu yerda statistika paydo bo'ladi.</p></div>;
  }

  const today = allData[allData.length - 1] || {};
  const avgSaved = allData.length > 0 ? Math.round(allData.reduce((s, d) => s + d.energy_saved, 0) / allData.length) : 0;
  const totalMotions = allData.reduce((s, d) => s + d.motions, 0);

  return (
    <div className="statistics">
      {/* Period toggle */}
      <div className="card" style={{ padding: '8px 16px' }}>
        <div className="mode-toggle" style={{ justifyContent: 'center' }}>
          <button className={period === 'week' ? 'active' : ''} onClick={() => setPeriod('week')}>Haftalik</button>
          <button className={period === 'today' ? 'active' : ''} onClick={() => setPeriod('today')}>Bugungi</button>
        </div>
      </div>

      {/* Summary Cards */}
      <div className="summary-grid">
        <div className="card summary-card green">
          <span className="summary-value">{period === 'today' ? today.energy_saved : avgSaved}%</span>
          <span className="summary-label">{period === 'today' ? 'Bugun tejash' : 'O\'rtacha tejash'}</span>
        </div>
        <div className="card summary-card blue">
          <span className="summary-value">{period === 'today' ? today.motions : totalMotions}</span>
          <span className="summary-label">{period === 'today' ? 'Bugun harakat' : 'Jami harakat'}</span>
        </div>
        <div className="card summary-card orange">
          <span className="summary-value">{period === 'today' ? today.on_minutes : allData.reduce((s, d) => s + d.on_minutes, 0)} min</span>
          <span className="summary-label">{period === 'today' ? 'Bugun yonish' : 'Jami yonish'}</span>
        </div>
      </div>

      {period === 'week' && (
        <>
          {/* Energy Savings Chart */}
          <div className="card chart-card">
            <h3>⚡ Energiya tejash (haftalik)</h3>
            <ResponsiveContainer width="100%" height={200}>
              <LineChart data={data}>
                <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
                <XAxis dataKey="date" stroke="#94a3b8" />
                <YAxis unit="%" stroke="#94a3b8" />
                <Tooltip contentStyle={{ background: '#1e293b', border: 'none', borderRadius: 8 }} />
                <Line type="monotone" dataKey="energy_saved" stroke="#10b981" strokeWidth={2} dot={{ fill: '#10b981' }} name="Tejash %" />
              </LineChart>
            </ResponsiveContainer>
          </div>

          {/* Motion Count Chart */}
          <div className="card chart-card">
            <h3>🚶 Harakatlar soni (haftalik)</h3>
            <ResponsiveContainer width="100%" height={200}>
              <BarChart data={data}>
                <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
                <XAxis dataKey="date" stroke="#94a3b8" />
                <YAxis stroke="#94a3b8" />
                <Tooltip contentStyle={{ background: '#1e293b', border: 'none', borderRadius: 8 }} />
                <Bar dataKey="motions" fill="#3b82f6" radius={[4, 4, 0, 0]} name="Harakatlar" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </>
      )}

      {period === 'today' && (
        <div className="card chart-card">
          <h3>📊 Bugungi xulosa</h3>
          <div className="today-summary">
            <div className="today-item">
              <div className="today-bar" style={{ height: `${today.energy_saved}%`, background: 'var(--green)' }}></div>
              <span>Tejash</span>
            </div>
            <div className="today-item">
              <div className="today-bar" style={{ height: `${Math.min(100, today.motions)}%`, background: 'var(--accent)' }}></div>
              <span>Harakat</span>
            </div>
            <div className="today-item">
              <div className="today-bar" style={{ height: `${Math.min(100, today.on_minutes / 3)}%`, background: 'var(--orange)' }}></div>
              <span>Yonish</span>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
