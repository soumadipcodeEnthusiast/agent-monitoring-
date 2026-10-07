import React from 'react';

export default function Failures() {
  return (
    <div className="p-8">
      <h2 className="text-3xl font-bold mb-6 text-slate-800">Failure Patterns</h2>
      <div className="bg-white p-6 rounded shadow mb-6">
        <h3 className="text-xl font-semibold border-b pb-2 mb-4">First-Result Anchoring</h3>
        <p className="mb-2"><strong>Description:</strong> Agent repeatedly selects first search result despite contradictions.</p>
        <p className="mb-2"><strong>First discovered:</strong> Experiment #14</p>
        <p className="mb-2"><strong>Occurrences:</strong> 8</p>
        <p className="mb-2"><strong>Severity range:</strong> 0.61 - 0.83</p>
        <p className="mb-2"><strong>Recovery rate:</strong> 37%</p>
      </div>
    </div>
  );
}
