"""
build_quran_data.py
Fetches all 114 surahs from quran.com API v4 (word-by-word data)
and regenerates data/quran_data.py with full injection-ready structure.

Run once:  python build_quran_data.py
"""

import urllib.request, json, time, re, os, sys

# ── Load WORDS for db_key matching ────────────────────────────────────────────
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data.word_db import WORDS

# ── Arabic normalisation for fuzzy matching ───────────────────────────────────
def _norm(text):
    """Strip diacritics and normalise alef/ya/ta-marbuta for matching."""
    text = re.sub(r'[\u064B-\u065F\u0610-\u061A\u06D6-\u06DC\u06DF-\u06E4\u06E7\u06E8\u06EA-\u06ED\u0670]', '', text)
    text = re.sub(r'\u0640', '', text)                  # tatweel
    text = re.sub(r'[أإآٱ]', 'ا', text)                # alef variants
    text = re.sub(r'ى', 'ي', text)                      # alef maqsura → ya
    text = re.sub(r'ة', 'ه', text)                      # ta marbuta → ha
    return text.strip()

# Build normalised lookup once
_NORM_LOOKUP: dict[str, str] = {}
for _ar in WORDS:
    _n = _norm(_ar)
    if _n not in _NORM_LOOKUP:
        _NORM_LOOKUP[_n] = _ar

def find_db_key(arabic_word: str):
    if arabic_word in WORDS:
        return arabic_word
    n = _norm(arabic_word)
    return _NORM_LOOKUP.get(n)          # None if no match

# ── HTTP helper ───────────────────────────────────────────────────────────────
def fetch(url: str, retries=3):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url, headers={"Accept": "application/json",
                              "User-Agent": "QuranLab/1.0 (open-source)"})
            with urllib.request.urlopen(req, timeout=15) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            if attempt == retries - 1:
                raise
            print(f"  Retry {attempt+1} after error: {e}")
            time.sleep(2 ** attempt)

# ── Surah descriptions (hand-written for the most common ones) ────────────────
DESCRIPTIONS = {
    1:   "The Opening — recited in every unit of prayer. Learning these 29 words transforms your Salah.",
    2:   "The Cow — the longest Surah. Contains Ayat al-Kursi and the most comprehensive legal guidance.",
    3:   "The Family of Imran — stories of Maryam, Isa, and the Battle of Uhud.",
    4:   "The Women — detailed rulings on family, inheritance, and justice.",
    5:   "The Table Spread — the last major Surah revealed. Covers food, covenants, and Jesus.",
    6:   "The Cattle — a Makkan Surah on monotheism, prophethood, and the unseen.",
    7:   "The Heights — stories of Adam, Nuh, Hud, Salih, Lut, and Shu'ayb.",
    9:   "Repentance — the only Surah without Bismillah. Revealed after the conquest of Makkah.",
    10:  "Jonah — on divine mercy, the stories of Nuh and Musa, and the nature of faith.",
    12:  "Joseph — described as 'the best of stories.' The complete narrative of Prophet Yusuf.",
    14:  "Ibrahim — a prayer of gratitude from Ibrahim for his descendants.",
    18:  "The Cave — four stories: the Sleepers, the Two Gardens, Musa and Khidr, Dhul-Qarnayn.",
    19:  "Mary — the story of Maryam, the birth of Isa, and Yahya.",
    20:  "Ta-Ha — the story of Musa and Fir'awn in detail.",
    24:  "The Light — the verse of light, rules of modesty, and the slander of Aisha.",
    25:  "The Criterion — the qualities of the servants of the Most Merciful.",
    36:  "Ya-Sin — the heart of the Quran. Often recited for the dying.",
    39:  "The Groups — on sincere worship, the Day of Judgement, and divine forgiveness.",
    55:  "The Most Merciful — the refrain 'Which of your Lord's favours will you deny?' repeated 31 times.",
    56:  "The Inevitable — vivid descriptions of the three groups on the Day of Judgement.",
    67:  "The Sovereignty — a Surah that intercedes for its reciter. On divine power and creation.",
    78:  "The Great News — the Day of Judgement described in vivid detail.",
    87:  "The Most High — 'Glorify the name of your Lord, the Most High.' Short and powerful.",
    89:  "The Dawn — the story of 'Ad, Thamud, and Fir'awn as warnings.",
    93:  "The Morning Brightness — a divine reassurance to the Prophet in a time of hardship.",
    94:  "Relief — one of the most comforting Surahs. Hardship and ease appear twice.",
    95:  "The Fig — by the fig, the olive, and Mount Sinai — mankind is in the best form.",
    96:  "The Clot — the first five verses revealed. 'Read in the name of your Lord who created.'",
    99:  "The Earthquake — the earth shakes and every atom of good and evil is shown.",
    100: "The Charging Steeds — a vivid oath by warhorses charging at dawn.",
    101: "The Calamity — the Day of Judgement described as a great calamity.",
    102: "Rivalry in Worldly Increase — the distraction of accumulation until the grave.",
    103: "Time — Imam Shafi'i said: if only this Surah was revealed, it would suffice mankind.",
    104: "The Slanderer — a warning to those who hoard wealth and slander others.",
    105: "The Elephant — the miraculous destruction of Abraha's army with birds.",
    106: "Quraysh — the blessing of security and provision for the Quraysh.",
    107: "Small Kindnesses — the Surah that exposes the character of the hypocrite.",
    108: "Abundance — the shortest Surah. Three verses, three roots from the top 200.",
    109: "The Disbelievers — a declaration of faith. Recited in the Sunnah of Fajr prayer.",
    110: "Divine Support — a sign of the Prophet's passing. Three verses, immense meaning.",
    111: "The Palm Fiber — a warning to the enemies of truth.",
    112: "Pure Sincerity — worth a third of the Quran. Four short verses, three key roots.",
    113: "The Daybreak — a prayer for protection. Often recited before sleep.",
    114: "Mankind — the final Surah. Three of the top 15 most frequent words appear here.",
}

