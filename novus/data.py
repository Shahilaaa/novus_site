"""
Static data ported 1:1 from the <script type="text/x-dc"> block in
'NOVUS Fest Redesign.dc.html'. No wording, numbers, or images were changed —
only the asset paths were rewritten to point at Django's static files
(novus/static/novus/assets/...) instead of the bare 'assets/...' paths used
by the design tool.
"""

GREEN = "#8eff01"
PURPLE = "#8b53fe"

EVENTS = [
    {
        "id": 1, "title": "Cyber Punch", "subtitle": "Coding Competition", "category": "Coding",
        "day": 1, "date": "Sept 3", "start": "10:00", "end": "", "venue": "Data Science Lab",
        "duration": "3 phases", "prize": "₹2000", "prize2": "₹1000", "fee": "₹30",
        "team_size": "Individual event", "registered": 28, "cap": 50, "spot": False,
        "form": "https://docs.google.com/forms/d/e/1FAIpQLScZ5AKRTohd_r9FJ9QiijN5oFDVjUp9bJppb1dK9VJUNcEV-w/viewform",
        "poster": "novus/assets/cyberpunch-poster-v2.jpg", "rules_img": "novus/assets/cyberpunch-rules-v2.jpg",
        "short": "Three timed phases — dry running, debugging and a final coding sprint.",
        "description": "A three-phase coding competition. Participants clear a dry-running round, then a debugging round, and the survivors face a final coding sprint. Open to college students from any stream, conducted as an individual event.",
        "phases": [
            {"name": "Phase 1: Dry Running", "items": ["No. of Question: 2", "Time Limit: 10 mins", "First 25 participants will move onto the next round. In case 25 participants do not complete, only the students who completed can move onto the next round."]},
            {"name": "Phase 2: Code Debugging", "items": ["No. of Question: 1", "Time Limit: 20 mins", "First 15 participants will move onto the next round. In case 15 participants do not complete, only the students who completed can move onto the next round."]},
            {"name": "Phase 3: Coding", "items": ["No. Of Question: 1", "Time Limit: 30 mins", "First participant who completes the code without errors will be declared the winner. In case of same time submission, code efficiency will be taken into consideration"]},
        ],
        "rules": ["The competition is open to college students from any stream and will be conducted as an individual event with no group entries.", "The competition will be conducted offline, and the use of external AI assistance is strictly prohibited; any such use will result in disqualification.", "All participants must arrive at the venue 30 minutes before the event starts.", "The decision of the committee members shall be final.", "Each participant may register for only one event; participation in multiple events is not allowed."],
        "requirements": ["Valid college ID", "Arrive 30 minutes early"],
        "faculty": "Ms. Ancy E.A", "coord_name": "Sakthiprasad Chandran & Neeraj E",
        "coord_email": "stc.novus@gmail.com", "coord_phone": "9497065334 · 9400723726",
    },
    {
        "id": 2, "title": "Data Hunt", "subtitle": "A Next-Gen Treasure Hunt", "category": "Hunt",
        "day": 1, "date": "Sept 3", "start": "11:00", "end": "", "venue": "St. Thomas College (Autonomous), Thrissur",
        "duration": "3 levels", "prize": "₹2000", "prize2": "", "fee": "₹100",
        "team_size": "Team of 2 or 3", "registered": 14, "cap": 20, "spot": True, "form": "",
        "poster": "novus/assets/datahunt-poster-v2.jpg", "rules_img": "novus/assets/datahunt-rules-v2.jpg",
        "short": "Three levels of clue-solving across campus. Top team from level 3 wins.",
        "description": "A next-gen treasure hunt run across three levels. Teams of two or three solve their way through each level, with only the strongest teams advancing.",
        "phases": [
            {"name": "Level progression", "items": ["Only the top 10 teams from level 1 can pass to level 2", "Only the top 5 teams from level 2 can pass to level 3", "The top 1 among the 5 teams from level 3 will be the winner"]},
        ],
        "rules": ["A team of 2 or 3 persons can register for the event", "A maximum of 20 teams is allowed to register", "Students from colleges can only participate in the event", "The participants should bring their ID Cards", "The event will be conducted as a total of 3 levels", "All participants must arrive at the venue 30 minutes before the event starts", "Registration Fee : 100/- per team", "Prize Pool : 2000/-", "Registration is available only through spot registration; online registration is not available.", "Each participant may register for only one event; participation in multiple events is not allowed."],
        "requirements": ["College ID card", "Team of 2 or 3"],
        "faculty": "Mr. Rejin Varghese", "coord_name": "Jagannath J & Sreehari S",
        "coord_email": "stc.novus@gmail.com", "coord_phone": "9497893455 · 9074387738",
    },
    {
        "id": 3, "title": "Clash of Minds", "subtitle": "Quiz Competition", "category": "Quiz",
        "day": 1, "date": "Sept 3", "start": "10:00", "end": "", "venue": "STC Room No. AC 322",
        "duration": "5 rounds", "prize": "₹2000", "prize2": "₹1000", "fee": "₹30",
        "team_size": "Team of 2", "registered": 18, "cap": 25, "spot": False,
        "form": "https://docs.google.com/forms/d/e/1FAIpQLSdAcSQX-c4ktgnm_P3GIsrPUwOvD7u2MdbIOyRcUQBXF9tVng/viewform",
        "poster": "novus/assets/clash-poster-v2.jpg", "rules_img": "novus/assets/clash-rules-v2.jpg",
        "short": "Computer Science, Data Science and Mathematics across five rounds.",
        "description": "A quiz covering Computer Science, Data Science and Mathematics, played by teams of two across five distinct rounds. Conducted offline, with instructions issued after registration.",
        "phases": [
            {"name": "Registration slots", "items": ["15 online registration slots", "10 offline / spot registration slots", "₹30 per team"]},
        ],
        "rules": ["The quiz covers Computer Science, Data Science, and Mathematics, with participation restricted to teams of 2 members.", "Registration fee: ₹30 per team. Online, offline, and spot registrations are available, with 15 online registration slots and 10 offline/spot registration slots.", "The quiz will be conducted offline and will consist of five distinct rounds. Further instructions will be provided after registration.", "The decision of the committee members and Quiz Master shall be final.", "The winning team will receive a cash prize of ₹2,000, while the runners-up will receive ₹1,000.", "All participants must arrive at the venue 30 minutes before the event starts", "Each participant may register for only one event; participation in multiple events is not allowed."],
        "requirements": ["Team of 2 members", "Valid college ID"],
        "faculty": "Mrs. Sonia V.V", "coord_name": "Mithra Praseed & Athulkrishna T.B",
        "coord_email": "stc.novus@gmail.com", "coord_phone": "8590394408 · 9747724793",
    },
    {
        "id": 4, "title": "Brain Race", "subtitle": "Aptitude Test Competition", "category": "Quiz",
        "day": 1, "date": "Sept 3", "start": "10:00", "end": "", "venue": "STC Room No. AC 323",
        "duration": "3 levels", "prize": "₹2000", "prize2": "₹1000", "fee": "₹30",
        "team_size": "Individual entries", "registered": 34, "cap": 50, "spot": False,
        "form": "https://docs.google.com/forms/d/e/1FAIpQLSf69N29FqzrXxJA1pv4HYHvioY517yQFgWKIK0M7g25PeOorw/viewform",
        "poster": "novus/assets/brainrace-poster-v2.jpg", "rules_img": "novus/assets/brainrace-rules-v3.jpg",
        "short": "Preliminary, advance and expert levels with buzzer finals.",
        "description": "An aptitude competition in three levels — preliminary, advance and expert — narrowing to a buzzer final. Open to UG, PG and Engineering students as individual entries.",
        "phases": [
            {"name": "Preliminary Level", "items": ["The round consists of 35 basic aptitude questions for a total of 35 marks, with a duration of 30 minutes. Each correct answer carries 1 mark, while each wrong answer carries a negative marking of 0.25 marks", "The top 20% of contestants will be selected for the next round"]},
            {"name": "Advance Level", "items": ["The round consists of 20 questions (15 advanced aptitude and 5 data science questions) for a total of 20 marks, with a duration of 20 minutes. Each correct answer carries 1 mark, while each wrong answer carries a negative marking of 0.25 marks.", "The top 6 contestants will be selected for the final round"]},
            {"name": "Expert Level 1: Pass or perish", "items": ["The round consists of 6 questions, each carrying 5 marks, with a time limit of 2 minute per question. If a contestant fails to answer, the question will be passed to other contestants through buzzer selection, with the passed question carrying 3 marks."]},
            {"name": "Expert Level 2: Final strike", "items": ["The buzzer round consists of 4 questions for a total of 60 marks, with 3 minutes allotted per question. The fastest contestant to answer earns 10 marks for a correct answer, while a wrong answer carries a penalty of 5 marks."]},
        ],
        "rules": ["The competition is open to college students (UG, PG, and Engineering), with individual entries only.", "Registration fee: ₹30.", "Participants must register before the due date; spot registrations are also allowed.", "The competition will be conducted offline, with 35 online registration slots and 15 offline/spot registration slots.", "The decision of the committee members shall be final.", "All participants must arrive at the venue 30 minutes before the event starts", "Each participant may register for only one event; participation in multiple events is not allowed."],
        "requirements": ["Pen and valid college ID", "Individual entry"],
        "faculty": "Mrs. Sreelekha K", "coord_name": "Akshaya S & Muhammed Shaban V.P",
        "coord_email": "stc.novus@gmail.com", "coord_phone": "6238629917 · 8606924541",
    },
    {
        "id": 5, "title": "Shadapadeyy", "subtitle": "WPM · Words Per Minute", "category": "Typing",
        "day": 1, "date": "Sept 3", "start": "10:30", "end": "", "venue": "STC Room No. AC-317",
        "duration": "4 levels · 90s each", "prize": "Keyboard", "prize2": "Mouse", "fee": "₹30",
        "team_size": "Individual entries", "registered": 9, "cap": 20, "spot": False,
        "form": "https://docs.google.com/forms/d/e/1FAIpQLSfg7rVAWt_gu4-1W1gx-OgFzKY4cepcnxEpa87vhgSLOPd8Fw/viewform",
        "poster": "novus/assets/vasnes-poster-v2.jpg", "rules_img": "novus/assets/vasnes-rules-v2.jpg",
        "short": "90 seconds. Type fast. Type right. Win.",
        "description": "A speed-typing contest over four levels of 90 seconds each. Twenty participants start together on the Admin's signal and the field narrows every round until a final ranking is set on net WPM.",
        "phases": [
            {"name": "Format", "items": ["20 participants compete across 4 levels, with 90 seconds per level. Everyone starts together on the Admin's signal."]},
            {"name": "Elimination", "items": ["20 → 15 → 10 → 5 → Final Ranking across Levels 1–4."]},
            {"name": "Scoring", "items": ["Net WPM is the main ranking factor. Ties are decided by Accuracy → Correct Characters → Fewer Errors → Completion Time. WPM and Accuracy are recorded after every round.", "After each level, WPM, Accuracy, Rank, and Qualification Status will be displayed."]},
        ],
        "rules": ["Typing Rules: Manually type the given passage; Backspace is allowed, self-starting is prohibited, and the test ends automatically after 90 seconds.", "All participants must arrive 30 minutes before the event starts.", "The decision of the committee members shall be final and binding.", "Each participant may register for only one event; participation in multiple events is not allowed."],
        "requirements": ["Valid college ID", "Arrive 30 minutes early"],
        "faculty": "Mr. Alan Jose", "coord_name": "Yaseen V.S, Rafna K.R & Ashwin Joy",
        "coord_email": "stc.novus@gmail.com", "coord_phone": "9061895540 · 7012727123",
    },
    {
        "id": 6, "title": "Lock & Load", "subtitle": "Mini Militia Tournament", "category": "Gaming",
        "day": 1, "date": "Sept 3", "start": "10:00", "end": "", "venue": "STC Room No. AC 321",
        "duration": "6 min matches", "prize": "Gift Voucher", "prize2": "", "fee": "₹50",
        "team_size": "4 player team", "registered": 11, "cap": 16, "spot": True, "form": "",
        "poster": "novus/assets/lockload-poster-v2.jpg", "rules_img": "novus/assets/lockload-rules-v2.jpg",
        "short": "Mini Militia Classic knockout — 4 players a team, 16 teams maximum.",
        "description": "A Mini Militia Classic tournament played on the Outpost map with four players per team. Maximum 16 teams on a first-come, first-served basis, spot registration only.",
        "phases": [
            {"name": "Match format", "items": ["Each match will last 6 minutes on the Outpost map", "Players must report 15 minutes before their match; late teams may forfeit", "Maximum 16 teams, first-come first-served"]},
        ],
        "rules": ["The tournament will be played using Mini Militia Classic from the Google Play Store/App Store, with 4 players per team and a maximum of 16 teams on a first-come, first-served basis. Spot registration only; no reservations are allowed.", "College ID is mandatory during registration and throughout the tournament, and teams may include players from different colleges.", "Each match will last 6 minutes on the Outpost map. Players must report 15 minutes before their match; late teams may forfeit. Players must use their own devices, connect to the official tournament network, and are responsible for individual connection issues.", "No substitutions are allowed after the tournament begins unless approved by the organizer. Only the official host may create matches, unauthorized rooms are prohibited, and all players must confirm readiness before the match starts.", "Sniper and Shield are prohibited. Modified APKs, hacks, cheats, third-party software, and outside assistance are strictly prohibited; their use will result in immediate team disqualification.", "Matches will be restarted only for host or multiplayer technical issues. Individual disconnections, low battery, calls, notifications, internet issues, or device faults are not grounds for a rematch and remain the player's responsibility.", "The decision of the committee members is final, and objections must be raised immediately after the match. Participants must maintain fair play, respect, and sportsmanship; abusive language, harassment, or unsportsmanlike conduct may result in a warning or disqualification.", "The tournament conductor's decision is final and binding, and the organizers reserve the right to modify the schedule or rules if necessary.", "Registration is available only through spot registration; online registration is not available.", "Each participant may register for only one event; participation in multiple events is not allowed."],
        "requirements": ["Own device with Mini Militia Classic", "College ID", "Team of 4 players"],
        "faculty": "Mrs. Jeeshma Jaison", "coord_name": "Roshan K.D & Helbin Joshy P",
        "coord_email": "stc.novus@gmail.com", "coord_phone": "9847237624 · 9539935471",
    },
]

