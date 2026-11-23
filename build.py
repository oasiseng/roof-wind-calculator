"""Builds index.html (one self-contained file) from src/page.html, src/cc-wind.js and src/cc-wind-diagram.js.
Run: python build.py        Check that index.html is current: python build.py --check"""
import sys, pathlib
R = pathlib.Path(__file__).parent
page = (R / "src" / "page.html").read_text(encoding="utf-8")
out = page.replace("%ENGINE%", (R / "src" / "cc-wind.js").read_text(encoding="utf-8")).replace("%DIAGRAM%", (R / "src" / "cc-wind-diagram.js").read_text(encoding="utf-8"))
target = R / "index.html"
if "--check" in sys.argv:
    sys.exit(0 if target.read_text(encoding="utf-8") == out else "index.html is out of date: run python build.py")
target.write_text(out, encoding="utf-8")
print("wrote index.html, %d bytes" % len(out.encode()))
