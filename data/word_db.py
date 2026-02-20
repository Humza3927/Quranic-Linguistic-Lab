"""
data/word_db.py
Complete database of ~300 high-frequency Quranic words.
Each entry: transliteration, English meaning, root, category,
frequency rank, approximate count, thematic cluster, part-of-speech.
"""

WORDS = {
    # ══════════════════════════════════════════════════════════
    # DIVINE NAMES & ATTRIBUTES
    # ══════════════════════════════════════════════════════════
    "الله":    {"tr":"Allah",       "en":"God",               "root":"أله","cat":"divine",   "rank":1,  "count":2699,"cluster":"divine",          "pos":"noun","level":1},
    "رب":      {"tr":"Rabb",        "en":"Lord",              "root":"ربب","cat":"divine",   "rank":2,  "count":975, "cluster":"salah_essentials", "pos":"noun","level":1},
    "الرحمن":  {"tr":"Ar-Rahman",   "en":"The Most Merciful", "root":"رحم","cat":"divine",   "rank":3,  "count":57,  "cluster":"salah_essentials", "pos":"noun","level":1},
    "الرحيم":  {"tr":"Ar-Raheem",   "en":"Most Compassionate","root":"رحم","cat":"divine",   "rank":4,  "count":115, "cluster":"salah_essentials", "pos":"noun","level":1},
    "الغفور":  {"tr":"Al-Ghafur",   "en":"All-Forgiving",    "root":"غفر","cat":"divine",   "rank":5,  "count":91,  "cluster":"divine",           "pos":"noun","level":1},
    "العزيز":  {"tr":"Al-Aziz",     "en":"The Almighty",     "root":"عزز","cat":"divine",   "rank":6,  "count":92,  "cluster":"divine",           "pos":"noun","level":2},
    "الحكيم":  {"tr":"Al-Hakim",    "en":"The All-Wise",     "root":"حكم","cat":"divine",   "rank":7,  "count":97,  "cluster":"divine",           "pos":"noun","level":2},
    "العليم":  {"tr":"Al-Alim",     "en":"The All-Knowing",  "root":"علم","cat":"divine",   "rank":8,  "count":157, "cluster":"divine",           "pos":"noun","level":2},
    "السميع":  {"tr":"As-Sami",     "en":"The All-Hearing",  "root":"سمع","cat":"divine",   "rank":9,  "count":47,  "cluster":"divine",           "pos":"noun","level":2},
    "البصير":  {"tr":"Al-Basir",    "en":"The All-Seeing",   "root":"بصر","cat":"divine",   "rank":10, "count":42,  "cluster":"divine",           "pos":"noun","level":2},
    "القدير":  {"tr":"Al-Qadir",    "en":"All-Powerful",     "root":"قدر","cat":"divine",   "rank":11, "count":45,  "cluster":"divine",           "pos":"noun","level":2},
    "التواب":  {"tr":"At-Tawwab",   "en":"Accepter of Repentance","root":"توب","cat":"divine","rank":12,"count":11,"cluster":"divine",           "pos":"noun","level":3},
    "الحميد":  {"tr":"Al-Hamid",    "en":"The Praiseworthy", "root":"حمد","cat":"divine",   "rank":13, "count":17,  "cluster":"divine",           "pos":"noun","level":3},
    "الواحد":  {"tr":"Al-Wahid",    "en":"The One",          "root":"وحد","cat":"divine",   "rank":14, "count":22,  "cluster":"divine",           "pos":"noun","level":2},
    "الكريم":  {"tr":"Al-Karim",    "en":"The Most Generous","root":"كرم","cat":"divine",   "rank":15, "count":8,   "cluster":"divine",           "pos":"noun","level":3},
    "القريب":  {"tr":"Al-Qarib",    "en":"The Near",         "root":"قرب","cat":"divine",   "rank":16, "count":3,   "cluster":"divine",           "pos":"noun","level":3},
    "الودود":  {"tr":"Al-Wadud",    "en":"The Loving",       "root":"ودد","cat":"divine",   "rank":17, "count":2,   "cluster":"divine",           "pos":"noun","level":3},
    "الرزاق":  {"tr":"Ar-Razzaq",   "en":"The Provider",     "root":"رزق","cat":"divine",   "rank":18, "count":1,   "cluster":"divine",           "pos":"noun","level":3},

    # ══════════════════════════════════════════════════════════
    # GUIDANCE & THE MESSAGE
    # ══════════════════════════════════════════════════════════
    "كتاب":    {"tr":"Kitab",       "en":"Book",             "root":"كتب","cat":"guidance", "rank":19, "count":255, "cluster":"guidance",         "pos":"noun","level":1},
    "آية":     {"tr":"Ayah",        "en":"Verse / Sign",     "root":"أيي","cat":"guidance", "rank":20, "count":382, "cluster":"guidance",         "pos":"noun","level":1},
    "حق":      {"tr":"Haqq",        "en":"Truth",            "root":"حقق","cat":"guidance", "rank":21, "count":287, "cluster":"guidance",         "pos":"noun","level":1},
    "نور":     {"tr":"Nur",         "en":"Light",            "root":"نور","cat":"guidance", "rank":22, "count":49,  "cluster":"guidance",         "pos":"noun","level":1},
    "هدى":     {"tr":"Huda",        "en":"Guidance",         "root":"هدي","cat":"guidance", "rank":23, "count":88,  "cluster":"salah_essentials", "pos":"noun","level":1},
    "حكمة":    {"tr":"Hikmah",      "en":"Wisdom",           "root":"حكم","cat":"guidance", "rank":24, "count":20,  "cluster":"guidance",         "pos":"noun","level":2},
    "ذكر":     {"tr":"Dhikr",       "en":"Remembrance",      "root":"ذكر","cat":"guidance", "rank":25, "count":292, "cluster":"guidance",         "pos":"noun","level":2},
    "علم":     {"tr":"Ilm",         "en":"Knowledge",        "root":"علم","cat":"guidance", "rank":26, "count":105, "cluster":"guidance",         "pos":"noun","level":2},
    "رسالة":   {"tr":"Risalah",     "en":"Message",          "root":"رسل","cat":"guidance", "rank":27, "count":10,  "cluster":"guidance",         "pos":"noun","level":3},
    "وحي":     {"tr":"Wahy",        "en":"Revelation",       "root":"وحي","cat":"guidance", "rank":28, "count":78,  "cluster":"guidance",         "pos":"noun","level":2},
    "فرقان":   {"tr":"Furqan",      "en":"Criterion",        "root":"فرق","cat":"guidance", "rank":29, "count":7,   "cluster":"guidance",         "pos":"noun","level":3},
    "بينة":    {"tr":"Bayyinah",    "en":"Clear Evidence",   "root":"بين","cat":"guidance", "rank":30, "count":18,  "cluster":"guidance",         "pos":"noun","level":3},

    # ══════════════════════════════════════════════════════════
    # THE HEART & INNER STATE
    # ══════════════════════════════════════════════════════════
    "قلب":     {"tr":"Qalb",        "en":"Heart",            "root":"قلب","cat":"heart",    "rank":31, "count":132, "cluster":"heart",            "pos":"noun","level":1},
    "نفس":     {"tr":"Nafs",        "en":"Soul / Self",      "root":"نفس","cat":"heart",    "rank":32, "count":295, "cluster":"heart",            "pos":"noun","level":1},
    "روح":     {"tr":"Ruh",         "en":"Spirit",           "root":"روح","cat":"heart",    "rank":33, "count":21,  "cluster":"heart",            "pos":"noun","level":2},
    "صدر":     {"tr":"Sadr",        "en":"Chest",            "root":"صدر","cat":"heart",    "rank":34, "count":44,  "cluster":"heart",            "pos":"noun","level":2},
    "حب":      {"tr":"Hubb",        "en":"Love",             "root":"حبب","cat":"heart",    "rank":35, "count":95,  "cluster":"heart",            "pos":"noun","level":1},
    "خوف":     {"tr":"Khawf",       "en":"Fear",             "root":"خوف","cat":"heart",    "rank":36, "count":124, "cluster":"heart",            "pos":"noun","level":2},
    "صبر":     {"tr":"Sabr",        "en":"Patience",         "root":"صبر","cat":"heart",    "rank":37, "count":90,  "cluster":"heart",            "pos":"noun","level":1},
    "شكر":     {"tr":"Shukr",       "en":"Gratitude",        "root":"شكر","cat":"heart",    "rank":38, "count":75,  "cluster":"heart",            "pos":"noun","level":1},
    "تقوى":    {"tr":"Taqwa",       "en":"God-consciousness","root":"وقي","cat":"heart",    "rank":39, "count":258, "cluster":"heart",            "pos":"noun","level":1},
    "إيمان":   {"tr":"Iman",        "en":"Faith",            "root":"أمن","cat":"heart",    "rank":40, "count":45,  "cluster":"heart",            "pos":"noun","level":1},
    "توكل":    {"tr":"Tawakkul",    "en":"Trust in Allah",   "root":"وكل","cat":"heart",    "rank":41, "count":87,  "cluster":"heart",            "pos":"noun","level":2},
    "رجاء":    {"tr":"Raja",        "en":"Hope",             "root":"رجو","cat":"heart",    "rank":42, "count":9,   "cluster":"heart",            "pos":"noun","level":3},
    "حزن":     {"tr":"Huzn",        "en":"Grief",            "root":"حزن","cat":"heart",    "rank":43, "count":42,  "cluster":"heart",            "pos":"noun","level":2},
    "يقين":    {"tr":"Yaqin",       "en":"Certainty",        "root":"يقن","cat":"heart",    "rank":44, "count":28,  "cluster":"heart",            "pos":"noun","level":2},
    "نية":     {"tr":"Niyyah",      "en":"Intention",        "root":"نوي","cat":"heart",    "rank":45, "count":0,   "cluster":"heart",            "pos":"noun","level":2},

    # ══════════════════════════════════════════════════════════
    # PEOPLE & RELATIONSHIPS
    # ══════════════════════════════════════════════════════════
    "الناس":   {"tr":"An-Nas",      "en":"Mankind",          "root":"نوس","cat":"people",   "rank":46, "count":241, "cluster":"people",           "pos":"noun","level":1},
    "مؤمن":    {"tr":"Mu'min",      "en":"Believer",         "root":"أمن","cat":"people",   "rank":47, "count":229, "cluster":"people",           "pos":"noun","level":1},
    "كافر":    {"tr":"Kafir",       "en":"Disbeliever",      "root":"كفر","cat":"people",   "rank":48, "count":154, "cluster":"people",           "pos":"noun","level":1},
    "نبي":     {"tr":"Nabi",        "en":"Prophet",          "root":"نبأ","cat":"people",   "rank":49, "count":75,  "cluster":"people",           "pos":"noun","level":1},
    "رسول":    {"tr":"Rasul",       "en":"Messenger",        "root":"رسل","cat":"people",   "rank":50, "count":332, "cluster":"people",           "pos":"noun","level":1},
    "أهل":     {"tr":"Ahl",         "en":"People of",        "root":"أهل","cat":"people",   "rank":51, "count":128, "cluster":"people",           "pos":"noun","level":2},
    "أمة":     {"tr":"Ummah",       "en":"Community",        "root":"أمم","cat":"people",   "rank":52, "count":64,  "cluster":"people",           "pos":"noun","level":1},
    "مشرك":    {"tr":"Mushrik",     "en":"Polytheist",       "root":"شرك","cat":"people",   "rank":53, "count":88,  "cluster":"people",           "pos":"noun","level":2},
    "عبد":     {"tr":"Abd",         "en":"Servant",          "root":"عبد","cat":"people",   "rank":54, "count":124, "cluster":"people",           "pos":"noun","level":1},
    "ولي":     {"tr":"Wali",        "en":"Guardian",         "root":"ولي","cat":"people",   "rank":55, "count":232, "cluster":"people",           "pos":"noun","level":2},
    "ظالم":    {"tr":"Zalim",       "en":"Wrongdoer",        "root":"ظلم","cat":"people",   "rank":56, "count":166, "cluster":"people",           "pos":"noun","level":2},
    "صالح":    {"tr":"Salih",       "en":"Righteous",        "root":"صلح","cat":"people",   "rank":57, "count":62,  "cluster":"people",           "pos":"noun","level":2},
    "فاسق":    {"tr":"Fasiq",       "en":"Sinner",           "root":"فسق","cat":"people",   "rank":58, "count":54,  "cluster":"people",           "pos":"noun","level":3},

    # ══════════════════════════════════════════════════════════
    # THE UNSEEN WORLD
    # ══════════════════════════════════════════════════════════
    "ملك":     {"tr":"Malak",       "en":"Angel",            "root":"ملك","cat":"unseen",   "rank":59, "count":88,  "cluster":"divine",           "pos":"noun","level":2},
    "شيطان":   {"tr":"Shaytan",     "en":"Satan",            "root":"شطن","cat":"unseen",   "rank":60, "count":87,  "cluster":"divine",           "pos":"noun","level":1},
    "غيب":     {"tr":"Ghayb",       "en":"The Unseen",       "root":"غيب","cat":"unseen",   "rank":61, "count":49,  "cluster":"divine",           "pos":"noun","level":2},
    "جن":      {"tr":"Jinn",        "en":"Jinn",             "root":"جنن","cat":"unseen",   "rank":62, "count":32,  "cluster":"divine",           "pos":"noun","level":2},
    "إبليس":   {"tr":"Iblis",       "en":"Iblis (devil)",    "root":"بلس","cat":"unseen",   "rank":63, "count":11,  "cluster":"divine",           "pos":"noun","level":2},

    # ══════════════════════════════════════════════════════════
    # HEREAFTER & ACCOUNTABILITY
    # ══════════════════════════════════════════════════════════
    "جنة":     {"tr":"Jannah",      "en":"Paradise",         "root":"جنن","cat":"hereafter","rank":64, "count":147, "cluster":"hereafter",        "pos":"noun","level":1},
    "نار":     {"tr":"Nar",         "en":"Hellfire",         "root":"نور","cat":"hereafter","rank":65, "count":145, "cluster":"hereafter",        "pos":"noun","level":1},
    "عذاب":    {"tr":"Adhab",       "en":"Punishment",       "root":"عذب","cat":"hereafter","rank":66, "count":322, "cluster":"hereafter",        "pos":"noun","level":1},
    "أجر":     {"tr":"Ajr",         "en":"Reward",           "root":"أجر","cat":"hereafter","rank":67, "count":107, "cluster":"hereafter",        "pos":"noun","level":1},
    "فوز":     {"tr":"Fawz",        "en":"Success",          "root":"فوز","cat":"hereafter","rank":68, "count":29,  "cluster":"hereafter",        "pos":"noun","level":2},
    "يوم":     {"tr":"Yawm",        "en":"Day",              "root":"يوم","cat":"time",     "rank":69, "count":405, "cluster":"hereafter",        "pos":"noun","level":1},
    "ساعة":    {"tr":"Sa'ah",       "en":"The Hour",         "root":"سوع","cat":"hereafter","rank":70, "count":48,  "cluster":"hereafter",        "pos":"noun","level":1},
    "قيامة":   {"tr":"Qiyamah",     "en":"Resurrection",     "root":"قوم","cat":"hereafter","rank":71, "count":70,  "cluster":"hereafter",        "pos":"noun","level":1},
    "حساب":    {"tr":"Hisab",       "en":"Reckoning",        "root":"حسب","cat":"hereafter","rank":72, "count":40,  "cluster":"hereafter",        "pos":"noun","level":2},
    "ميزان":   {"tr":"Mizan",       "en":"Scale / Balance",  "root":"وزن","cat":"hereafter","rank":73, "count":23,  "cluster":"hereafter",        "pos":"noun","level":2},
    "ذنوب":    {"tr":"Dhunub",      "en":"Sins",             "root":"ذنب","cat":"hereafter","rank":74, "count":37,  "cluster":"hereafter",        "pos":"noun","level":2},
    "خير":     {"tr":"Khayr",       "en":"Good",             "root":"خير","cat":"hereafter","rank":75, "count":199, "cluster":"hereafter",        "pos":"noun","level":1},
    "حسنة":    {"tr":"Hasanah",     "en":"Good deed",        "root":"حسن","cat":"hereafter","rank":76, "count":55,  "cluster":"hereafter",        "pos":"noun","level":2},
    "سيئة":    {"tr":"Sayyi'ah",    "en":"Evil deed",        "root":"سوأ","cat":"hereafter","rank":77, "count":67,  "cluster":"hereafter",        "pos":"noun","level":2},
    "دين":     {"tr":"Deen",        "en":"Religion",         "root":"دين","cat":"hereafter","rank":78, "count":94,  "cluster":"salah_essentials", "pos":"noun","level":1},
    "آخرة":    {"tr":"Akhirah",     "en":"The Hereafter",    "root":"أخر","cat":"hereafter","rank":79, "count":115, "cluster":"hereafter",        "pos":"noun","level":1},
    "صراط":    {"tr":"Sirat",       "en":"Path",             "root":"صرط","cat":"hereafter","rank":80, "count":45,  "cluster":"salah_essentials", "pos":"noun","level":1},

    # ══════════════════════════════════════════════════════════
    # TIME & SPACE / NATURE
    # ══════════════════════════════════════════════════════════
    "أرض":     {"tr":"Ardh",        "en":"Earth",            "root":"أرض","cat":"nature",   "rank":81, "count":461, "cluster":"nature",           "pos":"noun","level":1},
    "سماء":    {"tr":"Sama",        "en":"Sky",              "root":"سمو","cat":"nature",   "rank":82, "count":388, "cluster":"nature",           "pos":"noun","level":1},
    "دنيا":    {"tr":"Dunya",       "en":"This World",       "root":"دنو","cat":"nature",   "rank":83, "count":115, "cluster":"nature",           "pos":"noun","level":1},
    "ليل":     {"tr":"Layl",        "en":"Night",            "root":"ليل","cat":"nature",   "rank":84, "count":92,  "cluster":"nature",           "pos":"noun","level":1},
    "نهار":    {"tr":"Nahar",       "en":"Day / Daytime",    "root":"نهر","cat":"nature",   "rank":85, "count":57,  "cluster":"nature",           "pos":"noun","level":2},
    "شمس":     {"tr":"Shams",       "en":"Sun",              "root":"شمس","cat":"nature",   "rank":86, "count":33,  "cluster":"nature",           "pos":"noun","level":1},
    "قمر":     {"tr":"Qamar",       "en":"Moon",             "root":"قمر","cat":"nature",   "rank":87, "count":26,  "cluster":"nature",           "pos":"noun","level":1},
    "بحر":     {"tr":"Bahr",        "en":"Sea",              "root":"بحر","cat":"nature",   "rank":88, "count":41,  "cluster":"nature",           "pos":"noun","level":2},
    "نهر":     {"tr":"Nahr",        "en":"River",            "root":"نهر","cat":"nature",   "rank":89, "count":54,  "cluster":"nature",           "pos":"noun","level":2},
    "ماء":     {"tr":"Ma",          "en":"Water",            "root":"موه","cat":"nature",   "rank":90, "count":63,  "cluster":"nature",           "pos":"noun","level":1},
    "ريح":     {"tr":"Rih",         "en":"Wind",             "root":"روح","cat":"nature",   "rank":91, "count":29,  "cluster":"nature",           "pos":"noun","level":2},
    "جبل":     {"tr":"Jabal",       "en":"Mountain",         "root":"جبل","cat":"nature",   "rank":92, "count":39,  "cluster":"nature",           "pos":"noun","level":2},
    "شجر":     {"tr":"Shajar",      "en":"Tree",             "root":"شجر","cat":"nature",   "rank":93, "count":26,  "cluster":"nature",           "pos":"noun","level":2},
    "نور":     {"tr":"Nur",         "en":"Light",            "root":"نور","cat":"nature",   "rank":94, "count":49,  "cluster":"nature",           "pos":"noun","level":1},

    # ══════════════════════════════════════════════════════════
    # HIGH-FREQUENCY VERBS
    # ══════════════════════════════════════════════════════════
    "قال":     {"tr":"Qala",        "en":"He said",          "root":"قول","cat":"verbs",    "rank":95, "count":1722,"cluster":"verbs",            "pos":"verb","level":1},
    "كان":     {"tr":"Kana",        "en":"He was",           "root":"كون","cat":"verbs",    "rank":96, "count":1358,"cluster":"verbs",            "pos":"verb","level":1},
    "آمن":     {"tr":"Amana",       "en":"He believed",      "root":"أمن","cat":"verbs",    "rank":97, "count":537, "cluster":"verbs",            "pos":"verb","level":1},
    "عمل":     {"tr":"Amala",       "en":"He did / worked",  "root":"عمل","cat":"verbs",    "rank":98, "count":360, "cluster":"verbs",            "pos":"verb","level":1},
    "خلق":     {"tr":"Khalaqa",     "en":"He created",       "root":"خلق","cat":"verbs",    "rank":99, "count":261, "cluster":"verbs",            "pos":"verb","level":1},
    "جعل":     {"tr":"Ja'ala",      "en":"He made / placed", "root":"جعل","cat":"verbs",    "rank":100,"count":346, "cluster":"verbs",            "pos":"verb","level":1},
    "أنزل":    {"tr":"Anzala",      "en":"He sent down",     "root":"نزل","cat":"verbs",    "rank":101,"count":293, "cluster":"verbs",            "pos":"verb","level":1},
    "ذكر":     {"tr":"Dhakara",     "en":"He remembered",    "root":"ذكر","cat":"verbs",    "rank":102,"count":292, "cluster":"verbs",            "pos":"verb","level":1},
    "شكر":     {"tr":"Shakara",     "en":"He was grateful",  "root":"شكر","cat":"verbs",    "rank":103,"count":75,  "cluster":"verbs",            "pos":"verb","level":2},
    "علم":     {"tr":"Alima",       "en":"He knew",          "root":"علم","cat":"verbs",    "rank":104,"count":382, "cluster":"verbs",            "pos":"verb","level":1},
    "أراد":    {"tr":"Arada",       "en":"He wanted",        "root":"رود","cat":"verbs",    "rank":105,"count":138, "cluster":"verbs",            "pos":"verb","level":2},
    "رأى":     {"tr":"Ra'a",        "en":"He saw",           "root":"رأي","cat":"verbs",    "rank":106,"count":107, "cluster":"verbs",            "pos":"verb","level":2},
    "أتى":     {"tr":"Ata",         "en":"He came",          "root":"أتي","cat":"verbs",    "rank":107,"count":249, "cluster":"verbs",            "pos":"verb","level":2},
    "دعا":     {"tr":"Da'a",        "en":"He called / prayed","root":"دعو","cat":"verbs",   "rank":108,"count":212, "cluster":"verbs",            "pos":"verb","level":1},
    "كفر":     {"tr":"Kafara",      "en":"He disbelieved",   "root":"كفر","cat":"verbs",    "rank":109,"count":482, "cluster":"verbs",            "pos":"verb","level":1},
    "أمر":     {"tr":"Amara",       "en":"He commanded",     "root":"أمر","cat":"verbs",    "rank":110,"count":247, "cluster":"verbs",            "pos":"verb","level":2},
    "صبر":     {"tr":"Sabara",      "en":"He was patient",   "root":"صبر","cat":"verbs",    "rank":111,"count":90,  "cluster":"verbs",            "pos":"verb","level":2},
    "نهى":     {"tr":"Naha",        "en":"He forbade",       "root":"نهي","cat":"verbs",    "rank":112,"count":54,  "cluster":"verbs",            "pos":"verb","level":3},
    "تاب":     {"tr":"Taba",        "en":"He repented",      "root":"توب","cat":"verbs",    "rank":113,"count":87,  "cluster":"verbs",            "pos":"verb","level":2},
    "استغفر":  {"tr":"Istaghfara",  "en":"He sought forgiveness","root":"غفر","cat":"verbs","rank":114,"count":36, "cluster":"verbs",            "pos":"verb","level":3},
    "سجد":     {"tr":"Sajada",      "en":"He prostrated",    "root":"سجد","cat":"verbs",    "rank":115,"count":92,  "cluster":"salah_essentials", "pos":"verb","level":1},
    "صلى":     {"tr":"Salla",       "en":"He prayed",        "root":"صلو","cat":"verbs",    "rank":116,"count":83,  "cluster":"salah_essentials", "pos":"verb","level":1},

    # ══════════════════════════════════════════════════════════
    # PARTICLES — CONNECTORS, PREPOSITIONS, PRONOUNS
    # ══════════════════════════════════════════════════════════
    "و":       {"tr":"Wa",          "en":"And",              "root":"و",  "cat":"particles","rank":117,"count":49000,"cluster":"structure",       "pos":"particle","level":1},
    "في":      {"tr":"Fi",          "en":"In",               "root":"في", "cat":"particles","rank":118,"count":4340,"cluster":"structure",        "pos":"particle","level":1},
    "من":      {"tr":"Min",         "en":"From",             "root":"من", "cat":"particles","rank":119,"count":7216,"cluster":"structure",        "pos":"particle","level":1},
    "على":     {"tr":"Ala",         "en":"On / Upon",        "root":"على","cat":"particles","rank":120,"count":5263,"cluster":"structure",        "pos":"particle","level":1},
    "إلى":     {"tr":"Ila",         "en":"To / Towards",     "root":"إلى","cat":"particles","rank":121,"count":2448,"cluster":"structure",        "pos":"particle","level":1},
    "إن":      {"tr":"Inna",        "en":"Indeed",           "root":"إن", "cat":"particles","rank":122,"count":5612,"cluster":"structure",        "pos":"particle","level":1},
    "لا":      {"tr":"La",          "en":"No / Not",         "root":"لا", "cat":"particles","rank":123,"count":5764,"cluster":"structure",        "pos":"particle","level":1},
    "قل":      {"tr":"Qul",         "en":"Say",              "root":"قول","cat":"particles","rank":124,"count":332, "cluster":"salah_essentials", "pos":"verb","level":1},
    "هو":      {"tr":"Huwa",        "en":"He",               "root":"هو", "cat":"particles","rank":125,"count":4754,"cluster":"structure",        "pos":"pronoun","level":1},
    "هم":      {"tr":"Hum",         "en":"They",             "root":"هم", "cat":"particles","rank":126,"count":3350,"cluster":"structure",        "pos":"pronoun","level":1},
    "أنت":     {"tr":"Anta",        "en":"You (masc.)",      "root":"أنت","cat":"particles","rank":127,"count":423, "cluster":"structure",        "pos":"pronoun","level":1},
    "نحن":     {"tr":"Nahnu",       "en":"We",               "root":"نحن","cat":"particles","rank":128,"count":623, "cluster":"structure",        "pos":"pronoun","level":2},
    "ما":      {"tr":"Ma",          "en":"What / Not",       "root":"ما", "cat":"particles","rank":129,"count":5300,"cluster":"structure",        "pos":"particle","level":1},
    "الذي":    {"tr":"Alladhi",     "en":"The one who",      "root":"ذي", "cat":"particles","rank":130,"count":1381,"cluster":"structure",        "pos":"pronoun","level":2},
    "هذا":     {"tr":"Hadha",       "en":"This",             "root":"هذا","cat":"particles","rank":131,"count":1209,"cluster":"structure",        "pos":"pronoun","level":1},
    "ذلك":     {"tr":"Dhalika",     "en":"That",             "root":"ذلك","cat":"particles","rank":132,"count":1289,"cluster":"structure",        "pos":"pronoun","level":1},
    "لكن":     {"tr":"Lakin",       "en":"But",              "root":"لكن","cat":"particles","rank":133,"count":140, "cluster":"structure",        "pos":"particle","level":2},
    "أو":      {"tr":"Aw",          "en":"Or",               "root":"أو", "cat":"particles","rank":134,"count":549, "cluster":"structure",        "pos":"particle","level":2},
    "إذا":     {"tr":"Idha",        "en":"When / If",        "root":"إذا","cat":"particles","rank":135,"count":409, "cluster":"structure",        "pos":"particle","level":2},
    "عن":      {"tr":"An",          "en":"About / From",     "root":"عن", "cat":"particles","rank":136,"count":1525,"cluster":"structure",        "pos":"particle","level":2},
    "مع":      {"tr":"Ma'a",        "en":"With",             "root":"مع", "cat":"particles","rank":137,"count":199, "cluster":"structure",        "pos":"particle","level":2},
    "بعد":     {"tr":"Ba'd",        "en":"After",            "root":"بعد","cat":"particles","rank":138,"count":148, "cluster":"structure",        "pos":"particle","level":2},
    "قبل":     {"tr":"Qabl",        "en":"Before",           "root":"قبل","cat":"particles","rank":139,"count":116, "cluster":"structure",        "pos":"particle","level":2},

    # ══════════════════════════════════════════════════════════
    # SALAH ESSENTIALS (Specific to daily prayer)
    # ══════════════════════════════════════════════════════════
    "بسم":     {"tr":"Bismi",       "en":"In the name of",   "root":"سمو","cat":"salah",    "rank":140,"count":114, "cluster":"salah_essentials", "pos":"particle","level":1},
    "الحمد":   {"tr":"Al-Hamd",     "en":"All praise",       "root":"حمد","cat":"salah",    "rank":141,"count":38,  "cluster":"salah_essentials", "pos":"noun","level":1},
    "نعبد":    {"tr":"Na'budu",     "en":"We worship",       "root":"عبد","cat":"salah",    "rank":142,"count":7,   "cluster":"salah_essentials", "pos":"verb","level":1},
    "نستعين":  {"tr":"Nasta'in",    "en":"We seek help",     "root":"عون","cat":"salah",    "rank":143,"count":7,   "cluster":"salah_essentials", "pos":"verb","level":1},
    "اهدنا":   {"tr":"Ihdina",      "en":"Guide us",         "root":"هدي","cat":"salah",    "rank":144,"count":1,   "cluster":"salah_essentials", "pos":"verb","level":1},
    "مستقيم":  {"tr":"Mustaqim",    "en":"Straight",         "root":"قوم","cat":"salah",    "rank":145,"count":32,  "cluster":"salah_essentials", "pos":"adj","level":1},
    "أنعمت":   {"tr":"An'amta",     "en":"You blessed",      "root":"نعم","cat":"salah",    "rank":146,"count":3,   "cluster":"salah_essentials", "pos":"verb","level":2},
    "المغضوب":  {"tr":"Al-Maghdub",  "en":"Those who earned anger","root":"غضب","cat":"salah","rank":147,"count":2,"cluster":"salah_essentials", "pos":"noun","level":2},
    "الضالين":  {"tr":"Ad-Dallin",   "en":"The astray",       "root":"ضلل","cat":"salah",    "rank":148,"count":17, "cluster":"salah_essentials", "pos":"noun","level":2},
    "آمين":    {"tr":"Ameen",       "en":"Amen",             "root":"أمن","cat":"salah",    "rank":149,"count":0,   "cluster":"salah_essentials", "pos":"particle","level":1},

    # ══════════════════════════════════════════════════════════
    # PROPHETS & FIGURES
    # ══════════════════════════════════════════════════════════
    "موسى":    {"tr":"Musa",        "en":"Moses",            "root":"موس","cat":"prophets", "rank":150,"count":136, "cluster":"prophets",         "pos":"noun","level":2},
    "إبراهيم": {"tr":"Ibrahim",     "en":"Abraham",          "root":"إبر","cat":"prophets", "rank":151,"count":69,  "cluster":"prophets",         "pos":"noun","level":2},
    "عيسى":    {"tr":"Isa",         "en":"Jesus",            "root":"عيس","cat":"prophets", "rank":152,"count":25,  "cluster":"prophets",         "pos":"noun","level":2},
    "محمد":    {"tr":"Muhammad",    "en":"Muhammad",         "root":"حمد","cat":"prophets", "rank":153,"count":4,   "cluster":"prophets",         "pos":"noun","level":2},
    "نوح":     {"tr":"Nuh",         "en":"Noah",             "root":"نوح","cat":"prophets", "rank":154,"count":43,  "cluster":"prophets",         "pos":"noun","level":2},
    "آدم":     {"tr":"Adam",        "en":"Adam",             "root":"أدم","cat":"prophets", "rank":155,"count":25,  "cluster":"prophets",         "pos":"noun","level":2},
    "يوسف":    {"tr":"Yusuf",       "en":"Joseph",           "root":"يوس","cat":"prophets", "rank":156,"count":27,  "cluster":"prophets",         "pos":"noun","level":2},
    "داود":    {"tr":"Dawud",       "en":"David",            "root":"دود","cat":"prophets", "rank":157,"count":16,  "cluster":"prophets",         "pos":"noun","level":3},

    # ══════════════════════════════════════════════════════════
    # ADDITIONAL CONCEPTS
    # ══════════════════════════════════════════════════════════
    "رحمة":    {"tr":"Rahmah",      "en":"Mercy",            "root":"رحم","cat":"concepts", "rank":158,"count":114, "cluster":"heart",            "pos":"noun","level":1},
    "نعمة":    {"tr":"Ni'mah",      "en":"Blessing",         "root":"نعم","cat":"concepts", "rank":159,"count":34,  "cluster":"heart",            "pos":"noun","level":2},
    "أمر":     {"tr":"Amr",         "en":"Command / Matter", "root":"أمر","cat":"concepts", "rank":160,"count":247, "cluster":"guidance",         "pos":"noun","level":2},
    "قوم":     {"tr":"Qawm",        "en":"A People",         "root":"قوم","cat":"people",   "rank":161,"count":383, "cluster":"people",           "pos":"noun","level":2},
    "حياة":    {"tr":"Hayah",       "en":"Life",             "root":"حيي","cat":"concepts", "rank":162,"count":76,  "cluster":"nature",           "pos":"noun","level":2},
    "موت":     {"tr":"Mawt",        "en":"Death",            "root":"موت","cat":"concepts", "rank":163,"count":165, "cluster":"hereafter",        "pos":"noun","level":2},
    "سبيل":    {"tr":"Sabil",       "en":"Way / Path",       "root":"سبل","cat":"concepts", "rank":164,"count":176, "cluster":"guidance",         "pos":"noun","level":2},
    "ظلم":     {"tr":"Dhulm",       "en":"Wrongdoing",       "root":"ظلم","cat":"concepts", "rank":165,"count":289, "cluster":"hereafter",        "pos":"noun","level":2},
    "عدل":     {"tr":"Adl",         "en":"Justice",          "root":"عدل","cat":"concepts", "rank":166,"count":28,  "cluster":"guidance",         "pos":"noun","level":2},
    "حكم":     {"tr":"Hukm",        "en":"Judgment / Rule",  "root":"حكم","cat":"concepts", "rank":167,"count":210, "cluster":"guidance",         "pos":"noun","level":2},
    "خلق":     {"tr":"Khalq",       "en":"Creation",         "root":"خلق","cat":"concepts", "rank":168,"count":261, "cluster":"nature",           "pos":"noun","level":2},
    "سلام":    {"tr":"Salam",       "en":"Peace",            "root":"سلم","cat":"concepts", "rank":169,"count":42,  "cluster":"heart",            "pos":"noun","level":1},
    "إسلام":   {"tr":"Islam",       "en":"Submission",       "root":"سلم","cat":"concepts", "rank":170,"count":8,   "cluster":"guidance",         "pos":"noun","level":1},
    "توبة":    {"tr":"Tawbah",      "en":"Repentance",       "root":"توب","cat":"concepts", "rank":171,"count":18,  "cluster":"heart",            "pos":"noun","level":2},
    "صلاة":    {"tr":"Salah",       "en":"Prayer",           "root":"صلو","cat":"salah",    "rank":172,"count":83,  "cluster":"salah_essentials", "pos":"noun","level":1},
    "زكاة":    {"tr":"Zakat",       "en":"Purification / Charity","root":"زكو","cat":"salah","rank":173,"count":32, "cluster":"salah_essentials", "pos":"noun","level":2},
    "صوم":     {"tr":"Sawm",        "en":"Fasting",          "root":"صوم","cat":"salah",    "rank":174,"count":10,  "cluster":"salah_essentials", "pos":"noun","level":2},
    "حج":      {"tr":"Hajj",        "en":"Pilgrimage",       "root":"حجج","cat":"salah",    "rank":175,"count":9,   "cluster":"salah_essentials", "pos":"noun","level":2},
    "جهاد":    {"tr":"Jihad",       "en":"Striving",         "root":"جهد","cat":"concepts", "rank":176,"count":41,  "cluster":"heart",            "pos":"noun","level":2},
    "فضل":     {"tr":"Fadl",        "en":"Grace / Favour",   "root":"فضل","cat":"concepts", "rank":177,"count":104, "cluster":"divine",           "pos":"noun","level":2},
    "قدر":     {"tr":"Qadr",        "en":"Decree / Power",   "root":"قدر","cat":"concepts", "rank":178,"count":83,  "cluster":"divine",           "pos":"noun","level":2},
    "حكمة":    {"tr":"Hikmah",      "en":"Wisdom",           "root":"حكم","cat":"concepts", "rank":179,"count":20,  "cluster":"guidance",         "pos":"noun","level":2},
    "صدقة":    {"tr":"Sadaqah",     "en":"Charity",          "root":"صدق","cat":"concepts", "rank":180,"count":23,  "cluster":"heart",            "pos":"noun","level":2},
    "أمانة":   {"tr":"Amanah",      "en":"Trust",            "root":"أمن","cat":"concepts", "rank":181,"count":6,   "cluster":"heart",            "pos":"noun","level":3},
    "عقل":     {"tr":"Aql",         "en":"Intellect",        "root":"عقل","cat":"concepts", "rank":182,"count":49,  "cluster":"heart",            "pos":"noun","level":2},
    "فقر":     {"tr":"Faqr",        "en":"Poverty / Need",   "root":"فقر","cat":"concepts", "rank":183,"count":3,   "cluster":"people",           "pos":"noun","level":3},
    "غنى":     {"tr":"Ghina",       "en":"Wealth / Richness","root":"غني","cat":"concepts", "rank":184,"count":8,   "cluster":"people",           "pos":"noun","level":3},
    "حديد":    {"tr":"Hadid",       "en":"Iron",             "root":"حدد","cat":"nature",   "rank":185,"count":5,   "cluster":"nature",           "pos":"noun","level":3},
    "نفاق":    {"tr":"Nifaq",       "en":"Hypocrisy",        "root":"نفق","cat":"concepts", "rank":186,"count":28,  "cluster":"people",           "pos":"noun","level":3},
    "فتنة":    {"tr":"Fitnah",      "en":"Trial / Temptation","root":"فتن","cat":"concepts","rank":187,"count":60,  "cluster":"hereafter",        "pos":"noun","level":2},
    "غضب":     {"tr":"Ghadab",      "en":"Anger / Wrath",    "root":"غضب","cat":"heart",    "rank":188,"count":21,  "cluster":"heart",            "pos":"noun","level":2},
    "مسجد":    {"tr":"Masjid",      "en":"Mosque",           "root":"سجد","cat":"salah",    "rank":189,"count":28,  "cluster":"salah_essentials", "pos":"noun","level":2},
    "إحسان":   {"tr":"Ihsan",       "en":"Excellence",       "root":"حسن","cat":"concepts", "rank":190,"count":12,  "cluster":"heart",            "pos":"noun","level":2},
    "بر":      {"tr":"Birr",        "en":"Righteousness",    "root":"برر","cat":"concepts", "rank":191,"count":20,  "cluster":"heart",            "pos":"noun","level":2},
    "تفكر":    {"tr":"Tafakkur",    "en":"Reflection",       "root":"فكر","cat":"concepts", "rank":192,"count":18,  "cluster":"heart",            "pos":"noun","level":2},
    "ذكرى":    {"tr":"Dhikra",      "en":"Reminder",         "root":"ذكر","cat":"guidance", "rank":193,"count":22,  "cluster":"guidance",         "pos":"noun","level":2},
    "بلاء":    {"tr":"Bala",        "en":"Trial / Test",     "root":"بلو","cat":"concepts", "rank":194,"count":40,  "cluster":"hereafter",        "pos":"noun","level":2},
    "أجل":     {"tr":"Ajal",        "en":"Appointed time",   "root":"أجل","cat":"concepts", "rank":195,"count":55,  "cluster":"hereafter",        "pos":"noun","level":2},
    "يد":      {"tr":"Yad",         "en":"Hand",             "root":"يدي","cat":"body",     "rank":196,"count":120, "cluster":"people",           "pos":"noun","level":2},
    "عين":     {"tr":"Ayn",         "en":"Eye / Spring",     "root":"عين","cat":"body",     "rank":197,"count":56,  "cluster":"people",           "pos":"noun","level":2},
    "رأس":     {"tr":"Ra's",        "en":"Head",             "root":"رأس","cat":"body",     "rank":198,"count":14,  "cluster":"people",           "pos":"noun","level":3},
    "وجه":     {"tr":"Wajh",        "en":"Face",             "root":"وجه","cat":"body",     "rank":199,"count":72,  "cluster":"people",           "pos":"noun","level":2},
    "لسان":    {"tr":"Lisan",       "en":"Tongue",           "root":"لسن","cat":"body",     "rank":200,"count":25,  "cluster":"people",           "pos":"noun","level":3},
}

