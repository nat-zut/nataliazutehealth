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
    steps=["Разбираемся, что может стоять за вашим самочувствием", "Вместе составляем план под вашу реальную неделю", "Помогаю не бросить с помощью коучинга"],
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
      ("Перерыв", "Сколько времени вы были без еды? Поздний обед после раннего подъёма означает долгий перерыв. Заметьте, когда приходит спад."),
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


T["coaching"] = {
  "en": dict(
    kick="Coaching", title="Knowing what to eat is only half of it",
    s2="You probably already know a lot. Vegetables help. Sleep matters. Water is good for you.",
    s3="The hard part is doing it on a busy Tuesday, when you&rsquo;re tired and everyone needs something from you.",
    s4_h="That&rsquo;s where coaching comes in", s4="I don&rsquo;t tell you what to do. Together we find what matters to you, what gets in the way, and small steps you choose yourself.",
    q_l="Questions I might ask you",
    qs=["What would feel different if this worked?", "What usually gets in the way?", "What&rsquo;s one small step you&rsquo;d really take this week?"],
    end="Nutrition gives you the plan. Coaching helps you live it.", swipe="Swipe"),
  "ru": dict(
    kick="Коучинг", title="Знать, что есть, это только половина дела",
    s2="Вы, скорее всего, уже многое знаете. Овощи полезны. Сон важен. Вода нужна.",
    s3="Сложнее всего сделать это в обычный загруженный вторник, когда вы устали и всем от вас что-то нужно.",
    s4_h="Вот здесь помогает коучинг", s4="Я не говорю, что вам делать. Вместе мы находим, что важно именно вам, что мешает, и маленькие шаги, которые вы выбираете сами.",
    q_l="Вопросы, которые я могу вам задать",
    qs=["Что изменится, если это получится?", "Что обычно мешает?", "Какой один маленький шаг вы правда сделаете на этой неделе?"],
    end="Питание даёт план. Коучинг помогает по нему жить.", swipe="Листайте"),
}


def coaching(lang):
    t, h, N = T["coaching"][lang], HANDLE[lang], 6
    s = []
    # 1 cover (grid type C, plain)
    s.append(page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">%s'
        '<div class="label" style="margin-top:70px">%s</div>'
        '<div class="h1" style="margin-top:34px;font-size:%dpx">%s</div>'
        '<div class="rule" style="margin-top:56px"></div>'
        '<div class="arrow" style="margin-top:44px">%s &rarr;</div></div>'
        % (EMBLEM.format(s=130), t["kick"], 100 if lang == "en" else 88, t["title"], t["swipe"]),
        "sage", 1, N, h))
    for i, txt in enumerate([t["s2"], t["s3"]], 2):
        s.append(page(
            '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
            '<div class="rule"></div><div class="big" style="margin-top:56px">%s</div></div>' % txt,
            "white" if i == 2 else "", i, N, h))
    s.append(page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
        '<div class="h2">%s</div><div class="rule" style="margin-top:48px"></div>'
        '<div class="body" style="margin-top:48px;font-size:42px">%s</div></div>' % (t["s4_h"], t["s4"]),
        "white", 4, N, h))
    s.append(page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
        '<div class="label">%s</div><ol class="steps">%s</ol></div>'
        % (t["q_l"], "".join('<li><span class="k">%d</span><span class="t">%s</span></li>' % (i + 1, q) for i, q in enumerate(t["qs"]))),
        "", 5, N, h))
    s.append(page(
        '<div style="display:flex;flex-direction:column;align-items:center;text-align:center;padding-top:110px">%s'
        '<div class="h2" style="margin-top:70px">%s</div>'
        '<div class="label" style="margin-top:56px;letter-spacing:.12em;text-transform:none">%s</div></div>'
        % (ring_photo("images/e65d692a766322ff9007f1e03d416859.jpg", 400, "50% 30%"), t["end"], h),
        "sage", 6, N, ""))
    return s


POSTS["coaching"] = coaching


# ---------------------------------------------------------------------------
# Pinned posts, 1 Nov 2026 (positioning "Feel at home in your body", 19 Oct)
# ---------------------------------------------------------------------------

def _list(items):
    return ('<ul style="list-style:none;margin-top:44px;border-top:1.5px solid #D8CFBF">%s</ul>' % "".join(
        '<li style="display:flex;gap:28px;align-items:center;padding:30px 0;border-bottom:1.5px solid #D8CFBF">'
        '<span style="width:14px;height:14px;border-radius:50%%;background:#B89A5E;flex:none"></span>'
        '<span style="font-size:44px;line-height:1.3">%s</span></li>' % x for x in items))


