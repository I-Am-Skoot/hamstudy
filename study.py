import json
import random
import os
import sys
import textwrap

# ------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_key():
    print("\nPress any key to continue...", end="", flush=True)
    if sys.platform == "win32":
        import msvcrt
        msvcrt.getch()
    else:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
    print()

def wrap(text, width=120):
    return textwrap.fill(text, width=width)

# ------------------------------------------------------------
# Names
# ------------------------------------------------------------

SUBELEMENT_NAMES = {
    "1": "Commission’s Rules",
    "2": "Operating Procedures",
    "3": "Radio Wave Propagation",
    "4": "Amateur Practices",
    "5": "Electrical Principles",
    "6": "Circuit Components",
    "7": "Practical Circuits",
    "8": "Signals and Emissions",
    "9": "Antennas & Transmission Lines",
    "0": "Safety",
}

SECTION_NAMES = {
    # Technician
    "T1A": "Purpose & permissible use of the Amateur Radio Service",
    "T1B": "Frequency allocations; Emission modes; Spectrum sharing",
    "T1C": "Licensing; Call signs; International communications",
    "T1D": "Authorized and prohibited transmissions",
    "T1E": "Control operator; Control point; Control types",
    "T1F": "Station identification; Repeaters; Third-party",
    "T2A": "Station operation; Band plans",
    "T2B": "VHF/UHF operating practices; Access tones; DMR",
    "T2C": "Public service; Emergency operations; RACES/ARES",
    "T3A": "Radio wave characteristics; Propagation basics",
    "T3B": "Electromagnetic wave properties; Wavelength & frequency",
    "T3C": "Propagation modes; Sporadic E; Tropospheric ducting",
    "T4A": "Station setup; Connecting equipment; RF grounding",
    "T4B": "Operating controls; Transceiver settings",
    "T5A": "Electrical principles; Current, voltage, resistance",
    "T5B": "Math for electronics; Metric prefixes; Decibels",
    "T5C": "Capacitance, inductance, reactance, impedance",
    "T5D": "Ohm’s Law; Series & parallel circuits",
    "T6A": "Electrical components; Resistors, capacitors, inductors",
    "T6B": "Semiconductors; Diodes, transistors",
    "T6C": "Circuit diagrams; Schematic symbols",
    "T6D": "Component functions; Transformers, relays, etc.",
    "T7A": "Station equipment; Receivers, transmitters, transceivers",
    "T7B": "Common problems; Interference, distortion",
    "T7C": "Antenna measurements; SWR, dummy loads",
    "T7D": "Basic repair; Soldering, test equipment",
    "T8A": "Modulation modes; AM, FM, SSB, CW",
    "T8B": "Amateur satellites; Orbital mechanics",
    "T8C": "Operating activities; Contests, fox hunting, radio direction finding",
    "T8D": "Non-voice communications; Digital modes, image",
    "T9A": "Antennas; Verticals, Yagis, loops, polarization",
    "T9B": "Feed lines; Coax, connectors, SWR, impedance matching",
    "T0A": "Safety; AC power circuits, hazardous voltages",
    "T0B": "Antenna safety; Tower climbing, grounding",
    "T0C": "RF exposure; Radiation, exposure limits",

    # General
    "G1A": "General class frequency privileges",
    "G1B": "Antenna structure limitations; Beacons; Prohibited transmissions",
    "G1C": "Transmitter power regulations; Data emission standards",
    "G1D": "Volunteer examiners; Temporary identification",
    "G1E": "Control categories; Repeater regulations; Third-party rules",
    "G2A": "Phone operating procedures; USB/LSB conventions",
    "G2B": "Operating effectively; Band plans; Emergency operations",
    "G2C": "CW operating procedures; Q signals; Full break-in",
    "G2D": "Volunteer Monitor program; HF operations",
    "G2E": "Digital mode operating procedures",
    "G3A": "Sunspots; Solar radiation; Geomagnetic field",
    "G3B": "Maximum/Lowest usable frequency; Short/long path",
    "G3C": "Ionospheric regions; Critical angle & frequency",
    "G4A": "Station setup and operation",
    "G4B": "Test equipment and measurements",
    "G4C": "Interference; Grounding and bonding",
    "G4D": "Speech processors; S-meters; Sideband operation",
    "G4E": "HF mobile installations; Alternative power",
    "G5A": "Reactance; Impedance; Resonance",
    "G5B": "The decibel; Power calculations; RMS & PEP",
    "G5C": "Resistors, capacitors, inductors in series/parallel",
    "G6A": "Resistors; Capacitors; Inductors; Transformers",
    "G6B": "Semiconductors; Diodes; Transistors; ICs",
    "G7A": "Power supplies; Schematic symbols",
    "G7B": "Digital circuits; Amplifiers; Oscillators",
    "G7C": "Receivers; Filters; Modulation circuitry",
    "G8A": "Carriers; Modulation; Bandwidth",
    "G8B": "Frequency mixing; Multiplication; Bandwidth of modes",
    "G8C": "Digital emission modes; Packet; PSK; FT8, etc.",
    "G9A": "Antenna basics; Radiation resistance; Polarization",
    "G9B": "Dipoles; Ground-plane; Random wire antennas",
    "G9C": "Directional antennas; Yagis; Loops; Quads",
    "G9D": "Specialized antennas; NVIS; Satellite; Mobile",
    "G0A": "RF safety; Exposure evaluation",
    "G0B": "Safety in the ham shack; Power circuits; Antenna safety",

    # Extra
    "E1A": "Frequency privileges; Signal frequency range; Automatic message forwarding",
    "E1B": "Station restrictions; Spurious emissions; Antenna structures; RACES",
    "E1C": "Automatic & remote control; Band-specific rules; Foreign operation",
    "E1D": "Amateur space & Earth stations; Telemetry; Balloon transmissions",
    "E1E": "Volunteer examiner program",
    "E1F": "Miscellaneous rules; Amplifiers; Spread spectrum; Auxiliary stations",
    "E2A": "Amateur radio in space; Satellites; Orbital mechanics",
    "E2B": "Television practices; Fast-scan & slow-scan TV",
    "E2C": "Contest & DX operating; Remote operation; Log formats",
    "E2D": "VHF/UHF digital modes; APRS; EME; Meteor scatter",
    "E2E": "HF digital modes",
    "E3A": "Electromagnetic waves; EME; Meteor scatter; Microwave propagation",
    "E3B": "Transequatorial; Long-path; Sporadic-E; Ground-wave",
    "E3C": "Propagation prediction; Space weather; Radio horizon",
    "E4A": "Test equipment; Spectrum analyzers; Antenna analyzers; Oscilloscopes",
    "E4B": "Measurement techniques; Instrument accuracy; S-parameters",
    "E4C": "Receiver performance; Phase noise; Noise floor; Dynamic range",
    "E4D": "Receiver performance; Intermodulation; Cross-modulation",
    "E4E": "Noise suppression; Interference",
    "E5A": "Resonance; Q; Relationship between parameters",
    "E5B": "Time constants; Phase angle; Complex impedance",
    "E5C": "Coordinate systems; Phasors",
    "E5D": "AC & RF energy in real circuits; Skin effect",
    "E6A": "Semiconductor materials; Bipolar & field-effect transistors",
    "E6B": "Diodes",
    "E6C": "Digital ICs; Families; Gates; Programmable logic",
    "E6D": "Inductors; Toroids; Piezoelectric devices",
    "E6E": "MMIC; RF semiconductor packages",
    "E6F": "Electro-optical technology; Photoconductivity; Optical sensors",
    "E7A": "Digital circuits; Flip-flops; Counters; Shift registers",
    "E7B": "Amplifiers; Class of operation; Distortion; Heat management",
    "E7C": "Filters; Impedance matching networks",
    "E7D": "Power supplies; Voltage regulators; Batteries",
    "E7E": "Modulation & demodulation; Mixers; Modulators",
    "E7F": "DSP filtering; Software defined radio essentials",
    "E7G": "Active filters; Op-amp circuits",
    "E7H": "Oscillators; Signal sources; Frequency synthesizers",
    "E8A": "AC waveforms; Fourier analysis; Pulse characteristics",
    "E8B": "Modulation systems; Deviation ratio; Modulation index",
    "E8C": "Digital signals; Digital modes; Bandwidth",
    "E8D": "Intermodulation; Noise; Peak-to-average power",
    "E9A": "Antenna basics; Radiation resistance; Efficiency; Beamwidth",
    "E9B": "Antenna patterns; E and H plane; Gain; Front-to-back",
    "E9C": "Practical wire antennas; Folded dipole; Rhombic; Beverage",
    "E9D": "Yagi antennas; Phased arrays; Log periodics",
    "E9E": "Matching; Feed line matching systems; Smith chart",
    "E9F": "Transmission lines; Velocity factor; Characteristic impedance",
    "E9G": "Smith chart",
    "E9H": "Receiving antennas; Loop antennas; Beverage; Direction finding",
    "E0A": "Safety; RF radiation hazards; Hazardous materials; Grounding",
}

