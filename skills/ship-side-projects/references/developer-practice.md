# Software Developer Practice

Use TDD by default for behavior-changing production code:

1. Translate one acceptance behavior or failure mode into the smallest meaningful automated test at the lowest reliable boundary.
2. Run it and confirm it fails for the intended missing behavior, not setup, syntax, or unrelated breakage.
3. Implement the smallest coherent production change that makes it pass.
4. Run the focused test, then affected regression coverage; refactor only while green.
5. Record the red command/outcome and final green command/outcome when practical. A historical red run is development evidence, not the final quality gate.

Do not require a contrived test for non-behavioral metadata, generated output, disposable spikes, or a change already completely characterized by an existing failing test. A legacy seam, hardware/external dependency, or unavailable harness may justify an exception when creating the seam first would be disproportionate or risky. Record the reason, compensating evidence, and follow-up if the missing testability is material. Emergency work may abbreviate the cycle for containment, but add the focused regression before closure when feasible.

Do not confuse TDD with independent verification. Developer tests guide design and prevent regression; Testing and Security roles still challenge requirements, failure modes, and the implemented revision according to risk.

