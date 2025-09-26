from pathlib import Path
from playwright.sync_api import sync_playwright
import json

AXE_JS_URL = "https://unpkg.com/axe-core@4.7.2/axe.min.js"

def scan(url: str, out_json: Path | None = None) -> dict:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        # inject axe
        page.add_script_tag(url=AXE_JS_URL)
        # run axe in page context
        results = page.evaluate("() => axe.run(document)")
        browser.close()
    if out_json:
        violations_only = results.get('violations', [])
        out_json.write_text(json.dumps(violations_only, indent=2))
    return results
