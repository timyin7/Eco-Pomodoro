# v1.0 release notes (draft) / v1.0 发布说明（草稿）

> **Status: draft.** Do not publish as a GitHub Release until the checklist at the bottom is complete. No release date is claimed here.
>
> Product version `v1.0` is the first public release. The internal save format is `v2` (with automatic v1 migration); the two version numbers are intentionally different.

---

## Highlights

- **An eco-friendly Pomodoro timer where focus grows a living pond.** Completed sessions drive growth, breeding and species unlocks; idle and paused time freeze the ecology.
- **Single file, zero dependencies.** Everything lives in `index.html`: structure, styles and logic. Double-click to use offline, or serve it locally.
- **Timing you can trust.** Countdown uses `Date.now()` timestamps; backgrounding, screen lock and refresh do not drift the clock. Crashes resume from the saved end time.
- **Local-first data.** Auto-saves to `localStorage`, with JSON export/import, corruption backup and two-step ecology reset with restore.
- **Bilingual UI.** English / 中文 switching, with device preferences stored separately from pond saves.

---

## What is included

### Timer

- Idle → focus → break state machine with pause, resume and skip.
- Automatic long break every 4 pomodoros.
- Focus durations 5 / 15 / 25 / 45 / 60 minutes; short breaks 3 / 5 / 10; long breaks 10 / 15 / 20 / 30.
- Completion chime and browser notifications, with in-page fallback when notifications are unavailable.
- `Space` starts or pauses focus; ignored while typing or when a control has focus.

### Pond

- Plankton, weeds, fish, shrimp, tadpoles / frogs and koi, with juvenile → adult → elder life cycles.
- Hue inheritance, metamorphosis, lily pads and detritus feeding shrimp.
- Oxygen, water quality and biodiversity vitals, endangered warnings and a "Tend the pond" action.
- Unlock curve based on completed focus time: shrimp 1h → frogs 5h → koi 20h.
- Pond-age ranks: Spring → Brook → Deep Pool → Lake → Ocean.

### Records and portability

- Task names and tags with per-tag statistics.
- Cumulative focus, today's pomodoros, current and longest streaks.
- Auto-save every 8 seconds and on page close; versioned save with v1 migration and field validation.
- Export / import JSON; reset backs up the pond and keeps focus history.

### Engineering details

- Timestamp-based timing, segmented eco-time settlement and capped away catch-up (30 minutes).
- High-DPI canvas scaling with CSS logical coordinates.
- No external network requests, analytics or third-party scripts in the app.
- MIT licensed.

---

## Known limitations

- System notifications require HTTPS or `localhost`; under `file://` they fall back to in-page toasts.
- While the page is suspended by the OS, real-time notifications do not fire; state is reconciled from timestamps when you return.
- Saves live in `localStorage`; clearing site data erases them. Export a JSON backup regularly.
- No packaged PWA yet; the demo GIF and a custom landing page are still pending.

---

## Links

- Live demo: <https://timyin7.github.io/Eco-Pomodoro/>
- Repository: <https://github.com/timyin7/Eco-Pomodoro>
- Feedback / bugs: <https://github.com/timyin7/Eco-Pomodoro/issues>
- Contributing: `CONTRIBUTING.md`
- License: `LICENSE` (MIT)
- Release checklist and video plan: `PROMOTION-PLAN.md`

---

## Thanks

Thanks to everyone who tried an early build and gave feedback on the timer rules, save behavior and language switching.

---

## Pre-publish checklist

- [ ] Push READMEs, `LICENSE`, `CONTRIBUTING.md`, `assets/` and `promo/` to `main`.
- [ ] Set GitHub description, website URL and the five topics from `REPO-SETUP.md`.
- [ ] Upload `assets/github-social.png` as the repository social preview.
- [ ] Replace the README GIF placeholder with `assets/demo.gif`, or explicitly keep the static screenshot.
- [ ] Confirm the demo URL and OG image URL both return 200.
- [ ] Add a real release date and tag `v1.0`.
- [ ] Paste the short demo video into the GitHub Release description when ready.