REGISTRATIONS = [

]

CAT_ACCENT = {"Coding": GREEN, "Hunt": PURPLE, "Quiz": GREEN, "Typing": PURPLE, "Gaming": GREEN}

ORGANIZERS = [
    {"name": "MR. REJIN VARGHESE", "role": "HOD"},
    {"name": "MRS. JEESHMA \nJAISON", "role": "FACULTY\n\nCOORDINATOR"},
    {"name": "BEWIN K BOBAN", "role": "STUDENT COORDINATORS"},
    {"name": "\nLAKSHMI GAYATHRY ", "role": "STUDENT COORDINATORS\n"},
]

RULES = [
    "All participants must carry valid college ID cards",
    "Registration is mandatory for all events",
    "Participants must reach venues 15 minutes before event time",
    "Decision of judges will be final",
    "Code of conduct must be maintained throughout",
    "No refunds after registration",
]

TIMELINE = [
    {"day": "09:30", "date": "REPORTING", "events": "Registration desk opens — all participants report 30 minutes before their event"},
    {"day": "10:00", "date": "FIRST BLOCK", "events": "Cyber Punch (Data Science Lab), Clash of Minds (AC 322) and Brain Race (AC 323)"},
    {"day": "11:00", "date": "DATA HUNT", "events": "Data Hunt begins across the campus"},
    {"day": "11:30", "date": "SECOND BLOCK", "events": "Shadapadeyy (AC-317) and Lock & Load (AC 321)"},
    {"day": "LATER", "date": "PRIZE DISTRIBUTION", "events": "Results, prize distribution and closing address"},
]

