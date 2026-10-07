# Adaptive Failure Discovery Engine (AFDE)

An adaptive experimentation framework for discovering behavioral failure boundaries in tool-using AI agents.

## Problem & Motivation
Evaluating tool-using AI agents is challenging. Generic benchmarks often test capabilities under ideal conditions, but real-world deployment requires understanding *where* and *how* an agent fails.
Random or fixed testing of failure conditions (e.g., rate limits, bad tool outputs) is inefficient. We need a way to find meaningful failures quickly.

## Research Question
Can an adaptive testing strategy discover meaningful AI-agent failures using fewer experiments than random or fixed testing?

## Architecture
The system consists of:
- **Agent Interface**: A mockable interface for a research agent.
- **Perturbation System**: A plugin architecture for injecting failures (tool, info, instruction, environment, adversarial).
- **Adaptive Discovery Engine**: The core component that selects the next experiment based on expected failure probability, information gain, novelty, and uncertainty.
- **Failure Boundary Estimator**: Estimates the severity threshold where an agent transitions from success to failure.
- **Evaluation Module**: Calculates metrics like failure rate, discovery efficiency, and adaptive advantage.

## Adaptive Discovery Algorithm
The adaptive strategy observes previous agent behavior, proposes failure hypotheses, and selects new perturbations to maximize information gain and efficiently search the failure boundary.

## Baselines
- **Random Strategy**: Selects perturbations randomly.
- **Fixed Strategy**: Uses predefined test scenarios.
- **Adaptive Strategy**: Learns and targets likely failure regions.

## Setup & Running (Planned)
\`\`\`bash
# Install dependencies
cd backend && pip install -r requirements.txt
cd ../frontend && npm install

# Start services
docker-compose up -d postgres
uvicorn backend.app.main:app --reload
cd frontend && npm run dev
\`\`\`
# agent-monitoring-
