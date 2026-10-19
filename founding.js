/* Founding client places: the one number to change.
   When a founding place is taken, lower LEFT by 1. Every page (English and Russian) updates itself. */
(function () {
  var TOTAL = 5;
  var LEFT = 5;

  var ru = (document.documentElement.lang || '').toLowerCase().indexOf('ru') === 0;

  function places(n) { return n === 1 ? 'place' : 'places'; }
  function mest(n) {
    var a = n % 100, b = n % 10;
    if (a >= 11 && a <= 14) return 'мест';
    if (b === 1) return 'место';
    if (b >= 2 && b <= 4) return 'места';
    return 'мест';
  }
  function set(sel, text) {
    document.querySelectorAll('[data-f="' + sel + '"]').forEach(function (el) { el.textContent = text; });
  }
  function run() {
    var n = Math.max(0, Math.min(TOTAL, LEFT));
    if (n === 0) {
      document.querySelectorAll('[data-f-hide]').forEach(function (el) { el.hidden = true; el.style.display = 'none'; });
      document.querySelectorAll('option[value="founding"]').forEach(function (o) { o.remove(); });
      return;
    }
    var full = n === TOTAL;
    if (ru) {
      set('bar', full ? 'Специальная цена для первых ' + TOTAL + ' клиенток · сессии с 8 декабря'
                      : 'Специальная цена · осталось всего ' + n + ' ' + mest(n));
      set('pill', full ? TOTAL + ' мест для первых клиенток' : 'Осталось всего ' + n + ' ' + mest(n) + ' для первых клиенток,');
      set('left', full ? 'всего ' + TOTAL + ' мест' : 'осталось ' + n + ' из ' + TOTAL + ' мест');
      return;
    }
    set('bar', full ? 'Special price for my first ' + TOTAL + ' clients · sessions from 8 Dec'
                    : 'Special price · only ' + n + ' ' + places(n) + ' left');
    set('pill', full ? TOTAL + ' founding places' : 'Only ' + n + ' founding ' + places(n) + ' left,');
    set('left', full ? 'Only ' + TOTAL + ' places' : n + ' of ' + TOTAL + ' places left');
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run); else run();
})();
