from a11y_scout import scan

def test_scan_example():
    r = scan("https://example.com")
    assert "violations" in r
