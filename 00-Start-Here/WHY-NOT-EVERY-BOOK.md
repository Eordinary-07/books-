# Why almost every book on your list isn't downloadable

You asked me to download these books "with the latest edition if possible." I have to be straight with you about why most of them aren't here.

---

## The short version

**Almost every title on your list is an in-copyright commercial textbook.** There is no legal free PDF of Bimbhra's *Electrical Machinery*, Kothari & Nagrath's *Modern Power System Analysis*, Mano's *Digital Logic and Computer Design*, Oppenheim's *Signals and Systems*, or any of the Kanodia GATE books. Not "hard to find" — **doesn't exist**, because the publisher never released one.

The PDFs floating around on Telegram groups, Scribd, "freebookcentre"-type sites and random GitHub repos are **pirated scans**. I won't download those for you, for three reasons that are actually practical, not just legalistic:

1. **Malware.** Textbook PDF dumps are a well-known malware vector. Many contain embedded scripts or are bundled with ".pdf.exe" droppers.
2. **They're often unusable.** Missing chapters, pages out of order, 40 MB of blurry 150-DPI OCR you can't read on a phone, or a "44th edition" that's actually the 1972 print.
3. **They're the wrong tool anyway.** For an exam, a topic-aligned free resource beats a pirated scan of a reference book you were never going to finish.

---

## What I did instead

For **every subject** on your list, each subject folder contains:

| | |
|---|---|
| 📕 **Your books, catalogued** | Title, author, publisher, edition, purpose — nothing lost from your list |
| ✅ **Free & legal substitutes** | The best open textbook / NPTEL course / MIT OCW lectures for **that specific subject** |
| 📥 **Actual downloaded books** | Six complete free textbooks, committed in this repo |
| 💰 **Buy guidance** | Which 3–4 books are actually worth your money, and which are library-only references |

The result: **you can study every subject on your list for ₹0**, and you know exactly which books to buy when you have the budget.

---

## Your list, sorted by what's actually possible

### ✅ Fully covered by free, legal books already in this repo

| Subject | Free book(s) | Pages |
|---|---|---|
| **Electric Circuits / Network Theory** | *Lessons In Electric Circuits* Vol 1 (DC) + Vol 2 (AC) | 1,131 |
| **Analog Electronics** | *Lessons In Electric Circuits* Vol 3 (Semiconductors) | 535 |
| **Digital Electronics** | *Lessons In Electric Circuits* Vol 4 (Digital) | 516 |
| **Measurements** | *Lessons In Electric Circuits* Vol 1 + Vol 5 (Reference) | 729 |
| **Signals and Systems** | *Think DSP* (PDF + EPUB) | ~200 |
| **Programming Techniques & Simulation** | *Physical Modeling in MATLAB* + *Think Python* | ~450 |

### ✅ Covered by free resources, listed with links (download with `tools/fetch_books.py`)

| Subject | Best free source |
|---|---|
| **Electrical Machines** | NPTEL *Electrical Machines I & II*; Kostenko & Piotrovsky (free full textbook, Internet Archive) |
| **Power Systems** | MIT OCW 6.061; NPTEL *Power System Analysis* |
| **Engineering Mathematics** | Lebl *Notes on Diffy Qs*; Treil *Linear Algebra Done Wrong*; Hammack *Book of Proof*; OpenStax Calculus |
| **Electromagnetic Fields** | OpenStax *University Physics Vol 2*; Ellingson *Electromagnetics*; MIT 8.02 |
| **Electrical Power Utilization** | NPTEL *Utilization of Electrical Energy* / *Electric Traction* |
| **PLC and SCADA** | Hugh Jack *Automating Manufacturing Systems with PLCs*; NPTEL *Industrial Automation and Control* |
| **Electrical Machine Design** | NPTEL *Electrical Machine Design* |

### ❌ Commercial only — no legal free edition exists

Every other title on your list. The `catalog.csv` marks these `PURCHASE`. To be explicit, this includes:

