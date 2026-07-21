# Artifact Contracts

Use existing project formats when they contain equivalent information. Otherwise copy and adapt the templates under `assets/templates/`.

## Artifact menu

Default to a short product brief, an ordered next-bets list, repository-native tests, and a concise handoff. Add the following records only when they reduce meaningful uncertainty, preserve decisions across long pauses, support collaborators, or control material risk. One file may satisfy several contracts.

- **Slice record:** identity, entry type, interaction mode, state and owner, risk class/rationale/escalation triggers, authorization source, exact revision/dirty state, goal, value hypothesis/outcome signal, time/energy budget, scope, traceable criteria, assumptions, decisions, actors/independence, UX collaboration and evidence for user-facing work, impacts, implementation readiness, TDD evidence/exception, required and obtained evidence, gates, acceptance, residual risks, next transition.
- **Requirements:** goals, stakeholders, context, constraints, quality needs, functional requirements, glossary, traceability, decisions, approval history.
- **User persona and agent context:** target segment, context, goals, behaviors, constraints, capabilities/accessibility needs, exclusions, evidence/assumption labels with source/date/confidence, contradictions, bounded User Agent missions, learning history, initial Requirements Engineer and UX authorship, and current UX owner.
- **Architecture:** context, constraints, quality attributes, boundaries, runtime/deployment views, cross-cutting decisions, risks/debt, ADR links.
- **ADR:** status, context, decision, alternatives, consequences, evidence.
- **Documentation impact map:** artifact, impact, status (`pending-review`, `update-required`, `updated`, `reviewed-unchanged`, or `not-applicable`), reason, owner/evidence.
- **Experiment record:** problem or opportunity, target users, intended outcome (utility, learning, community, revenue, or craft), hypothesis, evidence confidence, method, success/invalidation thresholds, guardrails, telemetry, result, decision, and disposal or productionization plan.
- **Context snapshot:** product/users, source-linked rules, stack/versions, architecture boundaries, security/privacy, commands, deployment/recovery, and unresolved conflicts; omit when authoritative repository guidance is already concise.
- **Course correction:** new evidence, invalidated item, value/scope/risk effects, preserved and discarded work, new authority, updated readiness, and gates to repeat.
- **Threat/privacy assessment:** assets/data, trust boundaries, threats, controls, verification, residual risks and acceptance, plus the increment's dated runtime/toolchain, direct-library, and framework currency check and update dispositions.
- **Acceptance record:** revision, criteria, environment, observations, result, rejection evidence, approver/date.
- **Handoff/PR:** scope, decisions, evidence, documentation, operations, recurring cost, maintenance expectations, residual risks, acceptance.

Keep one source of truth for each fact and link rather than duplicate. Stable identifiers should connect requirements, acceptance criteria, tests, ADRs, and evidence.

When a specialist skill contributes, record its name, bounded role, inputs, revision, output/evidence, permitted mutations, and independence label in the existing increment or review record rather than creating a parallel source of truth.
