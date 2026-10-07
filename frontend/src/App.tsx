import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Experiments from './pages/Experiments';
import Failures from './pages/Failures';
import Hypotheses from './pages/Hypotheses';
import Agent from './pages/Agent';

function App() {
  return (
    <Router>
      <div className="flex h-screen bg-slate-50">
        <aside className="w-64 bg-slate-900 text-white p-6">
          <h1 className="text-2xl font-bold mb-8">AFDE</h1>
          <nav className="space-y-4">
            <Link to="/" className="block hover:text-slate-300">Dashboard</Link>
            <Link to="/experiments" className="block hover:text-slate-300">Experiments</Link>
            <Link to="/failures" className="block hover:text-slate-300">Failures</Link>
            <Link to="/hypotheses" className="block hover:text-slate-300">Hypotheses</Link>
            <Link to="/agent" className="block hover:text-slate-300">Research Mode</Link>
          </nav>
        </aside>
        <main className="flex-1 overflow-y-auto">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/experiments" element={<Experiments />} />
            <Route path="/failures" element={<Failures />} />
            <Route path="/hypotheses" element={<Hypotheses />} />
            <Route path="/agent" element={<Agent />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
