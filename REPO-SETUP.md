# Repo discovery setup checklist / 仓库发现性设置清单

This file records what is already true and what still needs to be clicked in the GitHub UI. No push or settings change has been made by the assistant.

本文件区分「已验证」与「待你在 GitHub 网页端填写」。助手没有替你推送或修改仓库设置。

## Verified now / 已验证

| Field | Current value | Evidence |
|---|---|---|
| Repository | <https://github.com/timyin7/Eco-Pomodoro> | GitHub API |
| Default branch | `main` | GitHub API |
| GitHub Pages | **Enabled and serving the demo** | <https://timyin7.github.io/Eco-Pomodoro/> returned the app UI |
| Issues | Enabled; 0 open | GitHub API `has_issues: true` |
| License | MIT (local `LICENSE` file added in this pass; push required) | Local file |
| Stars / forks | 1 / 0 at time of check | GitHub API — do not quote as a marketing metric |

## Fill in on GitHub / 待填写

Open **Settings → General** for the first four; **Settings → Pages** is already done.

### 1. Description (About)

Paste exactly:

```text
An eco-friendly Pomodoro timer where focus grows a living pond. Single HTML file, offline, local-first.
```

### 2. Website URL

```text
https://timyin7.github.io/Eco-Pomodoro/
```

### 3. Topics

Add exactly these five (order does not matter):

```text
pomodoro
productivity
timer
javascript
html
```

Optional extras if GitHub allows more: `open-source`, `single-file`, `offline-first`, `canvas`, `self-hosted`.

### 4. README and social preview

- README: leave `README.md` as the default display file; the English version is linked from its first line.
- Social preview: **Settings → General → Social preview → Upload an image** → choose `assets/github-social.png` (1280×640). Do the same for the OG variant in `assets/og-image.png` when a custom landing page is deployed.
- Keep `assets/demo-screenshot.png` committed: both READMEs reference it.

### 5. Features to consider (not required)

- **Discussions**: enable it only if you are willing to answer thread questions; otherwise keep Issues as the single feedback entrance.
- **Issue templates**: add a short bug report form pointing to the checklist in `CONTRIBUTING.md`.
- **Releases**: create the `v1.0` release from the notes in `RELEASE-NOTES-v1.0.md` — but only after the release date and demo GIF are real.

## Commit and push the local changes

```bash
git add README.md README.en.md LICENSE CONTRIBUTING.md REPO-SETUP.md \
        PROMOTION-PLAN.md SEO-RECOMMENDATIONS.md RELEASE-NOTES-v1.0.md \
        assets promo
git commit -m "docs: polish READMEs, add MIT license, promo and SEO assets"
git push origin main
```

Then re-check <https://github.com/timyin7/Eco-Pomodoro> to confirm the social preview and license badge render.
