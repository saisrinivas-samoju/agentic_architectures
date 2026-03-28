# Architecture Selection Guide

Use these decision frameworks to pick the right architecture. Each flowchart covers one Part of this guide.

---

## Master Decision: Where to Start

```mermaid
flowchart LR
    Q1[Start here] --> Q2{How many agents?}
    Q2 -->|One| S1["Part I: Core Patterns<br/>(1-10)"]
    Q2 -->|Multiple| Q3{Need formal<br/>collaboration?}
    Q3 -->|Yes| S2["Part IV: Collaboration<br/>(19-26)"]
    Q3 -->|No, just infrastructure| S3["Part XII: Infrastructure<br/>(59-62)"]

    S1 --> Q4{Need quality gates?}
    Q4 -->|Yes| S4["Part II: Quality<br/>(11-13)"]
    Q4 -->|No| Q5{Need parallelism?}
    Q5 -->|Yes| S5["Part III: Pipelines<br/>(14-18)"]
    Q5 -->|No| Q6{Need memory?}
    S4 --> Q6
    S5 --> Q6
    Q6 -->|Yes| S6["Part X: Memory<br/>(46-52)"]
    Q6 -->|No| Q7{Need safety?}
    S6 --> Q7
    Q7 -->|Always yes in prod| S7["Part XI: Safety<br/>(53-58)"]
    S7 --> DONE[Ship it!]

    style Q1 fill:#4CAF50,color:#fff
    style DONE fill:#4CAF50,color:#fff
    style S1 fill:#2196F3,color:#fff
    style S2 fill:#9C27B0,color:#fff
    style S3 fill:#009688,color:#fff
    style S4 fill:#FF9800,color:#fff
    style S5 fill:#FF9800,color:#fff
    style S6 fill:#3F51B5,color:#fff
    style S7 fill:#F44336,color:#fff
```

---

## 1. Core Patterns (1–10): "What kind of agent system do I need?"

```mermaid
flowchart TD
    START[What's your task?] --> SINGLE{Single agent<br/>enough?}

    SINGLE -->|Yes| TOOLS{Needs external<br/>tools/APIs?}
    TOOLS -->|No| STEPS{Multi-step<br/>pipeline?}
    STEPS -->|Yes| PC[2. Prompt Chaining]
    STEPS -->|No| SIMPLE[Just use a plain LLM call]

    TOOLS -->|Yes| IMPROVE{Needs to improve<br/>its own output?}
    IMPROVE -->|No| REACT[1. ReAct]
    IMPROVE -->|Yes| CRITERIA{Has quantifiable<br/>scoring criteria?}
    CRITERIA -->|Yes| EO[8. Evaluator-Optimizer]
    CRITERIA -->|No| REFL[7. Reflection]

    SINGLE -->|No, need multiple agents| CLASSIFY{How do agents<br/>divide work?}

    CLASSIFY -->|Route input to the<br/>right specialist| ROUTE[3. Routing]
    CLASSIFY -->|Each processes<br/>independently| PAR[4. Parallelization]

    CLASSIFY -->|Agents coordinate<br/>together| CONTROL{Central<br/>controller?}

    CONTROL -->|Yes, one boss| PREDEFINED{Predefined agent<br/>assignments?}
    PREDEFINED -->|Yes| SUP[6. Supervisor]
    PREDEFINED -->|No, dynamic delegation| OW[5. Orchestrator-Worker]

    CONTROL -->|No, peer-to-peer| HANDOFF{Conversational<br/>handoffs?}
    HANDOFF -->|Yes| SWARM[9. Swarm]
    HANDOFF -->|No, nested teams| HIER[10. Hierarchical Teams]

    style START fill:#4CAF50,color:#fff
    style SIMPLE fill:#9E9E9E,color:#fff
    style PC fill:#2196F3,color:#fff
    style REACT fill:#2196F3,color:#fff
    style EO fill:#2196F3,color:#fff
    style REFL fill:#2196F3,color:#fff
    style ROUTE fill:#2196F3,color:#fff
    style PAR fill:#2196F3,color:#fff
    style OW fill:#2196F3,color:#fff
    style SUP fill:#2196F3,color:#fff
    style SWARM fill:#2196F3,color:#fff
    style HIER fill:#2196F3,color:#fff
```

---

## 2. Quality & Verification (11–13): "How should output be verified?"