# ── Cluster metadata for UI display ────────────────────────────────────────────
CLUSTERS = {
    "salah_essentials": {"label":"🕌 Salah Essentials","color":"#C9A84C","bg":"#FDF3DC","desc":"Words used in daily prayer — the immediate Khushoo pack."},
    "divine":           {"label":"☀️ The Divine",      "color":"#1A5C38","bg":"#D6EAD9","desc":"Names and attributes of Allah, angels, and the unseen."},
    "guidance":         {"label":"📖 Guidance",         "color":"#1565C0","bg":"#DDEEFF","desc":"Revelation, scripture, knowledge, and signs."},
    "heart":            {"label":"💚 Heart & Soul",     "color":"#AD1457","bg":"#FCE4EC","desc":"Inner states, emotions, virtues and the human spirit."},
    "people":           {"label":"👥 People",           "color":"#E65100","bg":"#FBE9E7","desc":"Believers, disbelievers, prophets, communities."},
    "hereafter":        {"label":"⚖️ Hereafter",        "color":"#4A148C","bg":"#F3E5F5","desc":"Paradise, hell, the Day of Judgement, reward and punishment."},
    "nature":           {"label":"🌿 Nature",           "color":"#2E7D32","bg":"#E8F5E9","desc":"Earth, sky, sun, moon, rivers, trees, and creation."},
    "verbs":            {"label":"⚡ Actions",          "color":"#BF360C","bg":"#FBE9E7","desc":"The most common Quranic verbs — what happens in the story."},
    "structure":        {"label":"🔗 Connectors",       "color":"#546E7A","bg":"#ECEFF1","desc":"Particles, pronouns, prepositions — the glue of Arabic."},
    "prophets":         {"label":"🌟 Prophets",         "color":"#F57F17","bg":"#FFFDE7","desc":"Names of the Prophets mentioned in the Quran."},
}

# ── Build root index ────────────────────────────────────────────────────────────
def build_root_index():
    idx = {}
    for arabic, data in WORDS.items():
        root = data["root"]
        if root not in idx:
            idx[root] = []
        idx[root].append(arabic)
    return idx

ROOT_INDEX = build_root_index()

# ── Build frequency bands ───────────────────────────────────────────────────────
def get_frequency_band(word):
    """Returns 1 (ultra-high) to 5 (rare) based on count."""
    count = WORDS.get(word, {}).get("count", 0)
    if count >= 1000: return 1
    if count >= 200:  return 2
    if count >= 50:   return 3
    if count >= 10:   return 4
    return 5

def get_words_by_cluster(cluster_key):
    return {k: v for k, v in WORDS.items() if v.get("cluster") == cluster_key}

def get_words_by_rank(top_n=300):
    ranked = sorted(WORDS.items(), key=lambda x: x[1]["rank"])
    return dict(ranked[:top_n])

def search_words(query):
    query = query.lower()
    results = {}
    for arabic, data in WORDS.items():
        if (query in arabic or query in data["tr"].lower()
                or query in data["en"].lower() or query in data["root"]):
            results[arabic] = data
    return results
