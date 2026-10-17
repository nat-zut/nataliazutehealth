/* Free diary sign-up: sends the form to MailerLite, then opens the thank-you page.
   Everyone joins the Diary group for their language (so the diary email goes out).
   Only people who tick the email box also join the Newsletter group. */
(function () {
  var ML = "https://assets.mailerlite.com/jsonp/2719080/forms/";
  var CFG = {
    en: { form: "201525118405444666", diary: "201525026818623056", news: "201525055575820054",
          sending: "Sending…", error: "Sorry, that didn't go through. Please check your email address and try again, or write to hello@nataliazutehealth.com." },
    ru: { form: "201525348693706476", diary: "201525042061772186", news: "201525059301409837",
          sending: "Отправляем…", error: "Не получилось отправить. Проверьте адрес электронной почты и попробуйте ещё раз или напишите на hello@nataliazutehealth.com." }
  };
  var lang = (document.documentElement.lang || "en").slice(0, 2) === "ru" ? "ru" : "en";
  var c = CFG[lang];

  function wire(form) {
    var email = form.querySelector('input[type="email"]');
    var name = form.querySelector('input[autocomplete="given-name"]');
    var focus = form.querySelector("select");
    var consent = form.querySelector('input[type="checkbox"]');
    var btn = form.querySelector('button[type="submit"]');
    if (!email) return;
    email.required = true;
    var msg = document.createElement("p");
    msg.setAttribute("role", "alert");
    msg.style.cssText = "margin:0;font-size:15px;line-height:1.5;color:#9C4F1E;display:none";
    form.appendChild(msg);

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!email.value || !email.checkValidity()) { email.reportValidity(); return; }
      var data = new FormData();
      data.append("fields[email]", email.value.trim());
      if (name && name.value.trim()) data.append("fields[name]", name.value.trim());
      if (focus && focus.value) data.append("fields[focus]", focus.value);
      data.append("groups[]", c.diary);
      if (consent && consent.checked) data.append("groups[]", c.news);
      data.append("ml-submit", "1");
      data.append("anticsrf", "true");
      var label = btn ? btn.textContent : "";
      if (btn) { btn.disabled = true; btn.textContent = c.sending; }
      msg.style.display = "none";

      function done() { window.location.href = form.getAttribute("action") || "thank-you.html"; }
      function fail() {
        if (btn) { btn.disabled = false; btn.textContent = label; }
        msg.textContent = c.error; msg.style.display = "block";
      }
      fetch(ML + c.form + "/subscribe", { method: "POST", body: data })
        .then(function (r) { return r.json().catch(function () { return { success: r.ok }; }); })
        .then(function (j) { if (j && j.success === false) fail(); else done(); })
        .catch(function () {
          // Some browsers block reading the reply; send again without reading it.
          fetch(ML + c.form + "/subscribe", { method: "POST", body: data, mode: "no-cors" }).then(done, fail);
        });
    });
  }
  document.querySelectorAll("form[data-signup]").forEach(wire);
})();
