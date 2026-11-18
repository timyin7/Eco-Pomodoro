# SEO and social preview recommendations / SEO 与社交预览建议

Status: recommendations plus changes already made locally. The assistant has not purchased a domain, deployed a new site, or posted anything.

---

## 1. Current state / 现状

- GitHub Pages already serves the app at <https://timyin7.github.io/Eco-Pomodoro/>.
- Before this pass, `index.html` had only `<title>` and viewport metadata — no description, canonical or Open Graph tags.
- `index.html` has now been updated with description, canonical, `og:*` and `twitter:*` tags pointing at `assets/og-image.png`.
- `assets/github-social.png` (1280×640) is ready to upload as the GitHub repository social preview.
- `assets/og-image.png` (1200×630) is ready for link previews on Product Hunt, X, LinkedIn, Slack and Discord.

**Important:** these absolute URLs only work after the new `assets/` files are pushed to `main`. Until then, previews will show an empty image.

---

## 2. Landing page recommendation / 落地页建议

**Recommendation:** keep the Pages demo as the conversion target, but add a lightweight landing page **in front of it** once there is a real domain or a stable custom path. Do not build a heavy site before the demo has users.

Two practical options:

| Option | When | How |
|---|---|---|
| A. Keep root app (now) | Default, zero cost | `timyin7.github.io/Eco-Pomodoro/` stays the app. Add a `?landing` static hero section above the app only if you are willing to add scroll length. |
| B. Separate landing page (later) | After custom domain or first real traction | Create a `landing/` folder with one static `index.html`, publish it as a second Pages site or at a custom domain root, and link "Try the demo" to the app URL. |

**Landing page structure (one screen + three short sections):**

1. Hero: `Eco-Pomodoro` + exact phrase **"An eco-friendly Pomodoro timer where focus grows a living pond."** + one button: **Try the live demo**.
2. Proof strip: single file · offline · local-first · no account · MIT.
3. Three benefit blocks: visible progress / reliable timing / your data stays yours.
4. Screenshot or 20–30s demo GIF using `assets/demo-screenshot.png` or `assets/demo.gif`.
5. Footer links: GitHub repo, issues, README, license.

**Do not add:** signup forms, email capture, analytics scripts, external fonts or CDNs. Any of these would contradict the project's local-first promise.

---

## 3. Wording to use / 关键词

Use the same core phrase everywhere so search engines and humans get one consistent signal:

- **Primary:** `eco-friendly Pomodoro timer`
- **Secondary:** `single-file Pomodoro`, `offline Pomodoro timer`, `local-first focus timer`, `pond Pomodoro`, `no-account Pomodoro`
- **Project name:** `Eco-Pomodoro`; subtitle `Eco Pond`
- **Avoid:** `Pomodoro timer ADHD`, `best Pomodoro app`, `free forever`, `privacy focused` without explanation, or any superlative you cannot support.

Example meta description (155 characters):

```text
An eco-friendly Pomodoro timer where focus grows a living pond. One HTML file, offline, local-first, no account.
```

---

## 4. Drop-in `<head>` block / 可直接复制

The live app already contains this block. Use it on a future landing page too, changing only the canonical URL if the page moves.

```html
<title>Eco-Pomodoro — An eco-friendly Pomodoro timer</title>
<meta name="description" content="An eco-friendly Pomodoro timer where focus grows a living pond. One HTML file, offline, local-first, no account.">
<link rel="canonical" href="https://timyin7.github.io/Eco-Pomodoro/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Eco-Pomodoro">
<meta property="og:title" content="Eco-Pomodoro — An eco-friendly Pomodoro timer">
<meta property="og:description" content="Focus grows a living pond. One HTML file, offline, local-first, no account.">
<meta property="og:url" content="https://timyin7.github.io/Eco-Pomodoro/">
<meta property="og:image" content="https://timyin7.github.io/Eco-Pomodoro/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Eco-Pomodoro — An eco-friendly Pomodoro timer">
<meta name="twitter:description" content="Focus grows a living pond. One HTML file, offline, local-first, no account.">
<meta name="twitter:image" content="https://timyin7.github.io/Eco-Pomodoro/assets/og-image.png">
```

**GitHub social preview:** Settings → General → Social preview → upload `assets/github-social.png`. GitHub uses a separate image from Open Graph; upload both.

---

## 5. Image specs / 图片规格

| File | Size | Used for |
|---|---|---|
| `assets/github-social.png` | 1280×640 | GitHub repo social preview card |
| `assets/og-image.png` | 1200×630 | Link unfurls on X, LinkedIn, Slack, Discord, Product Hunt |
| `assets/demo-screenshot.png` | 1440×900 | README hero and gallery images |
| `assets/demo.gif` | 20–30s, ≤10 MB target | README and landing page demo (not recorded yet) |

When a GIF is recorded, export a short muted loop and keep the static screenshot as the fallback. Do not stretch or crop the screenshot in a way that hides the timer.

---

## 6. Validation checklist / 验证清单

After pushing:

1. Open <https://timyin7.github.io/Eco-Pomodoro/assets/og-image.png> — must return the image, not 404.
2. Paste the demo URL into a private Slack/Discord/X/LinkedIn preview checker — confirm title, description and image.
3. Check the GitHub repo page social preview thumbnail.
4. Search `site:github.com/timyin7/Eco-Pomodoro "eco-friendly Pomodoro timer"` to confirm the description is indexed (may take days).
5. Re-check after any domain or canonical change.

**Privacy note:** do not add page-view counters to the single-file app. If a landing page ever needs anonymous traffic data, disclose it on that page and keep it separate from pond data.

---

## 7. Sources for platform guidance / 规则来源

Platform guidance checked 2026-11-18 while writing the promotion plan:

- Reddit Rules: <https://reddit.com/rules>
- Product Hunt launch guide: <https://www.producthunt.com/launch/sharing-your-launch>
- Dev Hunt FAQ: <https://devhunt.org/faq>
- AlternativeTo FAQ: <https://alternativeto.net/faq>
- Indie Hackers: <https://indiehackers.com/> and <https://indiehackers.com/terms>

Rules can change; re-read the target community's current rules on the day you post.
