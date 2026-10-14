"""Extract translatable units from the site's HTML pages and rebuild translated copies.

extract: python3 i18n.py extract SRC_DIR OUT_DIR   -> OUT_DIR/<page>.json  {id: source}
build:   python3 i18n.py build SRC_DIR TR_DIR DEST_DIR -> DEST_DIR/<page>.html using TR_DIR/<page>.ru.json
"""
import json, re, sys, os, copy, html
from bs4 import BeautifulSoup, NavigableString, Tag, Comment

INLINE = {"a", "em", "strong", "b", "i", "s", "u", "span", "br", "small", "sup", "sub", "mark", "abbr", "code", "wbr", "time", "q", "cite"}
SKIP = {"script", "style", "svg", "noscript", "template", "head"}
VOID = {"br", "wbr"}
ATTRS = ["alt", "aria-label", "title", "placeholder", "data-gbp", "data-eur"]


def has_text(el):
    return any(isinstance(s, NavigableString) and not isinstance(s, Comment) and s.strip() for s in el.descendants)


def inline_only(el):
    for d in el.descendants:
        if isinstance(d, Tag) and d.name not in INLINE:
            return False
    return True


def units(soup):
    """Yield ('el', tag) for inline-only containers and ('str', navstring) for loose strings."""
    out = []

    def walk(el):
        for ch in list(el.children):
            if isinstance(ch, Comment):
                continue
            if isinstance(ch, NavigableString):
                if ch.strip():
                    out.append(("str", ch))
                continue
            if not isinstance(ch, Tag) or ch.name in SKIP:
                continue
            if has_text(ch) and inline_only(ch) and ch.name not in ("option",):
                out.append(("el", ch))
            elif ch.name == "option":
                if has_text(ch):
                    out.append(("el", ch))
            else:
                walk(ch)
    walk(soup.body)
    return out


def encode(el):
    """Inner HTML of el with inline tags replaced by numbered markers. Returns (text, tags)."""
    tags = []

    def rec(node):
        parts = []
        for ch in node.children:
            if isinstance(ch, Comment):
                continue
            if isinstance(ch, NavigableString):
                parts.append(str(ch).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
            elif isinstance(ch, Tag):
                tags.append(ch)
                n = len(tags)
                if ch.name in VOID:
                    parts.append("<%d/>" % n)
                else:
                    parts.append("<%d>" % n + rec(ch) + "</%d>" % n)
        return "".join(parts)
    return rec(el), tags


def opening(tag):
    t = copy.copy(tag)
    t.clear()
    s = str(t)
    if tag.name in VOID:
        return s
    return s[: s.rindex("</")]


def decode(text, tags):
    def rep(m):
        close, n, void = m.group(1), int(m.group(2)), m.group(3)
        tag = tags[n - 1]
        if void:
            return opening(tag)
        return "</%s>" % tag.name if close else opening(tag)
    return re.sub(r"<(/?)(\d+)(/?)>", rep, text)


def collect(path):
    soup = BeautifulSoup(open(path, encoding="utf-8").read(), "html.parser")
    items = []  # (key, source, applyfn)
    for kind, u in units(soup):
        if kind == "str":
            src = str(u)
            core = src.strip()
            def apply(tr, u=u, src=src, core=core):
                u.replace_with(src.replace(core, html.unescape(tr)))
            items.append((core, apply))
        else:
            enc, tags = encode(u)
            core = enc.strip()
            def apply(tr, u=u, enc=enc, core=core, tags=tags):
                new = enc.replace(core, tr)
                frag = BeautifulSoup(decode(new, tags), "html.parser")
                u.clear()
                for c in list(frag.contents):
                    u.append(c)
            items.append((core, apply))
    text_items, items = items, []  # attributes must be applied before text rebuilds copy the tags
    # attributes in body
    for el in soup.body.find_all(True):
        if el.name in ("svg",) or el.find_parent("svg"):
            continue
        for a in ATTRS:
            v = el.get(a)
            if isinstance(v, str) and v.strip() and re.search("[A-Za-z]", v):
                def apply(tr, el=el, a=a):
                    el[a] = html.unescape(tr)
                items.append((v.strip(), apply))
        if el.name == "input" and el.get("type") in ("submit", "button") and el.get("value"):
            def apply(tr, el=el):
                el["value"] = html.unescape(tr)
            items.append((el["value"], apply))
    # head
    if soup.title and soup.title.string:
        def apply(tr):
            soup.title.string = html.unescape(tr)
        items.append((soup.title.string.strip(), apply))
    for m in soup.find_all("meta"):
        if m.get("name") == "description" or m.get("property") in ("og:title", "og:description"):
            def apply(tr, m=m):
                m["content"] = html.unescape(tr)
            items.append((m["content"], apply))
    for s in soup.find_all("script", type="application/ld+json"):
        data = json.loads(s.string)
        def walk(o, setter_path=()):
            res = []
            if isinstance(o, dict):
                for k, v in o.items():
                    if k in ("description", "jobTitle", "headline", "name") and isinstance(v, str) and k != "name":
                        res.append((o, k))
                    res += walk(v)
            elif isinstance(o, list):
                for v in o:
                    res += walk(v)
            return res
        for o, k in walk(data):
            def apply(tr, o=o, k=k, s=s, data=data):
                o[k] = html.unescape(tr)
                s.string = json.dumps(data, ensure_ascii=False)
            items.append((o[k], apply))
    return soup, items + text_items


def key_of(src):
    return re.sub(r"\s+", " ", src).strip()


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "extract":
        src, out = sys.argv[2], sys.argv[3]
        os.makedirs(out, exist_ok=True)
        for f in sorted(os.listdir(src)):
            if not f.endswith(".html"):
                continue
            soup, items = collect(os.path.join(src, f))
            d = {}
            for core, _ in items:
                k = key_of(core)
                if re.search("[A-Za-z]", k):
                    d[k] = ""
            json.dump(d, open(os.path.join(out, f[:-5] + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print(f, len(d), sum(len(k.split()) for k in d))
    elif cmd == "build":
        src, trd, dest = sys.argv[2], sys.argv[3], sys.argv[4]
        os.makedirs(dest, exist_ok=True)
        common = {}
        cp = os.path.join(trd, "_common.ru.json")
        if os.path.exists(cp):
            common = json.load(open(cp, encoding="utf-8"))
        for f in sorted(os.listdir(src)):
            if not f.endswith(".html"):
                continue
            tp = os.path.join(trd, f[:-5] + ".ru.json")
            tr = dict(common)
            if os.path.exists(tp):
                tr.update(json.load(open(tp, encoding="utf-8")))
            soup, items = collect(os.path.join(src, f))
            missing = []
            for core, apply in items:
                k = key_of(core)
                if k in tr and tr[k]:
                    apply(tr[k])
                elif re.search("[A-Za-z]", k):
                    missing.append(k)
            open(os.path.join(dest, f), "w", encoding="utf-8").write(str(soup))
            print(f, "missing:", len(missing))
            for m in missing[:40]:
                print("   ", m[:120])