def _steps(items):
    return '<ol class="steps">%s</ol>' % "".join(
        '<li><span class="k">%d</span><span class="t">%s</span></li>' % (i + 1, x) for i, x in enumerate(items))


T["meet"] = {
  "en": dict(
    hi="Hi, I&rsquo;m Natalia", role="Nutritional Therapist &amp; Wellness Coach",
    head="Feel at home<br>in your body.", head_sub="Nutrition and coaching, online, in English and Russian.",
    who_l="Who I help", who="Women who want to feel like themselves again. I can support you with:",
    areas=["Digestion and bloating", "Low energy", "Skin flare-ups", "Difficult cycles", "Stress and sleep"],
    how_l="How I can help",
    steps=["We look at what may be behind how you feel", "We write a plan that fits your real week", "I support you every week while it becomes a habit"],
    end="Start with a free<br>20-minute call", end_sub="A relaxed chat to see if we&rsquo;re a good fit. The link is in my bio.",
    swipe="Swipe"),
  "ru": dict(
    hi="Здравствуйте, я&nbsp;Наталья", role="Нутрициолог и коуч по здоровью",
    head="Почувствуйте себя в&nbsp;своём теле как&nbsp;дома.", head_sub="Питание и коучинг онлайн, на русском и английском.",
    who_l="Кому я помогаю", who="Женщинам, которые хотят снова чувствовать себя собой. Я помогаю, если беспокоят:",
    areas=["Пищеварение и вздутие", "Нехватка энергии", "Высыпания на коже", "Сложный цикл", "Стресс и сон"],
    how_l="Как я помогаю",
    steps=["Разбираемся, в чём может быть причина вашего самочувствия", "Составляем план, который впишется в вашу реальную неделю", "Каждую неделю поддерживаю вас, пока изменения не станут привычкой"],
    end="Начните с бесплатного <span style=\"white-space:nowrap\">20-минутного</span> звонка", end_sub="Спокойный разговор, чтобы понять, подходим ли мы друг другу. Ссылка в профиле.",
    swipe="Листайте"),
}


def meet(lang):
    """Pinned 1 (grid type A, photo)."""
    t, h, N = T["meet"][lang], HANDLE[lang], 5
    s = []
    s.append(page(
        '<div>%s</div>'
        '<div style="display:flex;flex-direction:column;align-items:center;text-align:center;margin-top:60px">%s'
        '<div class="h1" style="margin-top:56px;font-size:%dpx">%s</div>'
        '<div class="label" style="margin-top:34px">%s</div>'
        '<div class="arrow" style="margin-top:40px">%s &rarr;</div></div>'
        % (lockup(), ring_photo("images/bb046ce461b4ce6d97f4430a1fc7dddb.jpg", 450, "50% 35%"),
           112 if lang == "en" else 96, t["hi"], t["role"], t["swipe"]),
        "", 1, N, h))
    s.append(page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">%s'
        '<div class="h1" style="margin-top:70px;font-size:%dpx">%s</div>'
        '<div class="rule" style="margin-top:56px"></div>'
        '<div class="body" style="margin-top:48px;max-width:780px">%s</div></div>'
        % (EMBLEM.format(s=130), 108 if lang == "en" else 92, t["head"], t["head_sub"]),
        "sage", 2, N, h))
    s.append(page(
        '<div class="label" style="margin-top:30px">%s</div><div class="rule" style="margin-top:32px"></div>'
        '<div class="big" style="margin-top:44px;font-size:%dpx">%s</div>%s'
        % (t["who_l"], 62 if lang == "en" else 56, t["who"], _list(t["areas"])),
        "white", 3, N, h))
    s.append(page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
        '<div class="label">%s</div>%s</div>' % (t["how_l"], _steps(t["steps"])),
        "", 4, N, h))
    s.append(page(
        '<div style="display:flex;flex-direction:column;align-items:center;text-align:center;padding-top:120px">%s'
        '<div class="h2" style="margin-top:64px;font-size:%dpx">%s</div>'
        '<div class="body" style="margin-top:36px;max-width:800px">%s</div>'
        '<div class="label" style="margin-top:48px;letter-spacing:.12em;text-transform:none">%s</div></div>'
        % (ring_photo("images/cc4942476c283c1b1a3a7e8394274244.jpg", 380, "50% 30%"),
           80 if lang == "en" else 70, t["end"], t["end_sub"], h),
        "sage", 5, N, ""))
    return s


POSTS["meet"] = meet


