# Ship Side Projects

`ship-side-projects` is a Codex skill for turning personal, indie, open-source, homelab, and tiny-team software ideas into useful, maintainable releases without importing heavyweight organizational process.

The skill combines proportionate product discovery, scope control, architecture, UX, test-driven development, risk-based verification, security, deployment, and feedback practices. It is written for experienced software builders working with limited time and energy.

## Maintenance model

This is a personal, owner-maintained project. You are welcome to use it, copy it, modify it, and fork it under the [MIT License](LICENSE), but I am not currently looking for collaborators and do not have capacity to review issues or pull requests. Forks are the recommended way to adapt or extend it.

## Install

Clone this repository, then copy or link the skill directory into your Codex skills directory:

```sh
git clone https://github.com/porygon-zero/ship-side-projects.git
ln -s "$(pwd)/ship-side-projects/skills/ship-side-projects" ~/.codex/skills/ship-side-projects
```

Restart Codex after installation. Invoke the skill explicitly with `$ship-side-projects`, or let Codex select it for relevant side-project work.

## Repository layout

```text
skills/ship-side-projects/
├── SKILL.md
├── agents/openai.yaml
├── references/
└── assets/
```

Repository-level files document contribution, security, governance, validation, and release practices without becoming part of the installable skill.

## Validate

```sh
python3 scripts/validate_skill.py
```

The validator checks required skill metadata, directory naming, interface metadata, and local Markdown links. GitHub Actions runs the same checks on pushes and pull requests.

## Using and adapting the skill

See [CONTRIBUTING.md](CONTRIBUTING.md) for the owner-maintained project policy and [SECURITY.md](SECURITY.md) for security reporting guidance.
