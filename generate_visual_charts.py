#!/usr/bin/env python3
"""
Generate publication-quality visual charts from BBH-inspired experiment results.
Saves charts as PNG files for embedding in the blog post.
"""

import json
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import os

# Set non-interactive backend for headless environments
matplotlib.use('Agg')

# Color palette - professional, accessible colors
COLORS = {
    'zero_shot': '#2E86AB',      # Deep blue
    'few_shot': '#A23B72',       # Magenta
    'chain_of_thought': '#F18F01',  # Orange
    'background': '#FAFAFA',
    'grid': '#E0E0E0',
    'text': '#333333'
}

def load_results():
    """Load experiment results from JSON file."""
    filepath = '/home/azureuser/prompt_engineering/results.json'
    with open(filepath, 'r') as f:
        return json.load(f)

def create_accuracy_comparison_chart(results):
    """Generate accuracy comparison bar chart."""
    strategies = results['strategies']
    
    labels = ['Zero-Shot', 'Few-Shot', 'Chain-of-Thought']
    accuracies = [
        strategies['zero-shot']['summary']['accuracy'] * 100,
        strategies['few-shot']['summary']['accuracy'] * 100,
        strategies['chain-of-thought']['summary']['accuracy'] * 100
    ]
    
    colors = [COLORS['zero_shot'], COLORS['few_shot'], COLORS['chain_of_thought']]
    
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=COLORS['background'])
    ax.set_facecolor(COLORS['background'])
    
    bars = ax.bar(labels, accuracies, color=colors, edgecolor='white', linewidth=1.5, width=0.6)
    
    # Add value labels on bars
    for bar, acc in zip(bars, accuracies):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{acc:.1f}%',
                ha='center', va='bottom', fontsize=12, fontweight='bold', color=COLORS['text'])
    
    ax.set_ylabel('Accuracy (%)', fontsize=12, fontweight='bold', color=COLORS['text'])
    ax.set_xlabel('Prompting Strategy', fontsize=12, fontweight='bold', color=COLORS['text'])
    ax.set_title('Accuracy Comparison: 24 BBH-Inspired Hard Problems\n(Claude Sonnet 4.6 via OpenRouter)', 
                 fontsize=14, fontweight='bold', color=COLORS['text'], pad=20)
    
    ax.set_ylim(0, 105)
    
    # Add annotation about accuracy gap
    ax.annotate('Few-shot & CoT show\nslight improvement', 
                xy=(1.5, (accuracies[1] + accuracies[2])/2), 
                xytext=(0.5, 70),
                fontsize=10, color=COLORS['chain_of_thought'],
                arrowprops=dict(arrowstyle='->', color=COLORS['chain_of_thought'], lw=1.5))
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.3, color=COLORS['grid'])
    
    plt.tight_layout()
    output_path = '/home/azureuser/prompt_engineering/charts/accuracy_comparison.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=COLORS['background'])
    plt.close()
    print(f"Saved: {output_path}")
    return output_path

