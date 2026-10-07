import React, { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';

const dataCurve = [
  { exp: 10, Random: 2, Fixed: 4, Adaptive: 5 },
  { exp: 20, Random: 4, Fixed: 6, Adaptive: 12 },
  { exp: 30, Random: 6, Fixed: 8, Adaptive: 18 },
  { exp: 40, Random: 8, Fixed: 10, Adaptive: 25 },
  { exp: 50, Random: 10, Fixed: 12, Adaptive: 30 },
];

const boundaryData = [
  { severity: 0.1, prob: 0.05 },
  { severity: 0.3, prob: 0.1 },
  { severity: 0.5, prob: 0.2 },
  { severity: 0.6, prob: 0.45 },
  { severity: 0.7, prob: 0.8 },
  { severity: 0.9, prob: 0.95 },
];

const taxonomyData = [
  { name: 'Tool', value: 40 },
  { name: 'Information', value: 30 },
  { name: 'Instruction', value: 20 },
  { name: 'Planning', value: 10 },
];
const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];

export default function Dashboard() {
  return (
    <div className="p-8">
      <h2 className="text-3xl font-bold mb-6 text-slate-800">Research Dashboard</h2>
      
      <div className="grid grid-cols-4 gap-4 mb-8">
        <div className="bg-white p-4 rounded shadow">
          <div className="text-slate-500 text-sm">Experiments Executed</div>
          <div className="text-2xl font-bold">150</div>
        </div>
        <div className="bg-white p-4 rounded shadow">
          <div className="text-slate-500 text-sm">Failures Discovered</div>
          <div className="text-2xl font-bold">42</div>
        </div>
        <div className="bg-white p-4 rounded shadow">
          <div className="text-slate-500 text-sm">Average Failure Boundary</div>
          <div className="text-2xl font-bold">0.68</div>
        </div>
        <div className="bg-white p-4 rounded shadow">
          <div className="text-slate-500 text-sm">Adaptive Advantage</div>
          <div className="text-2xl font-bold text-emerald-600">2.1x</div>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-8 mb-8">
        <div className="bg-white p-6 rounded shadow">
          <h3 className="text-xl font-semibold mb-4">Failure Discovery Curve</h3>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={dataCurve}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="exp" label={{ value: 'Number of Experiments', position: 'insideBottom', offset: -5 }} />
                <YAxis label={{ value: 'Failures Discovered', angle: -90, position: 'insideLeft' }} />
                <Tooltip />
                <Legend verticalAlign="top" height={36}/>
                <Line type="monotone" dataKey="Random" stroke="#8884d8" />
                <Line type="monotone" dataKey="Fixed" stroke="#82ca9d" />
                <Line type="monotone" dataKey="Adaptive" stroke="#ff7300" strokeWidth={2} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="bg-white p-6 rounded shadow">
          <h3 className="text-xl font-semibold mb-4">Failure Boundary</h3>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={boundaryData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="severity" label={{ value: 'Severity', position: 'insideBottom', offset: -5 }} />
                <YAxis label={{ value: 'Probability of Failure', angle: -90, position: 'insideLeft' }} />
                <Tooltip />
                <Line type="monotone" dataKey="prob" stroke="#ef4444" strokeWidth={2} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-8">
        <div className="bg-white p-6 rounded shadow">
          <h3 className="text-xl font-semibold mb-4">Failure Taxonomy</h3>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie data={taxonomyData} cx="50%" cy="50%" outerRadius={80} fill="#8884d8" dataKey="value" label>
                  {taxonomyData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip />
                <Legend />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
}
