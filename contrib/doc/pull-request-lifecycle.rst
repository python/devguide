.. _docs-pull-request-lifecycle:

======================
Pull request lifecycle
======================


Making Good Pull Requests
=========================

- **Title Format**: Use a concise, imperative verb phrase (e.g., "Fix typo in setup guide", not "Fixed typo").
  - Start with a verb (e.g., "Add", "Fix", "Improve").
  - Avoid vague terms like "Update" or "Change".
  - Include an issue reference (e.g., "GH-123: Fix ...").
- **Description**: Explain the **what**, **why**, and **how**.
  - Reference related issues using ``GH-123`` or ``bpo-456``.
  - For complex changes, add a "Rationale" subsection.

  **Example:**
  **Good Title**: "GH-931: Enforce imperative tense in PR titles"
  **Bad Title**: "Updating docs"

  **Here is a checklist for contributors before submitting a PR**

  Before submitting a PR:
- [ ] Title follows the ``<Verb>: <Concise Summary>`` format.
- [ ] Description explains the **purpose** and **impact**.
- [ ] Linked to relevant issues (e.g., "Closes GH-123").
- [ ] Tests or documentation updated (if applicable).

.. warning::
   Poorly titled PRs may be rejected or delayed. Maintainers rely on clear titles to track changes in the project’s history.

Keep calm and code on! 🚀
