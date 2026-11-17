[中文](README.md) · **English**

# Eco Pond Pomodoro · 生态番茄钟

A Pomodoro timer that turns **focus** into **ecosystem evolution**: every focus session grows a tiny pond — plankton multiplies, weeds stretch upward, fish breed and pass down their body hue, tadpoles metamorphose into frogs, and a koi glides by. The longer you focus, the richer and livelier your pond becomes.

**Zero dependencies · Single file · Works offline · All data stays local.**

---

## How to use

### Start a focus session

1. Double-click `index.html` — no build, no network required (a local static server is recommended, see "Quick start" below).
2. Optional: type a task name (up to 24 characters) and pick a tag (Study / Work / Reading / Creation / Other). Tags are used for grouping in the diary and stats.
3. Pick durations: focus 5 / 15 / 25 / 45 / 60 minutes (default 25), short break 3 / 5 / 10 (default 5), long break 10 / 15 / 20 / 30 (default 15).
4. Click "Start focus" or press `Space`. When focus ends you **automatically** enter a break; when the break ends the pond returns to idle and waits for the next pomodoro.
5. Changing durations mid-session never interrupts the current stage — it takes effect at the **next** stage.

### Timer rules

- Full state machine: idle → focus → break → idle, with pause / resume / skip.
- A **long break starts automatically every 4 pomodoros**, in a repeating cycle.
- **Pause**: eco time freezes too; resuming picks up right where you paused.
- **Skip**: skips the current stage. A skipped focus earns **nothing** — no pomodoro count, no accumulated focus time; eco time already elapsed is still credited.
- `Space`: starts focus when idle, pauses / resumes while running. Ignored while an input, dropdown, or button has focus.
- Timing is based on `Date.now()` timestamps (`endAt`) and never drifts when backgrounded, screen-locked, or refreshed. Crashes / refreshes resume from `endAt`, and anything that came due while you were away is credited retroactively.

### Pond rules

- **Two clocks**: the animation always flows, but growth, hunger, breeding, and death advance only with "eco time" — ×1 full speed while focusing, ×0.25 during breaks, frozen when idle or paused.
- **Away catch-up**: while the page is suspended, eco time is back-computed from elapsed wall-clock time, capped at 30 minutes per catch-up (digested frame by frame, so no single jump starves the whole pond).
- **Vitals panel**: oxygen (produced by weeds − consumed by creatures), water quality (detritus pollutes − shrimp purify), biodiversity. Overcrowded fish cause hypoxia; piled-up detritus degrades water. Focusing restores health, and "Tend the pond" (oxygen +10, quality +12, scoops 30% of detritus, 90-second cooldown) lets you intervene manually.
- **Species unlock** by cumulative real focus time: shrimp at 1h → tadpoles & frogs at 5h → koi at 20h. Locked species appear as silhouettes in the guide.
- **Ecological feedback**: a species down to its last member triggers an endangered warning; extinction is not the end — completing a focus session calls unlocked species back.
- **Reset ecology**: two-step confirmation (first click arms it; click again within 3 seconds to execute), automatically backed up beforehand, with a "Restore backup" entry. Resetting clears only the ecology — cumulative focus, pomodoro count, and history are all kept.

### Interface language

The **Language** dropdown at the left of the settings row switches between **English / 中文**, takes effect immediately, and is remembered. First-time users get a language guessed from the system locale. Language, mute, and notifications are **device preferences**, stored separately — they never change when a pond save is exported, imported, or restored.

### Save

- Auto-saves to `localStorage` every 8 seconds, and once more before the page closes.
- Versioned save format + automatic v1 migration + per-field validation; corrupted saves are backed up and rebuilt automatically.
- **Export as JSON** and **import back** are supported — handy for moving between devices.

---

## Features

### Eco pond