def create_cost_comparison_chart(results):
    """Generate cost comparison bar chart."""
    strategies = results['strategies']
    
    labels = ['Zero-Shot', 'Few-Shot', 'Chain-of-Thought']
    costs = [
        strategies['zero-shot']['summary']['total_cost_usd'] * 1000,  # milli-dollars
        strategies['few-shot']['summary']['total_cost_usd'] * 1000,
        strategies['chain-of-thought']['summary']['total_cost_usd'] * 1000
    ]
    
    colors = [COLORS['zero_shot'], COLORS['few_shot'], COLORS['chain_of_thought']]
    
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=COLORS['background'])
    ax.set_facecolor(COLORS['background'])
    
    bars = ax.bar(labels, costs, color=colors, edgecolor='white', linewidth=1.5, width=0.6)
    
    # Add value labels on bars
    for bar, cost in zip(bars, costs):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{cost:.3f} m$',
                ha='center', va='bottom', fontsize=11, fontweight='bold', color=COLORS['text'])
    
    ax.set_ylabel('Total Cost (milli-dollars)', fontsize=12, fontweight='bold', color=COLORS['text'])
    ax.set_xlabel('Prompting Strategy', fontsize=12, fontweight='bold', color=COLORS['text'])
    ax.set_title('Cost Comparison: 24 BBH-Inspired Hard Problems\n(Claude Sonnet 4.6 via OpenRouter)', 
                 fontsize=14, fontweight='bold', color=COLORS['text'], pad=20)
    
    # Add annotation about cost multiplier
    if costs[2] > costs[0]:
        multiplier = costs[2] / costs[0]
        ax.annotate(f'CoT costs {multiplier:.1f}x more\nthan Zero-Shot', 
                    xy=(2, costs[2]), xytext=(1.5, costs[2] * 0.7),
                    fontsize=10, color=COLORS['chain_of_thought'],
                    arrowprops=dict(arrowstyle='->', color=COLORS['chain_of_thought'], lw=1.5))
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.3, color=COLORS['grid'])
    
    plt.tight_layout()
    output_path = '/home/azureuser/prompt_engineering/charts/cost_comparison.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=COLORS['background'])
    plt.close()
    print(f"Saved: {output_path}")
    return output_path

def create_latency_comparison_chart(results):
    """Generate latency comparison bar chart."""
    strategies = results['strategies']
    
    labels = ['Zero-Shot', 'Few-Shot', 'Chain-of-Thought']
    latencies = [
        strategies['zero-shot']['summary']['average_latency_seconds'],
        strategies['few-shot']['summary']['average_latency_seconds'],
        strategies['chain-of-thought']['summary']['average_latency_seconds']
    ]
    
    colors = [COLORS['zero_shot'], COLORS['few_shot'], COLORS['chain_of_thought']]
    
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=COLORS['background'])
    ax.set_facecolor(COLORS['background'])
    
    bars = ax.bar(labels, latencies, color=colors, edgecolor='white', linewidth=1.5, width=0.6)
    
    # Add value labels on bars
    for bar, lat in zip(bars, latencies):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{lat:.2f}s',
                ha='center', va='bottom', fontsize=11, fontweight='bold', color=COLORS['text'])
    
    ax.set_ylabel('Average Latency (seconds)', fontsize=12, fontweight='bold', color=COLORS['text'])
    ax.set_xlabel('Prompting Strategy', fontsize=12, fontweight='bold', color=COLORS['text'])
    ax.set_title('Latency Comparison: Average Response Time\n(Claude Sonnet 4.6 via OpenRouter)', 
                 fontsize=14, fontweight='bold', color=COLORS['text'], pad=20)
    
    # Add annotation
    if latencies[2] > latencies[0]:
        pct_increase = ((latencies[2] - latencies[0]) / latencies[0]) * 100
        ax.annotate(f'CoT adds {pct_increase:.0f}% latency\nvs Zero-Shot', 
                    xy=(2, latencies[2]), xytext=(1.5, latencies[2] * 0.85),
                    fontsize=10, color=COLORS['chain_of_thought'],
                    arrowprops=dict(arrowstyle='->', color=COLORS['chain_of_thought'], lw=1.5))
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.3, color=COLORS['grid'])
    
    plt.tight_layout()
    output_path = '/home/azureuser/prompt_engineering/charts/latency_comparison.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=COLORS['background'])
    plt.close()
    print(f"Saved: {output_path}")
    return output_path

