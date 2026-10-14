"""Build the Russian site and add the language switch to both languages.

Run from the scratch dir:  python3 site.py /home/claude/nataliazutehealth
Uses pristine English pages from git HEAD (orig/), so it can be re-run safely.
"""
import os, re, sys, subprocess, json
from bs4 import BeautifulSoup

REPO = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
ORIG = os.path.join(HERE, "orig")
RAW = os.path.join(HERE, "ru_raw")
DOMAIN = "https://nataliazutehealth.com/"

# 1. pristine English pages from git
os.makedirs(ORIG, exist_ok=True)
pages = [f for f in subprocess.check_output(["git", "-C", REPO, "ls-files", "*.html"], text=True).split() if "/" not in f]
def strip_lang(src):
    """Remove what this script added to the English pages, so re-runs start clean."""
    src = re.sub(r'<a class="langsw"[^>]*>[^<]*</a>', "", src)
    src = re.sub(r'\n<link rel="alternate" hreflang="[^"]*" href="[^"]*">', "", src)
    src = re.sub(r'<p style="margin: 8px 0 0; font-size: 15px; line-height: 1.5;"><a href="ru/[^"]*" hreflang="ru"[^>]*>Русская версия →</a></p>\n', "", src)
    src = re.sub(r'<style>\.nav a\{white-space:nowrap\}[^<]*</style>\n', "", src)
    return src.replace('justify-content: flex-end; gap: 24px;', 'justify-content: flex-end; gap: 32px;', 1)


for f in pages:
    open(os.path.join(ORIG, f), "w", encoding="utf-8").write(
        strip_lang(subprocess.check_output(["git", "-C", REPO, "show", "HEAD:" + f], text=True)))

# 2. translate
subprocess.check_call([sys.executable, os.path.join(HERE, "i18n.py"), "build", ORIG, os.path.join(HERE, "ru"), RAW])

SW_STYLE = "display: flex; align-items: center; gap: 6px; font-size: 13px; font-weight: 500; letter-spacing: 0.14em; white-space: nowrap; line-height: 1;"


def switch_html(lang, other_href):
    oth = "RU" if lang == "en" else "EN"
    title = "Русская версия сайта" if lang == "en" else "English version of this site"
    olang = "ru" if lang == "en" else "en-GB"
    return ('<a class="langsw" href="%s" hreflang="%s" lang="%s" title="%s" aria-label="%s" '
            'style="display: inline-block; font-size: 13px; font-weight: 500; letter-spacing: 0.14em; line-height: 1; '
            'text-decoration: none; color: #23392C; padding: 12px 2px; border-bottom: 1px solid #B89A5E; white-space: nowrap;">%s</a>'
            % (other_href, olang, olang, title, title, oth))


HEAD_CSS = {
    "en": "<style>.nav a{white-space:nowrap}@media (max-width: 1330px){.nav{display:none!important}.menubtn{display:flex!important}}@media (max-width: 900px){.hbtn{display:none!important}}</style>",
    "ru": "<style>.nav a{white-space:nowrap}@media (max-width: 1400px){.nav{display:none!important}.menubtn{display:flex!important}}@media (max-width: 980px){.hbtn{display:none!important}}</style>",
}
RIGHT_OLD = 'justify-content: flex-end; gap: 32px;'
RIGHT_NEW = 'justify-content: flex-end; gap: 24px;'


def menu_html(lang, other_href):
    text, olang = ("Русская версия", "ru") if lang == "en" else ("English version", "en-GB")
    return ('<p style="margin: 8px 0 0; font-size: 15px; line-height: 1.5;"><a href="%s" hreflang="%s" lang="%s" '
            'style="display: inline-block; padding: 10px 0; color: #23392C;">%s →</a></p>' % (other_href, olang, olang, text))


def canon_of(soup):
    c = soup.find("link", rel="canonical")
    return c["href"] if c else None


def ru_url(en_url):
    return en_url.replace(DOMAIN, DOMAIN + "ru/", 1)


