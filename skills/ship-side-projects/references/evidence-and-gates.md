# Evidence and Gates

## Risk-to-evidence matrix

For each material risk record:

| Risk/failure mode | Control or test | Command/artifact | Outcome | Residual risk |
|---|---|---|---|---|

Use one outcome: `passed`, `failed`, `not-applicable` with reason, or `not-run` with residual risk. Command output must reflect the final revision. Do not use an unrelated green test as evidence.

## Independence

- Prefer a separate qualified human or agent for quality/security gates when available, authorized, and proportionate.
- Give an independent verifier the acceptance criteria, risks, and raw artifact—not the implementer's desired conclusion.
- When separation is unavailable, perform a fresh requirements-led adversarial pass and label it `self-verified`.
- Never describe self-verification as independent assurance.

## Findings

Tie every actionable finding to an acceptance criterion, quality attribute, threat, or operational risk. Record severity, evidence, reproduction, blocking status, owner, and required re-verification. A role label alone is not expertise; use the role contract and relevant failure modes to calibrate the review.

## Review sequence

1. **Outcome and scope conformance:** verify the accepted need, criteria, exclusions, authority, and absence of unapproved behavior.
2. **Engineering quality:** review maintainability, security, test design, accessibility, compatibility, observability, operations, and recovery as applicable.
3. **Value challenge:** state whether implementation evidence supports, weakens, invalidates, or cannot yet assess the value hypothesis.

For user-facing work targeting users beyond the builder, add a pre-acceptance persona challenge after applicable gates pass. A fresh-context User Agent exercises the real workflow and reports directly to Product Stewardship and UX. Record its actor, persona version, missions, exact revision, observations, findings, dispositions, and reruns. This is independent feedback about conformance to supplied context, not independent evidence that the persona represents real users.

One actor may perform multiple passes, but keep findings and independence labels distinct. When confirmation bias or context saturation is material, use a fresh-context reviewer with the raw requirements, risks, revision, and evidence.

## Definition of Done

Applicable acceptance criteria are demonstrably met; required local and repository-hosted checks pass for the final revision or are explicitly unavailable; unexplained flakiness and blocking defects are absent; security/privacy decisions are approved; relevant accessibility and release-readiness evidence exists; applicable pre-acceptance User Agent findings are resolved or explicitly dispositioned; documentation and examples agree with behavior; the impact map is reconciled; residual risks and unavailable checks are explicit; unrelated work is preserved; and the handoff is reproducible.

## Handoff evidence

Include goal and value, included/excluded scope, requirement/UX/architecture decisions, risk-to-evidence results, security/privacy findings, documentation changes, operational/migration/rollback notes, repository-automation definitions and hosted run status, residual risks, acceptance outcome, and exact commands run.
