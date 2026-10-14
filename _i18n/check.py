"""Validate a translation file: python3 check.py src/u_<page>.json tr/<page>.ru.json"""
import json, re, sys
from collections import Counter

src = json.load(open(sys.argv[1], encoding="utf-8"))
tr = json.load(open(sys.argv[2], encoding="utf-8"))
bad = 0
for k in src:
    if k not in tr:
        print("MISSING KEY:", k[:100]); bad += 1; continue
    v = tr[k]
    if not v.strip():
        print("EMPTY:", k[:100]); bad += 1; continue
    m1 = Counter(re.findall(r"</?\d+/?>", k)); m2 = Counter(re.findall(r"</?\d+/?>", v))
    if m1 != m2:
        print("MARKERS DIFFER:", k[:80], "=>", v[:80]); bad += 1
    if re.search(r"&(?!amp;|lt;|gt;|nbsp;|#)", v):
        print("BARE &:", v[:80]); bad += 1
    if re.search(r"[<>]", re.sub(r"</?\d+/?>", "", v)):
        print("STRAY < >:", v[:80]); bad += 1
    low = v.lower()
    for w in ["лечи", "вылеч", "исцел", "детокс", "очищ", "суперфуд", "первопричин", "гарант", "диетолог", "зарегистрир"]:
        if w in low:
            print("WORD '%s':" % w, v[:100]); bad += 1
for k in tr:
    if k not in src:
        print("EXTRA KEY:", k[:100]); bad += 1
print("OK" if not bad else "%d problems" % bad, "(%d strings)" % len(src))
