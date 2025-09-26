import os, sys, shutil, subprocess
from pathlib import Path

def show_logo(version: str = "0.1.0") -> bool:
    """
    Try to render assets/logo.png with `chafa`. Return True if shown.
    Never raises on failure.
    """
    try:
        if os.environ.get("A11Y_SCOUT_NO_BANNER"):
            return False
        if not sys.stdout.isatty():
            return False
        if shutil.which("chafa") is None:
            return False
        root = Path(__file__).resolve().parents[3]  # repo root (go up 3 levels from ui/logo.py)
        img = root / "assets" / "logo.png"
        if not img.exists():
            return False
        cols = shutil.get_terminal_size().columns
        result = subprocess.run(
            ["chafa", str(img), "--size", f"{cols}x24", "--format", "symbols"],
            check=False,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(result.stdout, end="")
            meta = f"\033[2maxe-core · Playwright · v{version}\033[0m"
            print(meta.center(cols))
            return True
        return False
    except Exception:
        return False