```mermaid
flowchart TD
    START[Need output verification?] --> TYPE{Verification type?}

    TYPE -->|Objective: run code,<br/>check tests, pass/fail| GV[11. Generator-Verifier]
    TYPE -->|Subjective: LLM scores<br/>against rubric| JUDGE[12. Agent-as-a-Judge]
    TYPE -->|Human approval<br/>required| HITL[13. Human-in-the-Loop]

    style START fill:#4CAF50,color:#fff
    style GV fill:#FF9800,color:#fff
    style JUDGE fill:#FF9800,color:#fff
    style HITL fill:#FF9800,color:#fff
```

> **Already covered in Part I:** #7 Reflection (self-critique) and #8 Evaluator-Optimizer (scored iteration) are also quality patterns. Use Part II when you need *external* verification.

---

## 3. Parallelism & Pipelines (14–18): "How should work be distributed?"

```mermaid
flowchart TD
    START[Need parallel or<br/>pipeline execution?] --> INPUT{What varies?}

    INPUT -->|Large input needs<br/>chunking| MR[14. Map-Reduce]
    INPUT -->|Want model diversity<br/>for quality| MOA[15. Mixture-of-Agents]
    INPUT -->|Tasks have complex<br/>dependencies| DAG[16. DAG Orchestration]
    INPUT -->|Need explicit plan<br/>before execution| PE[17. Plan-and-Execute]
    INPUT -->|Want to minimize<br/>cost per query| CASC[18. Cascading Agents]

    style START fill:#4CAF50,color:#fff
    style MR fill:#FF9800,color:#fff
    style MOA fill:#FF9800,color:#fff
    style DAG fill:#FF9800,color:#fff
    style PE fill:#FF9800,color:#fff
    style CASC fill:#FF9800,color:#fff
```

---

## 4. Multi-Agent Collaboration (19–26): "How should agents work together?"

```mermaid
flowchart TD
    START[How should agents<br/>collaborate?] --> STRUCT{Communication<br/>structure?}

    STRUCT -->|Shared workspace,<br/>no direct communication| BB[19. Blackboard]
    STRUCT -->|Competitive bidding| BID{Formal protocol?}
    BID -->|Informal, market-style| MKT[20. Market-Based]
    BID -->|Formal FIPA protocol| CNP[21. Contract Net]

    STRUCT -->|Debate & argue| PURPOSE{Goal?}
    PURPOSE -->|Improve accuracy via<br/>disagreement| DEBATE[22. Debate]
    PURPOSE -->|Find vulnerabilities| RED[23. Red-Team]

    STRUCT -->|Structured roles &<br/>pipelines| FRAMEWORK{Preferred style?}
    FRAMEWORK -->|Fixed roles, persona-driven| CREW[24. Role-Based / CrewAI]
    FRAMEWORK -->|Open discussion, multi-turn| AUTOGEN[25. Conversational / AutoGen]

    STRUCT -->|Async event-driven| EVENT[26. Event-Driven]

    style START fill:#4CAF50,color:#fff
    style BB fill:#9C27B0,color:#fff
    style MKT fill:#9C27B0,color:#fff
    style CNP fill:#9C27B0,color:#fff
    style DEBATE fill:#9C27B0,color:#fff
    style RED fill:#9C27B0,color:#fff
    style CREW fill:#9C27B0,color:#fff
    style AUTOGEN fill:#9C27B0,color:#fff
    style EVENT fill:#9C27B0,color:#fff
```

---

## 5. Reasoning Patterns (27–30): "How should the agent think?"

```mermaid
flowchart TD
    START[How should the<br/>agent reason?] --> VIS{Should reasoning<br/>be visible to user?}

    VIS -->|No, hide internal thinking| IM[27. Inner Monologue]
    VIS -->|Yes / doesn't matter| SPEED{Latency critical?}
    SPEED -->|Yes, speculate on<br/>multiple paths| SE[28. Speculative Execution]
    SPEED -->|No| OUTPUT{Output type?}
    OUTPUT -->|Long structured document| SOT[29. Skeleton of Thought]
    OUTPUT -->|Problem needing<br/>multi-strategy exploration| REACTREE[30. ReAcTree]

    style START fill:#4CAF50,color:#fff
    style IM fill:#795548,color:#fff
    style SE fill:#795548,color:#fff
    style SOT fill:#795548,color:#fff
    style REACTREE fill:#795548,color:#fff
```

---

## 6. Domain Applications (31–34): "What domain am I working in?"

