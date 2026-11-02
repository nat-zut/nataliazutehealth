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
  function setBar(first, when) {
    document.querySelectorAll('[data-f="bar"]').forEach(function (el) {
      el.textContent = '';
      el.appendChild(document.createTextNode(first));
      if (when) {
        var dot = document.createElement('span'); dot.className = 'annsep'; dot.textContent = ' · ';
        var w = document.createElement('span'); w.className = 'annwhen'; w.textContent = when;
        el.appendChild(dot); el.appendChild(w);
      }
    });
  }
  function style() {
    if (document.getElementById('annbar-style')) return;
    var st = document.createElement('style'); st.id = 'annbar-style';
    st.textContent = '@media (max-width:560px){.annsep{display:none}.annwhen{display:block}.annwhen::first-letter{text-transform:uppercase}html[lang^=ru] .annbar>span:first-child{display:block;margin:0 0 2px!important}}';
    document.head.appendChild(st);
  }
  function run() {
    style();
    var n = Math.max(0, Math.min(TOTAL, LEFT));
    if (n === 0) {
      document.querySelectorAll('[data-f-hide]').forEach(function (el) { el.hidden = true; el.style.display = 'none'; });
      document.querySelectorAll('option[value="founding"]').forEach(function (o) { o.remove(); });
      return;
    }
    var full = n === TOTAL;
    if (ru) {
      if (full) setBar('Специальная цена для первых ' + TOTAL + ' клиенток', 'сессии с 8 января');
      else setBar('Специальная цена · осталось всего ' + n + ' ' + mest(n));
      set('pill', full ? TOTAL + ' мест для первых клиенток' : 'Осталось всего ' + n + ' ' + mest(n) + ' для первых клиенток,');
      set('left', full ? 'Всего ' + TOTAL + ' мест' : 'Осталось ' + n + ' из ' + TOTAL + ' мест');
      return;
    }
    if (full) setBar('Special price for my first ' + TOTAL + ' clients', 'sessions from 8 Jan');
    else setBar('Special price · only ' + n + ' ' + places(n) + ' left');
    set('pill', full ? TOTAL + ' founding places' : 'Only ' + n + ' founding ' + places(n) + ' left,');
    set('left', full ? 'Only ' + TOTAL + ' places' : n + ' of ' + TOTAL + ' places left');
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run); else run();
})();