- Five creatures plus plants: plankton, weeds, fish, shrimp, tadpoles / frogs, koi
- Life cycle: juvenile → adult → elder — they hunger, age out, and reproduce
- Hue inheritance: offspring inherit their parent's body color with slight mutations, creating generational drift
- Tadpole metamorphosis: grown frogs hop onto lily pads and lay eggs for the next generation
- Detritus sinks to feed the shrimp — a tiny matter cycle

### Stats & growth

- Cumulative focus time, today's pomodoros, current streak, longest streak
- Pond-age ranks: Spring → Brook → Deep Pool → Lake → Ocean (a long-term goal)

### Others

- Task name and tag, with per-tag statistics
- Chime on completion, browser system notifications (automatically degraded to in-page toasts when unavailable)
- Statistics and the species-unlock curve strictly share the same source of truth

---

## Quick start

**Option 1: just open it**

Double-click `index.html`. No build, no dependencies, no network required.

**Option 2: local static server** (recommended — notifications and some browser features are restricted under `file://`)

```bash
# pick one
npx serve .
python -m http.server 8080
```

Then visit `http://localhost:8080`.

---

## File structure

```
.
├── index.html      # the app: structure + styles + all logic (inlined, single file)
├── README.md       # 中文说明 (Chinese readme)
├── README.en.md    # English readme
└── .gitignore
```

The code is organized in four layers, all inside `index.html`'s `<script>`:

| Block | Responsibility |
|---|---|
| `CONFIG` | All tunable numbers (durations, caps, rates, unlock thresholds) in one place |
| `Creature` & subclasses | Creature base class plus `Fish` / `Shrimp` / `Tadpole` / `Frog` / `Koi` / `Weed` / `Pad` |
| `pond` | Ecology state, update & draw, save I/O, stats & unlocks |
| `pomo` | Pomodoro state machine, segmented time settlement, notifications & chime |

---

## Key designs

**Timestamps, not frame counts.** The main loop only does "due check → settle → digest"; even if rAF stalls, `endAt` stays correct.

**Eco time uses segmented settlement.** A time anchor plus a backlog queue (`pendingEco`): before every state switch, elapsed time is settled at the **pre-switch** rate and enqueued; the main loop digests at most 300 eco-seconds per frame. This keeps "25 minutes of focus" and "5 minutes of break" from ever sharing a rate.

**Accounting happens only on completion.** `totalFocusSec` is credited exclusively by `creditFocus()` when a pomodoro completes (or is recovered after a crash); pauses and skips count for nothing — so the unlock curve (1h / 5h / 20h) and the stats panel are strictly the same numbers.

**Catch-up is capped.** At most 1800 eco-seconds (30 minutes) per catch-up, so an overnight sleep can't starve the entire pond in one jump.

**High-DPI displays.** `ctx.setTransform(dpr, 0, 0, dpr, 0, 0)`; every creature uses CSS logical coordinates, with DPR capped at 2x.

**Device preferences live apart from the pond save.** Language / mute / notifications are stored in a separate `prefs` key, so exporting / importing / restoring a pond save never changes this device's interface preferences.

---

## Extension points

- **Add a species**: extend `Creature` (or `Fish`), add one row to `SPECIES_META`, and register the new class in `biodiversity()`'s groups.
- **Tune pacing**: every number lives in `CONFIG`; edit and refresh.
- **Restyle**: colors are centralized in CSS variables plus a few gradient definitions inside `draw()`.
- **Add a language**: add a new language key to the `I18N` dictionary with the full set of strings — the UI picks it up immediately.

---

## Known limitations

- System notifications require HTTPS or `localhost`; under `file://` they automatically degrade to in-page toasts.
- While the page is suspended by the OS, no real-time notifications fire — everything is back-computed and credited from timestamps when you return.
- Saves live in `localStorage`; clearing site data in the browser erases them — use "Export save" regularly to keep a backup.

---

## License

Personal project; no open-source license specified yet. Please contact the author before public reuse.
