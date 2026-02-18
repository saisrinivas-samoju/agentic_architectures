# 37. Language Agent Tree Search (LATS)

!!! example "Mini-Project: LATS"
    An MCTS-style tree search where the LLM proposes candidate next steps, scores partial solutions, and UCB1 selection balances exploration vs exploitation to find the best solution path.

    [View on GitHub :material-github:](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/37-lats.ipynb){ .md-button .md-button--primary }

---

## Description

**LATS** (Zhou et al., 2023) combines LLM-based agents with Monte Carlo Tree Search (MCTS). The agent builds a search tree where each node is a state (observation), and each edge is an action. LATS uses the LLM for four roles: (1) generating candidate actions, (2) evaluating states, (3) simulating outcomes, and (4) backpropagating values. This enables systematic exploration of large action spaces.

## How It Works (Algorithm)

1. **Selection**: Navigate the tree using UCB1 (Upper Confidence Bound) to balance exploration vs exploitation
2. **Expansion**: Use the LLM to generate candidate actions from the current state
3. **Simulation**: Use the LLM to simulate the outcome of each action
4. **Backpropagation**: Update node values based on simulation results

## Diagram

```mermaid
flowchart TD
    A[Root: Initial State] --> B[Action 1]
    A --> C[Action 2]
    B --> D[State 1a]
    B --> E[State 1b]
    C --> F[State 2a]
    D --> G[Value: 0.8]
    E --> H[Value: 0.3]
    F --> I[Value: 0.6]

    J[LATS Loop] --> K[1. Select via UCB1]
    K --> L[2. Expand with LLM]
    L --> M[3. Simulate outcome]
    M --> N[4. Backpropagate value]
    N --> J

    style A fill:#FF5722,color:#fff
    style G fill:#4CAF50,color:#fff
    style H fill:#F44336,color:#fff
    style J fill:#2196F3,color:#fff
```
