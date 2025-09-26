import os, sys, shutil, time, threading
RESET="\033[0m"; BOLD="\033[1m"; DIM="\033[2m"; BLINK="\033[5m"; UNDERLINE="\033[4m"
# Enhanced color palette with more vibrant colors
PAL=[45,51,87,129,171,177,213,219,255,219,213,177,171,129,87,51,45,39,33,27,21,15,9,3]
def _tty(): return sys.stdout.isatty() and os.environ.get("TERM") not in {None,"dumb"}
def _w(): 
    try: return shutil.get_terminal_size().columns
    except Exception: return 80
def _c(n): return f"\033[38;5;{n}m"
def _center(s): 
    w=min(_w(),100); return s if len(s)>=w else s.center(w)

ASCII=[
r"    _    ___  __   __   __   _____                 _           ",
r"   / \  / _ \ \ \ / /  / _| | ____|  ___   ___  __| | ___ ___  ",
r"  / _ \| | | | \ V /  | |_  |  _|   / _ \ / _ \/ _` |/ __/ _ \ ",
r" / ___ \ |_| |  | |   |  _| | |___ | (_) |  __/ (_| | (_|  __/ ",
r"/_/   \_\___/   |_|   |_|   |_____| \___/ \___|\__,_|\___\___| ",
r"                    A11Y SCOUT · accessibility scanner          ",
]

def _wave_line(text, phase):
    if not _tty(): return text
    out=[]; n=len(PAL)
    for i,ch in enumerate(text):
        out.append(f"{_c(PAL[(i+phase)%n])}{ch}{RESET}")
    return "".join(out)

def wave_banner(version="0.1.0", seconds=1.0):
    if _tty():
        os.system(""); os.system("cls" if os.name=="nt" else "clear")
    
    # Enhanced border characters with better styling
    w = min(_w(), 100)
    top = f"╔{'═' * (w - 2)}╗"
    bot = f"╚{'═' * (w - 2)}╝"
    
    t0 = time.time()
    phase = 0
    
    while time.time() - t0 < seconds:
        print("\r" + " " * _w(), end="")
        
        # Enhanced top border with gradient effect
        top_color = PAL[phase % len(PAL)]
        print(_center(_c(top_color) + BOLD + top + RESET))
        
        # Enhanced ASCII with better wave effects
        for i, line in enumerate(ASCII):
            wave_phase = phase + i * 2
            # Add different effects for different lines
            if i < 3:  # Top lines get more intense effects
                enhanced_line = _wave_line(line, wave_phase)
                print(_center(BOLD + BLINK + enhanced_line + RESET))
            else:  # Bottom lines get subtle effects
                enhanced_line = _wave_line(line, wave_phase)
                print(_center(BOLD + enhanced_line + RESET))
        
        # Enhanced metadata with better styling
        meta = f"{DIM}axe-core · Playwright · v{version}{RESET}"
        meta_wave = _wave_line(meta, phase + 6)
        print(_center(meta_wave))
        
        # Enhanced bottom border
        bot_color = PAL[(phase + 6) % len(PAL)]
        print(_center(_c(bot_color) + BOLD + bot + RESET), end="\r")
        phase += 1
        time.sleep(0.06)
    
    # Final frame with enhanced styling
    print(_center(_c(PAL[0]) + BOLD + top + RESET))
    for i, line in enumerate(ASCII):
        if i < 3:
            enhanced_line = _wave_line(line, i * 2)
            print(_center(BOLD + BLINK + enhanced_line + RESET))
        else:
            enhanced_line = _wave_line(line, i * 2)
            print(_center(BOLD + enhanced_line + RESET))
    
    meta = f"{DIM}axe-core · Playwright · v{version}{RESET}"
    print(_center(_wave_line(meta, 6)))
    print(_center(_c(PAL[6]) + BOLD + bot + RESET))

