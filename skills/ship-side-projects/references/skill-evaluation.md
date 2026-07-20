# Skill Behavioral Evaluation

Use clean agents to evaluate whether this skill produces its intended decisions under realistic pressure. Give each agent the skill and raw scenario only; do not disclose the expected result or prior diagnosis.

For each case under `assets/evaluations/`:

1. Capture the agent response and any emitted artifacts.
2. Assess every `must` and `must_not` invariant with evidence from the response.
3. Treat inconsistent, ambiguous, or context-leaking success as a failure to investigate.
4. Tighten the smallest relevant instruction, rerun with a fresh agent, and check that other cases do not regress.

Behavioral evaluation demonstrates instruction effectiveness, not correctness of a real product change. Keep fixtures free of secrets and production mutations.