_SPONSOR_LOGOS_RAW = [
    {"name": "Chungath Jewellery", "logo": "novus/assets/sponsor-chungath.png"},
    {"name": "Josco Jewellers", "logo": "novus/assets/sponsor-josco.png"},
    {"name": "Miya Convention Center", "logo": "novus/assets/sponsor-miya-v2.png", "dark": True},
    {"name": "Spanish Absolute", "logo": "novus/assets/sponsor-spanish-absolute-v2.png", "dark": True},
    {"name": "Queen Designo", "logo": "novus/assets/sponsor-queen-designo.png", "dark": True},
    {"name": "CX Gaming", "logo": "novus/assets/sponsor-cx-v2.png"},
    {"name": "T&T", "logo": "novus/assets/sponsor-tandt.png"},
]

SPONSOR_CARDS = [
    {"name": "Chungath Jewellery", "badge": "SPONSOR", "logo": "novus/assets/sponsor-chungath.png", "main": True},
    {"name": "Josco Jewellers", "badge": "SPONSOR", "logo": "novus/assets/sponsor-josco.png", "main": True},
    {"name": "Miya Convention Center", "badge": "SPONSOR", "logo": "novus/assets/sponsor-miya-v2.png", "dark": True, "main": True},
    {"name": "Spanish Absolute", "badge": "SPONSOR", "logo": "novus/assets/sponsor-spanish-absolute-v2.png", "dark": True, "main": True},
    {"name": "Queen Designo", "badge": "SPONSOR", "logo": "novus/assets/sponsor-queen-designo.png", "dark": True, "main": True},
    {"name": "CX Gaming", "badge": "SPONSOR", "logo": "novus/assets/sponsor-cx-v2.png", "main": True},
    {"name": "T&T", "badge": "SPONSOR", "logo": "novus/assets/sponsor-tandt.png", "main": True},
]

