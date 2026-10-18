#!/usr/bin/env python3
"""Build pages/mapscore/mapscore-main.html from its template.

Embeds the three page images (assets/mapscore/*.webp) as data URIs so the
block works as soon as it's pasted into GHL. Edit the template, not the
generated file, then run:  python3 scripts/build-mapscore.py
"""
import base64
from pathlib import Path

root = Path(__file__).resolve().parent.parent
tpl = (root / "pages/mapscore/mapscore-main.template.html").read_text(encoding="utf-8")
images = {
    "__HERO_PHOTO__": "assets/mapscore/hero-gold-pin.webp",
    "__HEATMAP_BEFORE__": "assets/mapscore/heatmap-before.webp",
    "__HEATMAP_AFTER__": "assets/mapscore/heatmap-after.webp",
}
for token, path in images.items():
    assert tpl.count(token) == 1, token
    data = base64.b64encode((root / path).read_bytes()).decode()
    tpl = tpl.replace(token, "data:image/webp;base64," + data)
out = root / "pages/mapscore/mapscore-main.html"
out.write_text(tpl, encoding="utf-8")
print(f"Wrote {out.relative_to(root)} ({out.stat().st_size // 1024} KB)")
