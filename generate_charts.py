#!/usr/bin/env python3
"""
Generate ASCII charts and analysis from experiment results.
"""

import json
import os

def load_results():
    with open('/home/azureuser/prompt_engineering/results.json', 'r') as f:
        return json.load(f)

def generate_ascii_bar_chart(data, labels, title, width=50):
    """Generate an ASCII bar chart."""
    max_val = max(data)
    lines = [f"\n{title}", "=" * len(title)]
    
    for label, value in zip(labels, data):
        bar_len = int((value / max_val) * width) if max_val > 0 else 0
        bar = "█" * bar_len
        lines.append(f"{label:20} | {bar} {value:.3f}")
    
    return "\n".join(lines)

def generate_comparison_table(results):
    """Generate a markdown comparison table."""
    strategies = results['strategies']
    
    table = """| Metric | Zero-Shot | Few-Shot | Chain-of-Thought |
|--------|-----------|----------|------------------|
"""
    
    # Accuracy
    acc_zs = strategies['zero-shot']['summary']['accuracy'] * 100
    acc_fs = strategies['few-shot']['summary']['accuracy'] * 100
    acc_cot = strategies['chain-of-thought']['summary']['accuracy'] * 100
    table += f"| Accuracy (%) | {acc_zs:.1f}% | {acc_fs:.1f}% | {acc_cot:.1f}% |\n"
    
    # Average Latency
    lat_zs = strategies['zero-shot']['summary']['average_latency_seconds']
    lat_fs = strategies['few-shot']['summary']['average_latency_seconds']
    lat_cot = strategies['chain-of-thought']['summary']['average_latency_seconds']
    table += f"| Avg Latency (s) | {lat_zs:.2f}s | {lat_fs:.2f}s | {lat_cot:.2f}s |\n"
    
    # Total Cost
    cost_zs = strategies['zero-shot']['summary']['total_cost_usd'] * 1000  # Convert to milli
    cost_fs = strategies['few-shot']['summary']['total_cost_usd'] * 1000
    cost_cot = strategies['chain-of-thought']['summary']['total_cost_usd'] * 1000
    table += f"| Total Cost (m$) | {cost_zs:.3f}m$ | {cost_fs:.3f}m$ | {cost_cot:.3f}m$ |\n"
    
    # Token Usage
    tok_zs = sum(r['tokens_prompt'] + r['tokens_completion'] for r in strategies['zero-shot']['results'])
    tok_fs = sum(r['tokens_prompt'] + r['tokens_completion'] for r in strategies['few-shot']['results'])
    tok_cot = sum(r['tokens_prompt'] + r['tokens_completion'] for r in strategies['chain-of-thought']['results'])
    table += f"| Total Tokens | {tok_zs} | {tok_fs} | {tok_cot} |\n"
    
    return table

def generate_latency_breakdown(results):
    """Generate latency breakdown per problem."""
    strategies = results['strategies']
    
    table = """| Problem | Zero-Shot | Few-Shot | Chain-of-Thought |
|---------|-----------|----------|------------------|
"""
    
    for i in range(5):
        prob_id = i + 1
        lat_zs = strategies['zero-shot']['results'][i]['latency_seconds']
        lat_fs = strategies['few-shot']['results'][i]['latency_seconds']
        lat_cot = strategies['chain-of-thought']['results'][i]['latency_seconds']
        table += f"| Problem {prob_id} | {lat_zs:.2f}s | {lat_fs:.2f}s | {lat_cot:.2f}s |\n"
    
    return table

def generate_cost_breakdown(results):
    """Generate cost breakdown per problem."""
    strategies = results['strategies']
    
    table = """| Problem | Zero-Shot | Few-Shot | Chain-of-Thought |
|---------|-----------|----------|------------------|
"""
    
    for i in range(5):
        prob_id = i + 1
        cost_zs = strategies['zero-shot']['results'][i]['estimated_cost_usd'] * 1000000  # microdollars
        cost_fs = strategies['few-shot']['results'][i]['estimated_cost_usd'] * 1000000
        cost_cot = strategies['chain-of-thought']['results'][i]['estimated_cost_usd'] * 1000000
        table += f"| Problem {prob_id} | {cost_zs:.1f}µ$ | {cost_fs:.1f}µ$ | {cost_cot:.1f}µ$ |\n"
    
    return table

def generate_ascii_latency_chart(results):
    """Generate ASCII bar chart for latency comparison."""
    strategies = results['strategies']
    
    labels = ['Zero-Shot', 'Few-Shot', 'Chain-of-Thought']
    latencies = [
        strategies['zero-shot']['summary']['average_latency_seconds'],
        strategies['few-shot']['summary']['average_latency_seconds'],
        strategies['chain-of-thought']['summary']['average_latency_seconds']
    ]
    
    return generate_ascii_bar_chart(latencies, labels, "Average Latency by Strategy (seconds)")

