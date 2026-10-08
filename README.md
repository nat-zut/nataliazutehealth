# Natalia Zute Health website

Built from the approved designs ("Website Design v1", 6 Oct 2026). Plain HTML, no build step.

## Pages
index.html (home), about.html, work-with-me.html, contact.html, free-guide.html,
thank-you.html, booked.html, 404.html, terms.html, privacy.html, cookies.html,
blog.html and articles: bloated-in-the-afternoon.html, tired-all-the-time.html, food-and-symptom-diary.html

## Still to connect before launch
- Free guide sign-up forms (home and free-guide.html): MailerLite embedded form. For now they go straight to thank-you.html and send nothing.
- Booking calendar on contact.html: Google Calendar booking page (Free fit call) embedded since 8 Oct, replacing Cal.com. Workspace Business Starter allows one booking page, so paid sessions start with a free call for now; add more booking pages after upgrading to Business Standard.
- Founding places left: change LEFT in founding.js (one number updates every page; at 0 the founding bar, pill, band and booking option disappear).
- Contact message form on contact.html: a form tool. For now it sends nothing.
- Payments: Stripe (with the customer portal turned on, so clients can manage 3 monthly payments online).
- Legal pages: remove the "Draft, not yet live" boxes once checked, and fill the dashed placeholders (business address, video service, questionnaire tool, retention period, governing law).
- Remove `<meta name="robots" content="noindex, nofollow">` from every page on launch day, so Google can list the site.
- Custom domain nataliazutehealth.com: Settings > Pages > Custom domain.
- SEO: when the domain is live, change https://nataliazutehealth.com/ to https://nataliazutehealth.com/ in canonical links, structured data, sitemap.xml and robots.txt, then submit sitemap.xml in Google Search Console.
