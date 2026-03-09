# 57. Least-Privilege Ephemeral Identity

!!! example "Mini-Project: Ephemeral Identity for Agent Tasks"
    An identity service that issues scoped, time-limited tokens to agents for each task execution, with automatic expiry and explicit revocation to enforce least-privilege access.

    [View on GitHub :material-github:](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/57-least-privilege-ephemeral-identity.ipynb){ .md-button .md-button--primary }

---

## Description

Prevents over-privileged agents from causing damage beyond their task scope. If an agent is compromised or makes an error, the blast radius is limited to only the permissions it was granted for that specific task.

Each agent task execution receives a **temporary, scoped identity token** with the minimum permissions needed. The token expires after task completion. This follows the principle of least privilege applied to agent systems.

## Architecture Diagram

```mermaid
flowchart TD
    A[Task Request] --> B[Identity Service]
    B --> C[Issue Ephemeral Token]
    C --> D[Token: read-only, 5min TTL]
    D --> E[Agent Executes with Token]
    E --> F{Token Expired?}
    F -->|Yes| G[Request New Token]
    F -->|No| H[Continue]
    E --> I[Task Complete]
    I --> J[Revoke Token]

    style B fill:#FF5722,color:#fff
    style D fill:#FFC107,color:#000
    style J fill:#F44336,color:#fff
```
