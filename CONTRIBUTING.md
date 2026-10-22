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


## Add real-world examples and Java DSA problems (v2)

- Interview questions can include an optional `example` field in `data/questions.json`. Make it a concrete, technically correct production scenario, not a generic placeholder.
- Add a new LeetCode-style problem to `data/leetcode.json` with a unique `LC###` ID, `title`, `difficulty`, `topic`, `problem`, `example`, `approach`, `time`, `space`, `language`, and `code`.
- Create a corresponding `docs/leetcode/lc###-slug.md` with the Java solution and update `docs/leetcode/README.md`.
- Write original summaries and original solutions; do not paste proprietary problem statements or confidential interview handbooks.
- Run `py scripts/validate_questions.py` and `py scripts/validate_leetcode.py` before opening a PR.


Coding exercises also require constraints, bruteForce, bruteTime, bruteSpace, bruteCode, walkthrough and edgeCases; keep the Markdown equivalent synchronized. Expanded DevOps entries use contentBlocks (type text or code, plus text) to preserve complete HCL/YAML examples in the portal.

Run `python scripts/validate_java_solutions.py` with JDK 17+ to compile and check both variants of all 20 exercises against samples and boundary cases.


System-design lessons are authored in `scripts/expand_system_design.py`; regenerate its 26 entries, five topic guides and diagrams with `python scripts/expand_system_design.py`. Case studies and component diagrams are authored in `scripts/build_system_design_cases.py`. Run `python scripts/build_system_design_cases.py` after editing them. The browser check `node scripts/test_system_design.cjs` requires Playwright and Microsoft Edge (or set PLAYWRIGHT_CHANNEL to another installed channel). It verifies lesson images, step controls, SVG text bounds and mobile page width.


Design-pattern lessons: edit `scripts/expand_design_patterns.py` and `examples/design-patterns/*.java`, regenerate with `python scripts/expand_design_patterns.py`, and run `python scripts/validate_pattern_labs.py` with JDK 21+. This checks all eight runnable labs and code/data synchronization. The shared browser check covers 34 system-design/design-pattern lessons and 44 diagrams.