def info_panel():
    w = min(_w(), 100)
    bar = "─" * (w - 2)
    
    # Neon color palette - bright, vibrant colors
    neon_colors = {
        'border': 226,      # Neon yellow for borders
        'title': 82,        # Neon green for titles  
        'accent': 214,       # Neon orange for accents
        'text': 226,        # Neon yellow for main text
        'highlight': 82,    # Neon green for highlights
        'separator': 214,   # Neon orange for separators
        'bullet': 226,      # Neon yellow for bullets
        'subtitle': 82      # Neon green for subtitles
    }
    
    # Better structured content with clear sections
    sections = [
        {
            "title": "🔍 CAPABILITIES",
            "subtitle": "What A11Y Scout Does",
            "items": [
                "Scans websites for accessibility violations",
                "Uses industry-standard axe-core engine", 
                "Generates detailed JSON/CLI reports",
                "Targets WCAG 2.x A/AA compliance standards",
                "Provides actionable fix suggestions"
            ]
        },
        {
            "title": "🚀 USAGE",
            "subtitle": "How to Use the Tool",
            "items": [
                "a11y-scout <website-url>",
                "--out report.json    Save results to file",
                "--fail-on N          Fail CI if N+ violations found",
                "--help               Show all available options",
                "--verbose            Show detailed scan progress"
            ]
        },
        {
            "title": "💡 PURPOSE", 
            "subtitle": "Why We Built This",
            "items": [
                "Make accessibility testing effortless",
                "Help teams build inclusive web experiences",
                "Ensure compliance with accessibility standards",
                "Integrate seamlessly into CI/CD pipelines",
                "Provide clear, actionable improvement guidance"
            ]
        }
    ]
    
    # Enhanced top border with neon styling
    top_border = f"{_c(neon_colors['border'])}{BOLD}┌{bar}┐{RESET}"
    print(_center(top_border))
    
    for i, section in enumerate(sections):
        # Main title with neon green - left aligned
        title_line = f"{_c(neon_colors['title'])}{BOLD}│ {section['title']}{' ' * (len(bar) - len(section['title']) - 2)} │{RESET}"
        print(_center(title_line))
        
        # Subtitle with neon orange - left aligned
        subtitle_line = f"{_c(neon_colors['accent'])}{DIM}│ {section['subtitle']}{' ' * (len(bar) - len(section['subtitle']) - 2)} │{RESET}"
        print(_center(subtitle_line))
        
        # Items with neon yellow bullets - left aligned
        for item in section['items']:
            # Enhanced bullet with neon yellow
            bullet = f"{_c(neon_colors['bullet'])}•{RESET}"
            content = f"{_c(neon_colors['text'])}│ {bullet} {item}{' ' * (len(bar) - len(f'• {item}') - 2)} │{RESET}"
            print(_center(content))
        
        # Separator between sections (except for last section)
        if i < len(sections) - 1:
            separator = f"{_c(neon_colors['separator'])}│{(' ' * (len(bar) - 2))}│{RESET}"
            print(_center(separator))
    
    # Enhanced bottom border
    bottom_border = f"{_c(neon_colors['border'])}{BOLD}└{bar}┘{RESET}"
    print(_center(bottom_border))
    
    # Enhanced footer with neon styling
    footer = f"{_c(neon_colors['highlight'])}{BOLD}✨ Built with Python • Playwright • axe-core ✨{RESET}"
    print(_center(footer))

# Enhanced spinner with multiple styles
SPIN="⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
SPIN_WAVE="🌊🌀💫✨🌟💎🔥⚡💥"
SPIN_TECH="⚙️🔧🛠️⚡💻🔍📊🎯✅"

def _spin(text, stop):
    i = 0
    while not stop[0]:
        # Rotate between different spinner styles for variety
        if i % 30 < 10:
            frame = SPIN[i % len(SPIN)]
            style = "wave"
        elif i % 30 < 20:
            frame = SPIN_WAVE[i % len(SPIN_WAVE)]
            style = "wave"
        else:
            frame = SPIN_TECH[i % len(SPIN_TECH)]
            style = "pulse"
        
        # Apply different effects based on style
        if style == "wave":
            line = _wave_line(f"{frame} {text}", i)
        else:
            # Pulse effect for tech spinners
            pulse_phase = i * 3
            line = _wave_line(f"{frame} {text}", pulse_phase)
        
        # Enhanced display with better centering
        display_line = _center(line)[:_w()]
        print("\r" + display_line, end="", flush=True)
        time.sleep(0.06)
        i += 1
    print("\r" + " " * _w() + "\r", end="")

class ScanSpinner:
    def __init__(self, text="scanning…"): self.text=text; self._stop=[False]
    def __enter__(self):
        self._t=threading.Thread(target=_spin, args=(self.text,self._stop), daemon=True)
        self._t.start()
    def __exit__(self, *a):
        self._stop[0]=True; self._t.join()