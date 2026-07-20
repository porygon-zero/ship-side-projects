# Software Developer Practice

Use TDD by default for behavior-changing production code:

1. Translate one acceptance behavior or failure mode into the smallest meaningful automated test at the lowest reliable boundary.
2. Run it and confirm it fails for the intended missing behavior, not setup, syntax, or unrelated breakage.
3. Implement the smallest coherent production change that makes it pass.
4. Run the focused test, then affected regression coverage; refactor only while green.
5. Record the red command/outcome and final green command/outcome when practical. A historical red run is development evidence, not the final quality gate.

Do not require a contrived test for non-behavioral metadata, generated output, disposable spikes, or a change already completely characterized by an existing failing test. A legacy seam, hardware/external dependency, or unavailable harness may justify an exception when creating the seam first would be disproportionate or risky. Record the reason, compensating evidence, and follow-up if the missing testability is material. Emergency work may abbreviate the cycle for containment, but add the focused regression before closure when feasible.

Do not confuse TDD with independent verification. Developer tests guide design and prevent regression; Testing and Security roles still challenge requirements, failure modes, and the implemented revision according to risk.

## Repository-hosted automation

Treat continuous integration as executable project memory: it should preserve the commands and controls that future changes must satisfy when the builder returns after a break.

Add or extend a hosted workflow when the repository has repeatable tests or quality commands, produces distributable artifacts, accepts changes through a forge, or would materially benefit from detecting platform, dependency, security, packaging, or deployment failures outside the local machine. Prefer the established provider. On GitHub, use GitHub Actions unless the repository deliberately uses another system.

Keep the workflow proportionate:

1. Reuse the same documented commands developers run locally; do not create a second hidden build path.
2. Trigger fast verification on the events that can invalidate the project, normally pushes and pull requests, with tag/release/deployment triggers only when those paths exist.
3. Start with the smallest useful matrix and supported runtime versions. Add platforms and versions because compatibility risk justifies them, not for decoration.
4. Set explicit least-privilege permissions, pin or deliberately version third-party actions, avoid exposing secrets to untrusted changes, and use concurrency/cancellation where it saves time or cost.
5. Cache only when it measurably helps and the cache key cannot silently reuse incompatible or untrusted output.
6. Make failures actionable through clear job names, commands, and logs. Do not hide required failures behind unconditional success or broad `continue-on-error` settings.
7. Separate verification from deployment. A green test job must not imply release authorization; deployments, package publication, paid services, secrets, and environment changes require their own authority and controls.
8. Run or validate the workflow's commands locally before pushing. After an authorized push, inspect the hosted run for the exact revision and record its result.

For a throwaway experiment, private local script, documentation-only repository, or project without stable automated commands, hosted CI may be premature. Record why it is `not-applicable` or defer it as a named next bet with the trigger that will make it worthwhile. Do not scaffold an empty workflow merely because the repository is on GitHub.
