# 5. Orchestrator-Worker

!!! example "Mini-Project: Competitive Intelligence Report Generator"
    An orchestrator that dynamically plans and dispatches research workers to gather and synthesize competitive intelligence on companies.

    [View on GitHub :material-github:](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/05-competitive-intelligence-report-generator.ipynb){ .md-button .md-button--primary }

---

## Description

In the **Orchestrator-Worker** pattern, a central orchestrator LLM dynamically breaks down a task into subtasks, delegates them to worker LLMs, and synthesizes their results. Unlike Parallelization (where subtasks are pre-defined), the orchestrator **dynamically determines** what subtasks are needed based on the specific input.

## When to Use

- Complex tasks where subtasks cannot be predicted in advance
- Coding tasks that require changes across multiple files
- Research tasks that need adaptive exploration strategies
- When the decomposition itself requires intelligence

## Benefits

| Benefit | Description |
|---|---|
| **Adaptability** | Subtask decomposition is dynamic, not hardcoded |
| **Scalability** | Can spawn as many workers as needed |
| **Intelligence** | Orchestrator applies reasoning to task breakdown |
| **Synthesis** | Final output integrates all worker contributions |

## Architecture Diagram

```mermaid
flowchart TD
    A[User Input] --> B[Orchestrator LLM]
    B -->|Plan & Delegate| C[Worker 1]
    B -->|Plan & Delegate| D[Worker 2]
    B -->|Plan & Delegate| E[Worker N]
    C --> F[Results]
    D --> F
    E --> F
    F --> B
    B -->|Synthesize| G[Final Output]

    style A fill:#4CAF50,color:#fff
    style B fill:#FF5722,color:#fff
    style C fill:#2196F3,color:#fff
    style D fill:#9C27B0,color:#fff
    style E fill:#00BCD4,color:#fff
    style F fill:#FFC107,color:#000
    style G fill:#4CAF50,color:#fff
```