def generate_ascii_cost_chart(results):
    """Generate ASCII bar chart for cost comparison."""
    strategies = results['strategies']
    
    labels = ['Zero-Shot', 'Few-Shot', 'Chain-of-Thought']
    costs = [
        strategies['zero-shot']['summary']['total_cost_usd'] * 1000,  # millicents
        strategies['few-shot']['summary']['total_cost_usd'] * 1000,
        strategies['chain-of-thought']['summary']['total_cost_usd'] * 1000
    ]
    
    return generate_ascii_bar_chart(costs, labels, "Total Cost by Strategy (milli-dollars)")

def main():
    results = load_results()
    
    output = """# Prompt Engineering Experiment Analysis

## Experiment Overview

This analysis compares three prompting strategies on complex reasoning tasks using Claude Sonnet 4.6 via OpenRouter API.

**Model:** anthropic/claude-sonnet-4.6  
**Problems:** 5 cognitive reasoning tasks (bat/ball problem, lily pad problem, etc.)  
**Strategies Tested:**
- Zero-Shot: Direct question without examples
- Few-Shot: Question with 2 example solutions
- Chain-of-Thought: Question with step-by-step reasoning examples

---

## Summary Comparison

"""
    
    output += generate_comparison_table(results)
    
    output += """

---

## Latency Analysis

### Per-Problem Latency Breakdown

"""
    
    output += generate_latency_breakdown(results)
    
    output += """

### Visual Comparison

"""
    output += generate_ascii_latency_chart(results)
    
    output += """

**Key Finding:** Zero-shot prompting is significantly faster (1.35s avg) compared to Few-shot (3.68s) and Chain-of-Thought (4.05s). This is expected as structured prompting requires more token generation.

---

## Cost Analysis

### Per-Problem Cost Breakdown (micro-dollars)

"""
    
    output += generate_cost_breakdown(results)
    
    output += """

### Visual Comparison

"""
    output += generate_ascii_cost_chart(results)
    
    output += """

**Key Finding:** Zero-shot is most cost-effective at 0.365m$ total, while Chain-of-Thought costs 15x more (5.472m$) due to longer output generation. Few-shot sits in the middle at 4.273m$.

---

## Accuracy Analysis

All three strategies achieved 100% accuracy on the test problems. This suggests that for these particular reasoning tasks with Claude Sonnet 4.6:

1. **Zero-shot** is sufficient for basic reasoning
2. **Few-shot** and **Chain-of-Thought** provide more detailed explanations but same correctness
3. The model demonstrates strong inherent reasoning capabilities

---

## Token Usage Analysis

"""
    
    strategies = results['strategies']
    tok_zs = sum(r['tokens_prompt'] + r['tokens_completion'] for r in strategies['zero-shot']['results'])
    tok_fs = sum(r['tokens_prompt'] + r['tokens_completion'] for r in strategies['few-shot']['results'])
    tok_cot = sum(r['tokens_prompt'] + r['tokens_completion'] for r in strategies['chain-of-thought']['results'])
    
    output += f"""| Strategy | Total Tokens | Prompt Tokens | Completion Tokens |
|----------|--------------|---------------|-------------------|
| Zero-Shot | {tok_zs} | {sum(r['tokens_prompt'] for r in strategies['zero-shot']['results'])} | {sum(r['tokens_completion'] for r in strategies['zero-shot']['results'])} |
| Few-Shot | {tok_fs} | {sum(r['tokens_prompt'] for r in strategies['few-shot']['results'])} | {sum(r['tokens_completion'] for r in strategies['few-shot']['results'])} |
| Chain-of-Thought | {tok_cot} | {sum(r['tokens_prompt'] for r in strategies['chain-of-thought']['results'])} | {sum(r['tokens_completion'] for r in strategies['chain-of-thought']['results'])} |
"""
    
    output += """

**Key Finding:** Chain-of-Thought uses 4.7x more completion tokens than Zero-shot due to step-by-step output generation.

---

## Key Insights for Prompt Engineering

1. **Trade-off Triangle:** There is a clear trade-off between speed, cost, and explainability. Zero-shot is fast and cheap but provides minimal reasoning transparency. Chain-of-Thought is slower and more expensive but produces interpretable reasoning steps.

2. **Context Matters:** Few-shot prompting added significant latency (+172%) and cost (+11.7x) compared to zero-shot, primarily due to longer prompts and more verbose outputs.

3. **Model Capability:** Claude Sonnet 4.6 handled all reasoning tasks correctly regardless of prompting strategy, suggesting strong baseline capabilities. The choice of strategy should depend on whether you need explanations (CoT) or just answers (Zero-shot).

4. **Token Efficiency:** Zero-shot used only 290 total tokens across 5 problems, while Chain-of-Thought used 2,186 tokens. For high-volume applications, this 7.5x difference matters significantly.

---

## Raw Data Reference

See `results.json` for complete experimental data including individual responses.

*Generated: """ + results['timestamp'] + """*
"""
    
    with open('/home/azureuser/prompt_engineering/analysis.md', 'w') as f:
        f.write(output)
    
    print("Analysis written to analysis.md")

if __name__ == "__main__":
    main()
