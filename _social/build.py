"""Instagram slides for Natalia Zute Health, rendered from HTML in the website's style.

python3 _social/build.py <post-name> [lang ...]   -> _social/out/<post>/<lang>-01.png ...
Posts are defined in _social/posts.py. Fonts in _social/fonts (installed to ~/.fonts).
"""
import asyncio, base64, os, sys, mimetypes
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

C = dict(cream="#F4EEE3", white="#FBF8F2", forest="#23392C", muted="#4A5A4E",
         rust="#9C4F1E", gold="#B89A5E", line="#D8CFBF", sage="#E7ECE2")


def img(path):
    p = path if os.path.isabs(path) else os.path.join(ROOT, path)
    mt = mimetypes.guess_type(p)[0] or "image/jpeg"
    return "data:%s;base64,%s" % (mt, base64.b64encode(open(p, "rb").read()).decode())


EMBLEM = """<svg width="{s}" height="{s}" viewBox="0 0 64 64" fill="none" aria-hidden="true"><path d="M43.39 6.42A28 28 0 1 1 20.61 6.42" stroke="#23392C" stroke-width="1.1" stroke-linecap="round" vector-effect="non-scaling-stroke"/><path d="M45.83 10.7A25.4 25.4 0 1 1 18.17 10.7" stroke="#B89A5E" stroke-width="1.1" stroke-linecap="round" vector-effect="non-scaling-stroke"/><path d="M32 12.6V4.4M32 7.6C29.4 7.9 26.2 6.1 25.5 2.5C28.9 2.2 31.6 4.1 32 7.6ZM32 7.6C34.6 7.9 37.8 6.1 38.5 2.5C35.1 2.2 32.4 4.1 32 7.6Z" stroke-linecap="round" stroke="#B89A5E" stroke-width="1.1" stroke-linejoin="round" vector-effect="non-scaling-stroke"/><text x="32.4" y="37.4" text-anchor="middle" font-family="Cormorant Garamond" font-weight="500" font-size="16.5" letter-spacing="0.8" fill="#23392C">NZ</text></svg>"""


def lockup(scale=1.0):
    return ('<div class="lockup" style="transform:scale(%s);transform-origin:left center">%s'
            '<span class="ln">NATALIA ZUTE</span><span class="lr"></span><span class="ls">HEALTH</span></div>'
            % (scale, EMBLEM.format(s=46)))


def ring_photo(src, size, pos="50% 30%"):
    """Photo in a circle with the brand's open ring, gold inner ring and sprout (as on the website hero)."""
    pad = size * 0.16
    box = size + 2 * pad
    r1, r2 = box / 2 - 2, box / 2 - pad * 0.45
    cx = cy = box / 2
    import math
    def arc(r, gap):
        a0, a1 = math.radians(-90 + gap), math.radians(-90 - gap)
        x0, y0 = cx + r * math.cos(a0), cy + r * math.sin(a0)
        x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1)
        return "M%.1f %.1fA%.1f %.1f 0 1 1 %.1f %.1f" % (x0, y0, r, r, x1, y1)
    sx, top = cx, cy - r1
    sprout = ("M{x} {a}V{b}M{x} {c}C{p1} {q1} {p2} {q2} {p3} {q3}C{p4} {q4} {p5} {q5} {x} {c}Z"
              "M{x} {c}C{m1} {q1} {m2} {q2} {m3} {q3}C{m4} {q4} {m5} {q5} {x} {c}Z").format(
        x=sx, a=top + 26, b=top - 10, c=top + 4,
        p1=sx - 9, q1=top + 5, p2=sx - 20, q2=top - 2, p3=sx - 22, q3=top - 14,
        p4=sx - 11, q4=top - 15, p5=sx - 2, q5=top - 8,
        m1=sx + 9, m2=sx + 20, m3=sx + 22, m4=sx + 11, m5=sx + 2)
    return ('<div class="ring" style="width:{b}px;height:{b}px">'
            '<svg width="{b}" height="{b}" viewBox="0 0 {b} {b}" fill="none" style="position:absolute;inset:0;overflow:visible">'
            '<path d="{a1}" stroke="#23392C" stroke-width="2" stroke-linecap="round"/>'
            '<path d="{a2}" stroke="#B89A5E" stroke-width="2" stroke-linecap="round"/>'
            '<path d="{sp}" stroke="#B89A5E" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            '<div style="position:absolute;left:{p}px;top:{p}px;width:{s}px;height:{s}px;border-radius:50%;'
            'background:url({src}) {pos}/cover"></div></div>').format(
        b=box, a1=arc(r1, 20), a2=arc(r2, 26), sp=sprout, p=pad, s=size, src=img(src), pos=pos)


CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px}
body{font-family:Jost;color:%(forest)s;-webkit-font-smoothing:antialiased}
.slide{position:relative;width:1080px;height:1350px;overflow:hidden;background:%(cream)s;padding:96px 96px 0}
.slide.white{background:%(white)s}.slide.sage{background:%(sage)s}
.lockup{display:inline-flex;align-items:center;gap:16px;white-space:nowrap}
.ln{font-family:'Cormorant Garamond';font-weight:500;font-size:24px;letter-spacing:.26em}
.lr{width:1px;height:26px;background:%(gold)s}.ls{font-size:11px;font-weight:500;letter-spacing:.32em}
.label{font-size:26px;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:%(rust)s}
.h1{font-family:'Cormorant Garamond';font-weight:500;font-size:112px;line-height:1.0;letter-spacing:-.01em}
.h2{font-family:'Cormorant Garamond';font-weight:500;font-size:84px;line-height:1.06;letter-spacing:-.005em}
.h3{font-family:'Cormorant Garamond';font-weight:500;font-size:64px;line-height:1.1}
.big{font-family:'Cormorant Garamond';font-weight:500;font-size:76px;line-height:1.14}
.body{font-size:38px;line-height:1.5;color:%(muted)s;font-weight:400}
.rule{width:120px;height:2px;background:%(gold)s}
.foot{position:absolute;left:96px;right:96px;bottom:72px;display:flex;justify-content:space-between;align-items:center;
  font-size:24px;letter-spacing:.06em;color:%(muted)s}
.foot .n{color:%(gold)s;letter-spacing:.2em}
.ring{position:relative;flex:none}
.photo{border-radius:999px 999px 24px 24px;background-size:cover;background-position:50%% 30%%}
.steps{list-style:none;margin-top:56px;border-top:1.5px solid %(line)s}
.steps li{display:flex;gap:40px;align-items:baseline;padding:40px 0;border-bottom:1.5px solid %(line)s}
.steps .k{font-family:'Cormorant Garamond';font-weight:500;font-size:88px;line-height:.8;color:%(gold)s;width:60px;flex:none}
.steps .t{font-size:40px;line-height:1.4}
.arrow{font-size:30px;color:%(rust)s;letter-spacing:.1em}
""" % C


def page(inner, cls="", n="", total="", handle="", arrow=""):
    foot = '<div class="foot"><span>%s</span><span class="n">%s</span></div>' % (handle, ("%s / %s" % (n, total)) if n else "")
    return ('<!doctype html><html><head><meta charset="utf-8"><style>%s</style></head><body>'
            '<div class="slide %s">%s%s</div></body></html>' % (CSS, cls, inner, foot))


async def render(post, langs):
    from posts import POSTS
    out = os.path.join(HERE, "out", post)
    os.makedirs(out, exist_ok=True)
    files = []
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for lang in langs:
            slides = POSTS[post](lang)
            for i, html in enumerate(slides, 1):
                await pg.set_content(html, wait_until="load")
                await pg.evaluate("document.fonts.ready")
                f = os.path.join(out, "%s-%02d.png" % (lang, i))
                await pg.screenshot(path=f, type="png")
                files.append(f)
        await b.close()
    return files


if __name__ == "__main__":
    post = sys.argv[1]
    langs = sys.argv[2:] or ["en", "ru"]
    for f in asyncio.run(render(post, langs)):
        print(f)
