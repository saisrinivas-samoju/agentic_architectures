# Mini-Projects

Each architecture is accompanied by a hands-on Jupyter notebook (or Python script) that demonstrates the pattern with a practical real-world use case.

## Running the Notebooks

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
# Install dependencies
uv sync --group dev

# Launch Jupyter
uv run jupyter notebook mini-projects/
```

---

## Part I — Core Patterns

| # | Notebook | Architecture | Description |
|---|---|---|---|
| 1 | [Smart Trip Budget Planner](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/01-smart-trip-budget-planner.ipynb) | [Single Agent (ReAct)](../architectures/single-agent.md) | A ReAct agent plans and prices a custom travel itinerary using web search and calculation tools |
| 2 | [Blog Post Refiner](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/02-blog-post-refiner.ipynb) | [Prompt Chaining](../architectures/prompt-chaining.md) | Sequential LLM steps draft, critique, and polish a blog post |
| 3 | [Customer Support Router](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/03-customer-support-router.ipynb) | [Routing](../architectures/routing.md) | Classifies customer queries and routes them to specialized support agents |
| 4 | [Editorial Review Board](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/04-editorial-review-board.ipynb) | [Parallelization](../architectures/parallelization.md) | Multiple specialist reviewers analyze a document in parallel |
| 5 | [Competitive Intelligence Report Generator](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/05-competitive-intelligence-report-generator.ipynb) | [Orchestrator-Worker](../architectures/orchestrator-worker.md) | Orchestrator dynamically dispatches research workers to gather competitive intel |
| 6 | [Data-Driven Market Analyzer](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/06-data-driven-market-analyzer.ipynb) | [Supervisor](../architectures/supervisor.md) | Supervisor coordinates research and analysis agents for market reports |
| 7 | [Self-Correcting Code Generator](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/07-self-correcting-code-generator.ipynb) | [Reflection](../architectures/reflection.md) | Generator-critic loop writes, tests, and iteratively fixes code |
| 8 | [Audience-Adaptive Content Optimizer](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/08-audience-adaptive-content-optimizer.ipynb) | [Evaluator-Optimizer](../architectures/evaluator-optimizer.md) | Adapts content to target audiences with scored quality iteration |
| 9 | [Customer Service Swarm](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/09-customer-service-swarm.ipynb) | [Swarm](../architectures/swarm.md) | Specialist agents hand off conversations based on customer needs |
| 10 | [Full-Stack Project Builder](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/10-full-stack-project-builder.ipynb) | [Hierarchical Teams](../architectures/hierarchical-teams.md) | Research and engineering teams collaborate to build a full-stack application |

---

## Part II — Quality, Verification & Oversight

| # | Notebook | Architecture | Description |
|---|---|---|---|
| 11 | [SQL Generator with Execution Verifier](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/11-sql-generator-verifier.ipynb) | [Generator-Verifier](../architectures/generator-verifier.md) | Generates SQL queries and verifies them by actual execution against a SQLite database |
| 12 | [LLM-as-a-Judge Evaluator](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/12-llm-as-a-judge.ipynb) | [Agent-as-a-Judge](../architectures/llm-as-a-judge.md) | Uses an LLM judge to evaluate and rank multiple candidate responses against a rubric |
| 13 | [Expense Approval with Human-in-the-Loop](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/13-expense-approval-hitl.ipynb) | [Human-in-the-Loop](../architectures/human-in-the-loop.md) | Routes expense requests through automated checks and human approval gates |

---

## Part III — Parallelism, Pipelines & Cost Optimization

| # | Notebook | Architecture | Description |
|---|---|---|---|
| 14 | [Long Document Summarizer](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/14-long-document-summarizer.ipynb) | [Map-Reduce Agents](../architectures/map-reduce.md) | Maps chunks of a long document to summarizers then reduces to a final summary |
| 15 | [Mixture of Agents Analysis](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/15-mixture-of-agents-analysis.ipynb) | [Mixture-of-Agents](../architectures/mixture-of-agents.md) | Aggregates diverse model outputs via a synthesizer for higher-quality answers |
| 16 | [DAG Data Pipeline](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/16-dag-data-pipeline.ipynb) | [DAG / Graph Orchestration](../architectures/dag-orchestration.md) | Executes a data processing pipeline with explicit dependency ordering |
| 17 | [Research Report Plan-and-Execute](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/17-research-report-plan-execute.ipynb) | [Plan-and-Execute](../architectures/plan-and-execute.md) | Creates an explicit research plan then executes each step, replanning on failure |
| 18 | [Cost-Optimized Model Cascade](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/18-cost-optimized-model-cascade.ipynb) | [Cascading Agents](../architectures/cascading-agents.md) | Routes queries through cheap models first, escalating to expensive ones only when needed |

---

## Part IV — Multi-Agent Collaboration

| # | Notebook | Architecture | Description |
|---|---|---|---|
| 19 | [Blackboard Pattern](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/19-blackboard-pattern.ipynb) | [Blackboard](../architectures/blackboard.md) | Specialist agents collaborate by reading and writing to a shared blackboard |
| 20 | [Market-Based Task Allocation](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/20-market-based-bidding.ipynb) | [Market-Based / Bidding](../architectures/market-based.md) | Agents bid for tasks based on their capabilities, with the best bid winning |
| 21 | [Contract Net Protocol](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/21-contract-net-protocol.ipynb) | [Contract Net Protocol](../architectures/contract-net.md) | Manager broadcasts tasks, contractors bid, and the best contractor is awarded the contract |
| 22 | [Debate / Adversarial Collaboration](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/22-debate-adversarial-collaboration.ipynb) | [Debate / Adversarial](../architectures/debate.md) | Two agents debate opposite positions with a judge synthesizing the final verdict |
| 23 | [Red-Team Agent](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/23-red-team-agent.ipynb) | [Red-Team Agent](../architectures/red-team.md) | Red-team agent attacks outputs to find vulnerabilities; blue-team agent defends |
| 24 | [Role-Based Collaboration](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/24-role-based-collaboration.ipynb) | [Role-Based Collaboration](../architectures/role-based.md) | Persona-driven agents with defined roles collaborate on a shared task pipeline |
| 25 | [Conversational Multi-Agent](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/25-conversational-multi-agent.ipynb) | [Conversational Multi-Agent](../architectures/conversational-multi-agent.md) | Multiple agents engage in open dialogue to solve a problem through emergent discussion |
| 26 | [Event-Driven Multi-Agent](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/26-event-driven-multi-agent.ipynb) | [Event-Driven Multi-Agent](../architectures/event-driven.md) | Agents react to asynchronous events via an event bus with no central coordinator |

---

## Part V — Reasoning Patterns

| # | Notebook | Architecture | Description |
|---|---|---|---|
| 27 | [Inner Monologue](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/27-inner-monologue.ipynb) | [Inner Monologue](../architectures/inner-monologue.md) | Agent uses hidden scratchpad reasoning before producing clean final output |
| 28 | [Speculative Execution](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/28-speculative-execution.ipynb) | [Speculative Execution](../architectures/speculative-execution.md) | Agent speculatively executes multiple branches in parallel, selecting the best result |
| 29 | [Skeleton of Thought](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/29-skeleton-of-thought.ipynb) | [Skeleton of Thought](../architectures/skeleton-of-thought.md) | Generates an outline skeleton first, then elaborates each section in parallel |
| 30 | [ReAcTree](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/30-reactree.ipynb) | [ReAcTree](../architectures/reactree.md) | Explores multiple reasoning strategies as a tree, selecting the best branch |

---

## Part VI — Domain Applications

| # | Notebook | Architecture | Description |
|---|---|---|---|
| 31 | [Agentic RAG](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/31-agentic-rag.ipynb) | [Agentic RAG](../architectures/agentic-rag.md) | Dynamically reformulates queries, routes to multiple sources, and synthesizes retrieved knowledge |
| 32 | [Agentic Coding](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/32-agentic-coding.ipynb) | [Agentic Coding](../architectures/agentic-coding.md) | Writes, executes, and iteratively repairs code until tests pass |
| 33 | [Self-Tooling Agent](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/33-self-tooling-agent.ipynb) | [Self-Tooling Agent](../architectures/self-tooling.md) | Agent creates its own tools at runtime when existing tools are insufficient |
| 34 | [Dynamic Tool Generation (ToolFactory)](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/34-dynamic-tool-generation.ipynb) | [Dynamic Tool Generation](../architectures/dynamic-tool-generation.md) | Systematically generates, validates, and registers new tools via a factory pipeline |

---

## Part VII — Cognitive Architectures

| # | Notebook | Architecture | Description |
|---|---|---|---|
| 35 | [Neuro-Symbolic Agent](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/35-neuro-symbolic-agent.ipynb) | [Neuro-Symbolic Agent](../architectures/neuro-symbolic.md) | Combines LLM reasoning with a symbolic rule engine for verifiable logic |
| 36 | [Dual-Paradigm Framework](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/36-dual-paradigm-framework.ipynb) | [Dual-Paradigm Framework](../architectures/dual-paradigm.md) | Routes simple queries to fast neural paths and complex ones to symbolic reasoning |

---

## Part VIII — Advanced Planning & Search

| # | Notebook | Architecture | Description |
|---|---|---|---|
| 37 | [Language Agent Tree Search (LATS)](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/37-lats.ipynb) | [LATS](../architectures/lats.md) | Uses Monte Carlo Tree Search with LLM evaluation to explore solution paths |
| 38 | [Introspective MCTS](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/38-introspective-mcts.ipynb) | [Introspective MCTS](../architectures/introspective-mcts.md) | MCTS where the agent introspects and critiques each simulation step |
| 39 | [Reflective MCTS](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/39-reflective-mcts.ipynb) | [Reflective MCTS](../architectures/reflective-mcts.md) | MCTS with cross-episode reflection that improves search heuristics over time |
| 40 | [Collaborative Tree Search](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/40-collaborative-tree-search.ipynb) | [Collaborative Tree Search](../architectures/collaborative-tree-search.md) | Multiple agents explore different branches of a solution tree in parallel |
| 41 | [Beam Search for Agents](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/41-beam-search-agents.ipynb) | [Beam Search](../architectures/beam-search.md) | Maintains top-K candidate solutions at each step, pruning low-scoring beams |

---

## Part IX — Agent Protocols

| # | File | Architecture | Description |
|---|---|---|---|
| 42 | [MCP Server](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/42-mcp.py) | [Model Context Protocol](../architectures/mcp.md) | Implements an MCP server exposing tools via the standard JSON-RPC protocol |
| 43 | [A2A Protocol](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/43-a2a-protocol.ipynb) | [Agent-to-Agent Protocol](../architectures/a2a.md) | Demonstrates cross-vendor agent communication using the A2A protocol |
| 44 | [Agent Communication Protocol (ACP)](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/44-acp.ipynb) | [ACP](../architectures/acp.md) | REST-based lightweight agent messaging using the ACP standard |
| 45 | [Agent Network Protocol (ANP)](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/45-anp.ipynb) | [ANP](../architectures/anp.md) | Decentralized agent discovery and communication using DID-based ANP |

---

## Part X — Agent Memory System

| # | Notebook | Architecture | Description |
|---|---|---|---|
| 46 | [Episodic Memory](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/46-episodic-memory.ipynb) | [Episodic Memory](../architectures/episodic-memory.md) | Agent stores and retrieves past interaction episodes to improve future responses |
| 47 | [Semantic Memory](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/47-semantic-memory.ipynb) | [Semantic Memory](../architectures/semantic-memory.md) | Agent maintains a vector-based knowledge store of facts and concepts |
| 48 | [Procedural Memory](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/48-procedural-memory.ipynb) | [Procedural Memory](../architectures/procedural-memory.md) | Agent learns and recalls how to perform tasks from prior successful runs |
| 49 | [Agentic Memory (A-MEM)](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/49-agentic-memory.ipynb) | [Agentic Memory](../architectures/agentic-memory.md) | Zettelkasten-style interconnected notes with dynamic linking and retrieval |
| 50 | [Collaborative Memory](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/50-collaborative-memory.ipynb) | [Collaborative Memory](../architectures/collaborative-memory.md) | Multiple agents share a common memory store, contributing and retrieving knowledge |
| 51 | [Contextual Experience Replay](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/51-contextual-experience-replay.ipynb) | [Contextual Experience Replay](../architectures/contextual-experience-replay.md) | Agent replays high-value past experiences to improve current task performance |
| 52 | [Meta-Memory](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/52-meta-memory.ipynb) | [Meta-Memory](../architectures/meta-memory.md) | Agent manages its own memory system, deciding what to store, forget, or consolidate |

---

## Part XI — Agent Safety & Resilience

| # | Notebook | Architecture | Description |
|---|---|---|---|
| 53 | [Guardrail Agent](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/53-guardrail-agent.ipynb) | [Guardrail Agent](../architectures/guardrail.md) | Constitutional filter that validates inputs and outputs against safety rules |
| 54 | [Circuit Breaker](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/54-circuit-breaker.ipynb) | [Circuit Breaker](../architectures/circuit-breaker.md) | Prevents cascading failures by opening the circuit after repeated service failures |
| 55 | [Saga Pattern](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/55-saga-pattern.ipynb) | [Saga Pattern](../architectures/saga-pattern.md) | Manages multi-step workflows with compensating actions to rollback on failure |
| 56 | [API Gateway / Gatekeeper](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/56-api-gateway-gatekeeper.ipynb) | [API Gateway](../architectures/api-gateway.md) | Centralized validation and rate-limiting layer for all agent tool calls |
| 57 | [Least-Privilege Ephemeral Identity](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/57-least-privilege-ephemeral-identity.ipynb) | [Least-Privilege Identity](../architectures/least-privilege.md) | Issues short-lived, scoped credentials per agent task to minimize blast radius |
| 58 | [Dead Letter / Escalation](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/58-dead-letter-escalation.ipynb) | [Dead Letter](../architectures/dead-letter.md) | Routes failed tasks to a dead-letter queue with automatic escalation |

---

## Part XII — Agent Infrastructure

| # | Notebook | Architecture | Description |
|---|---|---|---|
| 59 | [Agentic Mesh](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/59-agentic-mesh.ipynb) | [Agentic Mesh](../architectures/agentic-mesh.md) | Service mesh for agent-to-agent communication with discovery and load balancing |
| 60 | [Agent Registry and Discovery](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/60-agent-registry-discovery.ipynb) | [Agent Registry](../architectures/agent-registry.md) | Central registry where agents register capabilities and discover other agents |
| 61 | [Agent Control Plane](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/61-agent-control-plane.ipynb) | [Agent Control Plane](../architectures/agent-control-plane.md) | Governance layer for agent lifecycle, policy enforcement, and observability |
| 62 | [Data Flywheel](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/62-data-flywheel.ipynb) | [Data Flywheel](../architectures/data-flywheel.md) | Captures agent interaction data to continuously fine-tune and improve models |

---

## Part XIII — Embodied / Physical

| # | Notebook | Architecture | Description |
|---|---|---|---|
| 63 | [VLA Models](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/63-vla-models.ipynb) | [VLA Models](../architectures/vla.md) | Vision-Language-Action model that maps visual observations to robot actions |
| 64 | [Embodied AI](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/64-embodied-ai.ipynb) | [Embodied AI](../architectures/embodied-ai.md) | Agent that perceives a physical environment and takes grounded actions |
| 65 | [World Models](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/65-world-models.ipynb) | [World Models](../architectures/world-models.md) | Agent uses an internal world model to simulate outcomes before acting |

---

## Part XIV — Frameworks & Meta-Approaches

| # | Notebook | Architecture | Description |
|---|---|---|---|
| 66 | [CoALA](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/66-coala.ipynb) | [CoALA](../architectures/coala.md) | Uses CoALA taxonomy to compare and analyze different agent architectures |
| 67 | [AEGIS Framework](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/67-aegis-framework.ipynb) | [AEGIS](../architectures/aegis.md) | Layered safety composition combining guardrails, monitoring, and intervention |
| 68 | [ADAS](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/68-adas.ipynb) | [ADAS](../architectures/adas.md) | Meta-agent that searches for and designs new agent architectures automatically |
| 69 | [Self-Evolving Agents (MASE)](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/69-self-evolving-agents.ipynb) | [Self-Evolving Agents](../architectures/self-evolving.md) | Agent modifies its own prompts and strategies based on performance feedback |
| 70 | [Nested Learning](https://github.com/saisrinivas-samoju/agentic_architectures/blob/main/mini-projects/70-nested-learning.ipynb) | [Nested Learning](../architectures/nested-learning.md) | Multi-timescale optimization with inner, middle, and outer learning loops |