T["howiwork"] = {
  "en": dict(
    kick="Nutrition &amp; coaching", title="How I work", cover_sub="Knowing what to eat is only half of it",
    s2="You probably already know a lot. Vegetables help. Sleep matters. Water is good for you.",
    s3="The hard part is doing it on a busy Tuesday, when you&rsquo;re tired and everyone needs something from you.",
    two_l="So I bring two things together",
    two=[("Nutrition", "We find what may be behind how you feel and write a plan for your real week."),
         ("Coaching", "Every week we look at what&rsquo;s working, what gets in the way, and the next small step you choose.")],
    q_l="Questions I might ask you",
    qs=["What would feel different if this worked?", "What usually gets in the way?", "What&rsquo;s one small step you&rsquo;d really take this week?"],
    start_l="How we start",
    start=[("A free 20-minute call", "We get to know each other and see if we&rsquo;re a good fit. No advice yet, and no obligation."),
           ("Your 90-minute Health Review", "We look at what may be behind how you feel, and you get a written plan."),
           ("Weekly coaching", "If you choose a programme, I support you every week while the changes settle in.")],
    end="Nutrition gives you the plan. Coaching helps you live it.", cta="Book your free call &middot; link in bio",
    swipe="Swipe"),
  "ru": dict(
    kick="Питание и коучинг", title="Как я работаю", cover_sub="Знать, что есть, это только половина дела",
    s2="Вы, скорее всего, уже многое знаете. Овощи полезны. Сон важен. Вода нужна.",
    s3="Сложнее всего делать это в обычный загруженный вторник, когда вы устали и всем от вас что-то нужно.",
    two_l="Поэтому я соединяю два подхода",
    two=[("Питание", "Разбираемся, в чём может быть причина, и составляем план под вашу реальную неделю."),
         ("Коучинг", "Каждую неделю смотрим, что получается, что мешает и какой следующий маленький шаг вы выберете.")],
    q_l="Вопросы, которые я могу вам задать",
    qs=["Что изменится, если всё получится?", "Что обычно мешает?", "Какой маленький шаг вы правда сделаете на этой неделе?"],
    start_l="С чего мы начинаем",
    start=[("Бесплатный <span style=\"white-space:nowrap\">20-минутный</span> звонок", "Знакомимся и понимаем, подходим ли друг другу. Без рекомендаций и без обязательств."),
           ("Разбор здоровья, 90&nbsp;минут", "Разбираемся, в чём может быть причина вашего самочувствия, и вы получаете письменный план."),
           ("Коучинг каждую неделю", "Если вы выбираете программу, я поддерживаю вас каждую неделю, пока изменения не станут привычкой.")],
    end="Питание даёт план. Коучинг помогает жить по&nbsp;нему.", cta="Запишитесь на бесплатный звонок &middot; ссылка в профиле",
    swipe="Листайте"),
}


def howiwork(lang):
    """Pinned 2 (grid type C, plain)."""
    t, h, N = T["howiwork"][lang], HANDLE[lang], 7
    s = []
    s.append(page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">%s'
        '<div class="label" style="margin-top:70px">%s</div>'
        '<div class="h1" style="margin-top:34px;font-size:%dpx">%s</div>'
        '<div class="h3" style="margin-top:26px;font-style:italic;color:#4A5A4E;font-size:%dpx">%s</div>'
        '<div class="rule" style="margin-top:52px"></div>'
        '<div class="arrow" style="margin-top:44px">%s &rarr;</div></div>'
        % (EMBLEM.format(s=130), t["kick"], 132 if lang == "en" else 120, t["title"], 54 if lang == "en" else 48, t["cover_sub"], t["swipe"]),
        "sage", 1, N, h))
    for i, txt in enumerate([t["s2"], t["s3"]], 2):
        s.append(page(
            '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
            '<div class="rule"></div><div class="big" style="margin-top:56px">%s</div></div>' % txt,
            "white" if i == 2 else "", i, N, h))
    s.append(page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
        '<div class="label">%s</div><ol class="steps">%s</ol></div>'
        % (t["two_l"], "".join(
            '<li><span class="k">%d</span><span class="t"><b style="font-weight:500;color:#23392C">%s.</b> %s</span></li>'
            % (i + 1, a, b) for i, (a, b) in enumerate(t["two"]))),
        "white", 4, N, h))
    s.append(page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
        '<div class="label">%s</div>%s</div>' % (t["q_l"], _steps(t["qs"])),
        "", 5, N, h))
    s.append(page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
        '<div class="label">%s</div><ol class="steps">%s</ol></div>'
        % (t["start_l"], "".join(
            '<li><span class="k">%d</span><span class="t"><b style="font-weight:500;color:#23392C">%s.</b> %s</span></li>'
            % (i + 1, a, b) for i, (a, b) in enumerate(t["start"]))),
        "white", 6, N, h))
    s.append(page(
        '<div style="display:flex;flex-direction:column;align-items:center;text-align:center;padding-top:110px">%s'
        '<div class="h2" style="margin-top:64px;font-size:%dpx">%s</div>'
        '<div class="label" style="margin-top:52px;letter-spacing:.12em;text-transform:none">%s</div></div>'
        % (ring_photo("images/e65d692a766322ff9007f1e03d416859.jpg", 380, "50% 30%"),
           76 if lang == "en" else 68, t["end"], t["cta"]),
        "sage", 7, N, ""))
    return s


