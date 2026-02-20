# 🕌 The Quranic Linguistic Laboratory

> **A fully customisable, open-source Quran learning platform.**  
> Read the Quran as a book you finally understand — Arabic vocabulary is progressively and silently injected into the English text, word by word, at your own pace.

[![Open Source](https://img.shields.io/badge/Open%20Source-Free%20Forever-1A5C38)](https://github.com)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0%2B-black)](https://flask.palletsprojects.com)

---

## The Core Philosophy

> *You are not forced to study. You read the Quran as a book — a story you finally understand — and the Arabic 'gibberish' is slowly, visually, and predictably unmasked. You are not studying; you are observing.*

The **Recitation Paradox**: an estimated 1.8 billion Muslims recite the Quran daily, yet the vast majority of non-Arab Muslims do so without understanding a single word. This app builds a cognitive bridge between your existing English fluency and the Arabic text — using a progressive, immersive, and fully customisable interface.

| Key Metric | Value |
|---|---|
| Words for 70% Quran coverage | ~300 words |
| Words for 80% Quran coverage | ~500–600 words |
| Total Quranic words | 77,000+ / ~1,600 unique roots |
| Surahs available | **114 (complete Quran)** |
| Learning levels | 6 distinct modes |
| Thematic word clusters | 10+ pre-built categories |

---

## Features

### 🔡 Dynamic Injection Engine
The app renders a **single seamless hybrid translation** — English is the default, but Arabic words are progressively injected to replace their English equivalents. A continuous slider moves from `0%` (pure English) to `100%` (pure Arabic).

```
"Say, I seek refuge in the Rabb of An-Nas, the Malik of An-Nas, the Ilah of An-Nas."
```

### 📖 Book View *(New)*
A flowing, prose-style reading experience — like reading a novel. Arabic words appear inline within the English text, coloured by thematic cluster. Includes an independent injection slider and surah selector.

### 🌙 Dark Mode *(New)*
Full dark mode with persistent preference (saved to `localStorage`). Toggle with the `🌙 Dark` button in the top bar.

### 🧠 6 Navigation Levels
| Level | Name | Focus |
|---|---|---|
| 1 | Qaida / The Decoder | Visual recognition, Tajweed colour-coding |
| 2 | Tilawah / The Fluid Reader | Smooth reading with progressive injection |
| 3 | Hifz / The Memoriser | Active recall, ghosted English, blur-and-reveal |
| 4 | Sarf / The Pattern Recogniser | Morphology, root families, word-exploder |
| 5 | Nahw / The Architect | Sentence structure, grammar overlay |
| 6 | Alim / The Researcher | Full corpus analysis, semantic search |

### 🎨 Visual Customisation
- Per-cluster colour coding (10+ thematic clusters)
- Inter-word spacing slider
- Translation opacity slider
- Morpheme splitting (prefix | root | suffix)
- Frequency heatmap (5 bands)
- Root-glow highlight (tap any word → same-root words glow)

### 📊 Familiarity Tracking
Silent exposure counter per word. Mark words as known/unknown. View stats. Export to CSV. Print Salah Essentials sheet.

### 🔍 Corpus Search
Search by Arabic text, transliteration, English meaning, or root across the full word database.

### 👤 Learning Style Profiles
7 pre-built profiles: Contextual, Mathematical, Visual, Scaffolded, Memoriser, Researcher, Busy Parent.

---

## Quick Start

### Prerequisites
- Python 3.10+

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/quran_lab.git
cd quran_lab

# 2. Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
# or on Windows: double-click run.bat
```

Then open **http://localhost:5000** in your browser.

### Regenerate Quran Data (optional)
The full 114-surah dataset is included. To re-fetch from the quran.com API:

```bash
python build_quran_data.py
```

This fetches all 114 surahs (6,236 verses, 77,429 words) with word-by-word translations and maps them to the word database. Takes ~3–5 minutes.

---

## Project Structure

```
quran_lab/
│
├── app.py                    # Flask application — all API routes
├── build_quran_data.py       # One-time script: fetch full Quran from quran.com API
├── requirements.txt          # Python dependencies
├── run.bat                   # Windows quick-launch
├── TODO.md                   # Comprehensive feature roadmap & bug tracker
│
├── data/
│   ├── quran_data.py         # Full 114-surah Quran (word-by-word, auto-generated)
│   └── word_db.py            # ~200 high-frequency word database + 10 thematic clusters
│
├── engine/
│   ├── injection.py          # Dynamic Injection Engine (process_verse, level presets)
│   ├── tracker.py            # Familiarity tracking (exposure counts, known/unknown)
│   └── corpus.py             # Corpus tools (search, root families, wazn groups, heatmap)
│
├── templates/
│   └── index.html            # Single-page application (all UI, CSS, and JS)
│
├── exports/
│   └── familiarity.json      # User progress data (gitignored — generated at runtime)
│
└── static/                   # Static assets (CSS/JS/images if needed)
```

---

## API Reference

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/api/surahs` | List all 114 surahs |
| `GET` | `/api/surah/<n>` | Full surah data with word-by-word structure |
| `POST` | `/api/render/<n>` | Render surah with injection settings applied |
| `POST` | `/api/bookview/<n>` | Book view — structured word data for flowing prose |
| `GET` | `/api/words` | Full word database |
| `GET` | `/api/search?q=<query>` | Search words by Arabic/transliteration/English/root |
| `GET` | `/api/root-family/<root>` | All words sharing a 3-letter root |
| `GET` | `/api/heatmap/<n>` | Frequency heatmap data for a surah |
| `GET` | `/api/wazn-groups` | Morphological pattern groups |
| `GET` | `/api/pos-groups` | Part-of-speech groups |
| `GET` | `/api/familiarity` | Load familiarity data |
| `POST` | `/api/familiarity/save` | Save familiarity data |
| `POST` | `/api/familiarity/reset` | Reset all familiarity data |
| `POST` | `/api/familiarity/mark` | Mark word as known/unknown |
| `GET` | `/api/profiles` | Learning style profiles |
| `GET` | `/api/export/csv` | Export word database as CSV |

---

## Roadmap

See [`TODO.md`](TODO.md) for the full feature roadmap, bug tracker, and code audit findings.

**Priority next steps:**
- Fix 8 duplicate keys in `word_db.py`
- Add missing cluster definitions (`body`, `concepts`, `unseen`, `salah`)
- Tajweed colour-coding (Level 1)
- Auto-Hide Flashcard Mode
- Chunked Verse Display (cognitive accessibility)
- Excel/Anki export
- Audio playback integration

---

## Contributing

This is a community tool built for the Ummah. Contributions welcome:

- **Vocabulary Packs** — curate word lists for specific topics or Surahs
- **Translation Layers** — add Urdu, Malay, Turkish, French, Swahili support
- **Custom Skins** — share your visual configuration as a preset
- **Bug fixes** — see `TODO.md` for known issues
- **Feature implementations** — pick any item from the roadmap

No academic gatekeeping. A mother who knows which 15 words transformed her Salah can contribute a pack.

---

## Data Sources

- **[quran.com API v4](https://quran.com/api)** — word-by-word Arabic text, transliterations, Saheeh International translation
- **Word database** — hand-curated ~200 high-frequency Quranic words with roots, clusters, frequency counts, and POS tags

---

## License

MIT License — Free forever. Built by the community, for the Ummah.

---

*"Imagine reading Surah An-Nas in what feels like English. But by the end of the page, your brain has absorbed Rabb, Malik, Ilah, and An-Nas — not because you studied them, but because you read them in context, twelve times, in a text you already emotionally connected with."*
