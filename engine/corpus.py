"""
engine/corpus.py
Corpus tools:
  - Root family search
  - Pattern (Wazn) detection
  - Semantic / keyword search
  - Frequency heatmap data
  - CSV export generator
"""

import csv, io
from data.word_db import WORDS, ROOT_INDEX, CLUSTERS, get_words_by_cluster


def search_corpus(query):
    """
    Full-text search across transliterations, English meanings,
    Arabic text, and roots. Returns ranked list of matching words.
    """
    query = query.strip().lower()
    if not query:
        return []
    results = []
    for arabic, data in WORDS.items():
        score = 0
        if query in arabic: score += 10
        if query in data.get("tr","").lower(): score += 8
        if query in data.get("en","").lower(): score += 6
        if query in data.get("root","").lower(): score += 5
        if query in data.get("cluster","").lower(): score += 3
        if query in data.get("cat","").lower(): score += 2
        if score > 0:
            results.append({"arabic": arabic, "score": score, **data})
    results.sort(key=lambda x: (-x["score"], x.get("rank", 999)))
    return results[:50]


def get_root_family_detail(root):
    """Return full details of all words sharing a root."""
    members = ROOT_INDEX.get(root, [])
    return [{"arabic": k, **WORDS[k]} for k in members if k in WORDS]


def get_cluster_words(cluster_key):
    return [{"arabic": k, **v} for k, v in get_words_by_cluster(cluster_key).items()]


def get_frequency_heatmap_data():
    """Returns all words sorted by frequency for heatmap rendering."""
    data = []
    for arabic, info in WORDS.items():
        data.append({
            "arabic": arabic,
            "tr": info["tr"],
            "en": info["en"],
            "count": info["count"],
            "rank": info["rank"],
            "cluster": info["cluster"],
            "pos": info["pos"],
            "band": _freq_band(info["count"])
        })
    data.sort(key=lambda x: x["rank"])
    return data


def _freq_band(count):
    if count >= 1000: return 1
    if count >= 200:  return 2
    if count >= 50:   return 3
    if count >= 10:   return 4
    return 5


def get_pos_groups():
    """Group words by part of speech."""
    groups = {"noun":[], "verb":[], "particle":[], "pronoun":[], "adj":[]}
    for arabic, data in WORDS.items():
        pos = data.get("pos","noun")
        if pos not in groups: pos = "noun"
        groups[pos].append({"arabic": arabic, **data})
    for g in groups:
        groups[g].sort(key=lambda x: x.get("rank",999))
    return groups


def generate_csv_export(filter_fn=None, familiarity=None):
    """
    Generate a CSV string of the word database.
    filter_fn: optional function(arabic, data) -> bool
    """
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["Arabic","Transliteration","English Meaning","Root",
                     "Category","Cluster","Part of Speech","Frequency Rank",
                     "Approx. Count in Quran","Familiarity Score"])
    for arabic, data in sorted(WORDS.items(), key=lambda x: x[1]["rank"]):
        if filter_fn and not filter_fn(arabic, data):
            continue
        fam = familiarity.get(arabic, 0) if familiarity else 0
        writer.writerow([
            arabic,
            data.get("tr",""),
            data.get("en",""),
            data.get("root",""),
            data.get("cat",""),
            data.get("cluster",""),
            data.get("pos",""),
            data.get("rank",""),
            data.get("count",""),
            fam,
        ])
    return output.getvalue()


def get_wazn_groups():
    """
    Detect common Arabic morphological patterns by suffix/shape.
    Very simplified — groups words by common endings.
    """
    patterns = {
        "فَعَّال (Intense doer)":   {"suffix":"ال","example":"غَفَّار (Ghaffar)"},
        "فَعِيل (Quality noun)":    {"suffix":"يل","example":"رَحِيم (Raheem)"},
        "مَفْعُول (Passive)":       {"suffix":"ول","example":"مَقْتُول"},
        "فَاعِل (Active doer)":     {"suffix":"عل","example":"كَافِر (Kafir)"},
        "فِعَال (Plural pattern)":  {"suffix":"ال","example":"كِتَاب (Kitab)"},
        "أَفْعَال (Broken plural)": {"suffix":"اع","example":"أَفْعَال"},
        "مَفْعَل (Place/time)":     {"suffix":"عل","example":"مَسْجِد (Masjid)"},
        "إِسْتِفْعَال (Form X)":    {"prefix":"است","example":"اِسْتِغْفَار (Istighfar)"},
    }
    result = {}
    for pattern_name, meta in patterns.items():
        matches = []
        for arabic, data in WORDS.items():
            tr = data.get("tr","").lower()
            if meta["suffix"] and arabic.endswith(meta["suffix"]):
                matches.append({"arabic": arabic, **data})
            elif meta.get("prefix") and arabic.startswith(meta["prefix"]):
                matches.append({"arabic": arabic, **data})
        result[pattern_name] = {
            "matches": matches[:10],
            "example": meta["example"],
            "count": len(matches)
        }
    return result


def get_all_roots_summary():
    """Returns all unique roots with their word count."""
    summary = []
    for root, words in ROOT_INDEX.items():
        summary.append({
            "root": root,
            "word_count": len(words),
            "words": [{"arabic": w, **WORDS[w]} for w in words if w in WORDS],
            "min_rank": min(WORDS[w]["rank"] for w in words if w in WORDS) if words else 999,
        })
    summary.sort(key=lambda x: x["min_rank"])
    return summary
