"""
app.py — The Quranic Linguistic Laboratory
Main Flask application. All API routes for the frontend.
"""

from flask import Flask, jsonify, request, send_from_directory, Response
import json, os

from data.word_db   import WORDS, CLUSTERS, ROOT_INDEX, get_words_by_cluster, search_words, get_words_by_rank
from data.quran_data import SURAHS, get_surah, get_all_surahs, get_all_db_keys_in_surah
from engine.injection import (process_verse, get_root_family, explode_word,
                               get_frequency_heatmap_class, get_nav_level_settings,
                               LEVEL_PRESETS)
from engine.tracker  import (load_familiarity, save_familiarity, record_exposure,
                              reset_familiarity, mark_known, mark_unknown, get_stats)
from engine.corpus   import (search_corpus, get_root_family_detail, get_cluster_words,
                              get_frequency_heatmap_data, get_pos_groups, generate_csv_export,
                              get_wazn_groups, get_all_roots_summary)

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = "quranic_lab_2026"

# ── Serve the SPA ──────────────────────────────────────────────────────────────
@app.route("/")
def index():
    with open(os.path.join(app.template_folder, "index.html"), encoding="utf-8") as f:
        return f.read()

# ══════════════════════════════════════════════════════════════════════════════
#  QURAN TEXT ROUTES
# ══════════════════════════════════════════════════════════════════════════════

@app.route("/api/surahs")
def api_surahs():
    return jsonify(get_all_surahs())

@app.route("/api/surah/<int:number>")
def api_surah(number):
    surah = get_surah(number)
    if not surah:
        return jsonify({"error": "Surah not found"}), 404
    return jsonify(surah)

@app.route("/api/render/<int:surah_number>", methods=["POST"])
def api_render(surah_number):
    """
    POST body: { settings: {...}, familiarity: {...} }
    Returns rendered verse list with injection decisions applied.
    """
    body     = request.get_json(force=True)
    settings = body.get("settings", {})
    fam      = body.get("familiarity", load_familiarity())

    surah = get_surah(surah_number)
    if not surah:
        return jsonify({"error": "Surah not found"}), 404

    rendered_verses = []
    all_keys_seen   = []
    for verse in surah["verses"]:
        words = process_verse(verse, settings, fam)
        rendered_verses.append({
            "number":  verse["number"],
            "arabic":  verse["arabic"],
            "english": verse["english"],
            "words":   words,
        })
        all_keys_seen += [w["db_key"] for w in words if w.get("db_key")]

    # Silently record exposures
    fam = record_exposure(fam, all_keys_seen)

    return jsonify({
        "surah":   {"number": surah["number"], "name_ar": surah["name_ar"],
                    "name_en": surah["name_en"], "name_tr": surah["name_tr"],
                    "description": surah["description"]},
        "verses":  rendered_verses,
        "familiarity": fam,
        "stats":   get_stats(fam, WORDS),
    })

@app.route("/api/bookview/<int:surah_number>", methods=["POST"])
def api_bookview(surah_number):
    """
    POST body: { settings: {...}, familiarity: {...} }
    Returns structured verse/word data for Book View (flowing hybrid text).
    """
    body     = request.get_json(force=True)
    settings = body.get("settings", {})
    fam      = body.get("familiarity", load_familiarity())

    surah = get_surah(surah_number)
    if not surah:
        return jsonify({"error": "Surah not found"}), 404

    verses        = []
    all_keys_seen = []
    for verse in surah["verses"]:
        words = process_verse(verse, settings, fam)
        verses.append({
            "number": verse["number"],
            "words":  words,
        })
        all_keys_seen += [w["db_key"] for w in words if w.get("db_key")]

    fam = record_exposure(fam, all_keys_seen)

    return jsonify({
        "surah": {
            "number":      surah["number"],
            "name_ar":     surah["name_ar"],
            "name_en":     surah["name_en"],
            "name_tr":     surah["name_tr"],
            "description": surah.get("description", ""),
        },
        "verses":      verses,
        "familiarity": fam,
    })