POSTS["howiwork"] = howiwork


T["story"] = {
  "en": dict(
    kick="Meet Natalia", title="My story",
    move_h="It started with a move",
    move="In 2010 I moved to the UK. The stress of moving, culture shock, university and a full-time job. That&rsquo;s when my digestion problems began.",
    years="For years I ignored the symptoms. Tablets helped while I took them, and then everything came back.",
    vegan="Ten years of unbalanced vegetarian and vegan eating took a toll on my already shaky health. My energy kept dropping, I was losing weight, and my digestion and hormones got worse.",
    turn="At some point I knew there had to be another way. So I trained in nutrition.",
    turn2="It brought some uncomfortable truths: the way I lived didn&rsquo;t suit my body or my family history.",
    path="It isn&rsquo;t a magic pill. It&rsquo;s a path of discipline and awareness. Not an easy one, but for me the only way to real health.",
    path2="Recent viruses and stress set me back, and I&rsquo;m recovering again. That&rsquo;s real life too.",
    imp="I&rsquo;m not perfect,<br>and I&rsquo;m still on this path.",
    imp2="I just do what I can, every day. Doing it imperfectly beats not doing it at all.",
    end="Choose nourished,<br>not perfect.",
    end_sub="If you&rsquo;re looking for your own way, start with a free 20-minute call. The link is in my bio.",
    swipe="Swipe"),
  "ru": dict(
    kick="Знакомство", title="Моя история",
    move_h="Всё началось с переезда",
    move="В 2010 году я переехала в Великобританию. Стресс от переезда, культурный шок, университет и работа на полную ставку. Тогда и начались проблемы с пищеварением.",
    years="Годами я не обращала внимания на симптомы. Таблетки помогали, пока я их пила, а потом всё возвращалось.",
    vegan="Десять лет несбалансированного вегетарианства и веганства сыграли злую шутку с моим и без того пошатнувшимся здоровьем. Энергии становилось всё меньше, я теряла вес, а пищеварение и гормоны давали о себе знать всё сильнее.",
    turn="В какой-то момент я поняла, что должен быть другой путь. И пошла учиться на нутрициолога.",
    turn2="Пришли неудобные открытия: то, как я жила, просто не подходило моему телу и моей наследственности.",
    path="Это не волшебная таблетка, а путь дисциплины и осознанности. Путь непростой, но для меня единственный, чтобы вернуть здоровье <span style=\"white-space:nowrap\">по-настоящему</span>.",
    path2="Недавние вирусы и стресс откатили меня назад, и я снова восстанавливаюсь. Это тоже часть жизни.",
    imp="Я не идеальная,<br>и я всё ещё в пути.",
    imp2="Я просто каждый день делаю то, что в моих силах. Лучше сделать не идеально, чем не сделать совсем.",
    end="Выбирайте заботу о&nbsp;себе,<br>а&nbsp;не&nbsp;идеал.",
    end_sub="Если вы тоже ищете свой путь, начните с бесплатного <span style=\"white-space:nowrap\">20-минутного</span> звонка. Ссылка в профиле.",
    swipe="Листайте"),
}


def _text(body, sub=None, cls="", n=0, N=0, h="", size=None):
    return page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
        '<div class="rule"></div><div class="big" style="margin-top:56px%s">%s</div>%s</div>'
        % (";font-size:%dpx" % size if size else "", body,
           '<div class="body" style="margin-top:44px;font-size:40px">%s</div>' % sub if sub else ""),
        cls, n, N, h)


