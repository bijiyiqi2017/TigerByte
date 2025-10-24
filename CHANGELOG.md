# 🦁 TigerByte Changelog

All notable changes to TigerByte will be documented in this file.

The format is based on [Semantic Versioning](https://semver.org/).

## [v0.1.2] - 2025-10-23
### 📝 Overview

- Minor milestone updates for TigerByte: workflow improvements, Hacktoberfest preparation, and repository enhancements.

### ✅ Added / Updated

- Submitted and staged Changelog entry for 10/22/2025

- Added annotated version tag on GitHub to mark project milestone progress

- Updated contributors.json and committed changes

- Staged and committed changes for progress.md and Changelog.md

- Merged local and remote main branches

- Added “⭐ Star the repo” section in README.md

- Created GitHub issues for Hacktoberfest contributions:

- #7 – Create 3–5 small example programs for testing

- #8 – Generate CONTRIBUTORS.md from contributors.json

- #9 – Build a tokenizer

- #10 – Expand interpreter commands

- #12 – Add Pull Request Template + Wiki Doc

- Created assets directory and added interpreter v.01 image

- Added Demo section with interpreter v.01 image

- Staged, committed, and pushed all updates to remote main

- Merged and closed issue #12

- Added support for `version` and `about` commands to display interpreter metadata (#16)

## 🟡 Work in Progress

- Wiki Home Page draft not yet created

- Multi-OS SETUP.md issue not yet posted

- CONTRIBUTING.md issue not yet drafted

- Example scripts folder and issues not yet created

- Debug / verbose mode for interpreter not yet implemented

- Tokenizer unit tests not yet written

## 🔜 Next Steps

- Draft TigerByte Wiki Home Page and link from README.md

- Create SETUP.md issue for multi-OS contributions (Linux, macOS, Windows)

- Encourage contributors to claim OS sections for Hacktoberfest

- Draft CONTRIBUTING.md issue for beginner-friendly PR guide

- Create issue for example scripts in /examples folder

- Implement debug/verbose mode feature for interpreter and document usage

- Write initial unit tests for tokenizer using pytest

- Update README badges / add Docs / Wiki badge for visibility

- Review and merge PRs for setup, contributing, examples, and assets

- Plan post-Hacktoberfest migration of docs to Wiki (Setup, Contributing, Examples)

- Track contributors for credit on Wiki pages

## [v0.1.1] - 2025-10-22
### 📝 Overview

- Documentation and synchronization updates to align the project for Hacktoberfest 2025 contributions, finalize file naming conventions, and prepare for interpreter development.

### 🚀 Added

- contributors.json file to track Hacktoberfest contributors.

- Annotated version tag (v0.1.1) added on GitHub for this milestone.

### 🧩 Changed

- Updated all README.md files to use the .tb extension (replacing .tbyte).

- Improved project clarity by standardizing file references and linking the new contributor file.

### 🔧 Fixed

- Divergence between local and remote main branches resolved via merge and sync.

### 🧠 Documentation

- Added detailed daily progress entry (progress.md) for October 22, 2025.

- Reviewed and merged pull requests with review feedback.

- Encouraged contributors to star the repository.

### 🎯 Next Focus

- Begin core development of interpreter.py (TigerByte Interpreter v0.1).

- Introduce tokenizer implementation issue for contributors.

- Establish roadmap for parser and executor components.

## [0.2.0] - 2025-10-21
### Added
- Added **Contributing** section in `README.md` linking to `CONTRIBUTING.md`.
- Mentioned that **TigerByte is implemented in Python** in `README.md`, `CONTRIBUTING.md`, and `progress.md`.
- Drafted updates for `README.md` to include Python, languages section, and contribution guidance.
- Prepared draft branch for Python mention and contributing updates.
- Created `interpreter.py` (empty for now) to help list the project as a Python project for Hacktoberfest.

### Changed
- **Updated `progress.md`** (first update) to log today’s tasks.
- **Updated `progress.md` and `changelog.md` again** (second update) to reflect completed actions.
- Added **hacktoberfest-accepted** label on the pull/merge.

### Fixed
- Reviewed and merged pull requests for **issues #2 and #4**.

### [v0.1.2] – 2025-10-21
#### Added
- Contributing section in `README.md` linking to `CONTRIBUTING.md`.
- Mentioned that TigerByte is implemented in **Python** in `README.md`, `CONTRIBUTING.md`, and `progress.md`.
- Draft updates for `README.md` including Python mention, Languages section, and contribution guidance.

#### Notes
- Updates improve clarity for contributors and highlight the Python-based implementation of TigerByte.
- Prepared draft branch for ongoing documentation improvements.

## [0.1.1] - 2025-10-20

### Added
- `CONTRIBUTING.md` — detailed contribution guidelines including multilingual keyword suggestions, translation ideas, and conventional commit examples.
- `CODE_OF_CONDUCT.md` — implemented using the Contributor Covenant to set a welcoming and inclusive community standard.
- Planned link addition in `README.md` to direct contributors to `CONTRIBUTING.md`.

### Improved
- Project prepared for **Hacktoberfest 2025** participation with structured contribution workflow and open collaboration approach.
- Strengthened overall documentation consistency and contributor clarity.

### Notes
- Marks TigerByte’s first step into public community readiness.
- Next planned release `v0.1.2` will focus on issue templates, PR templates, and README enhancements.

## [0.1.0] - 2025-10-19
### Added
- File system design formalized with extensions:
  - `.tbyte` → Main source code files
  - `.cub` → Example/tutorial files
  - `.roar` → Output/log files
  - `.den` → Configuration/environment files
- README updated to include file extensions and planned features
- Concepts documented in `concepts.md` with file system table
- Tiger Mode / emoji output planned as a feature

### Notes
- Milestone represents initial structure setup and documentation improvements
- Marks the first meaningful feature set for TigerByte (pre-release)

## [0.0.1] - 2025-10-18
### Added
- Initial project structure
- Created README, gitignore, docs, and placeholders
