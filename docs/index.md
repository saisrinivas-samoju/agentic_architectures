# Agentic AI Architectures

A practical guide to **70 agentic design patterns** used in modern AI systems. Each architecture includes a description, when to use it, key benefits, a diagram, and a hands-on mini-project notebook.

---

## What is an Agentic Architecture?

An agentic architecture defines how one or more AI agents are structured, coordinated, and given autonomy to accomplish complex tasks. These patterns range from simple single-agent loops to hierarchical teams of dozens of specialized agents.

---

## The 70 Architectures

| # | Architecture | Part | Complexity | Best For |
|---|---|---|---|---|
| 1 | [Single Agent (ReAct)](architectures/single-agent.md) | I | Low | Simple tool-augmented tasks |
| 2 | [Prompt Chaining](architectures/prompt-chaining.md) | I | Low | Sequential multi-step pipelines |
| 3 | [Routing](architectures/routing.md) | I | Low-Med | Multi-domain classification |
| 4 | [Parallelization](architectures/parallelization.md) | I | Medium | Independent concurrent subtasks |
| 5 | [Orchestrator-Worker](architectures/orchestrator-worker.md) | I | Med-High | Unpredictable task decomposition |
| 6 | [Supervisor](architectures/supervisor.md) | I | Med-High | Coordinated multi-agent control |
| 7 | [Reflection / Self-Correction](architectures/reflection.md) | I | Medium | Self-improving output quality |
| 8 | [Evaluator-Optimizer](architectures/evaluator-optimizer.md) | I | Medium | Scored quality iteration |
| 9 | [Swarm](architectures/swarm.md) | I | High | Conversational multi-domain handoffs |
| 10 | [Hierarchical Teams](architectures/hierarchical-teams.md) | I | High | Large-scale enterprise workflows |
| 11 | [Generator-Verifier](architectures/generator-verifier.md) | II | Medium | Execution-based verification |
| 12 | [Agent-as-a-Judge](architectures/llm-as-a-judge.md) | II | Medium | One-shot quality evaluation |
| 13 | [Human-in-the-Loop](architectures/human-in-the-loop.md) | II | Medium | High-stakes approval workflows |
| 14 | [Map-Reduce Agents](architectures/map-reduce.md) | III | Medium | Processing large documents/datasets |
| 15 | [Mixture-of-Agents](architectures/mixture-of-agents.md) | III | High | Maximum quality via model diversity |
| 16 | [DAG / Graph Orchestration](architectures/dag-orchestration.md) | III | Medium | Complex dependency workflows |
| 17 | [Plan-and-Execute](architectures/plan-and-execute.md) | III | Medium | Strategic multi-step tasks |
| 18 | [Cascading Agents](architectures/cascading-agents.md) | III | Medium | Cost-optimized inference |
| 19 | [Blackboard Pattern](architectures/blackboard.md) | IV | High | Incremental collaborative problem-solving |
| 20 | [Market-Based / Bidding](architectures/market-based.md) | IV | Medium | Dynamic task allocation |
| 21 | [Contract Net Protocol](architectures/contract-net.md) | IV | Medium | Formal task delegation |
| 22 | [Debate / Adversarial](architectures/debate.md) | IV | Medium | Rigorous decision analysis |
| 23 | [Red-Team Agent](architectures/red-team.md) | IV | Medium | Security & safety testing |
| 24 | [Role-Based Collaboration](architectures/role-based.md) | IV | Medium | Persona-driven team pipelines |
| 25 | [Conversational Multi-Agent](architectures/conversational-multi-agent.md) | IV | Medium | Emergent group problem-solving |
| 26 | [Event-Driven Multi-Agent](architectures/event-driven.md) | IV | High | Reactive async systems |
| 27 | [Inner Monologue](architectures/inner-monologue.md) | V | Low | Clean output with hidden reasoning |
| 28 | [Speculative Execution](architectures/speculative-execution.md) | V | Medium | Low-latency branching decisions |
| 29 | [Skeleton of Thought](architectures/skeleton-of-thought.md) | V | Medium | Fast long-form generation |
| 30 | [ReAcTree](architectures/reactree.md) | V | High | Multi-strategy tree exploration |
| 31 | [Agentic RAG](architectures/agentic-rag.md) | VI | Medium | Intelligent document retrieval |
| 32 | [Agentic Coding](architectures/agentic-coding.md) | VI | Medium | Self-healing code generation |
| 33 | [Self-Tooling Agent](architectures/self-tooling.md) | VI | Medium | Runtime tool creation |
| 34 | [Dynamic Tool Generation](architectures/dynamic-tool-generation.md) | VI | Medium | Systematic tool generation |
| 35 | [Neuro-Symbolic Agent](architectures/neuro-symbolic.md) | VII | High | LLM + formal logic/rules |
| 36 | [Dual-Paradigm Framework](architectures/dual-paradigm.md) | VII | Medium | System 1 / System 2 routing |
| 37 | [LATS](architectures/lats.md) | VIII | High | LLM + Monte Carlo Tree Search |
| 38 | [Introspective MCTS](architectures/introspective-mcts.md) | VIII | High | Per-simulation introspective search |
| 39 | [Reflective MCTS](architectures/reflective-mcts.md) | VIII | High | Cross-episode reflective search |
| 40 | [Collaborative Tree Search](architectures/collaborative-tree-search.md) | VIII | High | Multi-agent collaborative search |
| 41 | [Beam Search for Agents](architectures/beam-search.md) | VIII | Medium | Top-K solution exploration |
| 42 | [Model Context Protocol (MCP)](architectures/mcp.md) | IX | Low | Tool integration standard |
| 43 | [Agent-to-Agent Protocol (A2A)](architectures/a2a.md) | IX | Medium | Cross-vendor agent communication |
| 44 | [Agent Communication Protocol (ACP)](architectures/acp.md) | IX | Medium | Framework-agnostic agent messaging |
| 45 | [Agent Network Protocol (ANP)](architectures/anp.md) | IX | High | Internet-scale agent networking |
| 46 | [Episodic Memory](architectures/episodic-memory.md) | X | Medium | Learning from past experiences |
| 47 | [Semantic Memory](architectures/semantic-memory.md) | X | Medium | Storing facts and relationships |
| 48 | [Procedural Memory](architectures/procedural-memory.md) | X | Medium | Remembering how to do tasks |
| 49 | [Agentic Memory (A-MEM)](architectures/agentic-memory.md) | X | High | Interconnected knowledge notes |
| 50 | [Collaborative Memory](architectures/collaborative-memory.md) | X | Medium | Shared team knowledge |
| 51 | [Contextual Experience Replay](architectures/contextual-experience-replay.md) | X | Medium | Prioritized experience replay |
| 52 | [Meta-Memory](architectures/meta-memory.md) | X | High | Memory system optimization |
| 53 | [Guardrail Agent](architectures/guardrail.md) | XI | Low | Content safety filtering |
| 54 | [Circuit Breaker](architectures/circuit-breaker.md) | XI | Low | Preventing cascading failures |
| 55 | [Saga Pattern](architectures/saga-pattern.md) | XI | Medium | Multi-step rollback |
| 56 | [API Gateway / Gatekeeper](architectures/api-gateway.md) | XI | Low | Centralized access control |
| 57 | [Least-Privilege Ephemeral Identity](architectures/least-privilege.md) | XI | Medium | Per-task scoped credentials |
| 58 | [Dead Letter / Escalation](architectures/dead-letter.md) | XI | Low | Handling failed tasks |
| 59 | [Agentic Mesh](architectures/agentic-mesh.md) | XII | High | Enterprise multi-agent infrastructure |
| 60 | [Agent Registry and Discovery](architectures/agent-registry.md) | XII | Medium | Large-scale agent management |
| 61 | [Agent Control Plane](architectures/agent-control-plane.md) | XII | High | Agent governance and lifecycle |
| 62 | [Data Flywheel](architectures/data-flywheel.md) | XII | Medium | Continuous improvement from usage |
| 63 | [VLA Models](architectures/vla.md) | XIII | Very High | Vision + language + robot actions |
| 64 | [Embodied AI](architectures/embodied-ai.md) | XIII | Very High | Physical world agents |
| 65 | [World Models](architectures/world-models.md) | XIII | Very High | Internal environment simulation |
| 66 | [CoALA](architectures/coala.md) | XIV | — | Agent architecture taxonomy |
| 67 | [AEGIS Framework](architectures/aegis.md) | XIV | High | Comprehensive layered safety |
| 68 | [ADAS](architectures/adas.md) | XIV | High | Automated agent design search |
| 69 | [Self-Evolving Agents (MASE)](architectures/self-evolving.md) | XIV | High | Self-improving agents |
| 70 | [Nested Learning](architectures/nested-learning.md) | XIV | High | Multi-timescale optimization |

