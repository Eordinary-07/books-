# 📚 RTMNU B.Tech Electrical (NEP) + GATE EE — Book Library

A structured study library built from **your** book list (RTMNU B.Tech Electrical, NEP, up to Semester 5 + GATE EE).

Books are organised exactly the way you grouped them: **dual-purpose (RTMNU + GATE) → GATE-only → RTMNU-only**.

---

## ⚠️ Read this first — what this library is (and isn't)

**What it isn't:** a collection of pirated PDFs. Almost every title on your list is an **in-copyright commercial textbook** — Bimbhra's *Electrical Machinery* (Khanna), Kothari & Nagrath's *Modern Power System Analysis* (McGraw-Hill), Oppenheim's *Signals and Systems* (Pearson), the Kanodia GATE practice books (Nodia). **No legal free edition of these exists anywhere.** Sites offering them are distributing pirated scans, and those files routinely carry malware or are truncated OCR garbage.

**What it is:** every book on your list is catalogued here with its author, publisher and purpose — plus, for each subject, the **best legally free equivalent** (NPTEL, MIT OCW, OpenStax, author-released open textbooks), and concrete free books that are **already downloaded into this repo for you**.

> **Bottom line:** you can study every single subject on your list for ₹0 using the free resources here. When you can afford it, buy the 3–4 genuinely load-bearing books (marked 🏆 below). Don't waste money on the rest.

---

## 🚀 Start here

| I want to… | Go to |
|---|---|
| Know how to use this library | [`00-Start-Here/README.md`](00-Start-Here/README.md) |
| Understand the copyright situation | [`00-Start-Here/WHY-NOT-EVERY-BOOK.md`](00-Start-Here/WHY-NOT-EVERY-BOOK.md) |
| **Read these books free & legally (Internet Archive, NDLI)** | [`00-Start-Here/LEGAL-FREE-ACCESS.md`](00-Start-Here/LEGAL-FREE-ACCESS.md) |
| See every book on my list in one table | [`catalog.csv`](catalog.csv) |
| Download the rest of the free books | run `python3 tools/fetch_books.py` on your own machine |
| Find the 6 free books already here | [`00-Common-Library/`](00-Common-Library/) |

---

## 📖 Free books already downloaded into this repo ✅

These are **legally redistributable** and are committed here — open them right now.

### *Lessons In Electric Circuits* — Tony R. Kuphaldt (Design Science License)
The single most useful free EE set that exists. **2,779 pages, fully worked, no paywall.**

| Volume | Pages | Covers | Maps to your subject |
|---|---|---|---|
| [Vol 1 — DC](00-Common-Library/Lessons-in-Electric-Circuits/LEC-Vol1-DC-Circuits.pdf) | 557 | Ohm's law, series/parallel, network theorems, DC metering | **Electric Circuits**, **Measurements** |
| [Vol 2 — AC](00-Common-Library/Lessons-in-Electric-Circuits/LEC-Vol2-AC-Circuits.pdf) | 574 | Reactance, impedance, resonance, filters, transformers, polyphase | **Electric Circuits**, **Power Systems** |
| [Vol 3 — Semiconductors](00-Common-Library/Lessons-in-Electric-Circuits/LEC-Vol3-Semiconductors.pdf) | 535 | Diodes, BJT/FET, amplifiers, op-amps, active filters, oscillators | **Analog Electronics** |
| [Vol 4 — Digital](00-Common-Library/Lessons-in-Electric-Circuits/LEC-Vol4-Digital.pdf) | 516 | Number systems, Boolean algebra, K-maps, counters, ADC/DAC, logic families | **Digital Electronics** ⭐ |
| [Vol 5 — Reference](00-Common-Library/Lessons-in-Electric-Circuits/LEC-Vol5-Reference.pdf) | 172 | Component data, troubleshooting reference | **Measurements** |
| [Vol 6 — Experiments](00-Common-Library/Lessons-in-Electric-Circuits/LEC-Vol6-Experiments.pdf) | 425 | Full lab manual | Lab / practicals |

### Other free books in this repo

| Book | Author | Covers | Location |
|---|---|---|---|
| **Think DSP** (PDF + EPUB) | Allen B. Downey | Signals, spectra, sampling, convolution, DFT — CC BY-NC | [`02-GATE-only/05-Signals-and-Systems/free-books/`](02-GATE-only/05-Signals-and-Systems/free-books/) |
| **Physical Modeling in MATLAB** | Allen B. Downey | MATLAB programming + simulation — CC BY-NC | [`03-RTMNU-only/13-Programming-Techniques-and-Simulation/free-books/`](03-RTMNU-only/13-Programming-Techniques-and-Simulation/free-books/) |
| **Think Python** | Allen B. Downey | Programming fundamentals — CC BY-NC | [`03-RTMNU-only/13-Programming-Techniques-and-Simulation/free-books/`](03-RTMNU-only/13-Programming-Techniques-and-Simulation/free-books/) |

---

## 🗂️ Library structure

