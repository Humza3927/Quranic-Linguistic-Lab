"""
engine/injection.py
The Dynamic Injection Engine.
Processes Quran verse data and returns a structured render list that the
frontend uses to draw either English, Arabic, or hybrid text per word.
"""

from data.word_db import WORDS, CLUSTERS, ROOT_INDEX, get_frequency_band

# ── Injection Level Presets ────────────────────────────────────────────────────
LEVEL_PRESETS = {
    "0":  {"label":"Pure English",        "inject_rank_threshold": 0,   "clusters": []},
    "10": {"label":"Divine Names Only",   "inject_rank_threshold": 5,   "clusters": ["salah_essentials"]},
    "25": {"label":"Salah Essentials",    "inject_rank_threshold": 50,  "clusters": ["salah_essentials","divine"]},
    "50": {"label":"Top 100 Words",       "inject_rank_threshold": 100, "clusters": ["salah_essentials","divine","guidance","heart"]},
    "75": {"label":"Top 200 Words",       "inject_rank_threshold": 200, "clusters": ["salah_essentials","divine","guidance","heart","people","verbs","structure"]},
    "90": {"label":"Top 300 Words",       "inject_rank_threshold": 300, "clusters": list(CLUSTERS.keys())},
    "100":{"label":"Pure Arabic",         "inject_rank_threshold": 9999,"clusters": list(CLUSTERS.keys())},
}

def _should_inject(db_key, settings):
    """Returns True if this word should be shown in Arabic given current settings."""
    if not db_key or db_key not in WORDS:
        return False
    word_data = WORDS[db_key]
    rank = word_data.get("rank", 9999)
    cluster = word_data.get("cluster","")

    level = int(settings.get("injection_level", 25))
    # Find nearest preset threshold
    threshold = 0
    for pct, preset in LEVEL_PRESETS.items():
        if int(pct) <= level:
            threshold = preset["inject_rank_threshold"]

    # Check user-toggled clusters
    active_clusters = settings.get("active_clusters", [])
    if cluster in active_clusters:
        return True

    return rank <= threshold


def process_verse(verse, settings, familiarity):
    """
    Takes a verse dict and returns a list of word-render objects.
    Each object: { ar, en, tr, db_key, show_arabic, data, familiarity_score,
                   freq_band, root, cluster, pos, is_known }
    """
    render = []
    for word in verse.get("words", []):
        db_key = word.get("db_key")
        word_data = WORDS.get(db_key, {}) if db_key else {}
        fam_score = familiarity.get(db_key, 0) if db_key else 0
        known_threshold = settings.get("known_threshold", 50)
        is_known = fam_score >= known_threshold

        show_arabic = _should_inject(db_key, settings)

        # In Hifz mode, ghost the English
        # In "What's Left" mode, hide known words
        whats_left_mode = settings.get("whats_left_mode", False)
        if whats_left_mode and is_known:
            show_arabic = False  # collapse known words visually

        render.append({
            "ar": word["ar"],
            "en": word["en"],
            "tr": word.get("tr",""),
            "db_key": db_key,
            "show_arabic": show_arabic,
            "data": word_data,
            "familiarity_score": fam_score,
            "freq_band": get_frequency_band(db_key) if db_key else 5,
            "root": word_data.get("root",""),
            "cluster": word_data.get("cluster",""),
            "pos": word_data.get("pos",""),
            "rank": word_data.get("rank", 999),
            "count": word_data.get("count", 0),
            "is_known": is_known,
        })
    return render


def get_root_family(db_key):
    """Return all words sharing the same root as db_key."""
    if not db_key or db_key not in WORDS:
        return []
    root = WORDS[db_key]["root"]
    return ROOT_INDEX.get(root, [])