def story(lang):
    """My story (grid type B, colourful). Natalia's own story, 1 Nov 2026."""
    t, h, N = T["story"][lang], HANDLE[lang], 8
    sz = None if lang == "en" else 66
    s = []
    s.append(page(
        '<div style="position:absolute;inset:0;background:url(%s) 50%% 20%%/cover"></div>'
        '<div style="position:absolute;left:80px;right:80px;bottom:150px;background:rgba(251,248,242,.95);'
        'border-radius:28px;padding:56px 64px 50px;text-align:center">'
        '<div class="label">%s</div>'
        '<div class="h1" style="margin-top:22px;font-size:%dpx">%s</div>'
        '<div class="arrow" style="margin-top:30px">%s &rarr;</div></div>'
        % (img("images/35e2f5bc66badfbb8809fc1d85e00f0c.jpg"), t["kick"], 110 if lang == "en" else 100, t["title"], t["swipe"]),
        "", 1, N, h))
    s.append(page(
        '<div class="photo" style="height:600px;background-image:url(%s);background-position:50%% 22%%"></div>'
        '<div class="h2" style="margin-top:56px;font-size:%dpx">%s</div>'
        '<div class="body" style="margin-top:26px;font-size:%dpx">%s</div>'
        % (img("images/8d4e7cf590b2ebfa2cbed8f4f339360f.jpg"), 76 if lang == "en" else 68, t["move_h"],
           36 if lang == "en" else 34, t["move"]),
        "", 2, N, h))
    s.append(_text(t["years"], None, "white", 3, N, h, sz))
    s.append(_text(t["vegan"], None, "", 4, N, h, 64 if lang == "en" else 58))
    s.append(page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
        '<div>%s</div>'
        '<div class="h2" style="margin-top:64px;font-size:%dpx">%s</div><div class="rule" style="margin-top:56px"></div>'
        '<div class="body" style="margin-top:48px;font-size:40px">%s</div></div>'
        % (EMBLEM.format(s=120), 76 if lang == "en" else 66, t["turn"], t["turn2"]),
        "sage", 5, N, h))
    s.append(_text(t["path"], t["path2"], "white", 6, N, h, 62 if lang == "en" else 56))
    s.append(page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
        '<div>%s</div>'
        '<div class="h2" style="margin-top:64px;font-size:%dpx">%s</div><div class="rule" style="margin-top:56px"></div>'
        '<div class="big" style="margin-top:52px;font-size:%dpx;font-style:italic;color:#4A5A4E">%s</div></div>'
        % (EMBLEM.format(s=120), 84 if lang == "en" else 76, t["imp"], 56 if lang == "en" else 52, t["imp2"]),
        "sage", 7, N, h))
    s.append(page(
        '<div style="display:flex;flex-direction:column;align-items:center;text-align:center;padding-top:110px">%s'
        '<div class="h1" style="margin-top:60px;font-size:%dpx;font-style:italic">%s</div>'
        '<div class="rule" style="margin-top:44px"></div>'
        '<div class="body" style="margin-top:40px;max-width:820px">%s</div>'
        '<div class="label" style="margin-top:44px;letter-spacing:.12em;text-transform:none">%s</div></div>'
        % (ring_photo("images/cc4942476c283c1b1a3a7e8394274244.jpg", 360, "50% 30%"),
           88 if lang == "en" else 74, t["end"], t["end_sub"], h),
        "", 8, N, ""))
    return s


POSTS["story"] = story


# ---------------------------------------------------------------------------
# Profile topics, 1 Nov 2026: digestion and coaching (from the blog articles)
# ---------------------------------------------------------------------------

def _cover_photo(photo, pos, kick, title, sub, swipe, tsize, ssize, N, h):
    """Grid type B (colourful): full-bleed photo, title on a cream card."""
    return page(
        '<div style="position:absolute;inset:0;background:url(%s) %s/cover"></div>'
        '<div style="position:absolute;left:80px;right:80px;top:50%%;transform:translateY(-50%%);background:rgba(251,248,242,.95);'
        'border-radius:28px;padding:64px 64px 56px;text-align:center">'
        '<div class="label">%s</div>'
        '<div class="h1" style="margin-top:26px;font-size:%dpx">%s</div>'
        '<div class="h3" style="margin-top:20px;font-style:italic;color:#4A5A4E;font-size:%dpx">%s</div>'
        '<div class="arrow" style="margin-top:34px">%s &rarr;</div></div>'
        % (img(photo), pos, kick, tsize, title, ssize, sub, swipe),
        "", 1, N, h)


def _cover_plain(kick, title, sub, swipe, tsize, N, h, cls="sage"):
    """Grid type C (plain)."""
    return page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">%s'
        '<div class="label" style="margin-top:70px">%s</div>'
        '<div class="h1" style="margin-top:34px;font-size:%dpx">%s</div>'
        '<div class="h3" style="margin-top:26px;font-style:italic;color:#4A5A4E;font-size:52px">%s</div>'
        '<div class="rule" style="margin-top:48px"></div>'
        '<div class="arrow" style="margin-top:40px">%s &rarr;</div></div>'
        % (EMBLEM.format(s=130), kick, tsize, title, sub, swipe),
        cls, 1, N, h)