def create_token_usage_chart(results):
    """Generate token usage stacked bar chart."""
    strategies = results['strategies']
    
    labels = ['Zero-Shot', 'Few-Shot', 'Chain-of-Thought']
    
    # Calculate token breakdown
    prompt_tokens = [
        sum(r['tokens_prompt'] for r in strategies['zero-shot']['results']),
        sum(r['tokens_prompt'] for r in strategies['few-shot']['results']),
        sum(r['tokens_prompt'] for r in strategies['chain-of-thought']['results'])
    ]
    
    completion_tokens = [
        sum(r['tokens_completion'] for r in strategies['zero-shot']['results']),
        sum(r['tokens_completion'] for r in strategies['few-shot']['results']),
        sum(r['tokens_completion'] for r in strategies['chain-of-thought']['results'])
    ]
    
    fig, ax = plt.subplots(figsize=(10, 6), facecolor=COLORS['background'])
    ax.set_facecolor(COLORS['background'])
    
    x = range(len(labels))
    width = 0.6
    
    # Create stacked bars
    bars1 = ax.bar(x, prompt_tokens, width, label='Prompt Tokens', 
                   color='#5DADE2', edgecolor='white', linewidth=1.5)
    bars2 = ax.bar(x, completion_tokens, width, bottom=prompt_tokens, 
                   label='Completion Tokens', color='#E74C3C', edgecolor='white', linewidth=1.5)
    
    # Add total labels
    for i, (pt, ct) in enumerate(zip(prompt_tokens, completion_tokens)):
        total = pt + ct
        ax.text(i, total + 200, f'{total:,} tokens', 
                ha='center', va='bottom', fontsize=10, fontweight='bold', color=COLORS['text'])
    
    ax.set_ylabel('Total Tokens', fontsize=12, fontweight='bold', color=COLORS['text'])
    ax.set_xlabel('Prompting Strategy', fontsize=12, fontweight='bold', color=COLORS['text'])
    ax.set_title('Token Usage Breakdown: 24 BBH-Inspired Hard Problems\n(Claude Sonnet 4.6 via OpenRouter)', 
                 fontsize=14, fontweight='bold', color=COLORS['text'], pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(loc='upper left', framealpha=0.9)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.3, color=COLORS['grid'])
    
    plt.tight_layout()
    output_path = '/home/azureuser/prompt_engineering/charts/token_usage.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=COLORS['background'])
    plt.close()
    print(f"Saved: {output_path}")
    return output_path

def create_category_accuracy_chart(results):
    """Generate category-wise accuracy comparison."""
    strategies = results['strategies']
    
    # Get all categories
    categories = set()
    for strategy in strategies.values():
        for cat in strategy['summary']['category_breakdown']:
            categories.add(cat)
    categories = sorted(list(categories))
    
    # Prepare data
    x = np.arange(len(categories))
    width = 0.25
    
    zero_shot_acc = [strategies['zero-shot']['summary']['category_breakdown'].get(cat, {}).get('accuracy', 0) * 100 for cat in categories]
    few_shot_acc = [strategies['few-shot']['summary']['category_breakdown'].get(cat, {}).get('accuracy', 0) * 100 for cat in categories]
    cot_acc = [strategies['chain-of-thought']['summary']['category_breakdown'].get(cat, {}).get('accuracy', 0) * 100 for cat in categories]
    
    fig, ax = plt.subplots(figsize=(14, 7), facecolor=COLORS['background'])
    ax.set_facecolor(COLORS['background'])
    
    # Create grouped bars
    bars1 = ax.bar(x - width, zero_shot_acc, width, label='Zero-Shot', 
                   color=COLORS['zero_shot'], edgecolor='white', linewidth=1)
    bars2 = ax.bar(x, few_shot_acc, width, label='Few-Shot', 
                   color=COLORS['few_shot'], edgecolor='white', linewidth=1)
    bars3 = ax.bar(x + width, cot_acc, width, label='Chain-of-Thought', 
                   color=COLORS['chain_of_thought'], edgecolor='white', linewidth=1)
    
    # Format category labels
    cat_labels = [cat.replace('_', ' ').title() for cat in categories]
    
    ax.set_ylabel('Accuracy (%)', fontsize=12, fontweight='bold', color=COLORS['text'])
    ax.set_xlabel('Problem Category', fontsize=12, fontweight='bold', color=COLORS['text'])
    ax.set_title('Accuracy by Problem Category: BBH-Inspired Hard Problems\n(Claude Sonnet 4.6 via OpenRouter)', 
                 fontsize=14, fontweight='bold', color=COLORS['text'], pad=20)
    ax.set_xticks(x)
    ax.set_xticklabels(cat_labels, rotation=45, ha='right', fontsize=10)
    ax.legend(loc='upper right', framealpha=0.9)
    ax.set_ylim(0, 105)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(axis='y', alpha=0.3, color=COLORS['grid'])
    
    plt.tight_layout()
    output_path = '/home/azureuser/prompt_engineering/charts/category_accuracy.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=COLORS['background'])
    plt.close()
    print(f"Saved: {output_path}")
    return output_path

