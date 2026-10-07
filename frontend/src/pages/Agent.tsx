import React from 'react';

export default function Agent() {
  return (
    <div className="p-8">
      <h2 className="text-3xl font-bold mb-6 text-slate-800">Research Evaluation Mode</h2>
      <div className="bg-white p-6 rounded shadow max-w-2xl">
        <form className="space-y-4">
          <div>
            <label className="block mb-1 font-semibold">Agent</label>
            <select className="w-full border p-2 rounded">
              <option>Research Assistant Mock</option>
            </select>
          </div>
          <div>
            <label className="block mb-1 font-semibold">Strategy</label>
            <select className="w-full border p-2 rounded">
              <option>Adaptive</option>
              <option>Fixed</option>
              <option>Random</option>
            </select>
          </div>
          <div>
            <label className="block mb-1 font-semibold">Number of Experiments</label>
            <input type="number" defaultValue={50} className="w-full border p-2 rounded" />
          </div>
          <div>
            <label className="block mb-1 font-semibold">Random Seed</label>
            <input type="number" defaultValue={42} className="w-full border p-2 rounded" />
          </div>
          <div>
            <label className="block mb-1 font-semibold">Maximum Severity (0-1.0)</label>
            <input type="number" step="0.1" defaultValue={1.0} className="w-full border p-2 rounded" />
          </div>
          <button type="button" className="bg-blue-600 text-white px-4 py-2 rounded font-semibold hover:bg-blue-700">
            Run Evaluation
          </button>
        </form>
      </div>
    </div>
  );
}