def _pairs(items, start, n, N, h, cls):
    """Two numbered items on one slide."""
    blocks = "".join(
        '<div style="padding:44px 0;border-bottom:1.5px solid #D8CFBF;display:flex;gap:40px">'
        '<div style="font-family:\'Cormorant Garamond\';font-weight:500;font-size:110px;line-height:.8;color:#B89A5E;width:70px;flex:none">%d</div>'
        '<div><div class="h3" style="font-size:56px">%s</div><div class="body" style="margin-top:16px;font-size:36px">%s</div></div></div>'
        % (start + i, a, b) for i, (a, b) in enumerate(items))
    return page('<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
                '<div style="border-top:1.5px solid #D8CFBF">%s</div></div>' % blocks, cls, n, N, h)


T["bloating"] = {
  "en": dict(
    kick="Digestion", title="Bloated by the afternoon?", sub="8 everyday things that may be behind it",
    intro="Your jeans fit in the morning. By 4pm, they don&rsquo;t.",
    intro2="Most bloating comes from gas in your gut. Food, drinks and the air you swallow add up through the day, and stress and long hours at a desk can slow things down.",
    items=[("Eating quickly", "When you eat fast, you swallow more air. Sit down for lunch, even for 15 minutes."),
           ("Fizzy drinks", "The bubbles are gas. Swap one fizzy drink a day for still water or herbal tea."),
           ("A big lunch, no breakfast", "One large meal can be harder to manage. Try a simple breakfast and a lighter lunch."),
           ("Not enough water", "Water helps keep things moving. Keep a glass where you can see it."),
           ("Lots of fibre at once", "Beans, lentils and cabbage are good for you. Add them slowly while your gut gets used to them."),
           ("Sitting for hours", "Movement helps digestion. A 10-minute walk after lunch is an easy start."),
           ("Stress", "Your gut and brain are closely connected. Try a few slow breaths before you eat."),
           ("Your cycle", "Some women notice more bloating at certain times. Note your cycle day next to how you feel.")],
    one="Start with one change",
    one2="Pick one thing from this list, try it for a week and notice what happens. My free 7-day diary makes it easier. The link is in my bio.",
    gp="See your GP if bloating keeps coming back, if you&rsquo;re losing weight without trying, or if you see blood in your poo.",
    swipe="Swipe"),
  "ru": dict(
    kick="Пищеварение", title="Вздутие к&nbsp;вечеру?", sub="8 обычных причин, которые могут за этим стоять",
    intro="Утром джинсы сидят свободно, а к четырём часам уже нет.",
    intro2="Чаще всего вздутие связано с газами в кишечнике. За день накапливаются еда, напитки и воздух, который мы заглатываем, а стресс и долгое сидение за столом могут замедлять пищеварение.",
    items=[("Едите быстро", "Когда едите быстро или на ходу, вы заглатываете больше воздуха. Садитесь за обед хотя бы на 15 минут."),
           ("Газированные напитки", "Пузырьки и есть газ. Замените один такой напиток в день на обычную воду или травяной чай."),
           ("Большой обед без завтрака", "С одной большой порцией справиться сложнее. Попробуйте простой завтрак и обед полегче."),
           ("Мало воды", "Вода помогает пищеварению. Держите стакан или бутылку на виду."),
           ("Много клетчатки сразу", "Фасоль, чечевица и капуста полезны. Добавляйте их понемногу, пока кишечник привыкает."),
           ("Долго сидите", "Движение помогает пищеварению. Начните с прогулки на 10 минут после обеда."),
           ("Стресс", "Кишечник и мозг тесно связаны. Сделайте несколько медленных вдохов перед едой."),
           ("Ваш цикл", "Некоторые женщины замечают, что вздутие сильнее в определённые дни. Записывайте день цикла рядом с самочувствием.")],
    one="Начните с одного изменения",
    one2="Выберите что-то одно из списка, попробуйте неделю и понаблюдайте. С бесплатным дневником «Что мне помогает» это проще. Ссылка в профиле.",
    gp="Обратитесь к врачу, если вздутие возвращается снова и снова, если вы худеете без причины или замечаете кровь в стуле.",
    swipe="Листайте"),
}