```mermaid
flowchart TD
    START[Domain-specific<br/>agent needed?] --> DOMAIN{What domain?}

    DOMAIN -->|Document Q&A,<br/>knowledge retrieval| ARAG[31. Agentic RAG]
    DOMAIN -->|Write, test,<br/>debug code| ACODE[32. Agentic Coding]
    DOMAIN -->|Need new tools<br/>at runtime| TTYPE{How?}
    TTYPE -->|Ad-hoc, on-the-fly| STA[33. Self-Tooling Agent]
    TTYPE -->|Systematic pipeline<br/>with testing| TF[34. ToolFactory]

    style START fill:#4CAF50,color:#fff
    style ARAG fill:#00BCD4,color:#fff
    style ACODE fill:#00BCD4,color:#fff
    style STA fill:#00BCD4,color:#fff
    style TF fill:#00BCD4,color:#fff
```

---

## 7–8. Cognitive Architectures & Advanced Search (35–41)

```mermaid
flowchart TD
    START[Need advanced<br/>reasoning?] --> TYPE{What kind?}

    TYPE -->|Combine LLM with<br/>formal logic/rules| PARADIGM{Always use both?}
    PARADIGM -->|Yes, both together| NS[35. Neuro-Symbolic]
    PARADIGM -->|Route: simple→neural,<br/>complex→symbolic| DP[36. Dual-Paradigm]

    TYPE -->|Systematic search<br/>over solution space| COMPLEXITY{Problem complexity?}
    COMPLEXITY -->|Very high, need<br/>backtracking| MCTS{Need reflection?}
    MCTS -->|No, standard MCTS| LATS[37. LATS]
    MCTS -->|Yes, per-simulation| IMCTS[38. I-MCTS]
    MCTS -->|Yes, cross-episode| RMCTS[39. R-MCTS]
    COMPLEXITY -->|Multi-agent search| COTS[40. CoTS]
    COMPLEXITY -->|Moderate, top-K paths| BEAM[41. Beam Search]

    style START fill:#4CAF50,color:#fff
    style NS fill:#607D8B,color:#fff
    style DP fill:#607D8B,color:#fff
    style LATS fill:#673AB7,color:#fff
    style IMCTS fill:#673AB7,color:#fff
    style RMCTS fill:#673AB7,color:#fff
    style COTS fill:#673AB7,color:#fff
    style BEAM fill:#673AB7,color:#fff
```

---

## 9. Agent Protocols (42–45): "How should agents connect?"

```mermaid
flowchart TD
    START[What connectivity<br/>do you need?] --> TYPE{Connecting to what?}

    TYPE -->|Tools, databases, APIs<br/>from a single agent| MCP[42. MCP]
    TYPE -->|Other agents from<br/>different vendors| SCALE{Scale?}
    SCALE -->|Enterprise,<br/>Google ecosystem| A2A[43. A2A Protocol]
    SCALE -->|Lightweight, REST-based,<br/>framework-agnostic| ACP[44. ACP]
    SCALE -->|Internet-scale, decentralized<br/>open marketplace| ANP[45. ANP]

    style START fill:#4CAF50,color:#fff
    style MCP fill:#E91E63,color:#fff
    style A2A fill:#E91E63,color:#fff
    style ACP fill:#E91E63,color:#fff
    style ANP fill:#E91E63,color:#fff
```

| Protocol | Created By | Transport | Best For | Maturity |
|---|---|---|---|---|
| **MCP** | Anthropic / Linux Foundation | JSON-RPC over stdio/SSE | Agent-to-tool | Production-ready |
| **A2A** | Google | HTTP + JSON-RPC | Agent-to-agent (enterprise) | Early adoption |
| **ACP** | IBM BeeAI | REST (HTTP verbs) | Agent-to-agent (lightweight) | Experimental |
| **ANP** | Community | DID + HTTP | Agent-to-agent (decentralized) | Research |

---

## 10. Agent Memory (46–52): "What should the agent remember?"

