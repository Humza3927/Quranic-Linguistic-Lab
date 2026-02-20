# Quranic Linguistic Laboratory — Roadmap & Bug Tracker

## ✅ Completed (v1.0)

### Core Features
- [x] Dynamic Injection Engine (`engine/injection.py`)
- [x] Familiarity tracking — silent exposure counter, mark known/unknown (`engine/tracker.py`)
- [x] Corpus tools — search, root families, wazn groups, heatmap (`engine/corpus.py`)
- [x] Full 114-surah Quran data (6,236 verses, 77,429 words) via `build_quran_data.py`
- [x] Word database — ~200 high-frequency words, 10 thematic clusters (`data/word_db.py`)
- [x] 7 learning style profiles (Contextual, Mathematical, Visual, Scaffolded, Memoriser, Researcher, Busy Parent)
- [x] 6 navigation level presets (Qaida → Tilawah → Hifz → Sarf → Nahw → Alim)

### Views
- [x] Reading View — verse-by-verse with injection, heatmap, POS colour, morpheme split
- [x] Word Database View — searchable, filterable, familiarity bars
- [x] Frequency Heatmap View — 5-band colour overlay
- [x] Corpus Search View — search by Arabic/transliteration/English/root
- [x] Wazn Groups View — morphological pattern browser
- [x] Settings & Profiles View
- [x] **Book View** *(new)* — flowing prose layout, inline Arabic, surah selector, injection slider
- [x] **Dark Mode** *(new)* — full CSS override, localStorage persistence, 🌙 toggle button

### Infrastructure
- [x] Flask SPA with all API routes
- [x] `build_quran_data.py` — fetches from quran.com API v4, maps to word_db
- [x] `README.md` — comprehensive setup + API reference
- [x] `.gitignore` — excludes user data, binaries, __pycache__
- [x] `run.bat` — Windows quick-launch
- [x] `static/` and `exports/` directories tracked via `.gitkeep`

---

## 🐛 Known Bugs (Code Audit Findings)

### High Priority
- [ ] **8 duplicate Arabic keys in `word_db.py`** — `نور`, `حكمة`, `ذكر`, `شكر`, `علم`, `صبر`, `أمر`, `خلق` appear twice; second definition silently overwrites first. Fix: deduplicate and merge.
- [ ] **`level-desc-bar` null reference** — `setLevel()` calls `document.getElementById("level-desc-bar")` before the reading pane is rendered. Fix: guard with `?.` optional chaining.
- [ ] **`buildWordListPanel()` forEach bug** — `return` inside `forEach` does nothing; should be `html +=`. *(Partially fixed — verify in panel word list)*

### Medium Priority
- [ ] **`show_tajweed` setting defined but never applied** — the toggle exists in Settings but `renderVerse()` never reads it. Fix: add Tajweed colour-coding to word rendering.
- [ ] **`explode_word()` naive prefix/suffix detection** — splits on fixed character counts, not actual morpheme boundaries. Fix: use Quranic Arabic Corpus morpheme data.
- [ ] **Dead imports in `app.py`** — `get_all_db_keys_in_surah` imported but never used. Fix: remove.
- [ ] **Missing cluster definitions** — `body`, `concepts`, `unseen`, `salah` referenced in code but not defined in `CLUSTERS` dict in `word_db.py`.

### Low Priority
- [ ] **2 profiles missing** — `auditory_rhythmic` and `deconstructivist` mentioned in MD but absent from `PROFILES` dict in `app.py`.
- [ ] **`What's Left` mode** — CSS class `.whats-left` exists but the actual word-hiding logic in `renderVerse()` is incomplete.
- [ ] **Book View injection slider** — currently triggers a full API re-fetch on every change; should debounce (300ms).

---

## 🚀 Feature Roadmap

### Phase 2 — Depth (v0.5 Beta)
- [ ] Tajweed colour-coding (Level 1 — Qaida)
- [ ] Morpheme Word-Exploder (Level 4 — Sarf)
- [ ] Root Family Tree panel (tap word → all Quran occurrences)
- [ ] Chunked Verse Display (cognitive accessibility — max 7 items per chunk)
- [ ] Minimal Mode (stripped reading view, no overlays)
- [ ] Dyslexia-friendly Arabic font option
- [ ] Diacritic opacity control (independent of word opacity)

### Phase 3 — Intelligence (v1.0 Release)
- [ ] Auto-Hide Flashcard Mode (word blurred until tapped)
- [ ] Hover Proximity Glow (word illuminates as cursor approaches)
- [ ] Difference Engine (changed endings highlighted when same word appears twice)
- [ ] Spaced repetition algorithm for weak words
- [ ] Blur-and-Reveal toggle (Hifz mode)
- [ ] Rhyme-Scheme Extractor (Saj' end-vowel filter)

### Phase 4 — Community (v1.5)
- [ ] Excel/CSV export with custom filters
- [ ] Anki flashcard export (`.apkg` format)
- [ ] Personal annotation layer (user-defined tags)
- [ ] Community preset library (shareable filter configs)
- [ ] Printable Salah sheet improvements

### Phase 5 — AI (v2.0)
- [ ] AI recitation feedback (voice recognition, no data stored)
- [ ] Semantic concept search (Quranic Ontology integration)
- [ ] Cross-reference highlighting (related verses across Surahs)
- [ ] Word-level audio playback (isolated pronunciation)

### Phase 6 — Expansion (v2.5+)
- [ ] Multi-language injection (Urdu, Malay, Turkish, French, Swahili)
- [ ] Plugin API for third-party extensions
- [ ] Offline-first full corpus (PWA / service worker)
- [ ] Mobile app (React Native / Expo)

---

## 📁 File Structure

```
quran_lab/
├── app.py                    # Flask app — all API routes
├── build_quran_data.py       # One-time: fetch full Quran from quran.com API v4
├── requirements.txt          # Python deps (Flask only)
├── run.bat                   # Windows quick-launch
├── README.md                 # Setup + API reference
├── TODO.md                   # This file
├── .gitignore
│
├── data/
│   ├── quran_data.py         # 114 surahs, 6,236 verses, 77,429 words (auto-generated)
│   └── word_db.py            # ~200 high-frequency words + 10 clusters
│
├── engine/
│   ├── injection.py          # Dynamic Injection Engine
│   ├── tracker.py            # Familiarity tracking
│   └── corpus.py             # Corpus tools
│
├── templates/
│   └── index.html            # SPA — all UI, CSS, JS
│
├── static/                   # Static assets (future use)
└── exports/                  # Runtime user data (gitignored)
```

---

*Built by the Community. For the Ummah. Open Source | Free Forever.*
