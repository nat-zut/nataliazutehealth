/* Founding client places: the one number to change.
   When a founding place is taken, lower LEFT by 1. Every page updates itself. */
(function () {
  var TOTAL = 5;
  var LEFT = 5;

  function places(n) { return n === 1 ? 'place' : 'places'; }
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
    set('bar', full ? TOTAL + ' founding client places at about half price'
                    : 'Only ' + n + ' founding ' + places(n) + ' left, at about half price');
    set('pill', full ? TOTAL + ' founding places' : 'Only ' + n + ' founding ' + places(n) + ' left,');
    set('left', n + ' of ' + TOTAL + ' places left');
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', run); else run();
})();
