# 11. Generator-Verifier (Generator-Discriminator)

!!! example "Mini-Project: SQL Generator with Execution Verifier"
    A generator LLM writes SQL queries to answer natural-language questions, and a verifier executes each query against a live SQLite database, routing failures back to the generator with error context until the query succeeds.

    [View on GitHub :material-github:](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/11-sql-generator-verifier.ipynb){ .md-button .md-button--primary }

---

## Description

The **Generator-Verifier** pattern pairs a generation model with a separate verification model. The generator produces candidate outputs, and the verifier independently assesses whether each candidate is correct, safe, or meets quality criteria. Unlike Reflection (which provides textual feedback for iteration), the verifier acts as a **binary or scored gate** — outputs either pass or fail. Failed outputs are regenerated, sometimes with the verification failure as context.

This mirrors the GAN (Generative Adversarial Network) concept at the agent level: one model creates, another judges.

## When to Use

- Code generation where output can be verified by execution
- Mathematical reasoning where answers can be checked
- Content moderation (generate then verify for safety)
- Any task with a cheap-to-compute verification function

## Benefits

| Benefit | Description |
|---|---|
| **High Accuracy** | Verification catches generation errors |
| **Separation of Concerns** | Generator and verifier can be different models |
| **Efficient** | Verifier is often cheaper than regeneration |
| **Composable** | Multiple verifiers can be chained (safety, accuracy, format) |

## Architecture Diagram

```mermaid
flowchart TD
    A[Input] --> B[Generator LLM]
    B --> C[Candidate Output]
    C --> D[Verifier]
    D --> E{Valid?}
    E -->|No| F[Reject + Context]
    F --> B
    E -->|Yes| G[Accepted Output]

    style A fill:#4CAF50,color:#fff
    style B fill:#2196F3,color:#fff
    style C fill:#FFC107,color:#000
    style D fill:#E91E63,color:#fff
    style E fill:#FF9800,color:#fff
    style F fill:#F44336,color:#fff
    style G fill:#4CAF50,color:#fff
```
