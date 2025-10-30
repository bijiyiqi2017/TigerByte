# 🐅 TigerByte Issue Tagging System Proposal

## Introduction

This report outlines the proposed standardized tagging system for the `TigerByte` repository. The system is designed to significantly improve issue discoverability, enforce clarity and consistency across the workflow, and infuse the project with unique, engaging tags.

## Current Tags

**(NOTE: This section is based on standard GitHub defaults as current repo tags were unavailable.)**

| Tag Name | Assumed Color (Hex) | Category | Identified Improvement |
| :--- | :--- | :--- | :--- |
| `bug` | `#d73a4a` (Red) | Type | Needs a color with higher contrast (e.g., darker red). |
| `documentation` | `#0075ca` (Blue) | Type | Good, but should be specialized (e.g., `type: docs`). |
| `help wanted` | `#008672` (Teal) | Contributor | Good. Needs clear pairing with "beginner" tags. |
| `enhancement` | `#a2eeef` (Light Cyan) | Type | Good. |

## Proposed Tags: TigerByte Tagging System

The following system uses seven distinct categories, ordered for consistency (Status first, Events last).

### Tag Order

1.  Status Tags (Workflow & State)
2.  Priority Tags (Urgency)
3.  Type of Issue Tags (Classification)
4.  Area/Component Tags (Code Location)
5.  Contributor-Focused Tags (Onboarding & Help)
6.  TigerByte-Specific Tags (Creative Identity)
7.  Special Event/Seasonal Tags (External Focus)

---

## Table of Tags for README.md

This table details the full set of proposed tags, categorized for easy reference.

| Tag Name | Category | Suggested Color (Hex) | Description |
| :--- | :--- | :--- | :--- |
| **--- 1. STATUS (Workflow & State) ---** | | | **Tracks the current state in the development workflow.** |
| `status: ready` | Status | `#5CB85C` (Medium Green) | Issue is refined, prioritized, and ready to be claimed/worked on. |
| `status: in progress` | Status | `#5BC0DE` (Light Blue) | Task is currently being actively worked on by an assignee. |
| `status: pending review` | Status | `#F0AD4E` (Orange/Amber) | PR has been opened and requires maintainer review. |
| `status: blocked` | Status | `#555555` (Dark Gray) | Cannot proceed due to a prerequisite or external dependency. |
| **--- 2. PRIORITY (Urgency) ---** | | | **Indicates the required level of attention.** |
| `priority: critical` | Priority | `#B60205` (Dark Red) | Immediate attention required; severely impacting the project. |
| `priority: high` | Priority | `#D9534F` (Medium Red) | Important issue that needs resolution soon. |
| `priority: low` | Priority | `#2E64A5` (Royal Blue) | Non-urgent task or minor improvement. |
| **--- 3. TYPE (Classification) ---** | | | **Defines the nature of the task.** |
| `type: bug` | Type of Issue | `#A73347` (Maroon) | Issues related to incorrect code behavior or a failure. |
| `type: feature request` | Type of Issue | `#674196` (Dark Purple) | Suggestion for adding new core functionality. |
| `type: docs` | Type of Issue | `#0075ca` (Blue) | Changes required for READMEs, guides, or code comments. |
| `type: maintenance` | Type of Issue | `#848484` (Gray) | Code cleanup, dependency updates, or tool configuration. |
| **--- 4. AREA/COMPONENT ---** | | | **Identifies the section of the codebase affected.** |
| `area: frontend` | Area/Component | `#F7E16B` (Yellow) | Issues related to UI, rendering, or client-side components. |
| `area: api` | Area/Component | `#00C29E` (Teal Green) | Issues related to API structure or data handling. |
| `area: database` | Area/Component | `#C63399` (Fuschia) | Issues related to database schema, migrations, or queries. |
| **--- 5. CONTRIBUTOR FOCUS ---** | | | **Onboarding and Recruitment Tags.** |
| `good first issue` | Contributor-Focused | `#339966` (Grass Green) | Simple task ideal for first-time or new contributors. |
| `help wanted` | Contributor-Focused | `#207DE5` (Blue) | Requesting additional assistance from the community. |
| **--- 6. TIGERBYTE SPECIFIC (Creative) ---** | | | **Unique tags reflecting project identity.** |
| `#TigerByteGoals` | Creative Tag | `#FF9933` (Gold) | For major project milestones or core roadmap objectives. |
| `#ByteSquad` | Creative Tag | `#A853FF` (Purple) | Designates tasks requiring synchronous, team-based collaboration. |
| `#ByteMe` | Creative Tag | `#FF4500` (OrangeRed) | For highly challenging or experimental, "figure-it-out" tasks. |
| **--- 7. SPECIAL EVENT ---** | | | **Seasonal/External Events.** |
| `#Hacktoberfest2025` | Special Event | `#FF8800` (Orange) | Related to Hacktoberfest participation. |
| `#HolidayRelease` | Special Event | `#CC0000` (Deep Red) | Tasks scheduled for a seasonal or holiday update. |

---

