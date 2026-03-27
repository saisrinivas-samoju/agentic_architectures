# Architectures Overview

This section covers **70 agentic design patterns** organised into 14 parts. Use the [Selection Guide](selection-guide.md) to find the right pattern for your use case.

---

## Part I — Core Patterns (1–10)

The foundational building blocks. Master these first — every subsequent pattern builds on one or more of these.

| # | Architecture | Complexity | Agents | Best For |
|---|---|---|---|---|
| 1 | [Single Agent (ReAct)](single-agent.md) | Low | 1 | Simple tool-augmented tasks |
| 2 | [Prompt Chaining](prompt-chaining.md) | Low | 1 | Sequential multi-step pipelines |
| 3 | [Routing](routing.md) | Low-Med | 1+N | Multi-domain classification |
| 4 | [Parallelization](parallelization.md) | Medium | N | Independent concurrent subtasks |
| 5 | [Orchestrator-Worker](orchestrator-worker.md) | Med-High | 1+N | Unpredictable task decomposition |
| 6 | [Supervisor](supervisor.md) | Med-High | 1+N | Coordinated multi-agent control |
| 7 | [Reflection / Self-Correction](reflection.md) | Medium | 1-2 | Self-improving output quality |
| 8 | [Evaluator-Optimizer](evaluator-optimizer.md) | Medium | 2 | Scored quality iteration |
| 9 | [Swarm](swarm.md) | High | N | Conversational multi-domain handoffs |
| 10 | [Hierarchical Teams](hierarchical-teams.md) | High | N | Large-scale enterprise workflows |

---

## Part II — Quality, Verification & Oversight (11–13)

| # | Architecture | Complexity | Agents | Best For |
|---|---|---|---|---|
| 11 | [Generator-Verifier](generator-verifier.md) | Medium | 2 | Execution-based verification (code, math) |
| 12 | [Agent-as-a-Judge](llm-as-a-judge.md) | Medium | 2 | One-shot quality evaluation & ranking |
| 13 | [Human-in-the-Loop](human-in-the-loop.md) | Medium | 1+ | High-stakes approval workflows |

---

## Part III — Parallelism, Pipelines & Cost Optimization (14–18)

| # | Architecture | Complexity | Agents | Best For |
|---|---|---|---|---|
| 14 | [Map-Reduce Agents](map-reduce.md) | Medium | N | Processing large documents/datasets |
| 15 | [Mixture-of-Agents](mixture-of-agents.md) | High | N models | Maximum quality via model diversity |
| 16 | [DAG / Graph Orchestration](dag-orchestration.md) | Medium | N | Complex dependency workflows |
| 17 | [Plan-and-Execute](plan-and-execute.md) | Medium | 1 | Strategic multi-step tasks with replanning |
| 18 | [Cascading Agents](cascading-agents.md) | Medium | 2-3 | Cost-optimized inference |

---

## Part IV — Multi-Agent Collaboration (19–26)

| # | Architecture | Complexity | Agents | Best For |
|---|---|---|---|---|
| 19 | [Blackboard Pattern](blackboard.md) | High | N | Incremental collaborative problem-solving |
| 20 | [Market-Based / Bidding](market-based.md) | Medium | N | Dynamic self-organizing task allocation |
| 21 | [Contract Net Protocol](contract-net.md) | Medium | N | Formal task delegation with accountability |
| 22 | [Debate / Adversarial](debate.md) | Medium | 2-3 | Rigorous decision analysis |
| 23 | [Red-Team Agent](red-team.md) | Medium | 2 | Security & safety testing |
| 24 | [Role-Based Collaboration](role-based.md) | Medium | N | Persona-driven team pipelines |
| 25 | [Conversational Multi-Agent](conversational-multi-agent.md) | Medium | N | Emergent group problem-solving |
| 26 | [Event-Driven Multi-Agent](event-driven.md) | High | N | Reactive async multi-agent systems |

---

## Part V — Reasoning Patterns (27–30)

| # | Architecture | Complexity | Agents | Best For |
|---|---|---|---|---|
| 27 | [Inner Monologue](inner-monologue.md) | Low | 1 | Clean output with hidden reasoning |
| 28 | [Speculative Execution](speculative-execution.md) | Medium | 1 | Low-latency branching decisions |
| 29 | [Skeleton of Thought](skeleton-of-thought.md) | Medium | 1 | Fast long-form generation |
| 30 | [ReAcTree](reactree.md) | High | 1 | Multi-strategy tree exploration |

---

## Part VI — Domain Applications (31–34)

| # | Architecture | Complexity | Agents | Best For |
|---|---|---|---|---|
| 31 | [Agentic RAG](agentic-rag.md) | Medium | 1 | Intelligent document retrieval |
| 32 | [Agentic Coding](agentic-coding.md) | Medium | 1 | Self-healing code generation |
| 33 | [Self-Tooling Agent](self-tooling.md) | Medium | 1 | Runtime tool creation |
| 34 | [Dynamic Tool Generation](dynamic-tool-generation.md) | Medium | 1 | Systematic tool generation pipeline |

