# HANDOFF — context for taking over the HTS case study

## Who & why
- **Author / user:** Lars Estrem (larsestrem@gmail.com). ~18 years in digital marketing,
  ~14 years in the fire service (including wildland fire). Lives in Canby, Oregon, near
  HTS's Aurora base.
- **Audience:** leadership at **Helicopter Transport Services (HTS)** — a ~50-year,
  privately held heavy-lift helicopter operator. Skycranes (S-64 / CH-54), Black Hawks,
  Bell mediums; 60+ aircraft across ~10 types. Two FAA Part 145 stations: a full-service
  depot in Aurora, OR (210,000+ sq ft) and an engine center in Perryville, MO (the JFTD12A
  that powers every Skycrane).
- **Purpose:** a "show, don't tell" pitch. Lars had reached out twice the normal way;
  instead of a third note he built this clickable case study plus a 120-page working
  prototype of HTS's own site, to demonstrate the marketing opportunity. The aim is a
  marketing role. The prototype itself is **not** in this repo and is kept unpublished.

## The argument (the 5-step route the site walks)
Home → **What HTS Does Right** (earn credibility by praising the company) → **The
Opportunity** (a great company the internet can't see: search/AI visibility gap, E-E-A-T,
and the visibility → branding → following → reputation → easier-sales flywheel) → **How I'd
Help HTS Grow** (six concrete levers, below) → **Why I Built This** (Lars's fit + the "this
is unpublished, let's review it together" caveat) → **The Path Forward** (a ~60-day plan:
review every page with HTS first, then go live).

## The six growth levers (the middle of the site)
Deliberately framed as **audience/outcome** pages, not SEO-technique pages:
1. **Win Contracts** — publish every capability/aircraft as a findable page so qualified
   buyers self-serve the specs, then a spec-driven quote form returns a faster, accurate
   answer. (CH-54B-at-10,000-ft example; real tail numbers; fleet "two outcomes.")
2. **MRO & Third-Party Work** — capture AOG (aircraft-on-ground) urgency and engine/
   component overhaul demand from other operators; facility-specialized pages (Aurora vs
   Perryville).
3. **Recruit Pilots** — make the career ladders findable (Bell ladder; PIC trainee →
   Skycrane; the internal-only Black Hawk seat); answer "why HTS" fast; military-to-civilian.
4. **Recruit Mechanics** — surface the 36-month A&P apprenticeship and depot-level variety;
   reach both licensed and aspiring mechanics.
5. **Brand & Reputation** — the visibility flywheel + turning real field operations (fire
   water drops, tower sets) into permanent, indexable pages + reviews/third-party signals.
6. **Capture & Measure Leads** — more contact pathways (online + emailable forms + phone,
   **added to** what HTS does now), forms where every field qualifies the lead, **and the
   measure-then-improve loop** (track which pages/campaigns produce the *right* leads,
   iterate; the site becomes a compounding asset competitors can't catch). **This
   measurement loop is the user's favorite part — keep it prominent.**

## Key decisions already made (don't undo without asking)
- The hub was renamed from "The Prototype" to **"How I'd Help HTS Grow"**; its six children
  are growth levers. The OLD technique pages (fleet-keywords, black-hawk-deep-dive,
  mro-lead-gen, talent-acquisition, conversion-engineering, real-time-authority) were
  **removed** — do not bring them back.
- Recruiting was **split** into pilots vs mechanics (the user's two explicit hiring goals).
- The **measurement/iteration** content was added to Capture & Measure Leads.
- Tone was softened to **respect HTS's existing sales success** ("broaden the channels," not
  "fix sales").

## Open items / likely next tasks
- Replace the hero image `portfolio/assets/img/hero-skycrane.png` (a pen-and-ink
  placeholder) with a real Skycrane photo — **keep the filename** — then re-run flatten.
- Replace the screenshot placeholders with real prototype screenshots.
- A content-accuracy pass **with HTS** (the prototype took liberties); correct specifics
  they flag.
- Soften any remaining unverifiable claims if HTS pushes back.
- Only if HTS approves: remove `noindex` and publish — **on explicit instruction only**.

## Canonical shared nav block (identical on all 12 pages)
The active page adds `class="active" aria-current="page"` to its top-level link; the
dropdown parent link is active on the hub and on all six lever pages.
```html
<nav class="cs-nav" aria-label="Site navigation">
  <a href="/portfolio/">Home</a>
  <a href="/portfolio/what-hts-does-right/">What HTS Does Right</a>
  <a href="/portfolio/the-opportunity/">The Opportunity</a>
  <span class="has-drop">
    <a href="/portfolio/hts-case-study/">How I'd Help HTS Grow &#9662;</a>
    <span class="drop">
      <a href="/portfolio/hts-case-study/win-contracts/">Win Contracts</a>
      <a href="/portfolio/hts-case-study/mro-work/">MRO &amp; Third-Party Work</a>
      <a href="/portfolio/hts-case-study/recruit-pilots/">Recruit Pilots</a>
      <a href="/portfolio/hts-case-study/recruit-mechanics/">Recruit Mechanics</a>
      <a href="/portfolio/hts-case-study/brand-reputation/">Brand &amp; Reputation</a>
      <a href="/portfolio/hts-case-study/capture-leads/">Capture &amp; Measure Leads</a>
    </span>
  </span>
  <a href="/portfolio/why-i-built-this/">Why I Built This</a>
  <a href="/portfolio/path-forward/">The Path Forward</a>
</nav>
```

## Deploy & verify (copy-paste)
Regenerate the flat build and sanity-check it:
```bash
python3 flatten.py   # expect: stray absolute refs: none / build files: 15
```
Full preflight (links, counts, banned characters):
```bash
python3 - <<'EOF'
import re, pathlib
root = pathlib.Path('portfolio'); files = list(root.rglob('*.html'))
targets = {'/portfolio/'} | {f'/{f.parent.as_posix()}/' for f in files if f.name=='index.html'}
bad=[]
for f in files:
    for m in re.findall(r'href="(/portfolio/[^"#]*?)(?:#[^"]*)?"', f.read_text()):
        if m.endswith(('.css','.pdf','.png')):
            if not pathlib.Path(m.lstrip('/')).exists(): bad.append((str(f),m))
        elif m not in targets: bad.append((str(f),m))
print('broken links:', bad or 'none')
print('pages:', len(files), '(expected 12)')
EOF
grep -rc '—\|&mdash;' portfolio --include=*.html | grep -v ':0' || echo "em-dash: 0"
grep -ric 'honest'      portfolio --include=*.html | grep -v ':0' || echo "honest: 0"
```
Ship it:
```bash
./deploy.sh "what changed"
```

## Preview locally
```bash
# structured source:
python3 -m http.server 8000      # http://localhost:8000/portfolio/
# flat build, exactly as deployed:
cd build && python3 -m http.server 8001   # http://localhost:8001/
```

## Fallback: manual Cloudflare upload (if git integration isn't wired yet)
```bash
python3 flatten.py && (cd build && zip -r ../site.zip .)   # then drag site.zip into Cloudflare
```
