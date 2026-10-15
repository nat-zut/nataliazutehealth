"""Brand reel builder: cuts clips, adds text cards in the brand style, outputs 1080x1920 MP4 per language.

python3 _social/reel.py market [en ru]
"""
import asyncio, os, subprocess, sys, json
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
U = "/root/.claude/uploads/abca156e-4e23-5c0f-9027-909366873bc2"
OUT = os.path.join(HERE, "out")

REELS = {
 "market": {
  "clips": [  # (file, start, duration, card key)
    (U + "/0c9bf7ad-IMG_9194.mov", 0.0, 3.0, "hook"),
    (U + "/ee340180-IMG_9191.mov", 0.0, 2.7, "count"),
    (U + "/0c9bf7ad-IMG_9194.mov", 3.0, 3.0, "why"),
    (U + "/20ddd407-IMG_9187.mov", 0.3, 4.0, "slow"),
    (U + "/20ddd407-IMG_9187.mov", 4.3, 3.5, "you"),
    (U + "/20ddd407-IMG_9187.mov", 10.5, 3.2, "end"),
  ],
  "text": {
   "en": {
    "hook": ("How many plants are in my market basket?", ""),
    "count": ("14", "different plants this week"),
    "why": ("Why it matters", "A variety of plants helps feed a variety of gut bacteria."),
    "slow": ("Not used to much veg?", "Go slowly. Add one new plant at a time, so your gut can adjust."),
    "you": ("Your turn", "How many different plants are on your plate today?"),
    "end": ("Choose nourished,<br>not perfect.", "@nataliazutehealth"),
   },
   "ru": {
    "hook": ("Сколько растений в&nbsp;моей корзине с&nbsp;рынка?", ""),
    "count": ("14", "разных растений на&nbsp;эту неделю"),
    "why": ("Почему это важно", "Разные растения помогают кормить разные полезные бактерии кишечника."),
    "slow": ("Пока едите мало овощей?", "Не спешите. Добавляйте по&nbsp;одному новому растению, чтобы кишечник привык."),
    "you": ("Ваша очередь", "Сколько разных растений на&nbsp;вашей тарелке сегодня?"),
    "end": ("Выбирайте заботу о&nbsp;себе,<br>а&nbsp;не&nbsp;идеал.", "@nataliazutehealth_rus"),
   },
  },
 }
}

CARD = """<!doctype html><html><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1920px;background:transparent}
.wrap{position:absolute;left:80px;right:80px;top:%(top)spx;display:flex;justify-content:center}
.card{background:rgba(251,248,242,.94);border-radius:28px;padding:44px 56px 48px;text-align:center;
 box-shadow:0 18px 48px rgba(35,57,44,.18);max-width:920px}
.h{font-family:'Cormorant Garamond';font-weight:500;color:#23392C;font-size:%(hs)spx;line-height:1.08;letter-spacing:-.005em}
.r{width:90px;height:2px;background:#B89A5E;margin:26px auto 24px}
.b{font-family:Jost;color:#4A5A4E;font-size:%(bs)spx;line-height:1.42}
.end .b{color:#9C4F1E;letter-spacing:.06em;font-size:36px}
</style></head><body><div class="wrap"><div class="card %(cls)s"><div class="h">%(h)s</div>%(rest)s</div></div></body></html>"""


def card_html(key, h, b):
    big = key == "count"
    hs = 220 if big else (78 if key in ("hook", "end") else 66)
    rest = ('<div class="r"></div><div class="b">%s</div>' % b) if b else ""
    top = 1240 if key not in ("hook", "end") else 760
    return CARD % dict(top=top, hs=hs, bs=44, h=h, rest=rest, cls="end" if key == "end" else "")


async def make_cards(name, lang, d):
    os.makedirs(d, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        for key, (h, body) in REELS[name]["text"][lang].items():
            await pg.set_content(card_html(key, h, body), wait_until="load")
            await pg.evaluate("document.fonts.ready")
            await pg.screenshot(path=os.path.join(d, key + ".png"), omit_background=True)
        await b.close()


def build(name, lang):
    d = os.path.join(OUT, name, "cards-" + lang)
    asyncio.run(make_cards(name, lang, d))
    clips = REELS[name]["clips"]
    args, filt = [], []
    for i, (f, ss, dur, key) in enumerate(clips):
        args += ["-ss", str(ss), "-t", str(dur), "-i", f]
    for i, (f, ss, dur, key) in enumerate(clips):
        args += ["-loop", "1", "-t", str(dur), "-i", os.path.join(d, key + ".png")]
    n = len(clips)
    for i, (f, ss, dur, key) in enumerate(clips):
        filt.append("[%d:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1,"
                    "eq=saturation=1.04:brightness=0.01[v%d]" % (i, i))
        filt.append("[%d:v]format=rgba,fade=t=in:st=0.15:d=0.35:alpha=1[c%d]" % (n + i, i))
        filt.append("[v%d][c%d]overlay=0:0:shortest=1,format=yuv420p[o%d]" % (i, i, i))
    filt.append("".join("[o%d]" % i for i in range(n)) + "concat=n=%d:v=1:a=0[out]" % n)
    out = os.path.join(OUT, name, "%s-%s.mp4" % (name, lang))
    cmd = ["ffmpeg", "-v", "error", "-y"] + args + ["-filter_complex", ";".join(filt), "-map", "[out]",
           "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out]
    subprocess.check_call(cmd)
    return out


if __name__ == "__main__":
    name = sys.argv[1]
    for lang in (sys.argv[2:] or ["en", "ru"]):
        print(build(name, lang))
