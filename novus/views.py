from django.shortcuts import render, redirect
from django.http import Http404

from . import data
from . import logic

CATEGORIES = ["All"] + sorted({e["category"] for e in data.EVENTS})


def _nav(request):
    active = request.resolver_match.url_name if request.resolver_match else ""
    items = []
    for key, label, url_name in data.NAV_ITEMS:
        is_active = active == key or (key == "events" and active == "event_detail")
        style = (
            "padding:9px 16px;border-radius:10px;background:rgba(142,255,1,.12);"
            "border:1px solid rgba(142,255,1,.35);color:#8eff01;font-family:'JetBrains Mono',monospace;"
            "font-size:11px;letter-spacing:.16em;text-transform:uppercase;cursor:pointer"
            if is_active else
            "padding:9px 16px;border-radius:10px;border:1px solid transparent;color:#9aa2b0;"
            "font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.16em;"
            "text-transform:uppercase;cursor:pointer"
        )
        items.append({"key": key, "label": label, "url_name": url_name, "style": style})
    return items


def home(request):
    decorated = logic.decorated_events()
    context = {
        "nav": _nav(request),
        "hero_style": (
            "position:relative;border-radius:28px;overflow:hidden;"
            "background:linear-gradient(122deg,#8eff01 0%,#8eff01 26%,#8b53fe 78%);"
            "box-shadow:0 30px 90px -30px rgba(139,83,254,.55)"
        ),
        "featured": decorated[:3],
        "sponsors": logic.sponsors_home(),
    }
    return render(request, "novus/home.html", context)


def about(request):
    context = {
        "nav": _nav(request),
        "organizers": data.ORGANIZERS,
        "rules": data.RULES,
    }
    return render(request, "novus/about.html", context)


def events(request):
    q = request.GET.get("q", "").strip()
    cat = request.GET.get("cat", "All")
    sort = request.GET.get("sort", "time")
    full_id = request.GET.get("full")

    decorated = logic.decorated_events()

    visible = [
        e for e in decorated
        if (cat == "All" or e["category"] == cat)
        and (not q or q.lower() in (e["title"] + " " + e["description"]).lower())
    ]
    if sort == "popularity":
        visible.sort(key=lambda e: e["registered"], reverse=True)
    elif sort == "prize":
        def prize_num(e):
            digits = "".join(ch for ch in e["prize"] if ch.isdigit())
            return int(digits) if digits else 0
        visible.sort(key=prize_num, reverse=True)
    else:
        visible.sort(key=lambda e: (e["day"], logic.to_min(e["start"])))

    categories = [
        {"label": c, "cat": c, "style": logic.pill_style(cat == c, data.GREEN)}
        for c in CATEGORIES
    ]
    sorts = [
        {"key": "time", "label": "Time", "style": logic.pill_style(sort == "time", data.PURPLE)},
        {"key": "popularity", "label": "Popular", "style": logic.pill_style(sort == "popularity", data.PURPLE)},
        {"key": "prize", "label": "Prize", "style": logic.pill_style(sort == "prize", data.PURPLE)},
    ]

    full_event = None
    if full_id:
        full_event = next((e for e in decorated if str(e["id"]) == str(full_id)), None)

    context = {
        "nav": _nav(request),
        "query": q,
        "categories": categories,
        "sorts": sorts,
        "current_cat": cat,
        "current_sort": sort,
        "result_label": f"{len(visible)} EVENT{'' if len(visible) == 1 else 'S'} FOUND",
        "visible_events": visible,
        "full_event": full_event,
    }
    return render(request, "novus/events.html", context)


def event_detail(request, event_id):
    decorated = logic.decorated_events()
    current = next((e for e in decorated if e["id"] == event_id), None)
    if current is None:
        raise Http404("Event not found")
    related = [e for e in decorated if e["category"] == current["category"] and e["id"] != current["id"]][:3]
    context = {
        "nav": _nav(request),
        "current": current,
        "related": related,
    }
    return render(request, "novus/event_detail.html", context)


def register(request):
    decorated = logic.decorated_events()
    reg_cards = []
    for e in decorated:
        card_style = (
            "border-radius:22px;border:1px solid rgba(139,83,254,.30);background:linear-gradient(120deg,rgba(139,83,254,.10),rgba(10,12,18,0) 60%),#0a0c12;padding:26px 28px"
            if e["spot"] else
            "border-radius:22px;border:1px solid rgba(255,255,255,.08);background:#0a0c12;padding:26px 28px"
        )
        mode_style = (
            "padding:5px 11px;border-radius:99px;background:#8b53fe;color:#0b0714;font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.14em;font-weight:700;white-space:nowrap"
            if e["spot"] else
            "padding:5px 11px;border-radius:99px;background:rgba(142,255,1,.14);border:1px solid rgba(142,255,1,.4);color:#8eff01;font-family:'JetBrains Mono',monospace;font-size:9px;letter-spacing:.14em;white-space:nowrap"
        )
        spot_note = (
            "Registration is available only through spot registration. Teams of 2 or 3 sign up at the desk on the day — maximum 20 teams, ₹100 per team, first come first served."
            if e["id"] == 2 else
            "Spot registration only; no reservations are allowed. Maximum 16 teams of 4 players on a first-come, first-served basis. College ID mandatory at registration."
        )
        reg_cards.append({**e, "card_style": card_style, "mode_style": mode_style, "spot_note": spot_note})

    context = {
        "nav": _nav(request),
        "reg_cards": reg_cards,
        "reg_notes": data.REG_NOTES,
    }
    return render(request, "novus/register.html", context)


def admin_login(request):
    if request.method == "POST":
        # Original mock had no real credential check either — clicking Sign in just navigated.
        request.session["is_admin"] = True
        return redirect("novus:dashboard")
    return render(request, "novus/login.html", {"nav": _nav(request)})


def admin_logout(request):
    request.session.pop("is_admin", None)
    return redirect("novus:home")


def dashboard(request):
    if not request.session.get("is_admin"):
        return redirect("novus:admin_login")

    tab = request.GET.get("tab", "events")
    tabs = []
    for key, label in [("events", "Events"), ("registrations", "Registrations"),
                        ("sponsors", "Sponsors"), ("theme", "Theme")]:
        active = tab == key
        style = (
            "padding:11px 20px;border-radius:12px;background:rgba(139,83,254,.16);"
            "border:1px solid rgba(139,83,254,.42);color:#c3a6ff;font-family:'JetBrains Mono',monospace;"
            "font-size:11px;letter-spacing:.16em;text-transform:uppercase;cursor:pointer"
            if active else
            "padding:11px 20px;border-radius:12px;border:1px solid rgba(255,255,255,.08);color:#9aa2b0;"
            "font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.16em;"
            "text-transform:uppercase;cursor:pointer"
        )
        tabs.append({"key": key, "label": label, "style": style})

    reg_filter = request.GET.get("regFilter", "All")
    reg_filters = []
    for c in ["All", "Coding", "Hunt", "Quiz", "Typing", "Gaming"]:
        reg_filters.append({"label": c, "style": logic.pill_style(reg_filter == c, data.PURPLE)})

    context = {
        "nav": _nav(request),
        "tab": tab,
        "tabs": tabs,
        "all_events": logic.decorated_events(),
        "event_form_fields": data.EVENT_FORM_FIELDS,
        "reg_filters": reg_filters,
        "reg_filter": reg_filter,
        "registrations": data.REGISTRATIONS,
        "sponsor_cards": logic.sponsor_cards_dashboard(),
        "theme_fields": data.THEME_FIELDS,
    }
    return render(request, "novus/dashboard.html", context)
