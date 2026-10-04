---
name: devguide-docs
description: Help with edits, reviews, and validation for the CPython developer guide and its reStructuredText documentation.
user-invocable: true
allowed-tools:
    - read_file
    - grep_search
    - file_search
    - run_in_terminal
---

# Devguide documentation helper

Use this skill when working on the CPython Developer Guide repository, especially when editing or reviewing documentation files in `.rst` format.

## Scope

This repository documents contributor workflows, project policies, team processes, and technical guidance. The goal is to keep the documentation clear, correct, and easy to navigate for contributors.

## Working approach

1. Read the target page and any nearby pages needed for context, such as indexes, related sections, or neighboring docs.
2. Keep the change focused on the user-visible issue or requested improvement.
3. Preserve the repository's documentation voice: precise, technical, and contributor-focused.
4. Follow the existing Sphinx reStructuredText conventions used in this repo, including heading hierarchy, lists, and directive syntax.
5. Verify that any new page, section, or link is consistent with the surrounding navigation and index structure.

## Repo conventions

- Most source files use `.rst` and should follow the project's heading and indentation conventions.
- Prefer clear prose that explains what contributors should do, why it matters, and any prerequisites.
- Maintain consistency with existing terminology, especially for CPython-specific terminology and contributor workflow language.
- Use relative links and references carefully so cross-references stay valid and readable.
- Avoid unrelated cleanup or broad reformatting in the same change.

## Validation

When practical, run the smallest relevant documentation validation command, for example:

- `make html`
- `python -m sphinx -b html . _build/html`

If a validation step is not available or is outside the scope of the request, clearly state that the content was not build-validated.

## Avoid

- Do not invent guidance or project claims that are not supported by the repo.
- Do not break toctrees, section references, or generated docs.
- Do not add unrelated formatting churn or autofixes.
- Do not leave a change without checking the surrounding document structure.

## Output expectations

When editing documentation, summarize:

- what changed,
- where the change was made,
- any validation or build checks that were run,
- and any follow-up caveats if the docs were not fully rebuilt.
