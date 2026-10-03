# 00 — Start Here

Everything you need to know to actually use this library.

---

## What this library is

Your RTMNU B.Tech Electrical (NEP) + GATE EE book list, reorganised into a study-ready structure:

1. **Every book you listed is catalogued** — title, author, publisher, why you wanted it ([`../catalog.csv`](../catalog.csv)).
2. **Every subject has a free, legal study path** — the best open textbook / NPTEL course / MIT OCW lectures for that exact topic.
3. **Six complete free books are already downloaded** in [`../00-Common-Library/`](../00-Common-Library/) and the subject `free-books/` folders.

## What this library is not

It is **not** a dump of pirated textbook PDFs. Almost everything on your list is in-copyright commercial material — see [`WHY-NOT-EVERY-BOOK.md`](WHY-NOT-EVERY-BOOK.md).

---

## How to study from this

The three parts of your list demand **three different strategies**. Don't study them the same way.

### ⭐ Part 1 — RTMNU + GATE (Electrical Machines, Power Systems, Digital Electronics)

These three earn you marks twice. Use the **free book first, prescribed book second**:

1. **Build intuition fast** — open the free substitute listed in the subject folder. Skim, don't grind. Goal: stop fearing the topic.
2. **Work the prescribed textbook unit-by-unit** against your course outcomes. Your university marks follow that book's structure, not GATE's.
3. **Then the practice book** (Kanodia) for numerical speed.
4. **Finish with PYQs, timed.** This is the step most people skip and it's the one that moves marks.

> ⚠️ If you're short on time, **buy only these three prescribed books**. They're the highest-leverage purchases on the entire list.

### 🎯 Part 2 — GATE-only (Maths, Signals, Circuits, EM Fields, Analog, Measurements)

These have **no university exam to bail you out** — it's all GATE.

1. **One theory book. Only one.** Reading Oppenheim *and* Rawat in parallel is the classic way to waste a semester.
2. **Free lectures for stubborn concepts** — MIT OCW and NPTEL are genuinely better than the books for first exposure.
3. **Practice book.** GATE tests speed and pattern recognition, not depth.
4. **PYQs, timed, repeatedly.** In a repetitive section like Analog Electronics, PYQs alone are worth more than any textbook.

> 💡 If GATE is your priority this semester, Part 2 is where your marginal hour is worth the most — because you're not double-counting it against a university exam.

### 🏫 Part 3 — RTMNU-only (Utilization, PLC/SCADA, Machine Design, MATLAB)

**Zero GATE value.** The goal is maximum marks per hour, then leave.

1. Use the **prescribed book directly** — university papers follow the syllabus verbatim.
2. Free NPTEL course only where the book is unclear.
3. **Do not read beyond the syllabus.** Every hour here is an hour stolen from Part 1 and Part 2.
4. Exception: **PLC/SCADA and MATLAB are genuinely employable skills.** If you want to invest beyond the exam, invest there.

---

## The 20-minute triage (do this today)

1. Open the three **Part 1** subject folders. Read the "Free & legal substitutes" section in each.
2. Download the free substitute for whichever Part 1 subject you *understand least*.
3. Skim its table of contents. Write down the 3 chapters that scare you.
4. That's your study plan for the week. Not the whole book — three chapters.

---

## Running the downloader

Most free books on your list live outside GitHub (NPTEL, MIT OCW, OpenStax, Internet Archive). To pull the GitHub-hosted ones automatically:

```bash
python3 tools/fetch_books.py          # download
python3 tools/fetch_books.py --list   # preview only
python3 tools/fetch_books.py --links  # print every free resource + purchase link
```

---

## Study order if you're preparing for both (recommended)

| Phase | Focus | Reasoning |
|---|---|---|
| 1 | Part 1 subjects, theory | Earns marks twice — maximum leverage |
| 2 | Part 3 subjects, to syllabus only | Quick university marks, then stop |
| 3 | Part 2 subjects, theory + practice | Pure GATE investment |
| 4 | PYQs across Parts 1 & 2 | The single highest-return activity |

---

## A note on free resources

**NPTEL** is the best free resource for an Indian EE student — it's taught to the same syllabus you're examined on, in the same conventions, by IIT professors. Where a subject folder links NPTEL, prefer it over MIT OCW for **exam alignment**, and prefer MIT OCW for **intuition**.

Both are free and legal. Use both.
