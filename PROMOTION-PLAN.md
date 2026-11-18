# Eco-Pomodoro promotion plan / 推广方案

Updated 2026-11-18. This is a **plan and copy kit**, not a publishing record. Nothing here has been posted by the assistant, and no result metric is claimed.

---

## 0. Verified baseline / 已核实信息

| Item | Status |
|---|---|
| Live browser demo | <https://timyin7.github.io/Eco-Pomodoro/> — GitHub Pages is enabled and serving the app |
| Repository | <https://github.com/timyin7/Eco-Pomodoro> |
| Issues | Enabled; used as the feedback entrance |
| License | MIT added locally in `LICENSE`; **push still required** |
| Repo topics | Empty — needs the five topics in `REPO-SETUP.md` |
| Description / website | Both unset — exact text in `REPO-SETUP.md` |
| Demo screenshot | `assets/demo-screenshot.png` captured from the live Pages URL |
| Social preview | `assets/github-social.png` (1280×640) and `assets/og-image.png` (1200×630) generated locally |
| Stars / forks | 1 / 0 at check time — do not use as a marketing claim |
| Demo GIF / video | Not recorded yet; README contains a clearly marked placeholder and shot list |

**Conversion path:** external post → live demo → GitHub repo → issue / star. Every post should keep that path short and explicit.

---

## 1. Positioning / 定位

**One-liner (English):** An eco-friendly Pomodoro timer where focus grows a living pond — one HTML file, offline, local-first.

**一句话（中文）：** 一个把专注变成生态演化的治愈系番茄钟：单文件、离线、无账号，数据只存在本地。

**SEO / discovery wording to repeat consistently:**

- primary phrase: **eco-friendly Pomodoro timer**
- secondary: single-file Pomodoro, offline Pomodoro timer, local-first focus timer, pond-growth Pomodoro
- project name: **Eco-Pomodoro** (write "Eco Pond" only as a subtitle)

**Proof points (all verified in repo):**

1. One `index.html`, zero dependencies, no build step; opens offline.
2. Completed focus sessions drive a pond ecosystem; species unlock at 1h / 5h / 20h.
3. Timestamp-based timing survives background tabs, refresh and crash; away catch-up is capped at 30 minutes.
4. Saves stay in `localStorage`, with JSON export/import and corruption recovery.
5. Bilingual UI; device preferences stored separately from pond data.
6. No external network requests in the app source.

**Do not say:**

- "treats ADHD", "cures procrastination", or any medical claim.
- "thousands of users", "fastest", "best", "replaces all other timers" — no evidence.
- "fully self-hosted server app" — it is a static local-first file, not a server deployment.
- "traffic / revenue results" — none measured.

---

## 2. Prerequisites before external posting (P0)

Do these first; traffic without a working conversion path is wasted.

1. Push the local docs/assets: READMEs, MIT `LICENSE`, `CONTRIBUTING.md`, `assets/`, `promo/`, `SEO-RECOMMENDATIONS.md`, `RELEASE-NOTES-v1.0.md`.
2. Fill GitHub About: description, website, five topics, social preview. See `REPO-SETUP.md`.
3. Confirm the Issues tab is open and add a short issue template or a link to `CONTRIBUTING.md`.
4. Replace the README GIF placeholder with a 20–30s recording when available. Until then, keep the static screenshot; do not imply a GIF exists.
5. Ask 10 people to use it for 3 days and report when they open it and why. Collect their words, not just likes.

**Completion test:** a stranger can open the demo in one click, understand it in five seconds, and find a place to give feedback.

---

## 3. Channel matrix / 渠道判断

