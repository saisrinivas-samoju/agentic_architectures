# 13. Human-in-the-Loop (HITL)

!!! example "Mini-Project: Expense Approval with Human-in-the-Loop"
    An expense approval agent that auto-approves low-value requests and pauses for human review on high-value ones, using LangGraph's interrupt mechanism to capture the human decision before resuming.

    [View on GitHub :material-github:](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/13-expense-approval-hitl.ipynb){ .md-button .md-button--primary }

---

## Description

**Human-in-the-Loop (HITL)** integrates human oversight into an agent's execution flow. At critical decision points, the agent pauses and requests human approval, input, or correction before proceeding. This is essential for high-stakes operations (financial transactions, data deletion, sending emails) where autonomous execution is too risky. LangGraph supports HITL natively through **interrupt points** and checkpointers that persist state while waiting for human input.

## When to Use

- High-stakes actions (payments, deletions, external communications)
- When agent confidence is low and human judgment adds value
- Compliance requirements mandating human approval
- Iterative workflows where human feedback steers the agent

## Benefits

| Benefit | Description |
|---|---|
| **Safety** | Prevents costly autonomous mistakes |
| **Trust** | Users maintain control over critical decisions |
| **Quality** | Human judgment supplements LLM reasoning |
| **Compliance** | Meets regulatory requirements for human oversight |

## Architecture Diagram

```mermaid
flowchart TD
    A[User Input] --> B[Agent Plans Action]
    B --> C{High-Stakes Action?}
    C -->|No| D[Execute Automatically]
    C -->|Yes| E[Pause: Request Approval]
    E --> F[Human Reviews]
    F -->|Approved| D
    F -->|Rejected| G[Agent Replans]
    G --> B
    D --> H[Return Result]

    style A fill:#4CAF50,color:#fff
    style B fill:#2196F3,color:#fff
    style C fill:#FF9800,color:#fff
    style E fill:#E91E63,color:#fff
    style F fill:#9C27B0,color:#fff
    style D fill:#00BCD4,color:#fff
    style G fill:#F44336,color:#fff
    style H fill:#4CAF50,color:#fff
```
