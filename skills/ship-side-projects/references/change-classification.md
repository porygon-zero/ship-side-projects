# Change Classification

Choose the highest applicable class. Explain the choice; do not lower it to avoid controls.

| Class | Typical scope | Minimum delivery evidence | Default artifact depth |
|---|---|---|---|
| `trivial` | Typo, comment, safe formatting, non-behavioral metadata | Worktree safety, focused check, documentation-impact note | Concise handoff record; no separate increment file unless established locally |
| `small` | Local bug fix or contained behavior change | Acceptance criteria, focused risk analysis, automated regression where feasible, documentation-impact note | Lightweight increment summary; reuse the project format |
| `standard` | User-facing capability or cross-component change | Increment record, traceability, architecture/security review as relevant, risk-derived gates, acceptance | Full increment record and impact map |
| `high-risk` | Auth, authorization, payments, personal/sensitive data, destructive migration, public contracts, safety/reliability critical path | Explicit approval, threat/privacy analysis, rollback/recovery, independent verification, residual-risk acceptance | Full records, exact revision, independent evidence, decision authority |
| `emergency` | Active incident or exploitable vulnerability | Expedited scoped fix, incident evidence, safety checks, authorized release; mandatory retrospective reconciliation | Minimal live incident record followed by full reconciliation |

Escalate when scope crosses trust boundaries, changes stored data or public contracts, increases irreversibility, exposes sensitive information, or invalidates approved assumptions.

Risk class controls ceremony, not engineering quality. A side project does not become low-risk merely because it is small or unpaid: public exposure, authentication, payments, personal data, destructive automation, and supply-chain publication still warrant strong controls. Conversely, a trivial change does not need fictional roles or empty documents; an emergency may defer non-blocking documentation but must record and reconcile the debt after stabilization.