def bloating(lang):
    t, h, N = T["bloating"][lang], HANDLE[lang], 7
    s = [_cover_photo("images/d9e980fc6f2525e38a3eef2ba0d7c5f3.jpg", "50% 50%", t["kick"], t["title"], t["sub"], t["swipe"],
                      104 if lang == "en" else 100, 52 if lang == "en" else 46, N, h)]
    s.append(_text(t["intro"], t["intro2"], "white", 2, N, h, 66 if lang == "en" else 60))
    for k in range(4):
        s.append(_pairs(t["items"][2 * k:2 * k + 2], 2 * k + 1, k + 3, N, h, "" if k % 2 == 0 else "white"))
    s.append(page(
        '<div style="display:flex;gap:56px;align-items:center;margin-top:20px">%s</div>'
        '<div class="h2" style="margin-top:56px;font-size:%dpx">%s</div>'
        '<div class="body" style="margin-top:30px;font-size:38px">%s</div>'
        '<div style="position:absolute;left:96px;right:96px;bottom:150px;background:#F4EEE3;border-left:6px solid #9C4F1E;border-radius:16px;padding:36px 40px">'
        '<div class="body" style="font-size:32px;color:#23392C">%s</div></div>'
        % (ring_photo("images/28f38d0abcb4b5b6bce8c61b60b663a7.jpg", 230, "50% 25%"),
           72 if lang == "en" else 64, t["one"], t["one2"], t["gp"]),
        "sage", N, N, h))
    return s


POSTS["bloating"] = bloating


T["diary"] = {
  "en": dict(
    kick="Digestion", title="How to find out what helps you", sub="A food and mood diary in&nbsp;5&nbsp;minutes a&nbsp;day",
    what_l="What to write down each day",
    what=["Food and drinks, roughly when", "Sleep, and how rested you felt", "Energy: a score from 1 to 5", "Digestion: bloating and comfort", "Skin, mood and stress", "Your cycle day"],
    easy_l="Keep it easy",
    easy=["Fill it in at the end of the day. It takes about 5 minutes.", "Be honest, not perfect. There are no wrong answers.", "Missed a day? Just pick it up tomorrow."],
    look_l="After 7 days, ask yourself",
    look=["Which days felt better? What was different?", "Do I feel worse at a certain time, or after certain meals?", "How did sleep and stress affect the next day?"],
    end="Get my free 7-day diary, What Helps Me",
    end_sub="The link is in my bio. Want help reading it? Bring it to a free 20-minute call.",
    swipe="Swipe"),
  "ru": dict(
    kick="Пищеварение", title="Как понять, что помогает именно вам", sub="Дневник питания и самочувствия за&nbsp;5&nbsp;минут в&nbsp;день",
    what_l="Что записывать каждый день",
    what=["Еду и напитки, примерно во сколько", "Сон и насколько вы отдохнули", "Энергию: оценка от 1 до 5", "Пищеварение: вздутие и комфорт", "Кожу, настроение и стресс", "День цикла"],
    easy_l="Как не бросить",
    easy=["Заполняйте вечером, это около 5 минут.", "Честно, а не идеально. Неправильных ответов нет.", "Пропустили день? Просто продолжите завтра."],
    look_l="Через 7 дней спросите себя",
    look=["В какие дни было лучше? Что тогда было иначе?", "Хуже ли мне в определённое время или после какой-то еды?", "Как сон и стресс влияли на следующий день?"],
    end="Заберите бесплатный дневник «Что мне помогает»",
    end_sub="Ссылка в профиле. Хотите разобрать его вместе? Приходите с ним на бесплатный <span style=\"white-space:nowrap\">20-минутный</span> звонок.",
    swipe="Листайте"),
}


def diary(lang):
    t, h, N = T["diary"][lang], HANDLE[lang], 5
    s = [_cover_plain(t["kick"], t["title"], t["sub"], t["swipe"], 96 if lang == "en" else 84, N, h)]
    s.append(page('<div class="label" style="margin-top:30px">%s</div><div class="rule" style="margin-top:32px"></div>%s'
                  % (t["what_l"], _list(t["what"])), "white", 2, N, h))
    s.append(page('<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
                  '<div class="label">%s</div>%s</div>' % (t["easy_l"], _steps(t["easy"])), "", 3, N, h))
    s.append(page('<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
                  '<div class="label">%s</div>%s</div>' % (t["look_l"], _steps(t["look"])), "white", 4, N, h))
    s.append(page(
        '<div style="display:flex;flex-direction:column;align-items:center;text-align:center;padding-top:110px">%s'
        '<div class="h2" style="margin-top:60px;font-size:%dpx">%s</div>'
        '<div class="body" style="margin-top:36px;max-width:820px">%s</div>'
        '<div class="label" style="margin-top:44px;letter-spacing:.12em;text-transform:none">%s</div></div>'
        % (ring_photo("images/f91da419f3c3f8d922409f82ce6a13df.jpg", 360, "50% 50%"),
           72 if lang == "en" else 62, t["end"], t["end_sub"], h),
        "sage", 5, N, ""))
    return s


