---
name: Bug-fix exercise
about: Reproduce a defect and define a regression check
title: "fix: "
---

## Planning

After verified Azure Boards handover, track the fix there and link this report to its actual Azure ID. Until then use roadmap #2, task code, phase, priority and status. Link prerequisites, related release and any blocker. See docs/AZURE_BOARDS_SETUP.md.

## Expected and actual behaviour

Describe both with synthetic data and sanitized output.

## Reproduction

Commit, environment, exact steps and smallest input that demonstrates the defect.

## Regression check

What test should fail before the fix and pass afterwards?

## Done when

- [ ] Failure reproduced on the parent version
- [ ] Meaningful regression test fails before and passes after the fix
- [ ] Reviewed PR and relevant release/check evidence recorded

## Impact and release

Who is affected? Use bugfix from develop for normal work; use the documented hotfix path if a deployed production release is affected.