POOLS = {
    "1": {
        "name": "Technician",
        "file": "tech.json",
        "url": "https://raw.githubusercontent.com/russolsen/ham_radio_question_pool/main/technician-2026-2030/technician-2026-2030.json",
        "exam_questions": 35,
        "pass_score": 26,
    },
    "2": {
        "name": "General",
        "file": "general.json",
        "url": "https://raw.githubusercontent.com/russolsen/ham_radio_question_pool/main/general-2023-2027/general-2023-2027.json",
        "exam_questions": 35,
        "pass_score": 26,
    },
    "3": {
        "name": "Extra",
        "file": "extra.json",
        "url": "https://raw.githubusercontent.com/russolsen/ham_radio_question_pool/main/extra-2024-2028/extra-2024-2028.json",
        "exam_questions": 50,
        "pass_score": 37,
    }
}

# ------------------------------------------------------------
# Global progress tracker (session only)
# ------------------------------------------------------------
mastered = set()   # set of question IDs that have been answered correctly

def is_group_mastered(section_id, sections):
    """True if every question in this group has been answered correctly at least once."""
    return all(q["id"] in mastered for q in sections[section_id])

def is_subelement_mastered(sub, subelements, sections):
    """True if every group in the subelement is mastered."""
    return all(is_group_mastered(g, sections) for g in subelements[sub])

