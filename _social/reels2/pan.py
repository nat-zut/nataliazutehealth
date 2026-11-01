import subprocess, os, sys
sys.path.insert(0, '/home/claude/reels')
import ov, spec
from build import assemble, dur, T, run
from pillow_heif import register_heif_opener; register_heif_opener()
from PIL import Image, ImageOps
DL = '/mnt/user-data/uploads/Downloads'; B = '/home/claude/reels/panbase'; os.makedirs(B, exist_ok=True)
CL = [  # file, start, dur, speed, zoom, cx, cy
 ("IMG_9611", 0.0, 4.0, 0.8, 1.05, 0.5, 0.5),
 ("IMG_9612", 5.2, 2.6, 1.0, 2.2, 0.45, 0.6),
 ("IMG_9613", 4.4, 2.6, 1.25, 1.8, 0.55, 0.34),
 ("IMG_9615", 1.0, 2.6, 1.25, 1.8, 0.42, 0.42),
 ("IMG_9616", 16.8, 2.8, 1.0, 1.4, 0.57, 0.5),
 ("IMG_9620", 1.6, 3.2, 1.25, 1.5, 0.45, 0.58),
 ("IMG_9621", 1.0, 2.8, 1.0, 1.45, 0.5, 0.55),
]
def still(src, out, l, cx=0.5, zin=True):
    im = ImageOps.exif_transpose(Image.open(f'{DL}/{src}.HEIC')).convert('RGB')
    w, h = im.size; tw = int(h * 9 / 16)
    x0 = int(min(max(cx * w - tw / 2, 0), w - tw)); im = im.crop((x0, 0, x0 + tw, h)).resize((2160, 3840), Image.LANCZOS)
    im.save(f'{B}/{src}.jpg', quality=93)
    N = int(l * 30)
    z = f"1+0.08*on/{N}" if zin else f"1.08-0.08*on/{N}"
    run(['ffmpeg','-v','error','-y','-loop','1','-i',f'{B}/{src}.jpg','-vf',
         f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={N}:s=1080x1920:fps=30,eq=contrast=1.03:saturation=1.06,format=yuv420p",
         '-frames:v',str(N),'-c:v','libx264','-preset','veryfast','-crf','16',out])
def base():
    files = []
    o = f'{B}/s0.mp4'; still('IMG_9359', o, 3.0 + T, 0.45); files.append(o)
    for i, (f, s, d, sp, z, cx, cy) in enumerate(CL):
        l = d + T
        cw = int(1080 / z / 18) * 18; ch = cw * 16 // 9; x0 = int(min(max(cx * 1080 - cw / 2, 0), 1080 - cw)); y0 = int(min(max(cy * 1920 - ch / 2, 0), 1920 - ch))
        o = f'{B}/c{i}.mp4'
        run(['ffmpeg','-v','error','-y','-ss',str(s),'-t',f'{l*sp+0.1:.2f}','-i',f'{DL}/{f}.MOV','-vf',
             f"crop={cw}:{ch}:{x0}:{y0},setpts=PTS/{sp},fps=30,tpad=stop_mode=clone:stop_duration=1,scale=w='2*trunc(1080*(1+0.08*t/{l})/2)':h=-2:eval=frame:flags=bicubic,crop=1080:1920,eq=contrast=1.04:saturation=1.1,format=yuv420p",
             '-an','-c:v','libx264','-preset','veryfast','-crf','16','-t',f'{l:.2f}',o])
        files.append(o)
    o = f'{B}/s9.mp4'; still('IMG_9361', o, 5.6, 0.5, False); files.append(o)
    return files
def build(lang, files):
    t = spec.PAN[lang]; d = f'/home/claude/reels/out/pan-{lang}'; os.makedirs(d, exist_ok=True)
    ov.hook(f'{d}/hook.png', t['title'], t['sub']); ov.end(f'{d}/end.png', t['end'][0], t['end'][1], 1230)
    n = len(t['steps'])
    for i, s in enumerate(t['steps']): ov.label(f'{d}/l{i}.png', f'{i+1}/{n}', s)
    plans = [[('hook.png', 0.15, 3.4, True, False)]]
    for i in range(7): plans.append([(f'l{i}.png', 0.0 if i == 0 else T, dur(files[i+1]), i > 0, False)])
    plans[1] = [('l0.png', T, dur(files[1]), True, False)]
    plans.append([('l7.png', T, 2.4, True, True), ('end.png', 2.6, 5.6, True, False)])
    return assemble(files, plans, d, f'/home/claude/reels/out/pan-{lang}.mp4')
if __name__ == '__main__':
    files = base() if 'base' in sys.argv else [f'{B}/s0.mp4'] + [f'{B}/c{i}.mp4' for i in range(7)] + [f'{B}/s9.mp4']
    for lg in ('en', 'ru'): print(build(lg, files))
