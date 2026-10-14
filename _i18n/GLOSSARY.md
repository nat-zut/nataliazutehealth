# Russian translation brief: Natalia Zute Health website

You are translating Natalia's website from British English into natural, modern Russian for Russian-speaking women (mostly living in the UK and Europe). It must read as if Natalia wrote it in Russian herself: calm, warm, clear and honest. Not a word-for-word translation; rephrase where Russian needs it, but keep every fact, price, number and promise exactly the same. Never add claims or content.

## Voice
- Address the reader with «вы» (lower-case, not «Вы»). Warm but professional.
- Natalia speaks in the first person, feminine forms (я работала, я училась, я рада).
- Clients are women: «клиентки», «каждая», «вы готовы» etc. Use feminine forms where the reader's gender shows (вы готовы is fine; «если вы устали»; but «я сама прошла через это»).
- Short sentences, plain everyday words. Many readers are not native Russian speakers either.
- Calm, gently encouraging; never hype, never shaming. No exclamation-mark gushing.
- Russian typography: quotes «ёлочки» (inner „лапки“), em dash « — » with spaces, use «ё» where standard (ещё, всё). Non-breaking details don't matter.

## Health advertising rules (UK ASA/CAP apply to the Russian pages too)
Never write: лечить/вылечить, исцелить, избавить от, устранить (a condition), гарантировать, детокс, очищение, вывести токсины, суперфуд, «правильное/неправильное питание», «полезные/вредные продукты», «первопричина», чудо, быстрый результат, похудеть на N кг.
Use instead: поддержать, разобраться, что может стоять за вашим самочувствием, помочь, план, постепенно, реалистично.
Don't name medical conditions that the English doesn't name. Weight: «поддержка, если вы хотите управлять своим весом, без жёстких диет».
Never call her «зарегистрированный», «диетолог», «врач», «нутрициолог-диетолог». No «лечение».

## Fixed terms (use exactly)
| English | Russian |
|---|---|
| Natalia Zute (in text) | Наталья Зуте |
| Natalia (in text) | Наталья |
| Natalja Zute (legal name) | keep in Latin: Natalja Zute |
| Natalia Zute Health (brand) | keep in Latin: Natalia Zute Health |
| NATALIA ZUTE / HEALTH (logo text) | keep exactly as in English |
| Nutritional Therapist & Wellness Coach | нутрициолог и коуч по здоровью (as a title line: Нутрициолог и коуч по здоровью) |
| nutritional therapy | нутрициология / работа с питанием (choose what reads naturally) |
| wellness coaching | коучинг по здоровью |
| coaching session | коуч-сессия |
| Root, Grow, Root & Grow (programme names) | Основа, Рост, Основа и рост (in running text: программа «Основа», so the name stays in the nominative) |
| SIGNATURE (sticker) | ФИРМЕННАЯ |
| Health Review | разбор здоровья (as a service name: «Разбор здоровья») |
| (nutrition) follow-up | повторная консультация |
| plan walk-through | разбор плана |
| free 20-minute call / free call / fit call | бесплатный 20-минутный звонок / бесплатный звонок-знакомство |
| Book a free call | Записаться на бесплатный звонок |
| founding client places / founding places | места для первых клиенток |
| founding client | первая клиентка (по сниженной цене) |
| at about half price | примерно за полцены |
| written plan | письменный план |
| health questionnaire | анкета о здоровье |
| food diary | дневник питания |
| email support | поддержка по email |
| GP | ваш врач (GP) the first time on a page, then «врач» |
| the free guide / free 7-day diary | бесплатный 7-дневный дневник |
| What Helps Me (diary title) | keep in Latin: What Helps Me |
| Choose nourished, not perfect. (tagline) | Выбирайте заботу о себе, а не идеал. |
| gut health | здоровье кишечника / пищеварение |
| bloating | вздутие |
| cycle | цикл |
| hormonal health | гормональное здоровье |
| energy and tiredness | энергия и усталость |
| Blog | Блог |
| Work with me (page/nav) | Услуги |
| About | Обо мне |
| How I work | Как я работаю |
| Free guide (nav) | Бесплатный дневник |
| Contact and booking | Контакты и запись |
| Privacy policy | Политика конфиденциальности |
| Terms | Условия |
| Cookie settings | Настройки cookie |
| Draft, not yet live | Черновик, ещё не действует |
| UK | Великобритания |

## Prices, dates, numbers
- Keep every price and number exactly; keep the currency symbol before the number as in English (£485, €535). Write thousands with a space: £1 155.
- «or 3 monthly payments: £155, £145, £145» → «или 3 ежемесячных платежа: £155, £145, £145».
- «if booked separately» → «при оплате по отдельности».
- Durations: «90 мин», «60 мин», «30 мин», «20 минут», «12 недель», «6 сессий».
- Dates: «8 декабря 2026», «Пн 19 октября».
- Email addresses, URLs and @handles stay unchanged.

## Format of the files
Each file is a JSON object: keys are English source strings, values are empty. Fill every value with the Russian translation. Do not change, add or remove keys.
- Markers like `<1>…</1>`, `<2/>` stand for links, bold text, line breaks etc. Keep every marker from the source, exactly once each, with the same numbers, wrapping the matching Russian words (you may move them to fit Russian word order). Never invent new markers.
- Text is HTML-escaped: write `&amp;` for &, never a bare `&`. Keep `&lt;` / `&gt;` if present.
- If a string should stay the same in Russian (an email address, «NATALIA ZUTE», «£485»), copy it unchanged as the value.
- Use typographic apostrophes/quotes as in Russian; no straight double quotes inside values unless escaped for JSON.
