# Ship Side Projects

`ship-side-projects` is a Codex skill for turning personal, indie, open-source, homelab, and tiny-team software ideas into useful, maintainable releases without importing heavyweight organizational process.

The skill combines proportionate product discovery, scope control, architecture, UX, test-driven development, risk-based verification, security, deployment, and feedback practices. It is written for experienced software builders working with limited time and energy.

## Install

Clone this repository, then copy or link the skill directory into your Codex skills directory:

```sh
git clone git@github.com:porygon-zero/ship-side-projects.git
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

The validator checks the required skill metadata, directory naming, local Markdown links, and YAML syntax when PyYAML is available. GitHub Actions runs the same checks on pushes and pull requests.

## Status

This repository is private and all rights are reserved. Before making it public, complete [the publication checklist](PUBLICATION_CHECKLIST.md), including selecting an open-source license and replacing the current license notice.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) for the contribution workflow and [SECURITY.md](SECURITY.md) for private vulnerability reporting guidance.
