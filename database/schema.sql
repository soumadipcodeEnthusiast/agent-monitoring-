CREATE TABLE agents (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE hypotheses (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    category VARCHAR(255),
    confidence FLOAT,
    status VARCHAR(50)
);

CREATE TABLE failures (
    id SERIAL PRIMARY KEY,
    category VARCHAR(255),
    description TEXT
);

CREATE TABLE failure_patterns (
    id SERIAL PRIMARY KEY,
    failure_id INTEGER REFERENCES failures(id),
    severity_min FLOAT,
    severity_max FLOAT,
    recovery_rate FLOAT
);

CREATE TABLE experiments (
    id SERIAL PRIMARY KEY,
    agent_id INTEGER REFERENCES agents(id),
    hypothesis_id INTEGER REFERENCES hypotheses(id),
    perturbation_type VARCHAR(255),
    severity FLOAT,
    target_step VARCHAR(255),
    parameters JSONB,
    result JSONB,
    failure BOOLEAN,
    failure_probability FLOAT,
    information_gain FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE traces (
    id UUID PRIMARY KEY,
    experiment_id INTEGER REFERENCES experiments(id),
    task TEXT,
    started_at TIMESTAMP,
    completed_at TIMESTAMP,
    final_answer TEXT,
    success BOOLEAN
);

CREATE TABLE trace_steps (
    id UUID PRIMARY KEY,
    trace_id UUID REFERENCES traces(id),
    type VARCHAR(50),
    timestamp TIMESTAMP,
    input TEXT,
    output TEXT,
    tool VARCHAR(255),
    arguments JSONB,
    result JSONB,
    latency_ms INTEGER
);

CREATE TABLE evaluation_results (
    id SERIAL PRIMARY KEY,
    experiment_id INTEGER REFERENCES experiments(id),
    metrics JSONB
);
