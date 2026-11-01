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
    kick="How I work", title="Knowing what to eat is only half of it",
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
    kick="Как я работаю", title="Знать, что есть, это только половина дела",
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
        '<div class="rule" style="margin-top:56px"></div>'
        '<div class="arrow" style="margin-top:44px">%s &rarr;</div></div>'
        % (EMBLEM.format(s=130), t["kick"], 100 if lang == "en" else 86, t["title"], t["swipe"]),
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
    move="In 2010 I moved to the UK. University, a full-time job and the stress of a new country. That&rsquo;s when my digestion problems began.",
    years="For years I ignored the symptoms. Tablets helped while I took them, and then everything came back.",
    vegan="Ten years of eating vegan didn&rsquo;t suit me. My energy kept dropping, and my digestion and hormones got worse.",
    turn="At some point I knew there had to be another way. So I trained in nutrition.",
    turn2="It brought some uncomfortable truths: the way I lived didn&rsquo;t suit my body or my family history.",
    path="It isn&rsquo;t a magic pill. It&rsquo;s a path of discipline and awareness, and I&rsquo;m still on it.",
    path2="Recent viruses and stress set me back, and I&rsquo;m recovering again. That&rsquo;s real life too.",
    end="Not an easy path, but for me the only way to real health.",
    end_sub="If you&rsquo;re looking for your own way, start with a free 20-minute call. The link is in my bio.",
    swipe="Swipe"),
  "ru": dict(
    kick="Знакомство", title="Моя история",
    move_h="Всё началось с переезда",
    move="В 2010 году я переехала в Великобританию. Университет, работа на полную ставку, стресс от переезда. Тогда и начались проблемы с пищеварением.",
    years="Годами я не обращала внимания на симптомы. Таблетки помогали, пока я их пила, а потом всё возвращалось.",
    vegan="Десять лет веганства мне не подошли. Энергии становилось всё меньше, а пищеварение и гормоны давали о себе знать всё сильнее.",
    turn="В какой-то момент я поняла, что должен быть другой путь. И пошла учиться на нутрициолога.",
    turn2="Пришли неудобные открытия: то, как я жила, просто не подходило моему телу и моей наследственности.",
    path="Это не волшебная таблетка. Это путь дисциплины и осознанности, и я иду по нему до сих пор.",
    path2="Недавние вирусы и стресс откатили меня назад, и я снова восстанавливаюсь. Это тоже часть жизни.",
    end="Путь непростой, но для меня единственный, чтобы вернуть здоровье по-настоящему.",
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
    t, h, N = T["story"][lang], HANDLE[lang], 7
    sz = None if lang == "en" else 66
    s = []
    s.append(page(
        '<div style="position:absolute;inset:0;background:url(%s) 50%% 25%%/cover"></div>'
        '<div style="position:absolute;left:80px;right:80px;bottom:150px;background:rgba(251,248,242,.95);'
        'border-radius:28px;padding:56px 64px 50px;text-align:center">'
        '<div class="label">%s</div>'
        '<div class="h1" style="margin-top:22px;font-size:%dpx">%s</div>'
        '<div class="arrow" style="margin-top:30px">%s &rarr;</div></div>'
        % (img("images/28f38d0abcb4b5b6bce8c61b60b663a7.jpg"), t["kick"], 110 if lang == "en" else 100, t["title"], t["swipe"]),
        "", 1, N, h))
    s.append(page(
        '<div class="photo" style="height:600px;background-image:url(%s);background-position:50%% 22%%"></div>'
        '<div class="h2" style="margin-top:56px;font-size:%dpx">%s</div>'
        '<div class="body" style="margin-top:26px;font-size:%dpx">%s</div>'
        % (img("images/8d4e7cf590b2ebfa2cbed8f4f339360f.jpg"), 76 if lang == "en" else 68, t["move_h"],
           36 if lang == "en" else 34, t["move"]),
        "", 2, N, h))
    s.append(_text(t["years"], None, "white", 3, N, h, sz))
    s.append(_text(t["vegan"], None, "", 4, N, h, sz))
    s.append(page(
        '<div style="height:1080px;display:flex;flex-direction:column;justify-content:center">'
        '<div>%s</div>'
        '<div class="h2" style="margin-top:64px;font-size:%dpx">%s</div><div class="rule" style="margin-top:56px"></div>'
        '<div class="body" style="margin-top:48px;font-size:40px">%s</div></div>'
        % (EMBLEM.format(s=120), 76 if lang == "en" else 66, t["turn"], t["turn2"]),
        "sage", 5, N, h))
    s.append(_text(t["path"], t["path2"], "white", 6, N, h, sz))
    s.append(page(
        '<div style="display:flex;flex-direction:column;align-items:center;text-align:center;padding-top:110px">%s'
        '<div class="h2" style="margin-top:60px;font-size:%dpx">%s</div>'
        '<div class="body" style="margin-top:36px;max-width:820px">%s</div>'
        '<div class="label" style="margin-top:44px;letter-spacing:.12em;text-transform:none">%s</div></div>'
        % (ring_photo("images/35e2f5bc66badfbb8809fc1d85e00f0c.jpg", 360, "50% 25%"),
           72 if lang == "en" else 62, t["end"], t["end_sub"], h),
        "", 7, N, ""))
    return s


POSTS["story"] = story
