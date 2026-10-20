# Contributing questions

Thank you for helping improve this interview preparation portal.

## Easiest workflow (browser only)

1. Open the published website and click **Contribute a question**.
2. GitHub opens `data/questions.json` in its editor. Sign in if prompted.
3. Add a new object **before the final `]`**, separated from the previous object by a comma. Use the next unused integer ID (do not change existing IDs).
4. Select **Commit changes**. If you cannot push directly, GitHub offers a fork and pull-request workflow.
5. Open the pull request, explain the change and wait for the **Validate interview questions** check.
6. A repository maintainer reviews and merges. GitHub Pages republishes the updated `main` branch.

Example:

```json
{
  "id": 168,
  "category": "Core Java — OOP & Language",
  "question": "When should you use a record?",
  "answer": "Use a record for transparent immutable-data-style carriers; record components are final, but referenced objects may still be mutable.",
  "priority": "High"
}
```

**Important:** This example is an individual object, not a complete replacement for `questions.json`. Keep the file a valid JSON array. Do not reuse an existing ID. The validator checks structure, not factual correctness.

## Local validation

```powershell
py -3 scripts/validate_questions.py
```

## Review guidelines

- Prefer official Java, Spring, Angular, PostgreSQL, or Azure docs for version-sensitive answers.
- Avoid proprietary interview questions, confidential customer examples, personal data, and copied copyrighted material.
- Keep answer cues short and clear. Include practical caveats when necessary.
- Use existing categories where possible; adding a new category is supported.
- Keep existing IDs stable because each browser stores revision progress by ID.

## Maintaining a protected main branch

Under **Settings → Branches** or **Settings → Rules → Rulesets**, add a rule for `main` requiring pull requests and the validation status check. Availability of ruleset enforcement depends on repository visibility and your GitHub plan. Avoid requiring reviews from the sole maintainer if it blocks your workflow.

## Keep Markdown in sync

If you add or modify questions in `data/questions.json`, update the corresponding `docs/*.md` guide as well. For Kafka questions, update `docs/apache-kafka-senior-staff.md`. Do not add content from confidential PDFs to a public repository without permission.
