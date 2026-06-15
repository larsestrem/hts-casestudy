#!/usr/bin/env python3
"""Regenerate the flat, single-folder deploy build in ./build from the structured
source in ./portfolio. Cloudflare Pages serves ./build. Run this before every commit
(or just use ./deploy.sh). Never hand-edit ./build."""
import pathlib, shutil

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / 'portfolio'
OUT = ROOT / 'build'
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)

# structured page path  ->  flat filename
pages = {
    'index.html': 'index.html',
    'what-hts-does-right/index.html': 'what-hts-does-right.html',
    'the-opportunity/index.html': 'the-opportunity.html',
    'hts-case-study/index.html': 'how-i-help-hts-grow.html',
    'hts-case-study/win-contracts/index.html': 'win-contracts.html',
    'hts-case-study/mro-work/index.html': 'mro-work.html',
    'hts-case-study/recruit-pilots/index.html': 'recruit-pilots.html',
    'hts-case-study/recruit-mechanics/index.html': 'recruit-mechanics.html',
    'hts-case-study/brand-reputation/index.html': 'brand-reputation.html',
    'hts-case-study/capture-leads/index.html': 'capture-leads.html',
    'why-i-built-this/index.html': 'why-i-built-this.html',
    'path-forward/index.html': 'path-forward.html',
}

# absolute source refs -> flat relative refs (most specific first)
repls = [
    ('https://example.com/portfolio/', '/portfolio/'),
    ('/portfolio/assets/portfolio.css', 'portfolio.css'),
    ('/portfolio/assets/img/hero-skycrane.png', 'hero-skycrane.png'),
    ('/portfolio/assets/lars-estrem-resume.pdf', 'lars-estrem-resume.pdf'),
    ('/portfolio/hts-case-study/win-contracts/', 'win-contracts.html'),
    ('/portfolio/hts-case-study/mro-work/', 'mro-work.html'),
    ('/portfolio/hts-case-study/recruit-pilots/', 'recruit-pilots.html'),
    ('/portfolio/hts-case-study/recruit-mechanics/', 'recruit-mechanics.html'),
    ('/portfolio/hts-case-study/brand-reputation/', 'brand-reputation.html'),
    ('/portfolio/hts-case-study/capture-leads/', 'capture-leads.html'),
    ('/portfolio/hts-case-study/', 'how-i-help-hts-grow.html'),
    ('/portfolio/what-hts-does-right/', 'what-hts-does-right.html'),
    ('/portfolio/the-opportunity/', 'the-opportunity.html'),
    ('/portfolio/why-i-built-this/', 'why-i-built-this.html'),
    ('/portfolio/path-forward/', 'path-forward.html'),
    ('/portfolio/', 'index.html'),
]

for src, dst in pages.items():
    t = (SRC / src).read_text()
    for a, b in repls:
        t = t.replace(a, b)
    (OUT / dst).write_text(t)

for asset in ['assets/portfolio.css', 'assets/img/hero-skycrane.png', 'assets/lars-estrem-resume.pdf']:
    shutil.copy(SRC / asset, OUT / pathlib.Path(asset).name)

stray = [f.name for f in OUT.glob('*.html')
         if '/portfolio/' in f.read_text() or 'example.com' in f.read_text()]
print('stray absolute refs:', stray or 'none')
print('build files:', len(list(OUT.iterdir())), '(expected 15)')