# ------------------------------------------------------------
# Data loading
# ------------------------------------------------------------

def load_pool(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def group_by_section(questions):
    sections = {}
    for q in questions:
        section = q["id"][:3]
        if section not in sections:
            sections[section] = []
        sections[section].append(q)
    return dict(sorted(sections.items()))

# ------------------------------------------------------------
# Menus
# ------------------------------------------------------------

def choose_pool():
    while True:
        clear_screen()
        print("=== Ham Radio Study Game ===")
        print("Which license class do you want to study?\n")

        available = []
        for key, info in POOLS.items():
            exists = os.path.exists(info["file"])
            status = "✓ found" if exists else "✗ missing"
            print(f"  {key}. {info['name']:<12} ({info['file']})  [{status}]")
            if exists:
                available.append(key)

        print("\n  Q. Quit")
        print()

        if not available:
            print("No question pool files found!")
            print("\nDownload the JSON files from:")
            for info in POOLS.values():
                print(f"  {info['name']}: {info['url']}")
            print("\nSave them in the same folder as this script with the names above.")
            wait_for_key()
            continue

        choice = input("Your choice: ").strip().upper()

        if choice == 'Q':
            return None

        if choice in POOLS:
            info = POOLS[choice]
            if os.path.exists(info["file"]):
                return info
            else:
                print(f"\n{info['file']} is missing!")
                print(f"Download it from:\n{info['url']}")
                print(f"\nSave it as: {info['file']}")
                wait_for_key()
        else:
            print("\nInvalid choice.")
            wait_for_key()


def choose_mode(pool_info):
    while True:
        clear_screen()
        print(f"=== {pool_info['name']} ===\n")
        print("  1. Study mode  (practice by section)")
        print("  2. Practice Test (realistic exam)")
        print("  Q. Back to license class menu")
        choice = input("\nYour choice: ").strip().upper()
        if choice == '1':
            return "study"
        if choice == '2':
            return "test"
        if choice == 'Q':
            return None
        print("\nInvalid choice.")
        wait_for_key()


def select_section(sections):
    subelements = {}
    for sec in sections:
        sub = sec[:2]
        if sub not in subelements:
            subelements[sub] = []
        subelements[sub].append(sec)

    sub_list = sorted(subelements.keys())

    while True:
        clear_screen()
        print("=== Choose a Subelement ===")
        print("( * = all questions in this area have been answered correctly )\n")

        for i, sub in enumerate(sub_list, 1):
            groups = subelements[sub]
            total_q = sum(len(sections[g]) for g in groups)
            title = SUBELEMENT_NAMES.get(sub[1], "")
            star = " *" if is_subelement_mastered(sub, subelements, sections) else ""
            print(f"  {i:2}. {sub}  – {title}{star}  ({len(groups)} groups, {total_q} questions)")

        print()
        print("  A.  Study ALL sections (entire pool)")
        print("  Q.  Back")

        choice = input("\nYour choice: ").strip().upper()

        if choice == 'Q':
            return None
        if choice == 'A':
            return list(sections.keys())

        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(sub_list):
                selected_sub = sub_list[idx]
                groups = sorted(subelements[selected_sub])

                while True:
                    clear_screen()
                    title = SUBELEMENT_NAMES.get(selected_sub[1], "")
                    print(f"=== {selected_sub} – {title} ===")
                    print("( * = all questions in this group mastered )\n")

                    for i, g in enumerate(groups, 1):
                        name = SECTION_NAMES.get(g, "")
                        count = len(sections[g])
                        star = " *" if is_group_mastered(g, sections) else ""
                        print(f"  {i:2}. {g}{star}  ({count} q)  – {name}")

                    print()
                    print("  A.  All groups in this subelement")
                    print("  B.  Back to subelement list")
                    print("  Q.  Back to license class menu")

                    sub_choice = input("\nYour choice: ").strip().upper()

                    if sub_choice == 'Q':
                        return None
                    if sub_choice == 'B':
                        break
                    if sub_choice == 'A':
                        return groups

                    if sub_choice.isdigit():
                        gidx = int(sub_choice) - 1
                        if 0 <= gidx < len(groups):
                            return [groups[gidx]]

                    print("\nInvalid choice.")
                    wait_for_key()
        else:
            print("\nInvalid choice.")
            wait_for_key()

# ------------------------------------------------------------
# Question handling
# ------------------------------------------------------------

def ask_question(q, section_id, current, total, is_test=False):
    section_name = SECTION_NAMES.get(section_id, section_id)
    clear_screen()
    if is_test:
        print(f"=== Practice Test – Question {current} of {total} ===\n")
    else:
        print(f"=== {section_id} – {section_name} ===")
        print(f"Question {current} of {total}")
        print("(Press Q to return to menu)\n")

    print(wrap(q['question']))
    print()

    answers = list(enumerate(q["answers"]))
    random.shuffle(answers)
    mapping = {}
    correct_display = None

    for i, (orig_idx, text) in enumerate(answers):
        letter = chr(65 + i)
        wrapped = textwrap.fill(
            f"{letter}. {text}",
            width=120,
            subsequent_indent="     "
        )
        print(wrapped)
        mapping[letter] = orig_idx
        if orig_idx == q["correct"]:
            correct_display = letter

    while True:
        prompt = "\nYour answer (A-D): " if is_test else "\nWhich letter is correct? (A-D or Q): "
        choice = input(prompt).strip().upper()

        if not is_test and choice == 'Q':
            return "quit"

        if choice in mapping:
            if mapping[choice] == q["correct"]:
                print("\nCorrect!")
                mastered.add(q["id"])          # mark as mastered
                return True
            else:
                correct_text = q["answers"][q["correct"]]
                print(f"\nThe correct answer was {correct_display} - {correct_text}")
                return False

        print("Please enter A, B, C or D" + ("" if is_test else " or Q") + ".")

# ------------------------------------------------------------
# Practice Test mode
# ------------------------------------------------------------

def run_practice_test(sections, pool_info):
    """Build a realistic exam: one random question from every group."""
    exam_questions = []
    for section_id, qs in sections.items():
        exam_questions.append(random.choice(qs))

    random.shuffle(exam_questions)
    total = len(exam_questions)
    correct_count = 0

    clear_screen()
    print(f"=== {pool_info['name']} Practice Test ===")
    print(f"{total} questions  |  Pass = {pool_info['pass_score']}/{total}")
    print("Answer each question. No going back.\n")
    wait_for_key()

    for i, q in enumerate(exam_questions, 1):
        section_id = q["id"][:3]
        result = ask_question(q, section_id, i, total, is_test=True)
        if result is True:
            correct_count += 1
        wait_for_key()

    # Final score
    clear_screen()
    pct = correct_count / total * 100
    passed = correct_count >= pool_info["pass_score"]

    print("=== Practice Test Results ===\n")
    print(f"Score: {correct_count} / {total}  ({pct:.1f}%)")
    print(f"Passing score: {pool_info['pass_score']} / {total}")
    print()
    if passed:
        print("★★★  CONGRATULATIONS – YOU PASSED!  ★★★")
    else:
        print("Not quite – keep studying and try again.")
    print()
    wait_for_key()

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------

def main():
    global mastered

    while True:
        pool_info = choose_pool()
        if pool_info is None:
            clear_screen()
            print("73! Goodbye.")
            break

        clear_screen()
        print(f"Loading {pool_info['name']} question pool...")
        questions = load_pool(pool_info["file"])
        sections = group_by_section(questions)
        mastered = set()          # reset progress for new pool

        while True:
            mode = choose_mode(pool_info)
            if mode is None:
                break

            if mode == "test":
                run_practice_test(sections, pool_info)
                continue

            # Study mode
            while True:
                selected = select_section(sections)
                if selected is None:
                    break

                for section_id in selected:
                    section_questions = sections[section_id][:]
                    total = len(section_questions)
                    random.shuffle(section_questions)

                    missed = []
                    quit_section = False

                    for i, q in enumerate(section_questions, 1):
                        result = ask_question(q, section_id, i, total)

                        if result == "quit":
                            quit_section = True
                            break
                        if result is False:
                            missed.append(q)
                        wait_for_key()

                    if quit_section:
                        break

                    # Review missed
                    while missed:
                        clear_screen()
                        print(f"=== Reviewing missed questions – {section_id} ===")
                        print(f"{len(missed)} remaining\n")
                        wait_for_key()

                        still_missed = []
                        for i, q in enumerate(missed, 1):
                            result = ask_question(q, section_id, i, len(missed))
                            if result == "quit":
                                quit_section = True
                                break
                            if result is False:
                                still_missed.append(q)
                            wait_for_key()
                        missed = still_missed
                        if quit_section:
                            break

                    if quit_section:
                        break

                    clear_screen()
                    print(f"Section {section_id} completed!")
                    if is_group_mastered(section_id, sections):
                        print("(All questions in this group are now marked as mastered *)")
                    wait_for_key()

if __name__ == "__main__":
    main()
