"""Slide content for each Instagram post. Each post is a function(lang) -> list of HTML pages."""
from build import page, lockup, ring_photo, img, EMBLEM

HANDLE = {"en": "@nataliazutehealth", "ru": "@nataliazutehealth_rus"}

T = {
 "intro": {
  "en": dict(
    hi="Hi, I&rsquo;m Natalia", role="Nutritional Therapist &amp; Wellness Coach",
    who_l="Who I help", who="I help women who feel tired, out of balance or just not quite themselves.", areas="Energy · Gut health · Skin · Cycle &amp; hormones · Stress &amp; sleep",
    been="I&rsquo;ve been there.", story="Gut problems run in my family, and in my 20s they started for me too.",
    so="So I trained in nutrition and coaching.", so2="Not for perfect plans, but for changes that fit a real week.",
    how_l="How I work", how="Three simple steps",
    steps=["Understand what may be behind how you feel", "Plan together around your real week", "Keep going, with coaching"],
    tag="Choose nourished, not perfect.", follow="Follow for simple ideas for your energy, gut, skin and cycle.",
    swipe="Swipe"),
  "ru": dict(
    hi="Здравствуйте, я&nbsp;Наталья", role="Нутрициолог и коуч по здоровью",
    who_l="Кому я помогаю", who="Женщинам, которые устали, потеряли равновесие или просто чувствуют себя не&nbsp;в&nbsp;своей тарелке.", areas="Энергия · Пищеварение · Кожа · Цикл&nbsp;и&nbsp;гормоны · Стресс&nbsp;и&nbsp;сон",
    been="Я знаю, каково это.", story="Проблемы с пищеварением есть у многих в моей семье, а в 20 с небольшим они начались и у меня.",
    so="Поэтому я выучилась на нутрициолога и коуча.", so2="Не ради идеальных планов, а ради перемен, которые вписываются в обычную неделю.",
    how_l="Как я работаю", how="Три простых шага",
    steps=["Разбираемся, что может стоять за вашим самочувствием", "Вместе составляем план под вашу реальную неделю", "Помогаю не бросить — с коучингом"],
    tag="Выбирайте заботу о&nbsp;себе, а&nbsp;не&nbsp;идеал.", follow="Подписывайтесь: простые идеи для энергии, пищеварения, кожи и цикла.",
    swipe="Листайте"),
 }
}


def intro(lang):
    t, h, N = T["intro"][lang], HANDLE[lang], 6
    s = []
    # 1 cover
    s.append(page(
        '<div>%s</div>'
        '<div style="display:flex;flex-direction:column;align-items:center;text-align:center;margin-top:70px">%s'
        '<div class="h1" style="margin-top:56px">%s</div>'
        '<div class="label" style="margin-top:34px">%s</div></div>'
        % (lockup(), ring_photo("images/bb046ce461b4ce6d97f4430a1fc7dddb.jpg", 470, "50% 35%"), t["hi"], t["role"]),
        "", 1, N, h))
    # 2 who I help
    s.append(page(
        '<div class="label" style="margin-top:40px">%s</div><div class="rule" style="margin-top:36px"></div>'
        '<div class="big" style="margin-top:48px">%s</div>'
        '<div class="body" style="margin-top:34px;font-size:32px;color:#9C4F1E;letter-spacing:.02em">%s</div>'
        '<div style="position:absolute;left:96px;right:96px;bottom:150px;height:330px;border-radius:24px;'
        'background:url(%s) 50%% 50%%/cover"></div>'
        % (t["who_l"], t["who"], t["areas"], img("images/403e3cc372607c1c837dbea7b381d086.jpg")),
        "white", 2, N, h))
    # 3 story with photo
    s.append(page(
        '<div class="photo" style="height:690px;background-image:url(%s);background-position:50%% 22%%"></div>'
        '<div class="h2" style="margin-top:60px">%s</div>'
        '<div class="body" style="margin-top:26px">%s</div>'
        % (img("images/8d4e7cf590b2ebfa2cbed8f4f339360f.jpg"), t["been"], t["story"]),
        "", 3, N, h))
    # 4 training
    s.append(page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
        '<div>%s</div>'
        '<div class="h2" style="margin-top:64px">%s</div><div class="rule" style="margin-top:56px"></div>'
        '<div class="big" style="margin-top:56px;font-style:italic;color:#4A5A4E">%s</div></div>'
        % (EMBLEM.format(s=120), t["so"], t["so2"]),
        "sage", 4, N, h))
    # 5 how I work
    s.append(page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
        '<div class="label">%s</div>'
        '<div class="h2" style="margin-top:28px">%s</div>'
        '<ol class="steps">%s</ol></div>'
        % (t["how_l"], t["how"], "".join('<li><span class="k">%d</span><span class="t">%s</span></li>' % (i + 1, x)
                                          for i, x in enumerate(t["steps"]))),
        "white", 5, N, h))
    # 6 tagline
    s.append(page(
        '<div style="display:flex;flex-direction:column;align-items:center;text-align:center;padding-top:190px">%s'
        '<div class="h1" style="margin-top:70px;font-size:104px">%s</div>'
        '<div class="rule" style="margin-top:64px"></div>'
        '<div class="body" style="margin-top:56px;max-width:760px">%s</div>'
        '<div class="label" style="margin-top:48px;letter-spacing:.12em;text-transform:none">%s</div></div>'
        % (EMBLEM.format(s=150), t["tag"], t["follow"], h),
        "", 6, N, ""))
    return s


POSTS = {"intro": intro}