```
books-/
├── README.md                          ← you are here
├── catalog.csv                        ← every book on your list: author, publisher, availability
├── 00-Start-Here/                     ← how to use this library + the copyright explainer
├── 00-Common-Library/                 ← multi-subject free books (Lessons In Electric Circuits)
├── 01-RTMNU-plus-GATE/                ← ⭐ PART 1: dual-purpose subjects
│   ├── 01-Electrical-Machines/
│   ├── 02-Power-Systems/
│   └── 03-Digital-Electronics/
├── 02-GATE-only/                      ← 🎯 PART 2: GATE-only subjects
│   ├── 04-Engineering-Mathematics/
│   ├── 05-Signals-and-Systems/
│   ├── 06-Electric-Circuits-Network-Theory/
│   ├── 07-Electromagnetic-Fields/
│   ├── 08-Analog-Electronics/
│   └── 09-Electrical-Electronic-Measurements/
├── 03-RTMNU-only/                     ← 🏫 PART 3: university-only, zero GATE value
│   ├── 10-Electrical-Power-Utilization/
│   ├── 11-PLC-and-SCADA/
│   ├── 12-Electrical-Machine-Design/
│   └── 13-Programming-Techniques-and-Simulation/
└── tools/
    └── fetch_books.py                 ← downloads the remaining free books on your machine
```

Every subject folder contains a `README.md` with:
- The books from your list (author, publisher, purpose, whether a legal free copy exists)
- **Free & legal substitutes** for that specific subject, with links
- A suggested study order

---

## 🏆 If you can only buy a few books, buy these

| Subject | Book | Why |
|---|---|---|
| Electrical Machines | **Bimbhra — *Electrical Machinery*** | Covers RTMNU + GATE in one. The Indian standard. |
| Power Systems | **Kothari & Nagrath — *Modern Power System Analysis*** | Prescribed text *and* the GATE standard. |
| Digital Electronics | **R.P. Jain — *Modern Digital Electronics*** | Prescribed #1 and GATE-friendly. |
| GATE practice | **Kanodia — one practice book per subject** | Where the marks actually come from. |

Everything else on your list is a *reference*. Reference books are what libraries are for.

---

## 🕸️ A note on how this was built (important)

This library was assembled inside a sandbox whose network egress was restricted to GitHub, PyPI and npm. That means:

- ✅ **GitHub-hosted open textbooks** were downloaded directly (all the books in `00-Common-Library/` and the `free-books/` folders).
- ⚠️ **Free resources on other sites** — NPTEL, MIT OCW, OpenStax, Internet Archive, TI, LibreTexts — could **not** be pulled from inside the sandbox. They are listed with accurate links in each subject README instead.
- ❌ **Commercial textbooks** were not downloaded, by design and by policy.

**To pull the rest automatically**, run this on your own machine (normal internet):

```bash
python3 tools/fetch_books.py            # downloads every free GitHub-hosted book
python3 tools/fetch_books.py --links    # prints the full curated free-resource list
```

---

## 🔓 Reading the rest for free — legally

Almost nothing on your list needs to be bought or pirated. See
[`00-Start-Here/LEGAL-FREE-ACCESS.md`](00-Start-Here/LEGAL-FREE-ACCESS.md) for the full map. The highlights:

| Route | What it gets you | Cost |
|---|---|---|
| 🔵 **Internet Archive / Open Library** | Free legal *borrowing* (Controlled Digital Lending, 1 h or 14 days) — incl. **Kothari & Nagrath, Modern Power System Analysis 4e** and **Hayt & Buck, Engineering Electromagnetics (3rd/4th ed)** | ₹0 |
| 🟢 **Public domain** | Steinmetz's *Alternating Current Phenomena*, *Transient Electric Phenomena*, *Electric Circuits* — free outright download | ₹0 |
| 🇮🇳 **NDLI** (IIT Kharagpur) | Free for Indian students; best source for Indian-published titles — Bimbhra, Sawhney, Kanodia, Rajput | ₹0 |
| 🟢 **NPTEL / MIT OCW / OpenStax** | Full free courses covering every subject on your list | ₹0 |

> ⚠️ About PDF Coffee / PDF Drive / LibGen: those host unauthorised scans of in-copyright
> textbooks. They're also a routine malware vector and often the wrong edition or truncated.
> The routes above cover the same books legally — and **older editions are usually the
> borrowable ones**, which is exactly the fallback you asked for.

---

## 📄 Licensing

| File | License | Redistributable |
|---|---|---|
| *Lessons In Electric Circuits* (all 6 vols) | [Design Science License](00-Common-Library/Lessons-in-Electric-Circuits/LICENSE-Design-Science-License.md) | ✅ Yes |
| *Think DSP*, *Think Python*, *Physical Modeling in MATLAB* | CC BY-NC (Green Tea Press) | ✅ Yes (non-commercial) |
| Metadata, READMEs, catalog | Yours | ✅ Yes |

See [`00-Start-Here/WHY-NOT-EVERY-BOOK.md`](00-Start-Here/WHY-NOT-EVERY-BOOK.md) for the full explanation of why the commercial titles aren't here.
