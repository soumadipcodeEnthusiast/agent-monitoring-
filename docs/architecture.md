# Architecture

AFDE is divided into a FastAPI backend and a React/Vite frontend.

## Components
- **API Routes**: RESTful interface.
- **Agents**: Interfaces and mock implementations of the test subjects.
- **Discovery**: Engine and strategies (Random, Fixed, Adaptive).
- **Perturbations**: Fault injection modules.
- **Evaluation**: Analyzes agent traces.
- **Tracing**: Records step-by-step execution.
