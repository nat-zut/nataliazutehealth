"""Master emblem + lockup (docs/Logo Master Spec v1.md). Shared by the site updater and the social builders."""
import re, os
HERE = os.path.dirname(os.path.abspath(__file__))
FOREST, CREAM, GOLD, BRONZE = '#23392C', '#F4EEE3', '#B89A5E', '#7D5A28'
OUTER = 'M43.39 6.42A28 28 0 1 1 20.61 6.42'
GOLD_A = 'M45.83 10.7A25.4 25.4 0 1 1 18.17 10.7'
GOLD_B = 'M45.29 11.54A24.4 24.4 0 1 1 18.71 11.54'
SPROUT = 'M32 9.4V4.4M32 7.6C29.4 7.9 26.2 6.1 25.5 2.5C28.9 2.2 31.6 4.1 32 7.6ZM32 7.6C34.6 7.9 37.8 6.1 38.5 2.5C35.1 2.2 32.4 4.1 32 7.6Z'
NZ_D = re.search(r'<path transform="translate\(18\.909 37\.938\) scale\(0\.19\)" d="([^"]+)"',
                 open(os.path.join(HERE, '..', 'favicon.svg')).read()).group(1)
# heaviest to lightest: outer ring, sprout, gold ring
WEIGHTS = {'A': (1.6, 1.3, 1.1, GOLD_A), 'B': (2.0, 1.6, 1.6, GOLD_B), 'P': (2.6, 2.0, 2.0, GOLD_B)}

def emblem_inner(kind='A', dark=False, nz=True):
    o, s, g, gp = WEIGHTS[kind]
    ink = CREAM if dark else FOREST
    out = (f'<path d="{OUTER}" stroke="{ink}" stroke-width="{o}" stroke-linecap="round"/>'
           f'<path d="{gp}" stroke="{GOLD}" stroke-width="{g}" stroke-linecap="round"/>'
           f'<path d="{SPROUT}" stroke="{GOLD}" stroke-width="{s}" stroke-linecap="round" stroke-linejoin="round"/>')
    if nz:
        out += f'<path transform="translate(18.909 37.938) scale(0.19)" d="{NZ_D}" fill="{ink}" stroke="none"/>'
    return out

def emblem(size, kind=None, dark=False, attrs='aria-hidden="true"'):
    kind = kind or ('A' if size >= 48 else 'B')
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" fill="none" {attrs}>{emblem_inner(kind, dark)}</svg>'

def photo_ring_inner():
    """Version C: fixed thin web lines over a photo clipped at r 21 (inset 17.1875%)."""
    ns = 'vector-effect="non-scaling-stroke"'
    return (f'<path d="{OUTER}" stroke="{FOREST}" stroke-width="1.5" stroke-linecap="round" {ns}/>'
            f'<path d="{GOLD_A}" stroke="{GOLD}" stroke-width="1.25" stroke-linecap="round" {ns}/>'
            f'<path d="{SPROUT}" stroke="{GOLD}" stroke-width="1.35" stroke-linecap="round" stroke-linejoin="round" {ns}/>')
