__all__ = ["scout"]

# Only import scan if playwright is available
try:
    from .core import scan
except ImportError:
    # Playwright not available, scan function will be imported when needed
    pass