# Contributing / 贡献指南

Thanks for considering a contribution to Eco-Pomodoro. The whole app is one `index.html`; there is no build step, no package manager and no test framework to install.

欢迎贡献。整个应用就是一份 `index.html`，没有构建步骤、包管理器或需要安装的测试框架。

## Before you start / 开始前

- Search [existing issues](https://github.com/timyin7/Eco-Pomodoro/issues) first. For a large change, open an issue to discuss it before writing code.
- Please keep the project's character: single file, zero dependencies, offline-first, local-only data. A PR that adds an external script, analytics, a CDN asset or a required network call conflicts with the project's core promise and will be declined.
- UI text is bilingual. Any new user-facing string needs entries in both `en` and `zh` inside the `I18N` dictionary.

## Reporting a bug / 报告问题

Open an issue with:

1. What you expected and what happened.
2. Browser and version, OS, and how you opened the app (live demo, `file://`, or local server).
3. Steps to reproduce, plus whether a save export can be attached (remove personal task names first).
4. A screenshot if it is a visual problem.

## Making a change / 提交改动

1. Fork the repo and create a branch from `main`.
2. Keep changes focused. All tunable numbers belong in `CONFIG`; all species metadata belongs in `SPECIES_META`.
3. Verify manually in at least Chromium and one other browser if the change touches canvas rendering, notifications or `localStorage`.
4. If you change timing or ecology math, describe the before/after behavior in the PR. Timing correctness is the part most likely to regress.
5. Run a quick offline check: open `index.html` directly, start a 5-minute focus, pause, resume, skip, export and re-import a save.
6. Open a pull request. Small, measurable improvements are preferred over large rewrites.

## Ideas that are especially welcome / 欢迎的改进方向

- Accessibility review of controls, focus order and screen-reader labels.
- More languages, with complete `I18N` entries.
- Small visual refinements that keep the single-file constraint.
- Regression tests that can run without dependencies (DOM stubs are OK).

## Not accepted / 暂不接受

- Telemetry, analytics, tracking pixels or third-party requests.
- Cloud sync or accounts.
- Dependencies, bundlers or a multi-file rewrite.
- Medical or therapeutic claims in docs or marketing copy.

By contributing you agree that your contribution is licensed under the repository's [MIT License](LICENSE).