| Channel | Fit | Goal | What to do | Caveat from current platform guidance |
|---|---|---|---|---|
| **r/productivity** | Medium | Honest feedback from people who care about focus systems | First-person text post about the pond idea; link in body only if rules allow | Reddit Rule 2 requires following each community's rules and no spam; "9:1" is a community heuristic, not a universal platform rule. Read the sidebar rules and post history first. |
| **r/selfhosted** | Low–medium | Niche signal from local-first/privacy audience | Only if framed as "local-first static app, no server, no cloud"; ask mods before posting | It is not a self-hosted service. Do not imply Docker/server deployment. |
| **Product Hunt** | Medium | One-day burst of early adopter feedback | Need landing/OG assets, gallery images, maker comment, and a full day in comments | Official guide: use a personal account; never ask for upvotes or run upvote-linked contests; launch starts 12:01 AM PT; avoid communities you have not participated in. |
| **Dev Hunt** | Low | Probably skip for now | If tried, lead with "open-source single-file web app" and link the repo | DevHunt only accepts tools for developers; a general Pomodoro timer may be rejected. Free listing gets a permanent page; paid launch is optional. Verify current rules before spending. |
| **Indie Hackers** | High | Build-in-public story and thoughtful discussion | Post the motivation/design/development story below; ask one specific question | Keep it first-person and substantive; avoid link-only posts. |
| **AlternativeTo** | Low | Long-tail discovery only if accepted | Submit once with clean official URL, no UTM, and honest category/tags | FAQ explicitly declines simple "timers and clocks" and single-purpose online tools; expect rejection. Do not spend effort here before stronger differentiation. |
| **Discord / dev communities** | Medium | Warm feedback from people you know | Only in servers where you are already active; ask a mod, then share demo + one question | Do not drop links in unrelated servers. No mass DMs. |
| **Chinese channels** (V2EX, 少数派, 即刻, 小红书, B站) | Medium–high | Visual + storytelling reach | Reuse the same evidence with different angles: 故事型 / 极客型 / 隐私型; see earlier Chinese plan sections | Keep one channel at a time; first-person; no crown-tagging or vote manipulation. |

**Priority order:** GitHub/Pages baseline → Indie Hackers + one developer community → Product Hunt (after landing page) → Reddit with rule check → directories. Skip Dev Hunt / AlternativeTo unless their eligibility changes or the product becomes clearly developer-tool-like.

---

## 4. Ready-to-adapt copy / 可直接改用的文案

### r/productivity — title options

1. I built a Pomodoro timer where a tiny pond grows while you focus
2. Tried making focus sessions visible: completed pomodoros breed fish in a pond
3. A low-pressure timer that grows an ecosystem instead of a streak counter

**Body:**

> I wanted a timer that showed the result of focusing without turning into another streak-based chore, so I built Eco-Pomodoro.
>
> Each completed focus session advances a small pond: plankton multiplies, weeds grow, fish breed and pass on their color, tadpoles become frogs. Unlocked species follow real focus hours (shrimp 1h, frogs 5h, koi 20h). Breaks slow the ecology down; idle time freezes it.
>
> It is one HTML file, works offline, has no account and keeps saves in localStorage with JSON export. Timing uses timestamps rather than frame counts, so switching tabs or refreshing does not drift the countdown.
>
> Live demo: https://timyin7.github.io/Eco-Pomodoro/
> Source: https://github.com/timyin7/Eco-Pomodoro
>
> I am mainly curious whether the pond feedback actually makes you come back for a second session, or whether it is just a novelty. Honest feedback welcome.

### r/selfhosted — conditional title and body

> **Title:** Local-first static Pomodoro timer with a growing pond — no server or cloud involved
>
> This is not a server app, so posting here only makes sense if your community accepts local-first static tools. Eco-Pomodoro is a single `index.html`: no backend, no account, no third-party requests, and saves stay in the browser with JSON export/import. Focus sessions grow a small pond ecosystem. Demo and source linked in the first comment if allowed.

### Product Hunt — tagline and maker comment

**Tagline:** A Pomodoro timer that grows a living pond

**Maker comment:**

> I built Eco-Pomodoro because I wanted focus time to leave something visible behind, not just a number in a streak.
>
> Every completed session advances a tiny pond. Fish breed and pass on their color, tadpoles become frogs, and koi unlock after 20 hours of real focus time. It is one HTML file with no build step, no account and no network requests; saves stay in your browser and can be exported as JSON.
>
> What works today: the full timer state machine, the pond ecosystem, bilingual UI, notifications and save recovery. What is still missing: a demo GIF, a packaged PWA and a custom landing page.
>
> I would love feedback on the first-minute experience: does the pond make you want to start a session, or is it too subtle?

### Dev Hunt — conditional short description

> Single-file, zero-dependency Pomodoro timer with a timestamp-based state machine and a canvas ecosystem that evolves with completed focus sessions. Open source under MIT.

First comment: say what works, what is missing, and ask for one specific type of feedback. Do not ask for votes.

### Indie Hackers — post