# ══════════════════════════════════════════════════════════════════════════════
#  WORD DATABASE ROUTES
# ══════════════════════════════════════════════════════════════════════════════

@app.route("/api/words")
def api_words():
    top = int(request.args.get("top", 300))
    return jsonify(list(get_words_by_rank(top).items()))

@app.route("/api/word/<path:db_key>")
def api_word(db_key):
    data = WORDS.get(db_key)
    if not data:
        return jsonify({"error":"Not found"}), 404
    root_family = get_root_family(db_key)
    return jsonify({
        "arabic": db_key,
        **data,
        "root_family": root_family,
        "root_family_details": [{"arabic":k,**WORDS[k]} for k in root_family if k in WORDS],
        "freq_band": get_frequency_heatmap_class(db_key),
        "exploded": explode_word(db_key, db_key),
    })

@app.route("/api/root/<path:root>")
def api_root(root):
    return jsonify(get_root_family_detail(root))

@app.route("/api/clusters")
def api_clusters():
    return jsonify(CLUSTERS)

@app.route("/api/cluster/<cluster_key>")
def api_cluster(cluster_key):
    return jsonify(get_cluster_words(cluster_key))

@app.route("/api/search")
def api_search():
    q = request.args.get("q","")
    return jsonify(search_corpus(q))

# ══════════════════════════════════════════════════════════════════════════════
#  NAVIGATION LEVELS
# ══════════════════════════════════════════════════════════════════════════════

@app.route("/api/nav-levels")
def api_nav_levels():
    levels = ["qaida","tilawah","hifz","sarf","nahw","alim"]
    return jsonify({k: get_nav_level_settings(k) for k in levels})

@app.route("/api/nav-level/<level>")
def api_nav_level(level):
    return jsonify(get_nav_level_settings(level))

# ══════════════════════════════════════════════════════════════════════════════
#  FAMILIARITY & PROGRESS
# ══════════════════════════════════════════════════════════════════════════════

@app.route("/api/familiarity")
def api_familiarity():
    fam = load_familiarity()
    return jsonify({"familiarity": fam, "stats": get_stats(fam, WORDS)})

@app.route("/api/familiarity/reset", methods=["POST"])
def api_fam_reset():
    return jsonify(reset_familiarity())

@app.route("/api/familiarity/mark-known", methods=["POST"])
def api_mark_known():
    body    = request.get_json(force=True)
    db_key  = body.get("db_key","")
    fam     = load_familiarity()
    fam     = mark_known(fam, db_key)
    return jsonify({"ok":True, "familiarity": fam})

@app.route("/api/familiarity/mark-unknown", methods=["POST"])
def api_mark_unknown():
    body    = request.get_json(force=True)
    db_key  = body.get("db_key","")
    fam     = load_familiarity()
    fam     = mark_unknown(fam, db_key)
    return jsonify({"ok":True, "familiarity": fam})

# ══════════════════════════════════════════════════════════════════════════════
#  CORPUS TOOLS
# ══════════════════════════════════════════════════════════════════════════════

@app.route("/api/heatmap")
def api_heatmap():
    return jsonify(get_frequency_heatmap_data())

@app.route("/api/pos-groups")
def api_pos_groups():
    return jsonify(get_pos_groups())

@app.route("/api/wazn")
def api_wazn():
    return jsonify(get_wazn_groups())

@app.route("/api/roots-summary")
def api_roots_summary():
    return jsonify(get_all_roots_summary()[:80])

# ══════════════════════════════════════════════════════════════════════════════
#  EXPORT
# ══════════════════════════════════════════════════════════════════════════════

@app.route("/api/export/csv")
def api_export_csv():
    cluster = request.args.get("cluster","")
    pos     = request.args.get("pos","")
    fam     = load_familiarity()

    def filter_fn(arabic, data):
        if cluster and data.get("cluster") != cluster: return False
        if pos     and data.get("pos")     != pos:     return False
        return True

    csv_data = generate_csv_export(filter_fn=filter_fn, familiarity=fam)
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=quran_lab_export.csv"}
    )

