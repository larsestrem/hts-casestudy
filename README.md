# HTS Growth Strategy — Case Study Site

A static, zero-JavaScript case-study site built for Helicopter Transport Services (HTS).
System fonts, one shared stylesheet, no frameworks, no tracking. Every page is set to
`noindex`.

The site lives under `portfolio/`. Once this repo is published to a static host
(GitHub Pages, Cloudflare Pages, Netlify), the home page is at `/portfolio/`.

## Pages
- `portfolio/index.html` — Home (the case in five steps)
- `portfolio/what-hts-does-right/` — Step 1
- `portfolio/the-opportunity/` — Step 2
- `portfolio/hts-case-study/` — Step 3, The Prototype (hub + six deep-dives)
- `portfolio/why-i-built-this/` — Step 4
- `portfolio/path-forward/` — Step 5
- `portfolio/assets/portfolio.css` — shared stylesheet
- `portfolio/assets/img/hero-skycrane.png` — home hero image (PLACEHOLDER — replace this file)
- `portfolio/assets/lars-estrem-resume.pdf` — résumé

## Replace the hero image
Replace `portfolio/assets/img/hero-skycrane.png` with your Skycrane image, keeping the
same filename. No code change needed.

## noindex
Every page carries a `noindex` meta tag so it isn't surfaced in search. Remove those tags
to make it publicly discoverable.