> **Title:** I built a Pomodoro timer that grows a pond, because streaks were not motivating me
>
> Streak counters always made me feel like I was protecting a number rather than doing useful work. So I made the reward the work itself: each completed focus session changes a small pond. Fish breed and inherit color, tadpoles turn into frogs, and a koi shows up after 20 hours of real focus.
>
> The design constraint was that it had to stay a single HTML file. No build, no account, no server, no analytics, no cloud. Saves live in localStorage and can be exported as JSON. Timing uses timestamps, so a background tab or a refresh does not lose the session.
>
> The hardest part was not the visuals, it was the accounting: only completed pomodoros may add focus time, and the species unlock curve must use that exact same number. Pauses and skips cannot inflate it. I settled eco-time in segments before every state change so focus and break rates never mix.
>
> It is still early. I would like to know whether the pond actually changes behavior, or is only a nice first impression. If you try it, tell me whether you came back for a second session and why.

### AlternativeTo — short description (expect review)

> Eco-Pomodoro is a local-first focus timer that grows a small pond as you complete sessions. Single HTML file, offline, no account, local saves with JSON export.

### Discord / dev community — short message

> Built a small focus timer: one HTML file, offline, no account, and completed sessions grow a little pond with fish, frogs and koi. Live demo: https://timyin7.github.io/Eco-Pomodoro/ — would love one honest opinion on whether the pond is motivating or just distracting.

### Short motivation / design / development post (one post)

> **Motivation.** I did not want another streak counter. I wanted the time I spent focusing to leave something visible behind, so I made a pond that grows only when a focus session is actually completed.
>
> **Design.** The timer and the pond use two different clocks. Animation always flows, but growth and breeding advance only during focus, slowly during breaks, and not at all while idle. That makes the pond feel alive without making the timer feel unfair.
>
> **Development.** The whole app is one HTML file with no dependencies. The tricky part was time: counting by frames drifts in background tabs, so the timer uses timestamps, and eco-time is settled in segments before every state change. The rate-limit and crash-recovery details matter more than the visuals.

---

## 5. Demo video plan / 视频计划

**Core 30–45 second storyboard (silent, music only, captions burned in):**

1. 0–5s: cold open — 25:00 timer, pond idle, caption "Focus time you can see."
2. 5–15s: choose 5 minutes, press Start; daylight warms the pond, bubbles increase.
3. 15–25s: time-lapse-style crop showing fish/plants moving; caption "A completed session feeds the pond."
4. 25–35s: focus ends → moonlit break; caption "Breaks slow the ecosystem down."
5. 35–45s: species guide with locked silhouettes and progress; end card with demo URL.

**Platform cuts:**

| Platform | Length / format | Hook | CTA |
|---|---|---|---|
| YouTube | 45–60s, 16:9, title + description links | "I made a Pomodoro timer that grows fish" | Description: live demo, GitHub, issue tracker |
| LinkedIn | 30–45s, 1:1 or 16:9, captions on | "A focus timer without a streak counter" | Comment link to demo; ask one question |
| TikTok / Reels | 15–30s, 9:16, large captions | "专注 25 分钟，池塘真的会变化" | Bio / pinned comment with demo link |

**Production rules:** screen recording only; no fake stats; no voice claim about health benefits; keep the original audio or use licensed music; label any sped-up footage as time-lapse.

---

## 6. Feedback and issue tracker / 反馈入口

- Primary: <https://github.com/timyin7/Eco-Pomodoro/issues>
- Contribution rules: `CONTRIBUTING.md`
- Suggested issue labels: `feedback`, `bug`, `idea`, `i18n`, `visual`
- In every post, ask **one** concrete question. Example: "Did you come back for a second session, and why?"
- Save user wording verbatim in a feedback note; tag as 视觉 / 工具 / 生态驱动 / 隐私.

---

## 7. Ongoing small, measurable improvements / 持续改进

Weekly loop (30–60 minutes):

1. Triage issues: reply to every new one within 48 hours; label it.
2. Pick **one** small change with a clear before/after signal (e.g. clearer start button label, one accessibility fix, one i18n string).
3. Ship it, update `RELEASE-NOTES-v1.0.md` with a dated line.
4. Check the demo link and one community post; record click-through and qualitative feedback only.
5. Decide: keep, revert, or expand. No vanity metrics.

**Signals worth tracking:**

- demo link clicks per post (platform analytics)
- number of people who report completing a first session (voluntary)
- 7-day return reports (voluntary)
- issues opened by strangers, PRs, forks
- which wording people repeat back to you

**Privacy red line:** the app claims local-only data. Do not add analytics scripts to the single-file app. Any anonymous page counting on the landing page must be disclosed and must never touch pond data.

**Release cadence:** publish `v1.0` when the demo GIF, MIT license, repo metadata and contribution guide are all live. After that, ship small dated updates instead of accumulating a large unreleased batch.
