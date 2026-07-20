# Adoption and Exception Paths

## Existing project

1. Read repository instructions before editing.
2. Inspect the branch and dirty worktree; preserve unrelated changes.
3. Discover actual entry points, module boundaries, dependencies, build/test/lint/type-check commands, CI, deployment model, schemas, and documentation.
4. Separate observations from documented claims and proposed changes.
5. Reuse existing issue, ADR, requirements, and release formats.
6. Repair only control or decision-record gaps needed to deliver the requested change safely. Put broader improvements in the ordered next-bets list.
7. Identify side-project constraints: realistic weekly attention, acceptable recurring spend, hosting and support burden, likely pause duration, and whether another person must be able to recover the project.

## Dormant or abandoned project

Recover from repository evidence rather than redesigning immediately. Establish what still runs, what is obsolete, current dependencies and exposure, the smallest useful next outcome, and whether revival is worth the maintenance cost. Prefer an archive, export, or clean shutdown when continued ownership no longer delivers enough value.

## Risk-reduction spike

Use a time/effort-bounded experiment when uncertainty prevents a credible increment. Define the question, evidence to collect, excluded production behavior, cleanup/disposal plan, and decision that the result will inform. A spike result is learning, not automatically production-ready code.

## Emergency

Prioritize containment and safe restoration. Require an authorized scope, reproducible incident evidence, focused regression/security checks, rollback or recovery, and explicit release authority. Record skipped non-blocking work and reconcile it after stabilization. Never bypass secrets, access, or destructive-action safeguards.

## Stop and ask

Request user direction when:

- alternatives materially change user-visible behavior, recurring cost, available-time commitment, privacy, or risk;
- sensitive-data use or residual material risk needs acceptance;
- destructive or irreversible work lacks approval or recovery evidence;
- credentials, external authority, or an environment required for completion is unavailable;
- user changes overlap the intended edits and safe preservation is uncertain;
- acceptance criteria cannot be made objective from available context.

Do not stop merely because implementation is difficult or could benefit from preference input. Make and record reversible low-impact assumptions.

