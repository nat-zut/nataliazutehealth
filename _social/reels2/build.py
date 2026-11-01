import subprocess, os, sys, json
sys.path.insert(0, '/home/claude/reels')
import ov, spec
T = 0.4
BASE = '/mnt/user-data/uploads/Downloads/.reels_tmp/base'
OUT = '/home/claude/reels/out'; os.makedirs(OUT, exist_ok=True)
def run(c): subprocess.run(c, check=True)
def dur(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).decode())

def assemble(clipfiles, plans, ovdir, out):
    """clipfiles: base clips; plans: per clip list of (png, a, b, fadein, fadeout)."""
    n = len(clipfiles); Ls = []
    seg = []
    for i, (cf, pl) in enumerate(zip(clipfiles, plans)):
        l = dur(cf); Ls.append(l)
        inputs = ['-i', cf]; fc = ['[0:v]null[b]']; last = 'b'
        for k, (png, a, b, fi, fo) in enumerate(pl, 1):
            inputs += ['-loop', '1', '-t', f'{l:.2f}', '-i', os.path.join(ovdir, png)]
            f = f'[{k}:v]format=rgba'
            if fi: f += f',fade=in:st={a:.2f}:d=0.3:alpha=1'
            if fo: f += f',fade=out:st={b-0.3:.2f}:d=0.3:alpha=1'
            fc += [f + f'[o{k}]', f"[{last}][o{k}]overlay=0:0:enable='between(t,{a:.2f},{b:.2f})'[v{k}]"]; last = f'v{k}'
        fc.append(f'[{last}]format=yuv420p[out]')
        o = f'{ovdir}/seg{i}.mp4'; seg.append(o)
        run(['ffmpeg','-v','error','-y'] + inputs + ['-filter_complex', ';'.join(fc), '-map', '[out]', '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', '-t', f'{l:.2f}', o])
    total = sum(Ls) - (n - 1) * T
    inputs = []
    for s in seg: inputs += ['-i', s]
    fc = []; last = '0:v'; off = 0
    for i in range(1, n):
        off += Ls[i-1] - T
        fc.append(f'[{last}][{i}:v]xfade=transition=smoothleft:duration={T}:offset={off:.3f}[x{i}]'); last = f'x{i}'
    fc.append(f'color=c=0xF4EEE3@0.35:s=960x8:r=30:d={total:.2f},format=rgba[trk]')
    fc.append(f'color=c=0xF4EEE3@1.0:s=960x8:r=30:d={total:.2f},format=rgba[bar]')
    fc.append(f"[trk][bar]overlay=x='-960+960*t/{total:.2f}':y=0[pb]")
    fc.append(f"[{last}][pb]overlay=60:236,fade=in:st=0:d=0.3,fade=out:st={total-0.5:.2f}:d=0.5,format=yuv420p[out]")
    inputs += ['-f', 'lavfi', '-t', f'{total:.2f}', '-i', 'anullsrc=r=44100:cl=stereo']
    run(['ffmpeg','-v','error','-y'] + inputs + ['-filter_complex', ';'.join(fc), '-map', '[out]', '-map', f'{n}:a', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20',
         '-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-c:a','aac','-b:a','128k','-t', f'{total:.2f}', '-movflags', '+faststart', out])
    return out, round(total, 2)

def workout(name, lang):
    title, sub, endsub, moves = (spec.W_EN if lang == 'en' else spec.W_RU)[name]
    d = f'{OUT}/{name}-{lang}'; os.makedirs(d, exist_ok=True)
    ov.hook(f'{d}/hook.png', title, sub); ov.end(f'{d}/end.png', spec.END_T[lang], endsub, 1230 if name == 'stand' else 300)
    n = len(moves)
    for i, m in enumerate(moves): ov.label(f'{d}/l{i}.png', f'{i+1}/{n}', m)
    files = [f'{BASE}/{name}/c{i}.mp4' for i in range(n)]
    plans = []
    for i in range(n):
        l = dur(files[i])
        if i == 0: plans.append([('hook.png', 0, 2.3, False, True), ('l0.png', 2.45, l, True, False)])
        elif i == n - 1: plans.append([(f'l{i}.png', T, 2.6, True, True), ('end.png', 2.75, l, True, False)])
        else: plans.append([(f'l{i}.png', T, l, True, False)])
    return assemble(files, plans, d, f'{OUT}/{name}-{lang}.mp4')

if __name__ == '__main__':
    for a in sys.argv[1:]:
        nm, lg = a.split(':'); print(workout(nm, lg), flush=True)
