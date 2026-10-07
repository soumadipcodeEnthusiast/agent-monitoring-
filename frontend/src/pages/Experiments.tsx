import React from 'react';

export default function Experiments() {
  return (
    <div className="p-8">
      <h2 className="text-3xl font-bold mb-6 text-slate-800">Experiments Timeline</h2>
      <div className="bg-white rounded shadow p-6">
        <table className="w-full text-left">
          <thead>
            <tr className="border-b">
              <th className="py-2">ID</th>
              <th>Task</th>
              <th>Perturbation</th>
              <th>Severity</th>
              <th>Status</th>
              <th>Selection Score</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b">
              <td className="py-3">Exp-142</td>
              <td>Search for current paper...</td>
              <td>timeout</td>
              <td>0.72</td>
              <td><span className="text-red-500 font-semibold">Failed</span></td>
              <td>
                <div className="text-sm">Score: 0.69</div>
                <div className="text-xs text-slate-500">Exp. Fail: 0.72, Info Gain: 0.81</div>
              </td>
            </tr>
            <tr>
              <td className="py-3">Exp-141</td>
              <td>Summarize doc 45...</td>
              <td>stale_data</td>
              <td>0.45</td>
              <td><span className="text-green-500 font-semibold">Success</span></td>
              <td>
                <div className="text-sm">Score: 0.51</div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}
