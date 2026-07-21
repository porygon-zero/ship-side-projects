# Lifecycle Evidence State Machine

Treat states as evidence maturity, not exclusive work phases. Record the current state, required evidence, owner, authorization source, and next transition at the artifact depth required by the change class. Resume from recorded evidence; do not restart completed discovery. Discovery, design, and verification may overlap when scope ownership remains clear and evidence is reconciled before a gate decision.

| State | Required input | Allowed work | Exit evidence | Normal next state |
|---|---|---|---|---|
| `ORIENT` | Request and repository | Inspect, classify, identify unknowns | Entry type, risk class, current-state summary | `DISCOVERY` or `PLAN` |
| `DISCOVERY` | Unresolved product outcome | Questions, prototypes, requirement analysis | Testable outcome and constraints | `REQUIREMENTS_APPROVAL` |
| `REQUIREMENTS_APPROVAL` | Proposed material baseline/change not already authorized | Clarification and reversible analysis | User direction or recorded existing authorization | `ARCHITECTURE` or `DISCOVERY` |
| `ARCHITECTURE` | Approved requirements | Architecture analysis, ADRs, threat framing | Proportionate design evidence | `PLAN` |
| `PLAN` | Goal, constraints, design evidence | Define increment, impact map, and readiness | Proposal plus `ready`, `ready-with-concerns`, or `not-ready` outcome | `INCREMENT_APPROVAL` or responsible earlier state |
| `INCREMENT_APPROVAL` | Proposal requiring new authority | Clarification, reversible preparation, and dedicated increment-branch setup | Approval/rejection or recorded authorization, plus PR base/head branches | `IMPLEMENT` or `PLAN` |
| `IMPLEMENT` | Authorized increment | Code, tests, documentation | Developer handoff | `QUALITY_GATE` |
| `QUALITY_GATE` | Implemented increment | Independent/risk-led verification and fixes | Recorded quality outcome | `SECURITY_GATE` or `IMPLEMENT` |
| `SECURITY_GATE` | Threat/privacy scope | Assurance, fixes, and one runtime/library/framework currency check per increment | Recorded assurance and update-disposition outcome | `RELEASE_READINESS` or `ACCEPTANCE` |
| `RELEASE_READINESS` | Releasable artifact and runtime impact | Validate packaging, configuration, rollout, observability, migration and recovery | Deployment-readiness outcome | `ACCEPTANCE` or earlier state |
| `ACCEPTANCE` | Passing required gates | Real workflow review by the builder or representative target user | Acceptance or reproducible rejection, with evidence source labeled | `HANDOFF` or earlier state |
| `HANDOFF` | Accepted increment | Reconcile all merge-required artifacts and retrospective; inspect full diff; commit accepted increment; push branch; open PR last | PR URL and final head revision, or exact blocker plus ready-to-use manual PR title/body | `CLOSED` or blocked `HANDOFF` |
| `CLOSED` | Opened PR or builder-confirmed manual PR | Record PR and order next bets; make no further increment changes | Closure record | Next increment |

States may be combined for trivial/small work when their evidence remains visible. High-risk work must not silently skip applicable states.

Do not pause at an approval state when the original request or valid standing authority already covers the proposed reversible work. Record `authorization_source`, its scope, and any excluded external mutation. Pause only when the next action needs new authority.

Approval of an increment includes standing authority, after successful gates and acceptance, to commit all and only its merge-required work, push its increment branch, and open its PR. It does not authorize merging, deployment, release, spending, secret creation, or unrelated changes. PR creation is the last closeout action: retrospective and all merge-required code, tests, documentation, evidence, migrations, and generated artifacts must be committed first.

## Implementation readiness

- `ready`: required inputs, authority, testability, controls, and rollback depth are sufficient for the classified risk.
- `ready-with-concerns`: named non-blocking concerns have an owner, impact, and required recheck point.
- `not-ready`: a specific missing decision, authority, testability seam, or material uncontrolled risk blocks implementation.

Readiness is an engineering recommendation, not duplicate user approval. Reassess it when material evidence changes.

## Recovery transitions

- Requirement contradiction: return to `DISCOVERY` or `REQUIREMENTS_APPROVAL`.
- Architecture invalidated: return to `ARCHITECTURE` and repeat only affected planning and gates.
- Test/security failure: return to `IMPLEMENT` or the responsible design state.
- Acceptance rejection: classify the cause, return to the responsible state, and repeat affected verification.
- External blocker: record exact blocker, completed evidence, safe next action, and required authority or environmental change. Distinguish `blocked` from merely `incomplete`.
