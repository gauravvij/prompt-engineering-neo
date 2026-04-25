# Prompt Engineering Evaluation with Neo

A comprehensive evaluation of prompting techniques (zero-shot, few-shot, chain-of-thought) on BBH-inspired hard reasoning problems, built entirely with Neo - an autonomous AI engineering agent.

## Overview

This repository contains:
- **24 hard reasoning problems** across 8 categories (Dyck-4, Object Tracking, Web of Lies, MATH Algebra, Navigation, Temporal Reasoning, Geometric Proofs, Long-horizon Arithmetic)
- **Experimental framework** comparing zero-shot, few-shot, and chain-of-thought prompting
- **72 experimental results** from Claude Sonnet 4.6
- **Publication-quality visualizations** (6 charts showing accuracy, cost, latency, token usage, trade-offs)
- **Technical blog post** with grounded findings and historical analysis

## Key Findings

| Strategy | Accuracy | Avg Latency | Total Cost |
|----------|----------|-------------|------------|
| Zero-shot | **87.5%** (21/24) | 6.59s | $0.119 |
| Few-shot | **91.7%** (22/24) | 7.16s | $0.160 |
| Chain-of-Thought | **91.7%** (22/24) | 8.15s | $0.256 |

**Insights:**
- Modern models (Claude Sonnet 4.6) are remarkably capable even on hard BBH problems
- Few-shot and CoT provide modest accuracy gains (4.2%) but at higher cost
- CoT costs 2.1x more than zero-shot - use when interpretability matters
- Dyck-4 and Long-horizon Arithmetic were most challenging (67% accuracy)

## Repository Structure

```
prompt-engineering-neo/
├── blog_post.md              # Complete technical deep dive (30K+ words)
├── experiment.py             # Main experiment script with 24 BBH problems
├── results.json              # 72 experimental results (24 problems × 3 strategies)
├── generate_visual_charts.py # Chart generation code
├── analysis.md               # Detailed metrics and breakdowns
├── research_notes.md         # Historical research with verified citations
├── charts/                   # PNG visualizations
│   ├── accuracy_comparison.png
│   ├── category_accuracy.png
│   ├── cost_comparison.png
│   ├── latency_comparison.png
│   ├── token_usage.png
│   └── tradeoff_triangle.png
├── plans/                    # Execution plans
│   └── plan_hard_problems.md
└── README.md                 # This file
```

## Quick Start

### Prerequisites

- Python 3.8+
- OpenRouter API key (or other LLM provider)

### Installation

```bash
# Clone the repository
git clone https://github.com/gauravvij/prompt-engineering-neo.git
cd prompt-engineering-neo

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install requests matplotlib numpy

# Set up API key
export OPENROUTER_API_KEY="your-api-key-here"
```

### Running the Experiment

```bash
# Run the full experiment (72 API calls)
python experiment.py

# Generate visualizations
python generate_visual_charts.py

# View results
cat results.json
```

### Viewing the Blog

Open `blog_post.md` in any Markdown viewer or editor. The blog contains:
- Historical evolution of prompt engineering (GPT-2 to 2026)
- Experimental findings with data-backed claims
- Analysis of what drives prompt quality
- Claude-specific pipeline patterns (chaining, routing, evaluator-optimizer)
- Case study on how this evaluation was built with Neo

## Extending This Work

This evaluation was built entirely with Neo - an autonomous AI engineering agent. You can extend it by prompting Neo with any of these directions:

### 1. Test Different Models

```
Clone https://github.com/gauravvij/prompt-engineering-neo.git and modify 
the experiment to test GPT-4, Llama 3, and Gemini on the same BBH problems. 
Compare how different model families respond to prompting strategies.
```

### 2. Add New Problem Categories

```
Clone https://github.com/gauravvij/prompt-engineering-neo.git and extend 
the experiment with new BBH categories: causal reasoning, word sorting, 
multistep arithmetic with negative numbers. Design 3 problems per category 
with ground truth answers.
```

### 3. Test Advanced Techniques

```
Clone https://github.com/gauravvij/prompt-engineering-neo.git and add 
ReAct and Tree-of-Thought prompting to the comparison. Implement tool use 
for the navigation problems and deliberate search for Web of Lies puzzles.
```

### 4. Build a Prompt Optimization Pipeline

```
Clone https://github.com/gauravvij/prompt-engineering-neo.git and create 
an automated prompt optimizer that tests variations: different example 
orderings, varying context placement, role assignment phrasing. Use the 
BBH problems as a benchmark.
```

### 5. Create a Production Evaluation Suite

```
Clone https://github.com/gauravvij/prompt-engineering-neo.git and refactor 
the experiment into a reusable evaluation framework with configuration files, 
parallel execution, and standardized output format.
```

## How This Was Built

This entire evaluation was produced by Neo through autonomous iteration:

1. **Research Phase**: Neo searched arXiv, Anthropic docs, and OpenAI cookbooks to identify BBH as the right benchmark
2. **Initial Experiment**: Neo designed toy problems (Game of 24, simple logic) - they were too easy (100% zero-shot)
3. **Redesign**: Neo researched genuinely hard problems (Dyck-4, 15-swap tracking) and created 24 BBH-inspired problems
4. **Execution**: Neo ran 72 API calls, analyzed results, and generated 6 publication-quality charts
5. **Documentation**: Neo wrote the technical blog with grounded claims backed by actual data

The key insight: Neo handles implementation details so you can focus on experimental design and analysis.

## Technical Details

### Problem Categories

1. **Dyck-4 Language**: Complete nested bracket sequences (e.g., `<{[(` → `)]}>`)
2. **Object Tracking**: Follow 6 objects through 12-15 swap operations
3. **Web of Lies**: Boolean logic with 6-8 interdependent statements
4. **MATH Algebra**: Competition-level problems requiring 5+ steps
5. **Complex Navigation**: 20+ directional steps with obstacles
6. **Temporal Reasoning**: Multi-constraint scheduling
7. **Geometric Proof**: Deductive reasoning steps
8. **Long-horizon Arithmetic**: 6+ nested operations

### Prompting Strategies

- **Zero-shot**: Direct question without examples
- **Few-shot**: 3 simpler examples of same problem type
- **Chain-of-Thought**: 3 examples with explicit step-by-step reasoning

### Metrics Tracked

- Accuracy per strategy and per category
- Latency (seconds per query)
- Token usage (prompt vs completion)
- Cost (based on OpenRouter pricing)

## Citations

This work builds on:
- BBH (BIG-Bench Hard): Suzgun et al., 2022
- Chain-of-Thought: Wei et al., 2022
- Few-shot learning: Brown et al., 2020
- The Prompt Report: Schulhoff et al., 2024

See `blog_post.md` for complete references.

## License

MIT License - Feel free to use, extend, and build upon this work.

## About Neo

Neo is a fully autonomous AI engineering agent capable of:
- Fine-tuning and evaluating AI models
- Building and deploying AI pipelines (RAG, classical ML, etc.)
- Running end-to-end experiments from a single prompt
- Generating publication-quality analysis and visuals

Available as a VS Code extension, Cursor plugin, or standalone tool.

---

**Built with Neo. Prompted by humans. Executed autonomously.**
