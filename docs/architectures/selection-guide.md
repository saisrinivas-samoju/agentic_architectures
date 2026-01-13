# Architecture Selection Guide

Use this decision framework to pick the right architecture for your use case.

## Decision Flowchart

```mermaid
flowchart TD
    A[Start: What's your task?] --> B{Single domain?}
    B -->|Yes| C{Needs tools?}
    C -->|No| D[Prompt Chaining]
    C -->|Yes| E{Self-improvement needed?}
    E -->|No| F[Single Agent - ReAct]
    E -->|Yes| G{Quantifiable criteria?}
    G -->|Yes| H[Evaluator-Optimizer]
    G -->|No| I[Reflection]

    B -->|No| J{How many domains?}
    J -->|2-3| K{Central control needed?}
    K -->|Yes| L[Supervisor]
    K -->|No| M{Conversational handoffs?}
    M -->|Yes| N[Swarm]
    M -->|No| O[Routing]

    J -->|4+| P{Predictable subtasks?}
    P -->|Yes| Q[Parallelization]
    P -->|No| R{Many agents?}
    R -->|Yes| S[Hierarchical Teams]
    R -->|No| T[Orchestrator-Worker]

    style A fill:#4CAF50,color:#fff
    style D fill:#2196F3,color:#fff
    style F fill:#2196F3,color:#fff
    style H fill:#2196F3,color:#fff
    style I fill:#2196F3,color:#fff
    style L fill:#2196F3,color:#fff
    style N fill:#2196F3,color:#fff
    style O fill:#2196F3,color:#fff
    style Q fill:#2196F3,color:#fff
    style S fill:#2196F3,color:#fff
    style T fill:#2196F3,color:#fff
```

## Quick Reference Table

| Architecture | Complexity | Agents | Best For |
|---|---|---|---|
| [ReAct](single-agent.md) | Low | 1 | Simple tool-augmented tasks |
| [Prompt Chaining](prompt-chaining.md) | Low | 1 | Sequential multi-step pipelines |
| [Routing](routing.md) | Low-Medium | 1 + N handlers | Multi-domain classification |
| [Parallelization](parallelization.md) | Medium | N parallel | Independent concurrent subtasks |
| [Orchestrator-Worker](orchestrator-worker.md) | Medium-High | 1 + N dynamic | Complex tasks, unpredictable decomposition |
| [Supervisor](supervisor.md) | Medium-High | 1 + N managed | Coordinated multi-agent with central control |
| [Reflection](reflection.md) | Medium | 1-2 | Self-improving output quality |
| [Evaluator-Optimizer](evaluator-optimizer.md) | Medium | 2 | Scored quality iteration |
| [Swarm](swarm.md) | High | N peer | Conversational multi-domain handoffs |
| [Hierarchical Teams](hierarchical-teams.md) | High | N nested | Large-scale enterprise workflows |
