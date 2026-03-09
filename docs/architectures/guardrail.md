# 53. Guardrail Agent (Constitutional Filter)

!!! example "Mini-Project: Constitutional Guardrail Agent"
    A two-layer safety filter that wraps a main agent with an input guardrail and output guardrail, blocking harmful or policy-violating requests before they reach the user.

    [View on GitHub :material-github:](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/53-guardrail-agent.ipynb){ .md-button .md-button--primary }

---

## Description

A **Guardrail Agent** acts as a filter between the main agent and the user. It evaluates every input and output against a set of rules (a "constitution") and blocks, modifies, or flags violations. This can be implemented as a pre-processor (input guard), post-processor (output guard), or both.

Prevents harmful, biased, off-topic, or policy-violating outputs from reaching users. Guards against prompt injection, jailbreaks, and unintended content generation.

## Architecture Diagram

```mermaid
flowchart TD
    A[User Input] --> B[Input Guardrail]
    B -->|Safe| C[Main Agent]
    B -->|Blocked| D[Rejection Response]
    C --> E[Agent Output]
    E --> F[Output Guardrail]
    F -->|Safe| G[User Receives Response]
    F -->|Blocked| H[Sanitized Response]

    style B fill:#F44336,color:#fff
    style F fill:#F44336,color:#fff
    style D fill:#FF9800,color:#fff
    style H fill:#FF9800,color:#fff
```

## Extended: Sidecar Guardrail Pattern

A lightweight "sidecar" process runs alongside the main agent, intercepting all inputs and outputs. The sidecar applies guardrail checks independently, similar to how sidecar proxies (Envoy, Istio) work in microservices. Useful when you cannot change the agent's code but need to add safety checks (e.g., third-party agents, legacy systems).

```mermaid
flowchart LR
    A[User] --> B[Sidecar Proxy]
    B -->|Filtered Input| C[Main Agent]
    C -->|Raw Output| B
    B -->|Filtered Output| A

    style B fill:#F44336,color:#fff
    style C fill:#2196F3,color:#fff
```