---

## Part VII — Cognitive Architectures (35–36)

| # | Architecture | Complexity | Agents | Best For |
|---|---|---|---|---|
| 35 | [Neuro-Symbolic Agent](neuro-symbolic.md) | High | 1 | LLM + formal logic/rules |
| 36 | [Dual-Paradigm Framework](dual-paradigm.md) | Medium | 1 | System 1 / System 2 routing |

---

## Part VIII — Advanced Planning & Search (37–41)

| # | Architecture | Complexity | Agents | Best For |
|---|---|---|---|---|
| 37 | [LATS](lats.md) | High | 1 | LLM + Monte Carlo Tree Search |
| 38 | [Introspective MCTS](introspective-mcts.md) | High | 1 | Per-simulation introspective search |
| 39 | [Reflective MCTS](reflective-mcts.md) | High | 1 | Cross-episode reflective search |
| 40 | [Collaborative Tree Search](collaborative-tree-search.md) | High | N | Multi-agent collaborative tree search |
| 41 | [Beam Search for Agents](beam-search.md) | Medium | 1 | Top-K solution exploration |

---

## Part IX — Agent Protocols (42–45)

| # | Architecture | Complexity | Best For |
|---|---|---|---|
| 42 | [Model Context Protocol (MCP)](mcp.md) | Low | Tool integration standard |
| 43 | [Agent-to-Agent Protocol (A2A)](a2a.md) | Medium | Cross-vendor agent communication |
| 44 | [Agent Communication Protocol (ACP)](acp.md) | Medium | Framework-agnostic agent messaging |
| 45 | [Agent Network Protocol (ANP)](anp.md) | High | Internet-scale agent networking |

---

## Part X — Agent Memory System (46–52)

| # | Architecture | Complexity | Best For |
|---|---|---|---|
| 46 | [Episodic Memory](episodic-memory.md) | Medium | Learning from past experiences |
| 47 | [Semantic Memory](semantic-memory.md) | Medium | Storing facts and relationships |
| 48 | [Procedural Memory](procedural-memory.md) | Medium | Remembering how to do tasks |
| 49 | [Agentic Memory (A-MEM)](agentic-memory.md) | High | Interconnected knowledge notes |
| 50 | [Collaborative Memory](collaborative-memory.md) | Medium | Shared team knowledge |
| 51 | [Contextual Experience Replay](contextual-experience-replay.md) | Medium | Prioritized experience replay |
| 52 | [Meta-Memory](meta-memory.md) | High | Memory system optimization |

---

## Part XI — Agent Safety & Resilience (53–58)

| # | Architecture | Complexity | Best For |
|---|---|---|---|
| 53 | [Guardrail Agent](guardrail.md) | Low | Content safety filtering |
| 54 | [Circuit Breaker](circuit-breaker.md) | Low | Preventing cascading failures |
| 55 | [Saga Pattern](saga-pattern.md) | Medium | Multi-step rollback |
| 56 | [API Gateway / Gatekeeper](api-gateway.md) | Low | Centralized access control |
| 57 | [Least-Privilege Ephemeral Identity](least-privilege.md) | Medium | Per-task scoped credentials |
| 58 | [Dead Letter / Escalation](dead-letter.md) | Low | Handling failed tasks |

---

## Part XII — Agent Infrastructure (59–62)

| # | Architecture | Complexity | Best For |
|---|---|---|---|
| 59 | [Agentic Mesh](agentic-mesh.md) | High | Enterprise multi-agent infrastructure |
| 60 | [Agent Registry and Discovery](agent-registry.md) | Medium | Large-scale agent management |
| 61 | [Agent Control Plane](agent-control-plane.md) | High | Agent governance and lifecycle |
| 62 | [Data Flywheel](data-flywheel.md) | Medium | Continuous improvement from usage |

---

## Part XIII — Embodied / Physical (63–65)

| # | Architecture | Complexity | Best For |
|---|---|---|---|
| 63 | [VLA Models](vla.md) | Very High | Vision + language + robot actions |
| 64 | [Embodied AI](embodied-ai.md) | Very High | Physical world agents |
| 65 | [World Models](world-models.md) | Very High | Internal environment simulation |

---

## Part XIV — Frameworks & Meta-Approaches (66–70)

| # | Architecture | Complexity | Best For |
|---|---|---|---|
| 66 | [CoALA](coala.md) | — | Agent architecture taxonomy |
| 67 | [AEGIS Framework](aegis.md) | High | Comprehensive layered safety |
| 68 | [ADAS](adas.md) | High | Automated agent design search |
| 69 | [Self-Evolving Agents (MASE)](self-evolving.md) | High | Self-improving agents |
| 70 | [Nested Learning](nested-learning.md) | High | Multi-timescale optimization |
