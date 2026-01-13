# Agentic AI Architectures

A practical guide to the most important agentic design patterns used in modern AI systems. Each architecture includes a description, when to use it, key benefits, a diagram, and a hands-on mini-project notebook.

---

## What is an Agentic Architecture?

An agentic architecture defines how one or more AI agents are structured, coordinated, and given autonomy to accomplish complex tasks. These patterns range from simple single-agent loops to hierarchical teams of dozens of specialized agents.

---

## The 10 Core Architectures

| # | Architecture | Complexity | Best For |
|---|---|---|---|
| 1 | [Single Agent (ReAct)](architectures/single-agent.md) | Low | Simple tool-augmented tasks |
| 2 | [Prompt Chaining](architectures/prompt-chaining.md) | Low | Sequential multi-step pipelines |
| 3 | [Routing](architectures/routing.md) | Low-Medium | Multi-domain classification |
| 4 | [Parallelization](architectures/parallelization.md) | Medium | Independent concurrent subtasks |
| 5 | [Orchestrator-Worker](architectures/orchestrator-worker.md) | Medium-High | Complex tasks, unpredictable decomposition |
| 6 | [Supervisor](architectures/supervisor.md) | Medium-High | Coordinated multi-agent with central control |
| 7 | [Reflection / Self-Correction](architectures/reflection.md) | Medium | Self-improving output quality |
| 8 | [Evaluator-Optimizer](architectures/evaluator-optimizer.md) | Medium | Scored quality iteration |
| 9 | [Swarm](architectures/swarm.md) | High | Conversational multi-domain handoffs |
| 10 | [Hierarchical Teams](architectures/hierarchical-teams.md) | High | Large-scale enterprise workflows |

---

## Key Principles

1. **Start simple.** Use a single ReAct agent first. Only add complexity when needed.
2. **Match architecture to task.** Don't use a multi-agent swarm when prompt chaining suffices.
3. **Minimize autonomy.** Give the system the smallest amount of freedom that still delivers the outcome.
4. **Combine patterns.** Real systems often layer multiple patterns (e.g., Supervisor + Reflection).
5. **Observe everything.** Log all agent decisions, tool calls, and handoffs for debugging.

---

## References

- [Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [LangGraph Documentation](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
- [LangGraph Multi-Agent Workflows](https://blog.langchain.com/langgraph-multi-agent-workflows/)
- [LangGraph Supervisor (GitHub)](https://github.com/langchain-ai/langgraph-supervisor-py)
- [LangGraph Swarm (GitHub)](https://github.com/langchain-ai/langgraph-swarm-py)
- [Google Cloud: Agentic AI Design Patterns](https://docs.cloud.google.com/architecture/choose-design-pattern-agentic-ai-system)
- [Microsoft: Multi-Agent Reference Architecture](https://microsoft.github.io/multi-agent-reference-architecture/docs/reference-architecture/Reference-Architecture.html)
- [Anthropic Cookbook: Agent Patterns](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents)