def add_common(soup, lang, page, en_canon):
    head = soup.head
    # hreflang alternates
    for l in soup.find_all("link", rel="alternate"):
        if l.get("hreflang"):
            l.decompose()
    if en_canon:
        c = head.find("link", rel="canonical")
        for hl, url in (("en-GB", en_canon), ("ru", ru_url(en_canon)), ("x-default", en_canon)):
            t = soup.new_tag("link", rel="alternate", hreflang=hl, href=url)
            c.insert_after(t)
            c = t
    other = ("ru/" + page) if lang == "en" else ("../" + page)
    # header switch: before the header button
    hb = soup.find("a", class_="hbtn")
    if hb and not soup.find(class_="langsw"):
        hb.insert_before(BeautifulSoup(switch_html(lang, other), "html.parser"))
        right = hb.parent
        if right.get("style"):
            right["style"] = right["style"].replace(RIGHT_OLD, RIGHT_NEW)
        soup.head.append(BeautifulSoup(HEAD_CSS[lang], "html.parser"))
    # mobile menu
    menu = soup.find(id="menu")
    if menu and lang == "ru":
        for a in menu.find_all("a"):
            if a.string == "Дневник":
                a.string = "Бесплатный дневник"

    if menu and menu.nav:
        menu.nav.append(BeautifulSoup(menu_html(lang, other), "html.parser"))


def fix_paths_ru(soup):
    for tag in soup.find_all(True):
        for a in ("href", "src", "action"):
            v = tag.get(a)
            if not isinstance(v, str) or not v:
                continue
            if re.match(r"^(https?:|mailto:|tel:|#|data:|//|\.\./)", v):
                continue
            if re.match(r"^[\w-]+\.html(#.*)?$", v):
                continue
            tag[a] = "../" + v


report = []
for page in pages:
    en_path = os.path.join(ORIG, page)
    en = BeautifulSoup(open(en_path, encoding="utf-8").read(), "html.parser")
    en_canon = canon_of(en)
    has_switch = bool(en.find("a", class_="hbtn"))

    # English page: add alternates + switch, editing the original text in place minimally
    src = open(en_path, encoding="utf-8").read()
    other = "ru/" + page
    if en_canon:
        alt = "".join('\n<link rel="alternate" hreflang="%s" href="%s">' % (hl, u) for hl, u in
                      (("en-GB", en_canon), ("ru", ru_url(en_canon)), ("x-default", en_canon)))
        src = re.sub(r'(<link rel="canonical"[^>]*>)', lambda m: m.group(1) + alt, src, count=1)
    if has_switch:
        src = src.replace('<a class="hbtn"', switch_html("en", other) + '<a class="hbtn"', 1)
        src = src.replace(RIGHT_OLD, RIGHT_NEW, 1)
        src = src.replace("</head>", HEAD_CSS["en"] + "\n</head>", 1)
    # mobile menu: append before the menu nav's closing tag
    i = src.find('id="menu"')
    if i != -1:
        j = src.find("</nav>", i)
        src = src[:j] + menu_html("en", other) + "\n" + src[j:]
    open(os.path.join(REPO, page), "w", encoding="utf-8").write(src)

    # Russian page
    ru = BeautifulSoup(open(os.path.join(RAW, page), encoding="utf-8").read(), "html.parser")
    ru.html["lang"] = "ru"
    fix_paths_ru(ru)
    c = ru.find("link", rel="canonical")
    if c:
        c["href"] = ru_url(c["href"])
    for m in ru.find_all("meta", property="og:url"):
        m["content"] = ru_url(m["content"])
    add_common(ru, "ru", page, en_canon)
    if page in ("privacy.html", "terms.html", "cookies.html") and ru.h1:
        intro = ru.h1.find_next_sibling("p") or ru.h1
        note = BeautifulSoup(
            '<p style="margin: 0 0 24px; font-size: 15px; line-height: 1.5; color: #4A5A4E;">'
            'Это перевод для вашего удобства. Если русская и английская версии расходятся, действует '
            '<a href="../%s" hreflang="en-GB" lang="en-GB" style="color: #23392C;">английская версия</a>.</p>' % page,
            "html.parser")
        intro.insert_after(note)
    out = str(ru)
    # thousands separator in prices: £1,155 -> £1 155 (non-breaking)
    out = re.sub(r"([£€])(\d{1,3}),(\d{3})", "\\1\\2 \\3", out)
    # founding-place note passed to the booking calendar
    out = out.replace('"notes": "I\'d like to ask about a founding client place."',
                      '"notes": "Я бы хотела узнать о месте для первых клиенток."')
    os.makedirs(os.path.join(REPO, "ru"), exist_ok=True)
    open(os.path.join(REPO, "ru", page), "w", encoding="utf-8").write(out)
    report.append(page)

print("built", len(report), "pages")