POSTS["diary"] = diary


T["allornothing"] = {
  "en": dict(
    kick="Coaching", title="All or nothing?", sub="Why we give up by Wednesday, and what helps",
    s2="Sound familiar? On Monday you start a whole new life. By Wednesday, everything is back to how it was.",
    s2b="It isn&rsquo;t a lack of willpower. It&rsquo;s usually one of these four traps.",
    traps_l="Four common traps",
    traps=["Changing everything at once", "Following rules without your own reason", "Seeing one bad day as failure", "No plan for busy days"],
    help_l="What helps instead",
    help=["One small step you&rsquo;re sure you can do", "Your own reason: what will be different for you?", "A plan B for busy days", "Starting again, without guilt"],
    q_l="A question for this week", q="What&rsquo;s one small thing I could do, even on a bad day?",
    end="Choose nourished,<br>not perfect.",
    end_sub="In coaching we find your small steps together. Book a free 20-minute call: the link is in my bio.",
    swipe="Swipe"),
  "ru": dict(
    kick="Коучинг", title="Всё или ничего?", sub="Почему мы бросаем к&nbsp;среде и&nbsp;что помогает",
    s2="Знакомо? В понедельник начинается новая жизнь, а к среде всё снова как было.",
    s2b="Дело не в силе воли. Чаще всего это одна из четырёх ловушек.",
    traps_l="Четыре ловушки",
    traps=["Менять всё сразу", "Следовать правилам без своей причины", "Считать один плохой день провалом", "Не иметь плана на трудные дни"],
    help_l="Что помогает",
    help=["Один маленький шаг, в котором вы уверены", "Своя причина: что изменится именно для вас?", "План Б на загруженные дни", "Начинать заново без чувства вины"],
    q_l="Вопрос на эту неделю", q="Что одно маленькое я могу делать даже в плохой день?",
    end="Выбирайте заботу о&nbsp;себе,<br>а&nbsp;не&nbsp;идеал.",
    end_sub="На коучинге мы вместе находим ваши маленькие шаги. Запишитесь на бесплатный <span style=\"white-space:nowrap\">20-минутный</span> звонок, ссылка в профиле.",
    swipe="Листайте"),
}


def allornothing(lang):
    """Coaching (grid type A, her photo)."""
    t, h, N = T["allornothing"][lang], HANDLE[lang], 6
    s = [page(
        '<div>%s</div>'
        '<div style="display:flex;flex-direction:column;align-items:center;text-align:center;margin-top:50px">%s'
        '<div class="label" style="margin-top:44px">%s</div>'
        '<div class="h1" style="margin-top:22px;font-size:%dpx">%s</div>'
        '<div class="h3" style="margin-top:18px;font-style:italic;color:#4A5A4E;font-size:%dpx">%s</div>'
        '<div class="arrow" style="margin-top:30px">%s &rarr;</div></div>'
        % (lockup(), ring_photo("images/06423a6c00e39aeee5560e879c85eb10.jpg", 400, "40% 30%"), t["kick"],
           112 if lang == "en" else 104, t["title"], 50 if lang == "en" else 44, t["sub"], t["swipe"]),
        "", 1, N, h)]
    s.append(_text(t["s2"], t["s2b"], "white", 2, N, h, 66 if lang == "en" else 60))
    s.append(page('<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
                  '<div class="label">%s</div>%s</div>' % (t["traps_l"], _steps(t["traps"])), "", 3, N, h))
    s.append(page('<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
                  '<div class="label">%s</div>%s</div>' % (t["help_l"], _steps(t["help"])), "white", 4, N, h))
    s.append(page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
        '<div>%s</div><div class="label" style="margin-top:60px">%s</div>'
        '<div class="h2" style="margin-top:36px;font-style:italic;font-size:%dpx">%s</div></div>'
        % (EMBLEM.format(s=120), t["q_l"], 84 if lang == "en" else 74, t["q"]),
        "sage", 5, N, h))
    s.append(page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center">'
        '<div class="h1" style="font-size:%dpx;font-style:italic">%s</div>'
        '<div class="rule" style="margin-top:48px"></div>'
        '<div class="body" style="margin-top:44px;max-width:820px">%s</div>'
        '<div class="label" style="margin-top:44px;letter-spacing:.12em;text-transform:none">%s</div></div>'
        % (96 if lang == "en" else 80, t["end"], t["end_sub"], h),
        "", 6, N, ""))
    return s


POSTS["allornothing"] = allornothing
