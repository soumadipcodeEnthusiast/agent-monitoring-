import React from 'react';

export default function Hypotheses() {
  return (
    <div className="p-8">
      <h2 className="text-3xl font-bold mb-6 text-slate-800">Hypothesis Board</h2>
      <div className="grid grid-cols-3 gap-6">
        <div className="bg-white p-4 rounded shadow border-t-4 border-yellow-400">
          <h4 className="font-semibold mb-2">Testing</h4>
          <div className="bg-slate-50 p-3 rounded mb-2 border">
            Agent fails to recover from successive tool timeouts > 2.
          </div>
        </div>
        <div className="bg-white p-4 rounded shadow border-t-4 border-green-500">
          <h4 className="font-semibold mb-2">Supported</h4>
          <div className="bg-slate-50 p-3 rounded mb-2 border">
            Agent exhibits first-result anchoring when context is long.
          </div>
        </div>
        <div className="bg-white p-4 rounded shadow border-t-4 border-red-500">
          <h4 className="font-semibold mb-2">Rejected</h4>
          <div className="bg-slate-50 p-3 rounded mb-2 border">
            Agent cannot handle XML formatted instructions.
          </div>
        </div>
      </div>
    </div>
  );
}
