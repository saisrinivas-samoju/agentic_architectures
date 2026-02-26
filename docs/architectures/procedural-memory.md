# 48. Procedural Memory

!!! example "Mini-Project: Procedural Memory for an Operations Agent"
    A procedural memory system for an operations agent that stores named workflows (deploy, debug), matches incoming tasks via fast keyword lookup or LLM-based fuzzy matching, and executes the stored step-by-step procedure when a match is found.

    [View on GitHub :material-github:](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/48-procedural-memory.ipynb){ .md-button .md-button--primary }

---

## What It Is

**Procedural Memory** stores **how to do things** -- learned procedures, workflows, and successful action sequences. When the agent encounters a familiar task type, it retrieves the stored procedure rather than reasoning from scratch. Like human muscle memory for complex tasks.

## What It Stores (Examples)

- Successful tool call sequences for specific task types
- Multi-step workflows (e.g., "to deploy: test, build, push, verify")
- Error recovery procedures
- Optimized prompt templates

## How It's Implemented

Uses a **key-value store** or **pattern-matching database** where task patterns are keys and procedures are values.

## Mermaid Diagram

```mermaid
flowchart TD
    A[New Task] --> B[Match to Known Procedures]
    B --> C{Match Found?}
    C -->|Yes| D[Execute Stored Procedure]
    C -->|No| E[Reason from Scratch]
    D --> F[Task Complete]
    E --> F
    F --> G[Store Successful Procedure]
    G --> B

    style A fill:#4CAF50,color:#fff
    style D fill:#9C27B0,color:#fff
    style E fill:#FF9800,color:#fff
    style F fill:#4CAF50,color:#fff
```

## Extended: Hierarchical Procedural Memory

**Hierarchical Procedural Memory** organizes procedures into a tree hierarchy -- high-level strategies contain sub-procedures, which contain atomic actions. This allows agents to reason at different abstraction levels: select a high-level strategy, then drill down into specifics. Like how "cook a meal" decomposes into "prepare ingredients" -> "chop vegetables" -> individual knife cuts.

```mermaid
flowchart TD
    A[Incident Response] --> B[1. Diagnose]
    A --> C[2. Mitigate]
    A --> D[3. Post-mortem]
    B --> E[Check Logs]
    B --> F[Check Metrics]
    B --> G[Identify Root Cause]
    C --> H[Apply Fix]
    C --> I[Verify Recovery]
    D --> J[Write Report]
    D --> K[Update Runbook]

    style A fill:#F44336,color:#fff
    style B fill:#FF9800,color:#fff
    style C fill:#FF9800,color:#fff
    style D fill:#FF9800,color:#fff
    style E fill:#2196F3,color:#fff
    style H fill:#2196F3,color:#fff
    style J fill:#2196F3,color:#fff
```
