# A11Y Scout

A Python CLI tool for accessibility testing using axe-core and Playwright.

## Installation

```bash
pip install -e .
```

## Usage

```bash
a11y-scout <url>
```

## Optional rich banner

If `chafa` is installed and `assets/logo.png` exists, the CLI renders a color logo.

- macOS: `brew install chafa`
- Debian/Ubuntu: `sudo apt-get install chafa`

Disable banner with:
```bash
A11Y_SCOUT_NO_BANNER=1 a11y-scout https://example.com
```

## Features

- Scans websites for accessibility violations
- Uses industry-standard axe-core engine
- Generates JSON/CLI summaries with fix links
- Targets WCAG 2.x A/AA compliance
- Rich terminal interface with animated banners
