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


T["tired"] = {
  "en": dict(
    kick="Energy", title="Tired by lunchtime?", sub="4 things to look at",
    items=[
      ("Breakfast", "What did you have, if anything? Coffee alone, or a pastry on the go, may leave you running out of steam sooner than a breakfast with some protein and fibre, like eggs on toast or yoghurt with oats."),
      ("The gap", "How long did you go without eating? A late lunch after an early start is a long gap. Notice when the dip comes."),
      ("Sleep", "Look at the last two or three nights, not just last night. Short or broken sleep often shows up the next afternoon."),
      ("Drinks", "How much water did you have before lunch? And when was your last coffee? Not drinking enough can leave you feeling tired."),
    ],
    try_l="Try this week", try_t="Each day, write down when your energy dips and what came just before. A pattern often shows up within a few days.",
    gp="See your GP if you&rsquo;ve felt tired for a few weeks and don&rsquo;t know why, or if tiredness is affecting your daily life.",
    save="Save this for later", swipe="Swipe"),
  "ru": dict(
    kick="Энергия", title="Нет сил уже к&nbsp;обеду?", sub="4 вещи, на которые стоит посмотреть",
    items=[
      ("Завтрак", "Что вы ели утром и ели ли вообще? Один кофе или выпечка на бегу могут закончиться быстрее, чем завтрак с белком и клетчаткой, например яйца с тостом или йогурт с овсянкой."),
      ("Перерыв", "Сколько времени вы были без еды? Поздний обед после раннего подъёма — это долгий перерыв. Заметьте, когда приходит спад."),
      ("Сон", "Посмотрите на последние две-три ночи, а не только на вчерашнюю. Короткий или прерывистый сон часто чувствуется на следующий день после обеда."),
      ("Напитки", "Сколько воды вы выпили до обеда? И когда был последний кофе? Если пить мало, можно чувствовать усталость."),
    ],
    try_l="Попробуйте на этой неделе", try_t="Каждый день записывайте, когда падает энергия и что было прямо перед этим. Закономерность часто видна уже через несколько дней.",
    gp="Обратитесь к врачу, если усталость держится несколько недель без понятной причины или мешает обычной жизни.",
    save="Сохраните, чтобы не потерять", swipe="Листайте"),
}


def tired(lang):
    t, h = T["tired"][lang], HANDLE[lang]
    N = 2 + len(t["items"])
    s = []
    # 1 cover (grid type B, colourful): full-bleed photo, title on a cream card
    s.append(page(
        '<div style="position:absolute;inset:0;background:url(%s) 50%% 50%%/cover"></div>'
        '<div style="position:absolute;left:80px;right:80px;top:50%%;transform:translateY(-50%%);background:rgba(251,248,242,.94);'
        'border-radius:28px;padding:64px 64px 56px;text-align:center">'
        '<div class="label">%s</div>'
        '<div class="h1" style="margin-top:26px;font-size:%dpx">%s</div>'
        '<div class="h3" style="margin-top:20px;font-style:italic;color:#4A5A4E;font-size:%dpx">%s</div>'
        '<div class="arrow" style="margin-top:34px">%s &rarr;</div></div>'
        '<div style="position:absolute;left:0;right:0;bottom:0;height:150px;background:linear-gradient(transparent,rgba(251,248,242,.9))"></div>'
        % (img("images/41d0d2957ea062832eb648961566769a.jpg"), t["kick"], 108 if lang == "en" else 92, t["title"], 60 if lang == "en" else 50, t["sub"], t["swipe"]),
        "", 1, N, h))
    # 2-5 items
    for i, (head, body) in enumerate(t["items"], 1):
        s.append(page(
            '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
            '<div style="font-family:\'Cormorant Garamond\';font-weight:500;font-size:220px;line-height:.8;color:#B89A5E">%d</div>'
            '<div class="h2" style="margin-top:40px">%s</div><div class="rule" style="margin-top:44px"></div>'
            '<div class="body" style="margin-top:44px;font-size:40px">%s</div></div>'
            % (i, head, body),
            "white" if i % 2 else "", i + 1, N, h))
    # last: try this + GP
    s.append(page(
        '<div style="display:flex;gap:56px;align-items:center;margin-top:20px">%s'
        '<div><div class="label">%s</div></div></div>'
        '<div class="big" style="margin-top:56px;font-size:62px">%s</div>'
        '<div style="position:absolute;left:96px;right:96px;bottom:150px;background:#F4EEE3;border-left:6px solid #9C4F1E;border-radius:16px;padding:36px 40px">'
        '<div class="body" style="font-size:32px;color:#23392C">%s</div></div>'
        % (ring_photo("images/cc4942476c283c1b1a3a7e8394274244.jpg", 230, "50% 30%"), t["try_l"], t["try_t"], t["gp"]),
        "sage", N, N, h))
    return s


POSTS["tired"] = tired
