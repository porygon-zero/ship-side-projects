# Public publication checklist

Complete these items before changing repository visibility to public:

- [ ] Review the complete Git history for secrets, personal data, confidential material, and third-party content.
- [ ] Choose an open-source license and replace the current all-rights-reserved `LICENSE` file.
- [ ] Confirm every bundled asset and example is owned by the project or compatible with the selected license.
- [ ] Verify the installation example uses the preferred public clone URL.
- [ ] Review `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, and `SECURITY.md` for current contact and response details.
- [ ] Add a repository description, topics, social preview, and homepage where useful.
- [ ] Enable branch protection and require the validation workflow on the default branch.
- [ ] Enable secret scanning, push protection, dependency alerts, and private vulnerability reporting where available.
- [ ] Run `python3 scripts/validate_skill.py` and confirm GitHub Actions passes.
- [ ] Create a version tag and verify the generated release archive contains only the installable skill directory.
- [ ] Change visibility only after the preceding review is complete.