---

## Key Principles

1. **Start simple.** Use a single ReAct agent first. Only add complexity when needed.
2. **Match architecture to task.** Don't use a multi-agent swarm when prompt chaining suffices.
3. **Minimize autonomy.** Give the system the smallest amount of freedom that still delivers the outcome.
4. **Combine patterns.** Real systems often layer multiple patterns (e.g., Supervisor + Reflection + Guardrails).
5. **Observe everything.** Log all agent decisions, tool calls, and handoffs for debugging.
6. **Safety is not optional.** Every production agent needs guardrails, regardless of the architecture.
7. **Memory is a superpower.** Agents with memory outperform stateless agents on repeated tasks.
8. **Plan before acting.** For complex tasks, explicit planning reduces wasted effort.
9. **Verify outputs.** Generator-Verifier patterns catch errors that self-reflection misses.
10. **Design for failure.** Use circuit breakers, sagas, and dead letter queues for resilience.

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
- [Model Context Protocol (MCP) Specification](https://spec.modelcontextprotocol.io)
- [Google A2A Protocol](https://github.com/google/a2a)
- [Together AI: Mixture-of-Agents](https://www.together.ai/blog/together-moa)
- [LATS: Language Agent Tree Search (Zhou et al., 2023)](https://arxiv.org/abs/2310.04406)
- [CoALA: Cognitive Architectures for Language Agents (Sumers et al., 2023)](https://arxiv.org/abs/2309.02427)
- [Skeleton of Thought (Ning et al., 2023)](https://arxiv.org/abs/2307.15337)
- [LLM-as-a-Judge (Zheng et al., 2023)](https://arxiv.org/abs/2306.05685)
- [ADAS: Automated Design of Agentic Systems (Hu et al., 2024)](https://arxiv.org/abs/2408.08435)
- [CrewAI Documentation](https://docs.crewai.com)
- [AutoGen Documentation](https://microsoft.github.io/autogen)