# ── Fetch chapter metadata ────────────────────────────────────────────────────
def fetch_chapters():
    print("Fetching chapter metadata...")
    data = fetch("https://api.quran.com/api/v4/chapters?language=en")
    return {ch["id"]: ch for ch in data["chapters"]}

# ── Fetch verses with word-by-word data ───────────────────────────────────────
def fetch_verses(chapter_id: int):
    verses = []
    page = 1
    while True:
        url = (
            f"https://api.quran.com/api/v4/verses/by_chapter/{chapter_id}"
            f"?words=true"
            f"&word_fields=text_uthmani,transliteration,translation"
            f"&translations=131"          # Saheeh International (id=131)
            f"&per_page=50&page={page}"
            f"&language=en"
        )
        data = fetch(url)
        verses.extend(data["verses"])
        meta = data.get("pagination", data.get("meta", {}))
        next_page = meta.get("next_page") or meta.get("nextPage")
        if not next_page:
            break
        page += 1
        time.sleep(0.25)
    return verses

# ── Build a single surah dict ─────────────────────────────────────────────────
def build_surah(chapter_id: int, ch_meta: dict, raw_verses: list):
    verses_out = []
    for v in raw_verses:
        words_out = []
        for w in v.get("words", []):
            # Skip verse-end markers (ayah number glyphs)
            if w.get("char_type_name") in ("end", "pause"):
                continue
            ar = w.get("text_uthmani") or w.get("text") or ""
            # word-level translation
            tr_obj = w.get("translation") or {}
            en = tr_obj.get("text") or ""
            # transliteration
            tl_obj = w.get("transliteration") or {}
            tr = tl_obj.get("text") or ""
            db_key = find_db_key(ar)
            words_out.append({"ar": ar, "en": en, "tr": tr, "db_key": db_key})

        # verse-level English (from translations array)
        verse_en = ""
        for t in v.get("translations", []):
            verse_en = t.get("text") or ""
            # strip HTML tags that sometimes appear
            verse_en = re.sub(r'<[^>]+>', '', verse_en).strip()
            break

        verses_out.append({
            "number":  v["verse_number"],
            "arabic":  v.get("text_uthmani") or v.get("text") or "",
            "english": verse_en,
            "words":   words_out,
        })

    return {
        "number":       chapter_id,
        "name_ar":      ch_meta["name_arabic"],
        "name_en":      ch_meta["name_simple"],
        "name_tr":      ch_meta["name_complex"],
        "revelation":   ch_meta.get("revelation_place", "").capitalize(),
        "verses_count": ch_meta["verses_count"],
        "description":  DESCRIPTIONS.get(chapter_id, ""),
        "verses":       verses_out,
    }

# ── Python-literal serialiser (avoids json.dumps for readability) ─────────────
def _py_str(s: str) -> str:
    return json.dumps(s, ensure_ascii=False)