THEME_FIELDS = [
    {"label": "LOGO TEXT", "value": "NOVUS"},
    {"label": "PRIMARY COLOR", "value": "#8EFF01"},
    {"label": "SECONDARY COLOR", "value": "#8B53FE"},
    {"label": "HEADING FONT", "value": "Chakra Petch"},
    {"label": "BODY FONT", "value": "Space Grotesk"},
    {"label": "SPONSORS TITLE", "value": "Our Sponsors"},
]

EVENT_FORM_FIELDS = [
    "TITLE", "CATEGORY", "DATE", "DAY", "START TIME", "END TIME", "VENUE",
    "DURATION", "TEAM SIZE", "FIRST PRIZE", "SECOND PRIZE", "REGISTRATION FEE",
    "MAX PARTICIPANTS", "IMAGE URL",
]

REG_NOTES = [
    "Registration for Cyber Punch, Clash of Minds, Brain Race and Shadapadeyy is through each event's Google Form — one form submission per participant or team.",
    "Data Hunt and Lock & Load take spot registration only, at the venue on September 3.",
    "Carry your college ID; it is checked at registration and throughout the event.",
    "All participants must arrive at the venue 30 minutes before their event starts.",
    "Fees are collected at the registration desk on the day of the fest.",
]

NAV_ITEMS = [
    ("home", "Home", "novus:home"),
    ("about", "About", "novus:about"),
    ("events", "Events", "novus:events"),
    ("register", "Register", "novus:register"),
]
