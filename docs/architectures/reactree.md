# 30. ReAcTree

!!! example "Mini-Project: ReAcTree for Multi-Strategy Problem Solving"
    Generates multiple fundamentally different strategies for a problem, executes them in parallel, self-evaluates each branch's result, and selects the highest-scoring solution.

    [View on GitHub :material-github:](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/30-reactree.ipynb){ .md-button .md-button--primary }

---

## Description

**ReAcTree** extends the linear ReAct (Reasoning + Acting) pattern into a tree structure. Instead of following a single reasoning path, the agent explores multiple reasoning branches simultaneously, creating a tree of thought-action-observation sequences. Each branch represents a different strategy for solving the problem. The agent evaluates branches, prunes unpromising ones, and continues the most promising paths.

This combines the strengths of Tree-of-Thoughts (ToT) with ReAct's tool-calling capability, enabling more thorough exploration of solution spaces.

## When to Use

- Complex problems where the first approach may not work
- When multiple valid strategies exist and you want to explore them
- Tasks requiring backtracking and alternative approaches
- Research and exploration tasks with uncertain paths

## Benefits

| Benefit | Description |
|---|---|
| **Exploration** | Multiple strategies explored simultaneously |
| **Resilience** | Dead-end branches are pruned, others continue |
| **Quality** | Best path is selected from multiple candidates |
| **Thoroughness** | More of the solution space is covered |

## Architecture Diagram

```mermaid
flowchart TD
    A[Problem] --> B[Root: Initial Analysis]
    B --> C[Branch 1: Strategy A]
    B --> D[Branch 2: Strategy B]
    B --> E[Branch 3: Strategy C]
    C --> F[Action 1A]
    C --> G[Action 1B]
    D --> H[Action 2A]
    E --> I[Pruned - Low Promise]
    F --> J[Evaluate All Branches]
    G --> J
    H --> J
    J --> K[Select Best Path]
    K --> L[Final Solution]

    style A fill:#4CAF50,color:#fff
    style B fill:#FF5722,color:#fff
    style C fill:#2196F3,color:#fff
    style D fill:#2196F3,color:#fff
    style E fill:#F44336,color:#fff
    style I fill:#F44336,color:#fff
    style J fill:#FF9800,color:#fff
    style L fill:#4CAF50,color:#fff
```
