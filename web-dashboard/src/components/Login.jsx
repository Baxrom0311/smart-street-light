import { useState } from 'react';
import { auth } from '../firebase';
import { signInWithEmailAndPassword } from 'firebase/auth';

export default function Login() {
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
      setError(err.code === 'auth/invalid-credential' ? 'Email yoki parol noto\'g\'ri' : err.message);
    }
    setLoading(false);
  };

  return (
    <div className="login-page">
      <div className="login-card">
        <div className="login-icon">🔆</div>
        <h2>Smart Street Light</h2>
        <p className="login-subtitle">Tizimga kirish</p>
        <form onSubmit={handleLogin}>
          <input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} required />
          <input type="password" placeholder="Parol" value={password} onChange={e => setPassword(e.target.value)} required />
          {error && <p className="login-error">{error}</p>}
          <button type="submit" disabled={loading}>{loading ? 'Kirmoqda...' : 'Kirish'}</button>
        </form>
      </div>
    </div>
  );
}