```mermaid
flowchart TD
    START[What does the agent<br/>need to remember?] --> WHAT{Type of information?}

    WHAT -->|Specific past events<br/>with timestamps| EP[46. Episodic Memory]
    WHAT -->|Facts, concepts,<br/>relationships| SEM[47. Semantic Memory]
    WHAT -->|How to do things<br/>— learned routines| PROC[48. Procedural Memory]
    WHAT -->|Interconnected notes<br/>with dynamic links| AMEM[49. Agentic Memory]
    WHAT -->|Shared knowledge across<br/>multiple agents| COLLAB[50. Collaborative Memory]
    WHAT -->|Past successful<br/>task trajectories| CER[51. CER]
    WHAT -->|Deciding what to<br/>remember or forget| META[52. Meta-Memory]

    EP -.->|Feeds into| SEM
    SEM -.->|Informs| PROC
    META -.->|Manages all| EP
    META -.->|Manages all| SEM

    style START fill:#4CAF50,color:#fff
    style EP fill:#3F51B5,color:#fff
    style SEM fill:#3F51B5,color:#fff
    style PROC fill:#3F51B5,color:#fff
    style AMEM fill:#3F51B5,color:#fff
    style COLLAB fill:#3F51B5,color:#fff
    style CER fill:#3F51B5,color:#fff
    style META fill:#3F51B5,color:#fff
```

> **Tip:** Real agents typically combine 2–3 memory types. Episodic + Semantic + Procedural mirrors the human memory system. Add Meta-Memory when scale requires selective forgetting.

---

## 11. Agent Safety (53–58): "What can go wrong and how do I prevent it?"

```mermaid
flowchart TD
    START[What failure mode<br/>are you defending against?] --> THREAT{Threat type?}

    THREAT -->|Harmful/toxic content| GA[53. Guardrail Agent]
    THREAT -->|External service outages| CB[54. Circuit Breaker]
    THREAT -->|Multi-step task fails midway| SAGA[55. Saga Pattern]
    THREAT -->|Unauthorized access| ACCESS{Scope?}
    ACCESS -->|Centralized validation| GW[56. API Gateway]
    ACCESS -->|Per-task scoped credentials| EI[57. Ephemeral Identity]
    THREAT -->|Tasks failing silently| DL[58. Dead Letter]

    style START fill:#4CAF50,color:#fff
    style GA fill:#F44336,color:#fff
    style CB fill:#F44336,color:#fff
    style SAGA fill:#F44336,color:#fff
    style GW fill:#F44336,color:#fff
    style EI fill:#F44336,color:#fff
    style DL fill:#F44336,color:#fff
```

> **Production checklist:** At minimum, every production agent needs: Guardrail (content) + Circuit Breaker (availability) + Dead Letter (observability). Add Saga for multi-step workflows, Gateway + Ephemeral Identity for multi-tenant systems.

---

## Quick Reference Table

