# NOVUS 3.0 Tech Fest — Django conversion

Django port of the latest `NOVUS Fest Redesign.dc.html` — rebranded to
"NOVUS 3.0 Tech Fest 2026" (updated hero title/tagline, "About NOVUS 3.0
Tech Fest" heading, and refreshed poster/rules photos for all 6 events).
Nothing in the design's content, wording, numbers, or images was changed —
only the visual builder's templating was converted to real Django views +
templates, same as previous versions of this project.

## What's included
- All 6 events (Cyber Punch, Data Hunt, Clash of Minds, Brain Race,
  Shadapadeyy, Lock & Load) with their full data and the newest
  poster/rules images from this source file.
- Every screen: Home, About, Events (search + category + sort via real
  query params), the "Full view" overlay, a dedicated event Detail page,
  Register (per-event Google Form / spot-registration cards), Login, and
  the admin Dashboard (Events / Registrations / Sponsors / Theme tabs).
- **Mobile-responsive layout** — CSS media queries (760px/520px
  breakpoints) reproduce the original design's window-width-driven mobile
  layout: tighter padding, single-column grids, a full-screen event
  overlay, and stacked/labeled dashboard tables on small screens.
- **Mobile gets a slide-out hamburger menu** (pure CSS, no JavaScript)
  instead of the desktop's plain horizontal nav bar — desktop is untouched.
- **Admin sign-in is not linked anywhere in the public site.** No "ADMIN"
  button anywhere a regular visitor can see. The login page still works,
  reachable only by visiting `/admin-login/` directly, and logs into
  `/dashboard/` the same way the original mock did (no real password check
  in the original design either).

## Structure
```
novus_fest_v3/
  novus_fest_v3/         settings.py, urls.py
  novus/
    data.py               EVENTS/REGISTRATIONS/sponsors/organizers/etc.
    logic.py              chip()/decorate()/pillStyle() + sponsor card styling
    views.py               one view per screen
    urls.py
    static/novus/assets/   event posters, rules images, sponsor logos
    templates/novus/       base.html + one template per screen
  requirements.txt
  manage.py
```

## Routes
- `/` home
- `/about/`
- `/events/` (`?q=`, `?cat=`, `?sort=time|popularity|prize`, `?full=<id>` for the full-view overlay)
- `/events/<id>/` — dedicated detail page
- `/register/` — per-event Google Form links / spot-registration notes
- `/admin-login/` (not linked anywhere in the UI — visit it directly) → `/dashboard/`
- `/dashboard/?tab=events|registrations|sponsors|theme`

## Deploying (e.g. to Vercel) — read this if images/CSS don't show up

Locally, `python manage.py runserver` auto-serves everything under
`novus/static/` for you — that's a dev-server-only convenience, and it's
why images work when you test locally but can go missing after deploying
anywhere else (Vercel, Render, etc.). Nothing was serving them in
production before; this version fixes that with
[WhiteNoise](https://whitenoise.readthedocs.io/), which serves static files
straight from inside the Django app itself, no separate host or CDN needed.

What's included for this:
- `whitenoise` added to `requirements.txt` and wired into
  `novus_fest_v3/settings.py` (`MIDDLEWARE` + `STORAGES`)
- `vercel.json` and `build_files.sh` — a standard Django-on-Vercel setup.
  The build step runs `python manage.py collectstatic`, which gathers every
  image/CSS file into `staticfiles/`; WhiteNoise then serves that folder
  through the app on every request.

If you deploy to Vercel and images are *still* missing:
1. Check the Vercel build logs for the `collectstatic` step — it should
   print something like "165 static files copied". If that step didn't run
   or errored, that's the problem.
2. Confirm `whitenoise` actually installed — check the build log's
   `pip install -r requirements.txt` output.
3. If you're deploying somewhere other than Vercel (Render, Railway, a VPS,
   etc.), you don't need `vercel.json`/`build_files.sh` — just run
   `python manage.py collectstatic` once as part of your deploy step; the
   WhiteNoise settings in `settings.py` work anywhere.


```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Then visit `http://127.0.0.1:8000/`. To reach the admin dashboard, go to
`http://127.0.0.1:8000/admin-login/` directly.

## Notes
- Dashboard's "+ Add event" / "Save event" / "+ Add sponsor" / EDIT / DEL /
  "Save theme" controls remain decorative (no click handler), same as the
  original design. The Registrations tab still shows the mock sample data
  from the design file — this project doesn't have an internal registration
  database, since the design routes registration out to Google Forms or
  in-person sign-up.
