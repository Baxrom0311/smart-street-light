import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

export default function Statistics({ history }) {
  const data = Object.entries(history || {})
    .sort(([a], [b]) => a.localeCompare(b))
    .slice(-7)
    .map(([date, val]) => ({
      date: date.slice(5), // MM-DD
      energy_saved: val.energy_saved_percent || 0,
      motions: val.motions_count || 0,
      on_minutes: val.on_duration_min || 0
    }));

  if (data.length === 0) {
    return <div className="card"><h3>📈 Statistika</h3><p>Ma'lumot hali yo'q. Qurilma ishlagandan keyin bu yerda statistika paydo bo'ladi.</p></div>;
  }

  const today = data[data.length - 1] || {};

  return (
    <div className="statistics">
      {/* Summary Cards */}
      <div className="summary-grid">
        <div className="card summary-card green">
          <span className="summary-value">{today.energy_saved}%</span>
          <span className="summary-label">Bugungi tejash</span>
        </div>
        <div className="card summary-card blue">
          <span className="summary-value">{today.motions}</span>
          <span className="summary-label">Harakatlar</span>
        </div>
        <div className="card summary-card orange">
          <span className="summary-value">{today.on_minutes} min</span>
          <span className="summary-label">Yonish vaqti</span>
        </div>
      </div>

      {/* Energy Savings Chart */}
      <div className="card chart-card">
        <h3>⚡ Energiya tejash (haftalik)</h3>
        <ResponsiveContainer width="100%" height={200}>
          <LineChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="date" />
            <YAxis unit="%" />
            <Tooltip />
            <Line type="monotone" dataKey="energy_saved" stroke="#10b981" strokeWidth={2} name="Tejash %" />
          </LineChart>
        </ResponsiveContainer>
      </div>

      {/* Motion Count Chart */}
      <div className="card chart-card">
        <h3>🚶 Harakatlar soni (haftalik)</h3>
        <ResponsiveContainer width="100%" height={200}>
          <BarChart data={data}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="date" />
            <YAxis />
            <Tooltip />
            <Bar dataKey="motions" fill="#3b82f6" name="Harakatlar" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