@app.route("/api/export/salah-sheet")
def api_salah_sheet():
    """Returns JSON of the Salah Essentials cluster for printing."""
    words = get_cluster_words("salah_essentials")
    fam   = load_familiarity()
    for w in words:
        w["familiarity"] = fam.get(w["arabic"], 0)
    return jsonify({"cluster": "salah_essentials", "words": words})

# ══════════════════════════════════════════════════════════════════════════════
#  LEARNING PROFILES
# ══════════════════════════════════════════════════════════════════════════════

PROFILES = {
    "contextual": {
        "label":"🌊 The Contextual Learner","desc":"Learns through story and narrative. Dislikes abstract rules.",
        "settings":{"injection_level":30,"active_clusters":["salah_essentials","divine"],"word_spacing":100,
                    "show_translation":True,"translation_opacity":100,"hifz_ghost":False,"heatmap":False,
                    "color_pos":False,"show_morpheme_split":False},
    },
    "mathematical": {
        "label":"🔢 The Mathematical Learner","desc":"Loves patterns, root systems, morphological logic.",
        "settings":{"injection_level":90,"active_clusters":list(CLUSTERS.keys()),"word_spacing":150,
                    "show_translation":True,"translation_opacity":60,"hifz_ghost":False,"heatmap":True,
                    "color_pos":False,"show_morpheme_split":True},
    },
    "visual": {
        "label":"👁️ The Visual Learner","desc":"Remembers by spatial position, colour, and shape.",
        "settings":{"injection_level":50,"active_clusters":["salah_essentials","divine","heart","nature"],
                    "word_spacing":180,"show_translation":True,"translation_opacity":80,"hifz_ghost":False,
                    "heatmap":True,"color_pos":True,"show_morpheme_split":False},
    },
    "scaffolded": {
        "label":"🪜 The Scaffolded Learner","desc":"Easily overwhelmed — prefers gradual, low-pressure exposure.",
        "settings":{"injection_level":10,"active_clusters":["salah_essentials"],"word_spacing":100,
                    "show_translation":True,"translation_opacity":100,"hifz_ghost":False,"heatmap":False,
                    "color_pos":False,"show_morpheme_split":False},
    },
    "memoriser": {
        "label":"🧠 The Memoriser","desc":"Active recall and structural anchoring for Hifz.",
        "settings":{"injection_level":75,"active_clusters":list(CLUSTERS.keys()),"word_spacing":100,
                    "show_translation":True,"translation_opacity":15,"hifz_ghost":True,"heatmap":False,
                    "color_pos":False,"show_morpheme_split":False},
    },
    "researcher": {
        "label":"🔬 The Researcher","desc":"Wants data, cross-references, and full corpus access.",
        "settings":{"injection_level":100,"active_clusters":list(CLUSTERS.keys()),"word_spacing":100,
                    "show_translation":True,"translation_opacity":100,"hifz_ghost":False,"heatmap":True,
                    "color_pos":True,"show_morpheme_split":True},
    },
    "busy_parent": {
        "label":"⏱️ The Busy Parent","desc":"Limited time — immediate Salah impact only.",
        "settings":{"injection_level":10,"active_clusters":["salah_essentials"],"word_spacing":100,
                    "show_translation":True,"translation_opacity":100,"hifz_ghost":False,"heatmap":False,
                    "color_pos":False,"show_morpheme_split":False},
    },
}

@app.route("/api/profiles")
def api_profiles():
    return jsonify(PROFILES)

if __name__ == "__main__":
    print("\n" + "═"*60)
    print("  🕌  THE QURANIC LINGUISTIC LABORATORY  v1.0")
    print("  Open:  http://localhost:5000")
    print("═"*60 + "\n")
    app.run(debug=True, port=5000)
