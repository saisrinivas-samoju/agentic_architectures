# Mini-Projects

Each architecture is accompanied by a hands-on Jupyter notebook that demonstrates the pattern with a practical real-world use case.

## Notebooks

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

## Running the Notebooks

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
# Install dependencies
uv sync --group dev

# Launch Jupyter
uv run jupyter notebook mini-projects/
```