def explode_word(arabic_word, db_key):
    """
    Naive morpheme splitter — splits off common prefixes/suffixes.
    Returns list of segments: [{"text":..., "type":"prefix"|"root"|"suffix"}]
    """
    PREFIXES = ["وَ","فَ","بِ","لِ","كَ","أَ","وَال","فَال","بِال","لِال"]
    SUFFIXES = ["هُمْ","كُمْ","هُ","هَا","نَا","كَ","هِمْ","تَ","نَ","وَا","ونَ","ينَ","انِ","ينِ","تُمْ"]

    segments = []
    text = arabic_word
    prefix_found = ""
    suffix_found = ""

    for p in sorted(PREFIXES, key=len, reverse=True):
        if text.startswith(p) and len(text) > len(p) + 1:
            prefix_found = p
            text = text[len(p):]
            break

    for s in sorted(SUFFIXES, key=len, reverse=True):
        if text.endswith(s) and len(text) > len(s) + 1:
            suffix_found = s
            text = text[:-len(s)]
            break

    if prefix_found:
        segments.append({"text": prefix_found, "type": "prefix"})
    segments.append({"text": text, "type": "root"})
    if suffix_found:
        segments.append({"text": suffix_found, "type": "suffix"})

    return segments


def get_frequency_heatmap_class(db_key):
    """Returns CSS class name based on frequency."""
    if not db_key: return "freq-5"
    band = get_frequency_band(db_key)
    return f"freq-{band}"


def get_nav_level_settings(level_name):
    """Returns default settings object for each navigation level."""
    levels = {
        "qaida": {
            "name": "Qaida", "subtitle": "The Decoder",
            "injection_level": 0,
            "active_clusters": [],
            "word_spacing": 200,
            "show_tajweed": True,
            "show_morpheme_split": True,
            "show_translation": False,
            "translation_opacity": 0,
            "hifz_ghost": False,
            "heatmap": False,
            "color_pos": False,
            "description": "Visual recognition — train your eye to see word boundaries."
        },
        "tilawah": {
            "name": "Tilawah", "subtitle": "The Fluid Reader",
            "injection_level": 25,
            "active_clusters": ["salah_essentials"],
            "word_spacing": 100,
            "show_tajweed": False,
            "show_morpheme_split": False,
            "show_translation": True,
            "translation_opacity": 100,
            "hifz_ghost": False,
            "heatmap": False,
            "color_pos": False,
            "description": "English + injected Arabic. The immersion begins here."
        },
        "hifz": {
            "name": "Hifz", "subtitle": "The Memoriser",
            "injection_level": 75,
            "active_clusters": list(CLUSTERS.keys()),
            "word_spacing": 100,
            "show_tajweed": False,
            "show_morpheme_split": False,
            "show_translation": True,
            "translation_opacity": 15,
            "hifz_ghost": True,
            "heatmap": False,
            "color_pos": False,
            "description": "Root letters bolded as memory hooks. English ghosted."
        },
        "sarf": {
            "name": "Sarf", "subtitle": "The Pattern Recogniser",
            "injection_level": 90,
            "active_clusters": list(CLUSTERS.keys()),
            "word_spacing": 150,
            "show_tajweed": False,
            "show_morpheme_split": True,
            "show_translation": True,
            "translation_opacity": 60,
            "hifz_ghost": False,
            "heatmap": True,
            "color_pos": False,
            "description": "Word patterns highlighted — see the mathematical structure."
        },
        "nahw": {
            "name": "Nahw", "subtitle": "The Architect",
            "injection_level": 90,
            "active_clusters": list(CLUSTERS.keys()),
            "word_spacing": 120,
            "show_tajweed": False,
            "show_morpheme_split": False,
            "show_translation": True,
            "translation_opacity": 80,
            "hifz_ghost": False,
            "heatmap": False,
            "color_pos": True,
            "description": "Colour-coded by part of speech. Sentence architecture visible."
        },
        "alim": {
            "name": "Alim", "subtitle": "The Researcher",
            "injection_level": 100,
            "active_clusters": list(CLUSTERS.keys()),
            "word_spacing": 100,
            "show_tajweed": True,
            "show_morpheme_split": True,
            "show_translation": True,
            "translation_opacity": 100,
            "hifz_ghost": False,
            "heatmap": True,
            "color_pos": True,
            "description": "Full corpus view — every variable visible. Deep research mode."
        },
    }
    return levels.get(level_name, levels["tilawah"])
