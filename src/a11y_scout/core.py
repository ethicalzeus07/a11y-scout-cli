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
        axe_js = page.evaluate(f"await (await fetch('{AXE_JS_URL}')).text()")
        page.add_script_tag(content=axe_js)
        # run axe in page context
        results = page.evaluate("await axe.run(document)")
        browser.close()
    if out_json:
        out_json.write_text(json.dumps(results, indent=2))
    return results
