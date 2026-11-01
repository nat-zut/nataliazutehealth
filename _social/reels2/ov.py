from PIL import Image, ImageDraw, ImageFont
F='/home/claude/nataliazutehealth/_social/fonts/'
FOREST=(35,57,44); CREAM=(244,238,227); BRONZE=(156,79,30); MUTED=(74,90,78); GOLD=(184,154,94)
W,H=1080,1920; MAXW=940
def fnt(n,s): return ImageFont.truetype(F+n,s)
def fit(d,txt,name,size,maxw):
    while size>20:
        f=fnt(name,size)
        if d.textlength(txt,font=f)<=maxw: return f
        size-=2
    return fnt(name,size)
def hook(out,title,sub,y=300):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    ft=fit(d,title,'CormorantGaramond-Medium.ttf',100,MAXW-120); fs=fit(d,sub,'Jost-Regular.ttf',42,MAXW-120)
    tw=d.textlength(title,font=ft); sw=d.textlength(sub,font=fs)
    w=max(tw,sw)+120; x0=(W-w)/2; h=250
    d.rounded_rectangle([x0,y,x0+w,y+h],radius=40,fill=CREAM+(245,))
    d.text(((W-tw)/2,y+40),title,font=ft,fill=FOREST); d.text(((W-sw)/2,y+170),sub,font=fs,fill=MUTED)
    im.save(out)
def label(out,num,name,y=290):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    fn=fnt('Jost-Medium.ttf',30); n=' '.join(num); nw=d.textlength(n,font=fn)
    fl=fit(d,name,'Jost-Medium.ttf',50,MAXW-150-nw); lw=d.textlength(name,font=fl)
    w=nw+lw+150; x0=(W-w)/2; h=96
    d.rounded_rectangle([x0,y,x0+w,y+h],radius=48,fill=CREAM+(245,))
    d.text((x0+52,y+30),n,font=fn,fill=BRONZE)
    d.line([(x0+52+nw+24,y+26),(x0+52+nw+24,y+70)],fill=GOLD,width=2)
    asc=fl.getbbox(name)[1]; d.text((x0+52+nw+48,y+48-(fl.getbbox(name)[1]+fl.getbbox(name)[3])/2),name,font=fl,fill=FOREST)
    im.save(out)
def end(out,title,sub,y=1230):
    im=Image.new('RGBA',(W,H),(0,0,0,0)); d=ImageDraw.Draw(im)
    fl=fnt('Jost-Medium.ttf',28); lab=' '.join('NATALIA ZUTE HEALTH')
    ft=fit(d,title,'CormorantGaramond-Medium.ttf',88,MAXW-120); fs=fit(d,sub,'Jost-Regular.ttf',40,MAXW-120)
    lw=d.textlength(lab,font=fl); tw=d.textlength(title,font=ft); sw=d.textlength(sub,font=fs)
    w=max(tw,sw,lw)+120; x0=(W-w)/2; h=290
    d.rounded_rectangle([x0,y,x0+w,y+h],radius=40,fill=CREAM+(245,))
    d.text(((W-lw)/2,y+44),lab,font=fl,fill=BRONZE); d.text(((W-tw)/2,y+86),title,font=ft,fill=FOREST); d.text(((W-sw)/2,y+210),sub,font=fs,fill=MUTED)
    im.save(out)
