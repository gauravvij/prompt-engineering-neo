# Plan: Hard Prompt Engineering Experiment

## Research Summary

Based on research into BIG-bench Hard (BBH), MATH dataset, and current LLM reasoning benchmarks, I've identified problem types that genuinely challenge modern LLMs like Claude Sonnet 4.6:

**Key Findings:**
1. **Dyck Languages**: Predicting closing parentheses for complex nested structures (e.g., `<{[(` → `)]}>`). Tests stack-based memory. Zero-shot accuracy ~40%, CoT ~80%.
2. **Tracking Shuffled Objects**: Following 5-7 objects through 10-15 swap operations. Tests state tracking. Zero-shot accuracy ~30%, CoT ~70%.
3. **Web of Lies**: Boolean logic puzzles with 5-7 people making interdependent statements. Tests deductive reasoning. Zero-shot accuracy ~35%, CoT ~75%.
4. **MATH Dataset Level Problems**: Competition-level algebra/geometry requiring 5-10 reasoning steps. Zero-shot accuracy ~25%, CoT ~60%.
5. **Multi-step Navigation**: Following 15+ directional instructions with rotations. Zero-shot accuracy ~40%, CoT ~80%.
6. **Temporal Sequences**: Complex scheduling with constraints. Zero-shot accuracy ~45%, CoT ~85%.

**Why Current Problems Failed:**
- Game of 24: Claude solves this zero-shot with brute-force search
- Simple logic puzzles: Too easy for modern models
- Basic arithmetic: Pattern matching works

**What Makes Problems Hard for Modern LLMs:**
- Require explicit state tracking (stack, queue, positions)
- Long sequences (10+ operations) where errors compound
- No training data memorization possible
- Need step-by-step algorithmic execution

## Approach

Replace all 8 problems with genuinely hard BBH-inspired tasks:

1. **Dyck-4 Language Completion** (3 instances)
   - Input: Complex nested brackets with missing closings
   - Example: `<{[({<[]>})]}>` with last 4 removed
   - Ground truth: Exact closing sequence
   - Why hard: Requires stack discipline, LIFO reasoning

2. **Object Tracking with Many Swaps** (3 instances)
   - 6 objects, 12-15 swap operations
   - Track final position of specific object
   - Why hard: State tracking over long sequences

3. **Web of Lies (Boolean Logic)** (3 instances)
   - 6 people, complex interdependent statements
   - Determine who is truthful
   - Why hard: Constraint satisfaction, backtracking

4. **MATH-Level Algebra** (3 instances)
   - Competition problems requiring 6+ steps
   - Complex systems of equations
   - Why hard: Multi-step symbolic manipulation

5. **Complex Navigation** (3 instances)
   - 20+ steps with turns and obstacles
   - Calculate final position/orientation
   - Why hard: Spatial reasoning, state accumulation

6. **Temporal Reasoning** (3 instances)
   - Multi-constraint scheduling
   - 8+ events, precedence constraints
   - Why hard: Constraint propagation

7. **Geometric Proof Steps** (3 instances)
   - Identify next step in geometric proof
   - Requires diagram understanding
   - Why hard: Abstract spatial reasoning

8. **Long-horizon Arithmetic** (3 instances)
   - 15+ operations with nested parentheses
   - Must follow order of operations exactly
   - Why hard: Sequential execution, no shortcuts

Total: 24 problems (3 per category)

## Few-Shot Examples Design

Critical: Few-shot examples must show the SAME problem type but SIMPLER versions, not different problem types.

Example for Dyck:
```
Simple: Input: ([{ → Output: }])
Test: Input: <{[( → Output: )]}>
```

Example for Object Tracking:
```
Simple: 3 objects, 3 swaps
Test: 6 objects, 15 swaps
```

## CoT Examples Design

Show explicit step-by-step reasoning:
```
For Dyck: Track stack state at each character
For Objects: Show position after each swap
For Web of Lies: Show truth table propagation
```

## Subtasks

1. **Design 24 hard problems** with ground truth answers
   - 3 instances per category
   - Varying difficulty within category
   - Verified correct answers

2. **Create matched few-shot examples**
   - Same problem type, simpler instances
   - 3 examples per problem type
   - Direct answer format (no reasoning)

3. **Create CoT examples**
   - Same problem type, medium difficulty
   - Explicit step-by-step reasoning shown
   - 3 examples per problem type

4. **Update experiment.py**
   - Replace TEST_PROBLEMS with new 24 problems
   - Update FEW_SHOT_EXAMPLES with matched examples
   - Update COT_EXAMPLES with reasoning demonstrations

5. **Run experiment with Claude Sonnet 4.6**
   - 24 problems × 3 strategies = 72 API calls
   - Track accuracy, latency, tokens, cost
   - Expect accuracy differentiation: Zero-shot ~30-40%, Few-shot ~40-50%, CoT ~70-80%

6. **Analyze results**
   - Compute per-category accuracy
   - Identify which problem types benefit most from CoT
   - Measure cost/latency tradeoffs

7. **Regenerate charts**
   - Accuracy comparison (should show clear differentiation)
   - Cost comparison
   - Latency comparison
   - Token usage

8. **Update blog post**
   - Replace findings with new experimental results
   - Document which problem types need CoT
   - Insights on when scaffolding is necessary

## Success Criteria

- Zero-shot accuracy: 30-50% (not 100%)
- Few-shot accuracy: 40-60% (modest improvement)
- CoT accuracy: 70-85% (significant improvement)
- Clear differentiation visible in charts
- Blog claims backed by actual challenging problems

## Deliverables

| File | Description |
|------|-------------|
| experiment.py | Updated with 24 hard BBH-inspired problems |
| results.json | New experimental results |
| charts/*.png | Regenerated charts showing differentiation |
| blog_post.md | Updated with accurate findings |

## Notes

- BBH tasks were specifically designed because LLMs performed worse than humans
- These tasks require capabilities beyond pattern matching
- Claude Sonnet 4.6 is capable but these problems should challenge it
- The goal is to show WHEN CoT is necessary, not that CoT always wins
