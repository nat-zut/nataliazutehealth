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
        var dot = document.createElement('span'); dot.className = 'annsep'; dot.textContent = ' ';
        var w = document.createElement('span'); w.className = 'annwhen'; var w1 = document.createElement('span'); w1.className = 'annw1'; w1.textContent = when.charAt(0); w.appendChild(w1); w.appendChild(document.createTextNode(when.slice(1)));
        el.appendChild(dot); el.appendChild(w);
      }
    });
  }
  function style() {
    if (document.getElementById('annbar-style')) return;
    var st = document.createElement('style'); st.id = 'annbar-style';
    st.textContent = '@media (max-width:560px){.annsep{display:none}.annwhen::before{content:"\\A";white-space:pre}.annw1{text-transform:uppercase}}';
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
      if (full) setBar('Стартовая цена программ на\u00a049%\u00a0ниже будущей: ' + TOTAL + '\u00a0мест.', 'Сессии с\u00a012\u00a0января.');
      else setBar('Стартовая цена программ на\u00a049%\u00a0ниже будущей. Осталось ' + n + ' ' + mest(n) + '.');
      set('pill', full ? TOTAL + ' мест для первых клиенток' : 'Осталось ' + n + ' ' + mest(n) + ' для первых клиенток,');
      set('left', full ? TOTAL + '\u00a0мест' : 'Осталось ' + n + ' из ' + TOTAL + ' мест');
      return;
    }
    if (full) setBar('Introductory offer: ' + TOTAL + ' programme places at 49%\u00a0below\u00a0future\u00a0prices.', 'Sessions from 12\u00a0January.');
    else setBar('Introductory programme prices, 49% below future prices: ' + n + ' ' + places(n) + ' left.');
    set('pill', full ? TOTAL + ' founding places' : n + ' founding ' + places(n) + ' left,');
    set('left', full ? TOTAL + '\u00a0places' : n + ' of ' + TOTAL + ' places left');
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run); else run();
})();
