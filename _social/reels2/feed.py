from PIL import Image, ImageDraw, ImageFont
import os
F='/home/claude/nataliazutehealth/_social/fonts/'; O='/home/claude/nataliazutehealth/_social/out/'; C='/home/claude/reels/covers/'
REV='/tmp/claude-0/-home-claude/35ba8568-e60b-58ab-beae-64d7f9e3f4dc/scratchpad/review/'
CREAM=(244,238,227); FOREST=(35,57,44); MUTED=(74,90,78); RUST=(156,79,30); SAGE=(231,236,226)
TW,TH=276,368; XS=[30,312,594]; YS=[150,560,970,1380]
def f(n,s): return ImageFont.truetype(F+n,s)
def tile(src):
    im=Image.open(src).convert('RGB'); w,h=im.size
    th=int(w*4/3)
    if th<=h: im=im.crop((0,(h-th)//2,w,(h-th)//2+th))
    else:
        tw=int(h*3/4); im=im.crop(((w-tw)//2,0,(w-tw)//2+tw,h))
    return im.resize((TW,TH),Image.LANCZOS)
def oldtile(lang,col,row):
    im=Image.open(REV+f'feed-{lang}.png').convert('RGB'); x=[30,312,594][col]; y=[128,538,948,1358][row]
    return im.crop((x,y,x+TW,y+TH))
def talking(lang):
    im=Image.new('RGB',(TW,TH),SAGE); d=ImageDraw.Draw(im)
    t=('Video to camera','3 questions I’ll ask','you first') if lang=='en' else ('Видео в камеру','3 вопроса, которые','я задам вам первыми')
    d.text((TW/2,120),t[0].upper(),font=f('Jost-Medium.ttf',13),fill=RUST,anchor='mm')
    d.text((TW/2,170),t[1],font=f('CormorantGaramond-Medium.ttf',27),fill=FOREST,anchor='mm')
    d.text((TW/2,202),t[2],font=f('CormorantGaramond-Medium.ttf',27),fill=FOREST,anchor='mm')
    d.text((TW/2,262),'(you film it)' if lang=='en' else '(снимаете вы)',font=f('Jost-Regular.ttf',14),fill=MUTED,anchor='mm')
    return im
def play(d,x,y):
    d.polygon([(x+TW-30,y+12),(x+TW-30,y+34),(x+TW-12,y+23)],fill=(255,255,255))
def pin(d,x,y,lang):
    txt='PINNED' if lang=='en' else 'ЗАКРЕПЛЁН'; ft=f('Jost-Medium.ttf',12); w=d.textlength(txt,font=ft)
    d.rounded_rectangle([x+TW-w-26,y+10,x+TW-10,y+32],radius=11,fill=RUST); d.text((x+TW-w-18,y+14),txt,font=ft,fill=(251,248,242))
def build(lang):
    L=lang
    items=[  # (image, label, reel, pinned)
     (tile(O+f'story/{L}-01.png'), ('Thu 12 Nov','My story') if L=='en' else ('Чт 12 ноя','Моя история'), False, True),
     (tile(O+f'howiwork/{L}-01.png'), ('Mon 2 Nov','How I work') if L=='en' else ('Пн 2 ноя','Как я работаю'), False, True),
     (tile(O+f'intro/{L}-01.png'), ('published','Intro') if L=='en' else ('уже вышло','Знакомство'), False, True),
     (oldtile(L,0,1), ('Thu 19 Nov','Two breakfasts') if L=='en' else ('Чт 19 ноя','Два завтрака'), False, False),
     (talking(L), ('Wed 18 Nov','Talking video') if L=='en' else ('Ср 18 ноя','Видео в камеру'), True, False),
     (tile(O+f'diary/{L}-01.png'), ('Mon 16 Nov','Food and mood diary') if L=='en' else ('Пн 16 ноя','Дневник питания'), False, False),
     (tile(O+f'allornothing/{L}-01.png'), ('Fri 13 Nov','All or nothing?') if L=='en' else ('Пт 13 ноя','Всё или ничего?'), False, False),
     (tile(C+f'pan-{L}.jpg'), ('Wed 11 Nov','Pancake reel') if L=='en' else ('Ср 11 ноя','Блины'), True, False),
     (tile(O+f'tired/{L}-01.png'), ('Mon 9 Nov','Tired by lunchtime?') if L=='en' else ('Пн 9 ноя','Нет сил к обеду?'), False, False),
     (tile(C+f'warm-{L}.jpg'), ('Fri 6 Nov','Workout 1') if L=='en' else ('Пт 6 ноя','Зарядка 1'), True, False),
     (tile(O+f'bloating/{L}-01.png'), ('Thu 5 Nov','Bloating') if L=='en' else ('Чт 5 ноя','Вздутие к вечеру?'), False, False),
     (oldtile(L,2,3), ('Wed 4 Nov','Market basket') if L=='en' else ('Ср 4 ноя','Корзина с рынка'), True, False),
    ]
    W,H=900,1810; im=Image.new('RGB',(W,H),CREAM); d=ImageDraw.Draw(im)
    d.text((30,28),'@nataliazutehealth · to 19 Nov' if L=='en' else '@nataliazutehealth_rus · к 19 ноября',font=f('CormorantGaramond-Medium.ttf',44),fill=FOREST)
    d.text((30,92),'English feed. Pinned first, then newest first.' if L=='en' else 'Русская лента. Сначала закреплённые, потом новые посты.',font=f('Jost-Regular.ttf',18),fill=MUTED)
    for k,(t,(day,name),reel,pinned) in enumerate(items):
        x,y=XS[k%3],YS[k//3]; im.paste(t,(x,y))
        if reel: play(d,x,y)
        if pinned: pin(d,x,y,L)
        fb=f('Jost-Medium.ttf',16); fr=f('Jost-Regular.ttf',16)
        d.text((x,y+TH+10),day,font=fb,fill=FOREST); dw=d.textlength(day+'  ·  ',font=fb)
        d.text((x+d.textlength(day,font=fb),y+TH+10),'  ·  '+name,font=fr,fill=FOREST)
    out=f"/mnt/user-data/outputs/Posts/Plan - {'EN' if L=='en' else 'RU'} feed to 19 Nov.png"; im.save(out); return out
for l in ('en','ru'): print(build(l))
