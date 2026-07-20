# Specialist Skill Composition

Use this skill as the delivery control plane and invoke other skills for bounded specialist techniques.

## Ownership

Ship Side Projects owns user value, lifecycle state, scope and authorization, risk classification, perspective coordination, evidence reconciliation, gates, user acceptance, and handoff. A specialist skill may own a technique such as debugging, framework implementation, accessibility testing, threat modeling, performance analysis, or deployment mechanics within that boundary.

## Composition rules

1. Give the specialist the user need, authorized scope, relevant criteria and risks, repository rules, exact revision, permitted mutations, and required output.
2. Let the specialist refine methods and evidence for its bounded concern; do not let it silently expand product scope, accept risk, approve its own independent gate, or perform unauthorized external mutations.
3. Apply higher-authority instructions and established repository constraints first. When workflows conflict, preserve this skill's user authority, risk controls, evidence honesty, and lifecycle state; adapt or decline the conflicting specialist step with a recorded reason.
4. Reconcile specialist findings into the increment's criteria, risk-to-evidence matrix, documentation impact, readiness, and gates. A specialist's `done`, successful command, or local review does not establish product acceptance.
5. Avoid loading multiple overlapping methodology skills for the same concern. Choose the smallest qualified specialist and stop it when its contract is satisfied.

For systematic debugging, use it during orientation, implementation, or incident containment to establish root cause and a reproducible failure. Return material product, architecture, security, or scope discoveries to the accountable role before broadening the fix.

