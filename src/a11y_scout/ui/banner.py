# ui/banner.py
import os, sys, shutil, time

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
C1 = "\033[38;5;45m"   # cyan
C2 = "\033[38;5;213m"  # magenta
C3 = "\033[38;5;250m"  # gray

def _tty():
    return sys.stdout.isatty() and os.environ.get("TERM") not in {None, "dumb"}

def _w():
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return 80

def _center(s: str) -> str:
    w = _w()
    return s if len(s) >= w else s.center(w)

ASCII = [
    r"   ___   ___  __    __   ____                  _   ",
    r"  / _ | / _ \/ /__ / /  / ___|  ___  ___ _   _| |_ ",
    r" / __ |/ , _/ / -_) _ \ \___ \ / _ \/ __| | | | __|",
    r"/_/ |_/_/|_/_/\__/_//_/ |____/ \___/\__ \__,_|\__|",
    r"               A11Y SCOUT · accessibility scanner   ",
]

def print_banner(version: str = "0.1.0"):
    if _tty():
        os.system("")  # enable ANSI on Windows 10+
        os.system("cls" if os.name == "nt" else "clear")
    top = "╔" + "═" * (min(_w(), 80) - 2) + "╗"
    bot = "╚" + "═" * (min(_w(), 80) - 2) + "╝"
    if _tty():
        print(C1 + _center(top) + RESET)
        for i, line in enumerate(ASCII):
            color = C1 if i < 3 else C2
            print(_center(color + BOLD + line + RESET))
        meta = f"{C3}{DIM}axe-core · Playwright · v{version}{RESET}"
        print(_center(meta))
        print(_center(bot))
    else:
        for line in ASCII:
            print(_center(line))
        print(_center(f"v{version}"))

SPIN = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"

def spinner(text: str):
    i = 0
    try:
        while True:
            frame = SPIN[i % len(SPIN)]
            line = f"{C2 if _tty() else ''}{frame}{RESET if _tty() else ''} {text}"
            print("\r" + line.ljust(_w()), end="", flush=True)
            time.sleep(0.1)
            i += 1
    except KeyboardInterrupt:
        print()

def flash_ok(msg: str):
    ok = "\033[38;5;82m✔\033[0m " if _tty() else "[OK] "
    print(ok + msg)

def flash_err(msg: str):
    er = "\033[38;5;196m✖\033[0m " if _tty() else "[ERR] "
    print(er + msg)