def create_tradeoff_triangle_chart(results):
    """Generate a scatter plot showing the accuracy/cost/latency tradeoff."""
    strategies = results['strategies']
    
    fig, ax = plt.subplots(figsize=(10, 7), facecolor=COLORS['background'])
    ax.set_facecolor(COLORS['background'])
    
    # Data points
    strategies_data = [
        ('Zero-Shot', strategies['zero-shot'], COLORS['zero_shot']),
        ('Few-Shot', strategies['few-shot'], COLORS['few_shot']),
        ('Chain-of-Thought', strategies['chain-of-thought'], COLORS['chain_of_thought'])
    ]
    
    for name, data, color in strategies_data:
        cost = data['summary']['total_cost_usd'] * 1000  # milli-dollars
        latency = data['summary']['average_latency_seconds']
        accuracy = data['summary']['accuracy'] * 100
        
        # Bubble size proportional to accuracy
        bubble_size = accuracy * 10
        ax.scatter(cost, latency, s=bubble_size, c=color, alpha=0.7, 
                   edgecolors='white', linewidths=2, label=f'{name} ({accuracy:.1f}%)')
        
        # Add label
        ax.annotate(name, (cost, latency), xytext=(5, 5), textcoords='offset points',
                   fontsize=11, fontweight='bold', color=COLORS['text'])
    
    ax.set_xlabel('Total Cost (milli-dollars)', fontsize=12, fontweight='bold', color=COLORS['text'])
    ax.set_ylabel('Average Latency (seconds)', fontsize=12, fontweight='bold', color=COLORS['text'])
    ax.set_title('The Prompt Engineering Trade-off Triangle\nCost vs Latency vs Accuracy (Bubble Size)', 
                 fontsize=14, fontweight='bold', color=COLORS['text'], pad=20)
    
    # Add explanatory text
    ax.text(0.95, 0.95, '24 BBH-Inspired Hard Problems\nDyck-4, Object Tracking, Web of Lies\nMATH Algebra, Navigation, Temporal\nGeometric Proof, Long-horizon Arithmetic', 
            transform=ax.transAxes, fontsize=9, verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor=COLORS['grid']))
    
    ax.legend(loc='upper left', framealpha=0.9, title='Strategy (Accuracy)')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.grid(alpha=0.3, color=COLORS['grid'])
    
    plt.tight_layout()
    output_path = '/home/azureuser/prompt_engineering/charts/tradeoff_triangle.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor=COLORS['background'])
    plt.close()
    print(f"Saved: {output_path}")
    return output_path

def main():
    """Generate all charts."""
    # Ensure charts directory exists
    charts_dir = '/home/azureuser/prompt_engineering/charts'
    os.makedirs(charts_dir, exist_ok=True)
    
    # Load results
    results = load_results()
    
    print("Generating visual charts from BBH experiment data...")
    print("=" * 50)
    
    # Generate all charts
    create_accuracy_comparison_chart(results)
    create_cost_comparison_chart(results)
    create_latency_comparison_chart(results)
    create_token_usage_chart(results)
    create_category_accuracy_chart(results)
    create_tradeoff_triangle_chart(results)
    
    print("=" * 50)
    print("All charts generated successfully!")
    print(f"Charts saved to: {charts_dir}/")
    print("\nGenerated files:")
    print("  - accuracy_comparison.png")
    print("  - cost_comparison.png")
    print("  - latency_comparison.png")
    print("  - token_usage.png")
    print("  - category_accuracy.png")
    print("  - tradeoff_triangle.png")

if __name__ == "__main__":
    main()
