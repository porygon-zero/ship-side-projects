# Perspectives and Gates

Perspectives are accountability lenses, not a simulated organization and not instructions to spawn subagents. The experienced builder and lead agent normally cover several perspectives. Name them only when doing so improves a decision, and never claim independence that did not exist. Read [agent-orchestration.md](agent-orchestration.md) for selection and contracts; it is linked directly from `SKILL.md` and does not need to be followed recursively.

| Role | Core accountability | Gate or output |
|---|---|---|
| Product discovery | Underlying need, intended users, evidence and testable outcome | Credible product brief and open assumptions |
| Product stewardship | Product goal, ordered next bets, scope, value and user feedback | Authorized goal and current priorities |
| UX Designer | User research, interaction discovery, mock-ups, accessibility/usability criteria and observation | UX evidence and proposals |
| Solution Architect | Context-fit architecture, quality attributes, boundaries, evolutionary decisions and fitness evidence | Approved/current design evidence |
| Software Developer | Safe idiomatic implementation, behavior-first TDD where feasible, documentation and feedback | Reproducible developer handoff with red/green evidence or an explicit exception |
| Testing Engineer | Requirements-led risk verification and reproducible defects | Quality outcome with independence label |
| Security & Privacy Engineer | Threat/privacy, secret/data/log/dependency/config/deployment assurance | Assurance outcome and residual risks |
| Builder/user | Product, time and spending constraints, material design, sensitive-data, risk and acceptance authority | Direction, acceptance, rejection, or explicit risk acceptance |
| Deployment responsibility | Packaging, release configuration, runtime verification, observability and recovery | Deployment outcome when relevant |

Apply only the perspectives justified by uncertainty or risk. Every participating perspective remains accountable to user value and may ask the user questions directly when supported, or indirectly through the lead; the lead is not a mandatory proxy. Coordinate timing and scope commitments under `agent-orchestration.md`. Deployment involvement scales with runtime impact. For a solo project, the builder may own product authority, implementation, operation, and acceptance; keep those authorities distinct from claims of independent technical verification.

## Review lenses

For every lens, first ask: whose underlying need does this serve, what evidence supports that need, and how will the user experience or outcome improve? Challenge the stated solution when necessary, while keeping criticism specific, evidence-based, and directed toward a better outcome.

- **Product discovery:** Are the user, underlying need, intended outcome, assumptions, and criteria clear without embedding a predetermined solution?
- **Product stewardship:** Is this the smallest coherent value or learning slice that fits the builder's available attention, with an observable outcome and explicit exclusions?
- **UX Designer:** Is relevant user evidence represented, and are usability, accessibility, harmful-edge-case, and research/privacy concerns testable?
- **Solution Architect:** Does the design fit observed constraints and quality attributes, preserve useful architecture, expose tradeoffs, and include evolutionary fitness evidence?
- **Software Developer:** Did a focused test expose the missing behavior before production code where feasible, does the change remain idiomatic, cohesive, maintainable, secure by default, locally testable, documented, and free of unrelated edits?
- **Testing Engineer:** Can the evidence falsify the criteria across boundaries and failure modes, and does it avoid implementation-biased or flaky oracles?
- **Security & Privacy Engineer:** Are assets, data, trust boundaries, abuse cases, controls, verification, minimization, and residual risks explicit before and after implementation?
- **Deployment responsibility:** Is the artifact reproducible and observable, with compatible configuration, safe rollout/migration, recovery, and post-release verification?
- **Builder/user:** Are the demonstrated outcome, time and operating burden, material choices, unavailable evidence, and residual risks understandable enough for a real decision?

## Shared conduct

- Prefer the smallest independently valuable/testable increment or learning experiment.
- Order by value, risk, learning, and dependency; judge progress by outcomes rather than velocity.
- Seek the underlying need behind the stated request; distinguish user goals, requested solutions, constraints, and assumptions.
- Be constructively critical: expose contradictions, weak evidence, harmful tradeoffs, and low-value work, then offer a viable path forward.
- Invite user input from any role when it can materially improve the decision; coordinate questions and preserve the specialist's perspective rather than flattening it into anonymous consensus.
- Protect the active goal and put non-blocking ideas in the ordered next-bets list.
- Report observations, assumptions, decisions, failures, and residual risks distinctly.
- Treat flakiness as a defect to investigate, not noise to rerun away.
- Keep living documentation current in the same change.
- Summarize user-owned decisions in a concise decision digest with options, consequences, recommendation, and evidence.

## Shared security

- Architect: trust boundaries and security architecture.
- Developer: secure implementation and prevention of secrets/sensitive data in code, fixtures, commits, errors, and logs.
- Testing: adversarial behavior and regression evidence.
- Deployment: runtime secrets, TLS, access, patching, monitoring, recovery.
- Builder/user: privacy decisions and material residual-risk acceptance.
- Security & Privacy Engineer: challenge and assurance across all areas.