def write_quran_data(surahs: list, path: str):
    lines = [
        '"""',
        'data/quran_data.py  — AUTO-GENERATED by build_quran_data.py',
        'Full 114-surah Quran with word-by-word injection data.',
        'Source: quran.com API v4 (Saheeh International translation)',
        '"""',
        '',
        'SURAHS = [',
    ]

    for s in surahs:
        lines.append('  {')
        lines.append(f'    "number": {s["number"]}, "name_ar": {_py_str(s["name_ar"])}, "name_en": {_py_str(s["name_en"])},')
        lines.append(f'    "name_tr": {_py_str(s["name_tr"])}, "revelation": {_py_str(s["revelation"])}, "verses_count": {s["verses_count"]},')
        lines.append(f'    "description": {_py_str(s["description"])},')
        lines.append('    "verses": [')
        for v in s["verses"]:
            lines.append('      {')
            lines.append(f'        "number": {v["number"]}, "arabic": {_py_str(v["arabic"])},')
            lines.append(f'        "english": {_py_str(v["english"])},')
            lines.append('        "words": [')
            for w in v["words"]:
                db = f'"{w["db_key"]}"' if w["db_key"] else "None"
                lines.append(
                    f'          {{"ar":{_py_str(w["ar"])}, "en":{_py_str(w["en"])}, '
                    f'"tr":{_py_str(w["tr"])}, "db_key":{db}}},'
                )
            lines.append('        ]},')
        lines.append('    ]},')

    lines += [
        ']',
        '',
        'def get_surah(number):',
        '    for s in SURAHS:',
        '        if s["number"] == number: return s',
        '    return None',
        '',
        'def get_all_surahs():',
        '    return [{"number":s["number"],"name_ar":s["name_ar"],"name_en":s["name_en"],',
        '             "name_tr":s["name_tr"],"verses_count":s["verses_count"],"description":s["description"]}',
        '            for s in SURAHS]',
        '',
        'def get_all_db_keys_in_surah(surah):',
        '    keys = set()',
        '    for v in surah.get("verses",[]):',
        '        for w in v.get("words",[]):',
        '            if w.get("db_key"): keys.add(w["db_key"])',
        '    return keys',
    ]

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    out_path = os.path.join(os.path.dirname(__file__), "data", "quran_data.py")

    print("=" * 60)
    print("  QURANIC LAB — Full Quran Data Builder")
    print("  Source : quran.com API v4")
    print("  Output : data/quran_data.py")
    print("=" * 60)

    chapters = fetch_chapters()
    surahs = []

    for chapter_id in range(1, 115):
        ch = chapters[chapter_id]
        print(f"  [{chapter_id:3d}/114]  {ch['name_simple']:30s} ({ch['verses_count']} verses)...", end=" ", flush=True)
        try:
            raw = fetch_verses(chapter_id)
            surah = build_surah(chapter_id, ch, raw)
            surahs.append(surah)
            matched = sum(1 for v in surah["verses"] for w in v["words"] if w["db_key"])
            total   = sum(len(v["words"]) for v in surah["verses"])
            print(f"✓  ({matched}/{total} words matched to db)")
        except Exception as e:
            print(f"✗  ERROR: {e}")
            # Keep going — insert placeholder
            surahs.append({
                "number": chapter_id, "name_ar": ch["name_arabic"],
                "name_en": ch["name_simple"], "name_tr": ch["name_complex"],
                "revelation": ch.get("revelation_place","").capitalize(),
                "verses_count": ch["verses_count"],
                "description": DESCRIPTIONS.get(chapter_id, ""),
                "verses": [],
            })
        time.sleep(0.4)   # polite rate limiting

    print(f"\nWriting {len(surahs)} surahs to {out_path} ...")
    write_quran_data(surahs, out_path)

    total_verses = sum(len(s["verses"]) for s in surahs)
    total_words  = sum(len(v["words"]) for s in surahs for v in s["verses"])
    matched      = sum(1 for s in surahs for v in s["verses"] for w in v["words"] if w["db_key"])
    print(f"\n✅  Done!")
    print(f"   Surahs  : {len(surahs)}")
    print(f"   Verses  : {total_verses}")
    print(f"   Words   : {total_words}")
    pct = round(matched / total_words * 100, 1) if total_words else 0
    print(f"   Matched : {matched} ({pct}% of words linked to word database)")
    print(f"\n   Restart the Flask server to load the new data.")
    print("=" * 60)

if __name__ == "__main__":
    main()
