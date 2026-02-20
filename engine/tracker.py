"""
engine/tracker.py
Familiarity / Exposure Tracker.
Tracks how many times a user has "seen" each Arabic word.
Persists to a JSON file per session.
"""

import json, os, time
from collections import defaultdict

STORAGE_PATH = os.path.join(os.path.dirname(__file__), "..", "exports", "familiarity.json")

def load_familiarity():
    if os.path.exists(STORAGE_PATH):
        with open(STORAGE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_familiarity(data):
    os.makedirs(os.path.dirname(STORAGE_PATH), exist_ok=True)
    with open(STORAGE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def record_exposure(familiarity, db_keys):
    """Increment exposure count for each db_key in the list."""
    for key in db_keys:
        if key:
            familiarity[key] = familiarity.get(key, 0) + 1
    save_familiarity(familiarity)
    return familiarity

def reset_familiarity():
    if os.path.exists(STORAGE_PATH):
        os.remove(STORAGE_PATH)
    return {}

def mark_known(familiarity, db_key, threshold=50):
    """Force-set a word as known."""
    familiarity[db_key] = threshold
    save_familiarity(familiarity)
    return familiarity

def mark_unknown(familiarity, db_key):
    """Force-reset a word to unknown."""
    familiarity[db_key] = 0
    save_familiarity(familiarity)
    return familiarity

def get_stats(familiarity, word_db):
    total = len(word_db)
    seen = sum(1 for k in word_db if familiarity.get(k, 0) > 0)
    known = sum(1 for k in word_db if familiarity.get(k, 0) >= 50)
    return {
        "total_words": total,
        "seen": seen,
        "known": known,
        "unseen": total - seen,
        "pct_seen": round(seen / total * 100, 1) if total else 0,
        "pct_known": round(known / total * 100, 1) if total else 0,
    }
