# HTS Growth Strategy — case study site (project memory)

This repo is a **static, zero-JavaScript** portfolio case study built **by Lars Estrem**
**for the leadership of Helicopter Transport Services (HTS)**, a heavy-lift helicopter
operator in Aurora, Oregon. It argues that HTS is exceptional but nearly invisible online,
and shows, through a clickable case study plus a referenced 120-page prototype, how to fix
that. The goal is to win Lars a marketing role at HTS. **Read `HANDOFF.md`** for the full
backstory, the six growth levers, and open items.

## How this deploys (read first)
- `portfolio/` is the **editable source** (structured: one folder per page, absolute
  `/portfolio/...` links). This is the single source of truth. Edit here.
- `build/` is the **flat deploy artifact** (one folder, relative links) that Cloudflare
  Pages serves. It is **generated, never hand-edited**.
- `flatten.py` regenerates `build/` from `portfolio/`. Cloudflare Pages is connected to this
  repo (git integration, production branch `main`, output directory `build`) and
  **auto-deploys on every push to `main`**.
- To ship: run `python3 flatten.py`, then commit **both** `portfolio/` and `build/`, then
  push. Or just run `./deploy.sh "message"` (does all three).
- When the user says **"deploy" / "ship it" / "push it live"**, that means run
  `./deploy.sh "<short message>"`. Confirm the flatten verification printed cleanly first
  (`stray absolute refs: none`, `build files: 15`).
- The absolute `/portfolio/...` links in the source are **intentional** — flatten.py
  converts them to relative. Do not "fix" them to relative in `portfolio/`.

## The site: 12 pages
1. Home — `/portfolio/`
2. What HTS Does Right — `/portfolio/what-hts-does-right/`
3. The Opportunity — `/portfolio/the-opportunity/`
4. **How I'd Help HTS Grow** (hub) — `/portfolio/hts-case-study/` — routes to six levers:
   - Win Contracts — `/portfolio/hts-case-study/win-contracts/`
   - MRO & Third-Party Work — `/portfolio/hts-case-study/mro-work/`
   - Recruit Pilots — `/portfolio/hts-case-study/recruit-pilots/`
   - Recruit Mechanics — `/portfolio/hts-case-study/recruit-mechanics/`
   - Brand & Reputation — `/portfolio/hts-case-study/brand-reputation/`
   - Capture & Measure Leads — `/portfolio/hts-case-study/capture-leads/`
5. Why I Built This — `/portfolio/why-i-built-this/`
6. The Path Forward — `/portfolio/path-forward/`

The shared header/nav (with the "How I'd Help HTS Grow" dropdown) and footer are
**identical on all 12 pages**. If you change the nav, change it on all 12 and re-run
flatten. The canonical nav block is in `HANDOFF.md`.

## Hard content rules (do not break)
- **Zero JavaScript, zero web fonts.** The only `<script>` allowed is
  `application/ld+json` (structured data). The mobile nav is pure CSS (a checkbox toggle).
  If something seems to need JS, find a static/CSS way or ask.
- **No em dashes anywhere.** Use commas, periods, or parentheses. Source and build must
  contain zero `—` and zero `&mdash;`.
- **Avoid the word "honest"/"honestly"** (it implies the rest isn't).
- **Claims must be verifiable and measured.** Do not invent specifics about HTS. Avoid
  unverifiable absolutes (e.g. never "no off-season layoffs"; say "year-round work across a
  diversified portfolio"). When unsure of a fact, hedge or omit. The prototype "takes some
  liberties" and is pending HTS's own review — that caveat is already on the site; keep it.
- **Every page stays `noindex, nofollow`** (this is an unpublished demo). Keep the robots
  meta tag. Do not deindex/publish without the user's explicit instruction.
- **Screenshots are placeholders** (styled `.shot` boxes labeled "Screenshot to be added").
  Real screenshots come later.
- **Positioning:** respect HTS's existing, successful sales team. The site "broadens the
  channels that feed a team that already closes" — it does **not** "fix a sales problem."
  Growth and recruiting are framed as adding leads/candidates, never as criticism.

## Voice
Plain, confident, specific, peer-to-peer (a marketer talking to operators). Lead with the
buyer's or candidate's real question. Short paragraphs. Concrete nouns (tail numbers
N60HT/N61HT/N62HT, engines JFTD12A/T700/PT6T, the 210,000 sq ft Aurora depot). No hype.

## Before every commit, verify
- `python3 flatten.py` prints `stray absolute refs: none` and `build files: 15`.
- Internal links resolve (no `/portfolio/...` href without a matching page).
- Zero `—` / `&mdash;`, zero "honest", only `ld+json` scripts.
`HANDOFF.md` has copy-paste verification commands.

## What NOT to do
- Don't add analytics, fonts, frameworks, or any build step beyond `flatten.py`.
- Don't remove `noindex` or publish without explicit say-so.
- Don't open PRs or create branches unless asked — work toward `main`; deploy = push to
  `main` (that is the intended deploy path here).