- Bimbhra — *Electrical Machinery* / *Generalized Theory of Electrical Machines* (Khanna)
- Nagrath & Kothari — *Electric Machines*; Kothari & Nagrath — *Modern Power System Analysis*, *Power System Engineering* (McGraw-Hill)
- Fitzgerald/Umans — *Electric Machinery*; Chapman — *Electric Machinery Fundamentals*
- Krause et al. — *Analysis of Electric Machinery and Drive Systems* (Wiley-IEEE)
- Stevenson — *Elements of Power System Analysis*; Grainger & Stevenson — *Power System Analysis*; Saadat; Bergen & Vittal; Elgerd; Kundur; Wadhwa
- R.P. Jain — *Modern Digital Electronics*; Mano — *Digital Logic and Computer Design*; Mano & Ciletti — *Digital Design*; Anand Kumar; Taub & Schilling
- Grewal — *Higher Engineering Mathematics*; Kreyszig; Brown & Churchill; Gupta & Kapoor
- Oppenheim et al.; Rawat; Lathi; Hsu (Schaum's)
- Alexander & Sadiku — *Fundamentals of Electric Circuits*; Hayt; Van Valkenburg
- Sadiku — *Elements of Electromagnetics*; Hayt & Buck; Shevgaonkar
- Boylestad & Nashelsky; Sedra & Smith; Gayakwad; Millman & Halkias
- Sawhney — *Measurements* and *Machine Design*; David Bell
- **All Kanodia / Nodia GATE practice books**; MADE EASY / ACE solved papers
- Rajput; J.B. Gupta; Bolton; Bailey & Wright; Attaway

---

## Where to actually buy them (India)

| Source | Good for |
|---|---|
| **Amazon.in / Flipkart** | Current editions, fast delivery |
| **Nodia & Co.** (nodia.co.in) | Kanodia GATE books — cheapest direct, and they run combo discounts |
| **MADE EASY / ACE** (madeeasy.in, aceenggacademy.com) | Coaching practice sets and postal study packages |
| **Khanna Publishers** (khannapublishers.in) | Bimbhra's books direct |
| **Dhanpat Rai & Co.** | Sawhney's books direct |
| **Your college library** | ⭐ Use this aggressively for Kundur, Krause, Fitzgerald, Kreyszig — expensive books you'll consult a handful of times |
| **Second-hand: OLX, college seniors, book bazaar** | Bimbhra and Grewal are *always* available second-hand |

---

## The honest ranking of where your money goes

1. **Bimbhra — *Electrical Machinery*** — covers RTMNU *and* GATE. Highest single-book leverage on your list.
2. **Kothari & Nagrath — *Modern Power System Analysis*** — same double duty.
3. **R.P. Jain — *Modern Digital Electronics*** — prescribed #1 and GATE-friendly.
4. **Kanodia practice book for your weakest Part-2 subject** — marks come from problems, not theory.
5. **B.S. Grewal — *Higher Engineering Mathematics*** — you'll use this for four years.

**Skip buying:** Kundur, Krause, Fitzgerald, Kreyszig, Brown & Churchill, Hsu, Schaum's, Shevgaonkar, Van Valkenburg, David Bell. These are references. Library copy or ignore.

> ⚠️ **Edition note:** for Grewal use the **44th** edition, Bimbhra the **7th**. For everything else, the **latest available** is fine — RTMNU papers and GATE follow the syllabus, not a specific printing.

---

## One more thing

If you're at an RTMNU-affiliated college, check whether you have institutional access to:

- **DELNET / N-LIST** — free remote access to thousands of e-journals and e-books for college students in India
- **NDLI (National Digital Library of India)** — ndl.iitkgp.ac.in, free with a student login, and it does host legitimate copies of many engineering texts
- **NPTEL / SWAYAM** — free courses that count for credit transfer under NEP

NDLI in particular is worth ten minutes of your time. It's free, legal, government-run, and built exactly for this.
