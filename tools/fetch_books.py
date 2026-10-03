#!/usr/bin/env python3
"""
fetch_books.py — download every legally-free book referenced by this library.

Run this on YOUR machine (normal internet access — it will NOT work inside a
restricted sandbox):

    python3 tools/fetch_books.py            # download all free books
    python3 tools/fetch_books.py --list     # preview what would be downloaded
    python3 tools/fetch_books.py --links    # print the full curated free-resource list
    python3 tools/fetch_books.py --only 05  # download one subject (by number)

Every file here is PUBLIC DOMAIN, CC-licensed, or released free by its author.
No commercial textbook is downloaded — see 00-Start-Here/WHY-NOT-EVERY-BOOK.md.
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------------------
# DOWNLOADS — files committed as PDFs/EPUBs inside public GitHub repositories.
# Each entry: (subject_no, repo, repo_path, local_path, title, license)
# ---------------------------------------------------------------------------
LEC = "Leeds-Beckett-Engineering/lessons_elec"
LEC_DIR = "00-Common-Library/Lessons-in-Electric-Circuits"

DOWNLOADS = [
    # --- Lessons In Electric Circuits (Kuphaldt) — Design Science License ---
    ("00", LEC, "src/DC/DC.pdf",      f"{LEC_DIR}/LEC-Vol1-DC-Circuits.pdf",    "Lessons In Electric Circuits Vol 1 — DC",           "Design Science License"),
    ("00", LEC, "src/AC/AC.pdf",      f"{LEC_DIR}/LEC-Vol2-AC-Circuits.pdf",    "Lessons In Electric Circuits Vol 2 — AC",           "Design Science License"),
    ("00", LEC, "src/Semi/SEMI.pdf",  f"{LEC_DIR}/LEC-Vol3-Semiconductors.pdf", "Lessons In Electric Circuits Vol 3 — Semiconductors", "Design Science License"),
    ("00", LEC, "src/Digital/DIGI.pdf", f"{LEC_DIR}/LEC-Vol4-Digital.pdf",     "Lessons In Electric Circuits Vol 4 — Digital",      "Design Science License"),
    ("00", LEC, "src/Ref/REF.pdf",    f"{LEC_DIR}/LEC-Vol5-Reference.pdf",     "Lessons In Electric Circuits Vol 5 — Reference",    "Design Science License"),
    ("00", LEC, "src/Exper/EXP.pdf",  f"{LEC_DIR}/LEC-Vol6-Experiments.pdf",   "Lessons In Electric Circuits Vol 6 — Experiments",  "Design Science License"),

    # --- Signals and Systems ---
    ("05", "AllenDowney/ThinkDSP", "book/thinkdsp.pdf",
     "02-GATE-only/05-Signals-and-Systems/free-books/thinkdsp.pdf",
     "Think DSP", "CC BY-NC"),
    ("05", "AllenDowney/ThinkDSP", "book/thinkdsp.epub",
     "02-GATE-only/05-Signals-and-Systems/free-books/thinkdsp.epub",
     "Think DSP (EPUB)", "CC BY-NC"),

    # --- Programming Techniques & Simulation ---
    ("13", "AllenDowney/PhysicalModelingInMatlab", "PhysicalModelingInMatlab4.pdf",
     "03-RTMNU-only/13-Programming-Techniques-and-Simulation/free-books/physical_modeling_matlab.pdf",
     "Physical Modeling in MATLAB", "CC BY-NC"),
    ("13", "AllenDowney/Swampy", "python2/thinkpython.pdf",
     "03-RTMNU-only/13-Programming-Techniques-and-Simulation/free-books/thinkpython.pdf",
     "Think Python", "CC BY-NC"),
]

# ---------------------------------------------------------------------------
# LINKS — free books/courses hosted outside GitHub. Download these in a browser.
#   (subject_no, title, what it is, url)
# ---------------------------------------------------------------------------
LINKS = [
    ("00", "\U0001F4DA Internet Archive / Open Library \u2014 search any title",
     "Free legal borrowing via Controlled Digital Lending. Availability is per-edition; older editions are often the borrowable ones.",
     "https://openlibrary.org/search"),
    ("00", "\U0001F1EE\U0001F1F3 NDLI \u2014 National Digital Library of India",
     "Free for all Indian students (IIT Kharagpur / Ministry of Education). Best source for Indian-published titles.",
     "https://ndl.iitkgp.ac.in"),
    ("00", "Charles Steinmetz Collection \u2014 public domain, free full download",
     "Theory and Calculation of AC Phenomena; Transient Electric Phenomena and Oscillations; Electric Circuits.",
     "https://archive.org/details/charles-steinmetz-collection"),
    ("00", "FOSSEE / Scilab Textbook Companions (IIT Bombay)",
     "Free, legal chapter-by-chapter companion code and notes for standard textbooks.",
     "https://scilab.in/textbook-companion"),
    ("01", "NPTEL — Electrical Machines I & II",
     "IIT video lectures + PDF notes: DC machines, transformers, induction, synchronous.",
     "https://nptel.ac.in/courses"),
    ("01", "Kostenko & Piotrovsky — Electrical Machines (Parts 1 & 2)",
     "Complete classical textbook, free full-text scan on Internet Archive.",
     "https://archive.org/search?query=Kostenko+Piotrovsky+Electrical+Machines"),

    ("02", "MIT OCW 6.061 — Introduction to Electric Power Systems",
     "Full MIT course: notes, assignments, exams. Transmission, load flow, faults, stability.",
     "https://ocw.mit.edu/courses/6-061-introduction-to-electric-power-systems-spring-2011/"),
    ("02", "NPTEL — Power System Analysis / Engineering / Stability",
     "Search the Electrical Engineering discipline list for the current course code.",
     "https://archive.nptel.ac.in/courses/108/"),

    ("03", "Digital Circuit Projects — An Overview of Digital Circuits Through Implementing ICs",
     "Free open textbook (CC BY), hands-on lab companion.",
     "https://open.umn.edu/opentextbooks/textbooks/digital-circuit-projects-an-overview-of-digital-circuits-through-implementing-integrated-circuits"),
    ("03", "NPTEL — Digital Circuits / Digital Electronics",
     "K-maps, sequential logic, ADC/DAC — matches the GATE pattern closely.",
     "https://archive.nptel.ac.in/courses/108/"),
    ("03", "MIT OCW 6.004 — Computation Structures",
     "Digital logic from gates up to a simple processor.",
     "https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/"),

    ("04", "Jiří Lebl — Notes on Diffy Qs",
     "Free full textbook (CC BY-NC-SA): ODEs, Laplace transforms, Fourier series, systems.",
     "https://www.jirilebl.github.io/diffyqs/"),
    ("04", "Sergei Treil — Linear Algebra Done Wrong",
     "Free full textbook from Brown University. Excellent for the GATE linear algebra portion.",
     "https://www.math.brown.edu/streil/papers/LADW/LADW.html"),
    ("04", "Robert A. Beezer — A First Course in Linear Algebra",
     "Free, comprehensive, exercise-heavy.",
     "https://linear.ups.edu/"),
    ("04", "Richard Hammack — Book of Proof",
     "Free (CC BY-ND). Fixes the proof comfort gap that costs marks in GATE.",
     "https://www.people.vcu.edu/~rhammack/BookOfProof/"),
    ("04", "Juan Carlos Ponce Campuzano — Complex Analysis: A Visual and Interactive Introduction",
     "Free online book (CC BY-NC-SA). Best free source for residue theorem / contour integration.",
     "https://complex-analysis.com/"),
    ("04", "OpenStax — Calculus Vol 1-3, College Algebra, Introductory Statistics",
     "Peer-reviewed CC BY textbooks with free PDF downloads.",
     "https://openstax.org/subjects/math"),
    ("04", "MIT OCW 18.06 Linear Algebra (Gilbert Strang) + 18.03 Differential Equations",
     "The gold-standard free video courses.",
     "https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/"),

    ("05", "MIT OCW 6.003 — Signals and Systems (Oppenheim himself)",
     "The lectures for the actual 'bible' textbook, by its author. Best single free resource.",
     "https://ocw.mit.edu/courses/6-003-signals-and-systems-fall-2011/"),
    ("05", "Steven W. Smith — The Scientist and Engineer's Guide to DSP",
     "Free complete book online. Plain-English sampling, aliasing, convolution, DFT.",
     "https://www.dspguide.com/"),

    ("06", "James M. Fiore — DC & AC Electrical Circuit Analysis",
     "Two free, properly typeset open textbooks (CC BY-SA) with worked examples and problems.",
     "https://milnepublishing.geneseo.edu/concise-introduction-to-electric-circuits/"),
    ("06", "MIT OCW 6.002 — Circuits and Electronics (Anant Agarwal)",
     "The famous free MIT circuits course. Transients, op-amps, frequency response.",
     "https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/"),
    ("06", "NPTEL — Basic Electrical Circuits / Network Theory",
     "Indian-syllabus-aligned notes and conventions.",
     "https://archive.nptel.ac.in/courses/108/"),

    ("07", "OpenStax — University Physics Volume 2 (Electricity & Magnetism)",
     "Full peer-reviewed open textbook (CC BY), free PDF. Covers the whole GATE EE EMT syllabus.",
     "https://openstax.org/details/books/university-physics-volume-2"),
    ("07", "Steven W. Ellingson — Electromagnetics Volumes 1 & 2",
     "Free open textbook (CC BY-SA) written for electrical engineers.",
     "https://phys.libretexts.org/Bookshelves/Electricity_and_Magnetism"),
    ("07", "MIT OCW 8.02 — Electricity and Magnetism (Walter Lewin)",
     "Legendary free lecture series. Best intuition-builder for fields.",
     "https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/"),

    ("08", "Texas Instruments — Op Amps for Everyone",
     "Free, complete, authoritative PDF. Ideal op-amp theory through real design.",
     "https://www.ti.com/lit/ug/slod006b/slod006b.pdf"),
    ("08", "Analog Devices — Linear Circuit Design Handbook",
     "Free full engineering handbook. Superb on feedback, filters, noise, instrumentation.",
     "https://www.analog.com/en/education/education-library/linear-circuit-design-handbook.html"),
    ("08", "MIT OCW 6.012 — Microelectronic Devices and Circuits",
     "Semiconductor physics, MOS/BJT devices and amplifiers, above GATE depth.",
     "https://ocw.mit.edu/courses/6-012-microelectronic-devices-and-circuits-spring-2009/"),

    ("09", "NPTEL — Electrical Measurements and Instrumentation",
     "Error analysis, bridges, CT/PT, wattmeters, energy meters, DVMs, CRO.",
     "https://archive.nptel.ac.in/courses/108/"),
    ("09", "NIST — free measurement handbooks and references",
     "Primary-source material for error, uncertainty and calibration.",
     "https://www.nist.gov/pml"),

    ("10", "NPTEL — Utilization of Electrical Energy / Electric Traction / Illumination",
     "Traction, heating/welding, illumination, electroplating.",
     "https://archive.nptel.ac.in/courses/108/"),

    ("11", "Hugh Jack — Automating Manufacturing Systems with PLCs",
     "Free, complete, well-regarded textbook (CC BY-NC-SA). The standard Bolton substitute.",
     "https://www.hughjack.com/automating-manufacturing-systems-with-plcs/"),
    ("11", "NPTEL — Industrial Automation and Control (IIT Kharagpur)",
     "Free full course: PLCs, SCADA, DCS, HMI, industrial networking.",
     "https://archive.nptel.ac.in/courses/108/"),
    ("11", "LibreTexts — Industrial & Systems Engineering",
     "Free openly-licensed chapters on ladder logic and control hardware.",
     "https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering"),

    ("12", "NPTEL — Electrical Machine Design / Design of Electrical Machines",
     "Magnetic circuit design, winding design, transformer and rotating-machine design.",
     "https://archive.nptel.ac.in/courses/108/"),

    ("13", "Cleve Moler — Numerical Computing with MATLAB & Experiments with MATLAB",
     "Free official books by MATLAB's creator, published by MathWorks.",
     "https://www.mathworks.com/moler/index_ncm.html"),
    ("13", "MathWorks — MATLAB Onramp and official free courses",
     "Free, hands-on, browser-based. Fastest way to get productive in MATLAB.",
     "https://matlabacademy.mathworks.com/"),
]

# ---------------------------------------------------------------------------
# PURCHASE — commercial titles with no legal free edition.
# ---------------------------------------------------------------------------
PURCHASE = {
    "01": ["Bimbhra — Electrical Machinery (7th ed), Khanna",
           "Bimbhra — Generalized Theory of Electrical Machines, Khanna",
           "Nagrath & Kothari — Electric Machines, McGraw-Hill",
           "Fitzgerald/Umans — Electric Machinery, McGraw-Hill",
           "Chapman — Electric Machinery Fundamentals, McGraw-Hill",
           "Krause et al. — Analysis of Electric Machinery and Drive Systems, Wiley-IEEE",
           "Janardanan — Special Electrical Machines, PHI",
           "Kanodia/Murolia — Electrical Machines (GATE), Nodia",
           "Sawhney — Electrical Machine Design, Dhanpat Rai",
           "Shanmugasundaram et al. — Electrical Machine Design Data Book, New Age"],
    "02": ["Kothari & Nagrath — Modern Power System Analysis, McGraw-Hill",
           "Kothari & Nagrath — Power System Engineering, McGraw-Hill",
           "Stevenson — Elements of Power System Analysis, McGraw-Hill",
           "Grainger & Stevenson — Power System Analysis, McGraw-Hill",
           "Saadat — Power System Analysis",
           "Elgerd — Electric Energy Systems Theory",
           "Bergen & Vittal — Power System Analysis, Pearson",
           "Kundur — Power System Stability and Control, McGraw-Hill",
           "Wadhwa — Electrical Power Systems, New Age",
           "Kanodia/Murolia — Power Systems (GATE), Nodia"],
    "03": ["R.P. Jain — Modern Digital Electronics, McGraw-Hill",
           "Mano — Digital Logic and Computer Design, Pearson",
           "Mano & Ciletti — Digital Design, Pearson",
           "Anand Kumar — Fundamentals of Digital Circuits, PHI",
           "Taub & Schilling — Digital Integrated Electronics, McGraw-Hill",
           "Kanodia/Murolia — Digital Electronics (GATE), Nodia"],
    "04": ["Grewal — Higher Engineering Mathematics (44th ed), Khanna",
           "Kreyszig — Advanced Engineering Mathematics, Wiley",
           "Brown & Churchill — Complex Variables and Applications, McGraw-Hill",
           "Gupta & Kapoor — Fundamentals of Mathematical Statistics, Sultan Chand",
           "Kanodia — GATE Engineering Mathematics, Nodia",
           "MADE EASY / ACE — GATE Engineering Mathematics Solved Papers"],
    "05": ["Oppenheim, Willsky & Nawab — Signals and Systems, Pearson/PHI",
           "Rawat — Signals and Systems, OUP",
           "Lathi — Linear Systems and Signals, OUP",
           "Kanodia/Murolia — Signals and Systems (GATE), Nodia",
           "Hsu — Schaum's Outline of Signals and Systems, McGraw-Hill"],
    "06": ["Alexander & Sadiku — Fundamentals of Electric Circuits, McGraw-Hill",
           "Hayt, Kemmerly & Durbin — Engineering Circuit Analysis, McGraw-Hill",
           "Van Valkenburg — Network Analysis, Pearson",
           "Kanodia — Electric Circuits and Fields (GATE), Nodia",
           "Nahvi & Edminister — Schaum's Outline of Electric Circuits, McGraw-Hill"],
    "07": ["Sadiku — Elements of Electromagnetics, OUP",
           "Hayt & Buck — Engineering Electromagnetics, McGraw-Hill",
           "Shevgaonkar — Electromagnetic Waves, McGraw-Hill (SKIP for GATE)",
           "Kanodia — Electric Circuits and Fields (GATE) — EM unit, Nodia"],
    "08": ["Boylestad & Nashelsky — Electronic Devices and Circuit Theory, Pearson",
           "Sedra & Smith — Microelectronic Circuits, OUP",
           "Gayakwad — Op-Amps and Linear Integrated Circuits, Pearson",
           "Millman & Halkias — Electronic Devices and Circuits, McGraw-Hill",
           "Kanodia/Murolia — Analog Electronics (GATE), Nodia"],
    "09": ["Sawhney — A Course in Electrical and Electronic Measurements and Instrumentation, Dhanpat Rai",
           "Bell — Electronic Instrumentation and Measurements, OUP",
           "Kanodia — Electrical and Electronic Measurements (GATE), Nodia"],
    "10": ["Rajput — Utilisation of Electrical Power, Laxmi",
           "J.B. Gupta — Utilisation of Electric Power and Electric Traction, Kataria"],
    "11": ["Bolton — Programmable Logic Controllers, Newnes",
           "Bailey & Wright — Practical SCADA for Industry, Newnes"],
    "12": ["Sawhney — A Course in Electrical Machine Design, Dhanpat Rai"],
    "13": ["Attaway — MATLAB: A Practical Introduction to Programming and Problem Solving, Butterworth-Heinemann"],
}

SUBJECT_NAMES = {
    "00": "Common Library", "01": "Electrical Machines", "02": "Power Systems",
    "03": "Digital Electronics", "04": "Engineering Mathematics",
    "05": "Signals and Systems", "06": "Electric Circuits / Network Theory",
    "07": "Electromagnetic Fields", "08": "Analog Electronics",
    "09": "Electrical & Electronic Measurements", "10": "Electrical Power Utilization",
    "11": "PLC and SCADA", "12": "Electrical Machine Design",
    "13": "Programming Techniques & Simulation (MATLAB)",
}


def human(n):
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.0f}{unit}" if unit == "B" else f"{n:.1f}{unit}"
        n /= 1024
    return f"{n:.1f}TB"


def download(repo, repo_path, dest, token=None):
    """Try raw.githubusercontent.com first, then fall back to the GitHub blobs API."""
    dest_abs = os.path.join(ROOT, dest)
    os.makedirs(os.path.dirname(dest_abs), exist_ok=True)

    urls = []
    for branch in ("master", "main", "trunk"):
        urls.append(f"https://raw.githubusercontent.com/{repo}/{branch}/{urllib.parse.quote(repo_path)}")

    last_err = None
    for url in urls:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "book-fetch/1.0"})
            with urllib.request.urlopen(req, timeout=120) as r, open(dest_abs, "wb") as f:
                while True:
                    chunk = r.read(1 << 16)
                    if not chunk:
                        break
                    f.write(chunk)
            if os.path.getsize(dest_abs) > 1000:
                return os.path.getsize(dest_abs)
        except Exception as e:                                    # noqa: BLE001
            last_err = e
            continue

    # blobs API fallback (handles repos where raw is awkward)
    try:
        def api(u):
            req = urllib.request.Request(u, headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "book-fetch/1.0",
                **({"Authorization": f"Bearer {token}"} if token else {}),
            })
            return json.load(urllib.request.urlopen(req, timeout=120))

        meta = api(f"https://api.github.com/repos/{repo}")
        br = meta["default_branch"]
        tree = api(f"https://api.github.com/repos/{repo}/git/trees/{br}?recursive=1")
        m = [t for t in tree.get("tree", []) if t["path"] == repo_path]
        if not m:
            raise FileNotFoundError(f"{repo}:{repo_path} not found in repo tree")
        raw = urllib.request.Request(
            f"https://api.github.com/repos/{repo}/git/blobs/{m[0]['sha']}",
            headers={"Accept": "application/vnd.github.raw", "User-Agent": "book-fetch/1.0",
                     **({"Authorization": f"Bearer {token}"} if token else {})})
        with urllib.request.urlopen(raw, timeout=180) as r, open(dest_abs, "wb") as f:
            f.write(r.read())
        return os.path.getsize(dest_abs)
    except Exception as e:                                        # noqa: BLE001
        raise RuntimeError(f"could not fetch {repo}:{repo_path} ({last_err or e})")


def cmd_download(only=None, token=None):
    todo = [d for d in DOWNLOADS if only is None or d[0] == only]
    if not todo:
        print(f"No downloads defined for subject '{only}'.")
        return
    ok = skipped = failed = 0
    for num, repo, rpath, dest, title, lic in todo:
        dest_abs = os.path.join(ROOT, dest)
        tag = f"[{num}] {SUBJECT_NAMES.get(num, num)}"
        if os.path.exists(dest_abs) and os.path.getsize(dest_abs) > 1000:
            print(f"  skip  {dest}  (already present, {human(os.path.getsize(dest_abs))})")
            skipped += 1
            continue
        try:
            size = download(repo, rpath, dest, token)
            print(f"  OK    {dest}  ({human(size)})")
            ok += 1
        except Exception as e:                                    # noqa: BLE001
            print(f"  FAIL  {title}  [{tag}]")
            print(f"        {e}")
            print(f"        manual: https://github.com/{repo}")
            failed += 1
    print(f"\n{ok} downloaded, {skipped} already present, {failed} failed.")


def cmd_list():
    total = 0
    cur = None
    for num, repo, rpath, dest, title, lic in DOWNLOADS:
        if num != cur:
            print(f"\n[{num}] {SUBJECT_NAMES.get(num, num)}")
            cur = num
        print(f"    {title:<52} -> {dest}")
    print(f"\n{len(DOWNLOADS)} files across {len({d[0] for d in DOWNLOADS})} subjects.")
    print(f"{len(LINKS)} further free resources (non-GitHub) — run with --links.")


def cmd_links():
    cur = None
    for num, title, desc, url in LINKS:
        if num != cur:
            print(f"\n{'=' * 74}\n[{num}] {SUBJECT_NAMES.get(num, num)}\n{'=' * 74}")
            cur = num
        print(f"  • {title}")
        print(f"      {desc}")
        print(f"      {url}")
    print(f"\n\n{'=' * 74}\nCOMMERCIAL — no legal free edition exists (buy or library)\n{'=' * 74}")
    for num in sorted(PURCHASE):
        print(f"\n[{num}] {SUBJECT_NAMES.get(num, num)}")
        for b in PURCHASE[num]:
            print(f"  ✗ {b}")
    print("\nBuying guide and money ranking: 00-Start-Here/WHY-NOT-EVERY-BOOK.md")
    print("Cheapest direct sources: nodia.co.in (Kanodia), khannapublishers.in (Bimbhra),")
    print("                         madeeasy.in / aceenggacademy.com (practice sets)")


def main():
    ap = argparse.ArgumentParser(description="Download the legally-free books in this library.")
    ap.add_argument("--list", action="store_true", help="preview downloads only")
    ap.add_argument("--links", action="store_true", help="print all curated free resources + purchase list")
    ap.add_argument("--only", metavar="NN", help="restrict to one subject number, e.g. 05")
    ap.add_argument("--token", metavar="TOKEN", help="GitHub token (optional; raises rate limits)")
    a = ap.parse_args()

    if a.links:
        cmd_links()
    elif a.list:
        cmd_list()
    else:
        print(f"Library root: {ROOT}\n")
        cmd_download(a.only, a.token)
        print("\nNext: run with --links for the NPTEL / MIT OCW / OpenStax resources.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
