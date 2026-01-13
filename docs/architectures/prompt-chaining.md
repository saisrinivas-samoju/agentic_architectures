# 2. Prompt Chaining

!!! example "Mini-Project: Blog Post Refiner"
    A prompt chain that drafts, critiques, and polishes a blog post through sequential LLM steps.

    [View on GitHub :material-github:](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/02-blog-post-refiner.ipynb){ .md-button .md-button--primary }

---

## Description

**Prompt Chaining** decomposes a task into a fixed sequence of steps, where each LLM call processes the output of the previous one. Each step is a focused, well-defined subtask with its own prompt, and the output of one step feeds directly into the next.

## When to Use

- Tasks that can be cleanly decomposed into sequential subtasks
- When each step benefits from a specialized prompt
- Workflows where intermediate validation is needed (e.g., generate then verify)
- Data transformation pipelines (extract -> transform -> summarize)

## Benefits

| Benefit | Description |
|---|---|
| **Reliability** | Each step has a focused prompt, reducing errors |
| **Debuggability** | Easy to pinpoint which step failed |
| **Quality Control** | Each step's output can be validated before passing forward |
| **Modularity** | Steps can be independently tested and improved |

## Architecture Diagram

```mermaid
flowchart LR
    A[User Input] --> B[Step 1: Generate Draft]
    B --> C[Step 2: Analyze Draft]
    C --> D[Step 3: Finalize]
    D --> E[Final Output]

    style A fill:#4CAF50,color:#fff
    style B fill:#2196F3,color:#fff
    style C fill:#2196F3,color:#fff
    style D fill:#2196F3,color:#fff
    style E fill:#4CAF50,color:#fff
```
