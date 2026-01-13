# 1. Single Agent (ReAct)

!!! example "Mini-Project: Smart Trip Budget Planner"
    A ReAct agent that uses web search and calculation tools to plan and price a custom travel itinerary.

    [View on GitHub :material-github:](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/01-smart-trip-budget-planner.ipynb){ .md-button .md-button--primary }

---

## Description

The **ReAct (Reasoning + Acting)** pattern is the foundational agentic architecture. A single LLM alternates between **thinking** (reasoning about what to do) and **acting** (calling tools or producing output) in a loop. The agent continues this think-act cycle until it determines the task is complete.

## When to Use

- Tasks that require a single agent with access to tools (search, calculator, APIs)
- Simple question-answering with tool augmentation
- When the problem scope is narrow enough for one agent to handle
- Prototyping and getting started with agentic systems

## Benefits

| Benefit | Description |
|---|---|
| **Simplicity** | Easiest pattern to implement and debug |
| **Transparency** | Chain-of-thought reasoning is visible at each step |
| **Flexibility** | Agent dynamically decides which tools to use and when |
| **Low Overhead** | No coordination cost between multiple agents |

## Architecture Diagram

```mermaid
flowchart TD
    A[User Input] --> B[LLM Reasoning]
    B --> C{Tool Call Needed?}
    C -->|Yes| D[Execute Tool]
    D --> E[Tool Result]
    E --> B
    C -->|No| F[Final Response]
    F --> G[User Output]

    style A fill:#4CAF50,color:#fff
    style B fill:#2196F3,color:#fff
    style C fill:#FF9800,color:#fff
    style D fill:#9C27B0,color:#fff
    style F fill:#4CAF50,color:#fff
    style G fill:#607D8B,color:#fff
```
