from .data import EVENTS, CAT_ACCENT, GREEN, PURPLE, _SPONSOR_LOGOS_RAW, SPONSOR_CARDS


def to_min(t):
    if not t:
        return 0
    h, m = t.split(":")
    return int(h) * 60 + int(m)


def chip_style(category):
    c = CAT_ACCENT.get(category, GREEN)
    bg = "rgba(142,255,1,.14)" if c == GREEN else "rgba(139,83,254,.18)"
    return (
        f"padding:5px 11px;border-radius:99px;background:{bg};border:1px solid {c}44;"
        f"color:{c};font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:.14em;"
        f"text-transform:uppercase;white-space:nowrap"
    )


def pill_style(active, accent=None):
    c = accent or GREEN
    if active:
        return (
            f"padding:10px 18px;border-radius:99px;background:{c};color:#07080c;"
            f"font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.14em;"
            f"text-transform:uppercase;cursor:pointer;font-weight:700;box-shadow:0 0 22px {c}55"
        )
    return (
        "padding:10px 18px;border-radius:99px;background:rgba(255,255,255,.04);"
        "border:1px solid rgba(255,255,255,.10);color:#a3aab7;font-family:'JetBrains Mono',monospace;"
        "font-size:11px;letter-spacing:.14em;text-transform:uppercase;cursor:pointer"
    )


def decorate(ev):
    """Port of Component.decorate(ev)."""
    d = dict(ev)
    d["start_time"] = ev["start"]
    d["end_time"] = ev["end"]
    d["spot_label"] = "SPOT REGISTRATION" if ev["spot"] else ""
    d["has_form"] = bool(ev["form"])
    d["reg_mode_label"] = "ONLINE FORM" if ev["form"] else "SPOT REGISTRATION ONLY"
    d["time_line"] = f"{ev['start']} AM"
    d["is_full"] = ev["registered"] >= ev["cap"]
    d["chip_style"] = chip_style(ev["category"])
    d["date_line"] = f"{ev['date']}, 2026 · {ev['start']} AM"
    d["prize1_label"] = ev["prize"]
    d["prize2_label"] = ev["prize2"] or "—"
    d["has_prize2"] = bool(ev["prize2"])
    d["fee_label"] = ev["fee"]
    d["reg_line"] = f"{ev['registered']}/{ev['cap']}"
    d["seats_line"] = (
        "Registrations closed — event full"
        if ev["registered"] >= ev["cap"]
        else f"{ev['cap'] - ev['registered']} seats left"
    )
    d["cap_line"] = f"{ev['registered']} / {ev['cap']}"
    pct = round(ev["registered"] / ev["cap"] * 100) if ev["cap"] else 0
    d["bar_style"] = (
        f"height:100%;width:{pct}%;border-radius:99px;background:linear-gradient(90deg,{GREEN},{PURPLE})"
    )
    return d


def decorated_events():
    return [decorate(e) for e in EVENTS]


def sponsors_home():
    """Port of the 'sponsors' list built with .map(x => ({...cardStyle/logoStyle})) for the home page strip."""
    out = []
    for x in _SPONSOR_LOGOS_RAW:
        dark = x.get("dark")
        card_style = (
            "flex:0 1 210px;padding:6px;border-radius:14px;border:1px solid rgba(255,255,255,.14);"
            "background:#0b0b0d;display:flex;align-items:center;justify-content:center;min-height:96px;overflow:hidden"
            if dark else
            "flex:0 1 210px;padding:14px 18px;border-radius:14px;border:1px solid rgba(255,255,255,.10);"
            "background:#ffffff;display:flex;align-items:center;justify-content:center;min-height:96px"
        )
        logo_style = (
            "display:block;width:100%;height:84px;object-fit:contain"
            if dark else
            "display:block;max-width:100%;max-height:58px;object-fit:contain"
        )
        out.append({**x, "card_style": card_style, "logo_style": logo_style})
    return out


def sponsor_cards_dashboard():
    """Port of the 'sponsorCards' list used on the dashboard's Sponsors tab."""
    out = []
    for x in SPONSOR_CARDS:
        style = (
            "border-radius:18px;border:1px solid rgba(142,255,1,.32);background:rgba(142,255,1,.06);padding:24px"
            if x.get("main") else
            "border-radius:18px;border:1px solid rgba(255,255,255,.08);background:#0a0c12;padding:24px"
        )
        plate_style = (
            "height:92px;display:flex;align-items:center;justify-content:center;border-radius:12px;"
            "background:#0b0b0d;border:1px solid rgba(255,255,255,.14);padding:6px;margin-bottom:16px;overflow:hidden"
            if x.get("dark") else
            "height:92px;display:flex;align-items:center;justify-content:center;border-radius:12px;"
            "background:#ffffff;padding:10px;margin-bottom:16px"
        )
        out.append({**x, "style": style, "plate_style": plate_style})
    return out