| # | Architecture | Part | Complexity | Agents | Best For |
|---|---|---|---|---|---|
| 1 | **ReAct** | I | Low | 1 | Simple tool-augmented tasks |
| 2 | **Prompt Chaining** | I | Low | 1 | Sequential multi-step pipelines |
| 3 | **Routing** | I | Low-Med | 1+N | Multi-domain classification |
| 4 | **Parallelization** | I | Medium | N | Independent concurrent subtasks |
| 5 | **Orchestrator-Worker** | I | Med-High | 1+N | Unpredictable task decomposition |
| 6 | **Supervisor** | I | Med-High | 1+N | Coordinated multi-agent control |
| 7 | **Reflection** | I | Medium | 1-2 | Self-improving output quality |
| 8 | **Evaluator-Optimizer** | I | Medium | 2 | Scored quality iteration |
| 9 | **Swarm** | I | High | N | Conversational multi-domain handoffs |
| 10 | **Hierarchical Teams** | I | High | N | Large-scale enterprise workflows |
| 11 | **Generator-Verifier** | II | Medium | 2 | Execution-based verification (code, math) |
| 12 | **Agent-as-a-Judge** | II | Medium | 2 | One-shot quality evaluation & ranking |
| 13 | **Human-in-the-Loop** | II | Medium | 1+ | High-stakes approval workflows |
| 14 | **Map-Reduce** | III | Medium | N | Processing large documents/datasets |
| 15 | **Mixture-of-Agents** | III | High | N models | Maximum quality via model diversity |
| 16 | **DAG / Graph Orchestration** | III | Medium | N | Complex dependency workflows |
| 17 | **Plan-and-Execute** | III | Medium | 1 | Strategic multi-step tasks with replanning |
| 18 | **Cascading Agents** | III | Medium | 2-3 | Cost-optimized inference |
| 19 | **Blackboard** | IV | High | N | Incremental collaborative problem-solving |
| 20 | **Market-Based / Bidding** | IV | Medium | N | Dynamic self-organizing task allocation |
| 21 | **Contract Net Protocol** | IV | Medium | N | Formal task delegation with accountability |
| 22 | **Debate / Adversarial** | IV | Medium | 2-3 | Rigorous decision analysis |
| 23 | **Red-Team Agent** | IV | Medium | 2 | Security & safety testing |
| 24 | **Role-Based (CrewAI)** | IV | Medium | N | Persona-driven team pipelines |
| 25 | **Conversational (AutoGen)** | IV | Medium | N | Emergent group problem-solving |
| 26 | **Event-Driven Multi-Agent** | IV | High | N | Reactive async multi-agent systems |
| 27 | **Inner Monologue** | V | Low | 1 | Clean output with hidden reasoning |
| 28 | **Speculative Execution** | V | Medium | 1 | Low-latency branching decisions |
| 29 | **Skeleton of Thought** | V | Medium | 1 | Fast long-form generation |
| 30 | **ReAcTree** | V | High | 1 | Multi-strategy tree exploration |
| 31 | **Agentic RAG** | VI | Medium | 1 | Intelligent document retrieval |
| 32 | **Agentic Coding** | VI | Medium | 1 | Self-healing code generation |
| 33 | **Self-Tooling Agent** | VI | Medium | 1 | Runtime tool creation |
| 34 | **ToolFactory** | VI | Medium | 1 | Systematic tool generation pipeline |
| 35 | **Neuro-Symbolic** | VII | High | 1 | LLM + formal logic/rules |
| 36 | **Dual-Paradigm** | VII | Medium | 1 | System 1/System 2 routing |
| 37 | **LATS** | VIII | High | 1 | LLM + Monte Carlo Tree Search |
| 38 | **I-MCTS** | VIII | High | 1 | Per-simulation introspective search |
| 39 | **R-MCTS** | VIII | High | 1 | Cross-episode reflective search |
| 40 | **CoTS** | VIII | High | N | Multi-agent collaborative tree search |
| 41 | **Beam Search** | VIII | Medium | 1 | Top-K solution exploration |
| 42 | **MCP** | IX | Low | — | Tool integration standard |
| 43 | **A2A** | IX | Medium | — | Cross-vendor agent communication |
| 44 | **ACP** | IX | Medium | — | Framework-agnostic agent messaging |
| 45 | **ANP** | IX | High | — | Internet-scale agent networking |
| 46 | **Episodic Memory** | X | Medium | 1+ | Learning from past experiences |
| 47 | **Semantic Memory** | X | Medium | 1+ | Storing facts and relationships |
| 48 | **Procedural Memory** | X | Medium | 1+ | Remembering how to do tasks |
| 49 | **Agentic Memory (A-MEM)** | X | High | 1+ | Interconnected knowledge notes |
| 50 | **Collaborative Memory** | X | Medium | N | Shared team knowledge |
| 51 | **CER** | X | Medium | 1+ | Prioritized experience replay |
| 52 | **Meta-Memory** | X | High | 1+ | Memory system optimization |
| 53 | **Guardrail Agent** | XI | Low | 1+ | Content safety filtering |
| 54 | **Circuit Breaker** | XI | Low | 1+ | Preventing cascading failures |
| 55 | **Saga Pattern** | XI | Medium | 1 | Multi-step rollback |
| 56 | **API Gateway** | XI | Low | N | Centralized access control |
| 57 | **Ephemeral Identity** | XI | Medium | N | Least-privilege agent execution |
| 58 | **Dead Letter** | XI | Low | 1+ | Handling failed tasks |
| 59 | **Agentic Mesh** | XII | High | N | Enterprise multi-agent infrastructure |
| 60 | **Agent Registry** | XII | Medium | N | Large-scale agent management |
| 61 | **Agent Control Plane** | XII | High | N | Agent governance and lifecycle |
| 62 | **Data Flywheel** | XII | Medium | 1+ | Continuous improvement from usage |
| 63 | **VLA Models** | XIII | Very High | 1 | Vision + language + robot actions |
| 64 | **Embodied AI** | XIII | Very High | 1 | Physical world agents |
| 65 | **World Models** | XIII | Very High | 1 | Internal environment simulation |
| 66 | **CoALA** | XIV | — | — | Agent architecture taxonomy |
| 67 | **AEGIS Framework** | XIV | High | 1+ | Comprehensive layered safety |
| 68 | **ADAS** | XIV | High | Meta | Automated agent design search |
| 69 | **MASE** | XIV | High | 1+ | Self-evolving agents |
| 70 | **Nested Learning** | XIV | High | 1 | Multi-timescale optimization |
