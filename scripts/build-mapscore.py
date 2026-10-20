#!/usr/bin/env python3
"""Build the MapScore page from pages/mapscore/mapscore-main.template.html.

Writes two files:
  pages/mapscore/mapscore-main.html  the block to paste into GHL. The hero
                                     photo is embedded; every other image and
                                     media URL is left '' in SETTINGS.assets,
                                     ready for GHL Media URLs.
  pages/mapscore/preview.html        a review copy with the shared header and
                                     footer, using the local files in
                                     assets/mapscore/ so everything shows.

Run:  python3 scripts/build-mapscore.py
"""
import base64
from pathlib import Path

root = Path(__file__).resolve().parent.parent
tpl = (root / "pages/mapscore/mapscore-main.template.html").read_text(encoding="utf-8")

hero = base64.b64encode((root / "assets/mapscore/hero-gold-pin.webp").read_bytes()).decode()
assert tpl.count("__HERO_PHOTO__") == 1
tpl = tpl.replace("__HERO_PHOTO__", "data:image/webp;base64," + hero)

# setting key -> file in assets/mapscore/
ASSETS = {
    "graphicProfile": "graphics/google-business-profile.webp",
    "graphicPosts": "graphics/automated-google-posts.webp",
    "graphicReviews": "graphics/review-collection.webp",
    "graphicApproval": "graphics/review-approval.webp",
    "graphicDirectory": "graphics/directory-and-search-network.webp",
    "rroofLogo": "customers/rooster-roofers-logo.webp",
    "rroofBefore": "customers/rooster-roofers-before.webp",
    "rroofAfter": "customers/rooster-roofers-after.webp",
    "hybridLogo": "customers/hybrid-clinic-logo.webp",
    "hybridBefore": "customers/hybrid-clinic-before.webp",
    "hybridAfter": "customers/hybrid-clinic-after.webp",
    "homecrushLogo": "customers/home-crush-logo.webp",
    "homecrushBefore": "customers/home-crush-before.webp",
    "homecrushAfter": "customers/home-crush-after.webp",
    "rankingAnimation": "ranking-improvement.mp4",
    "rankingAnimationPoster": "ranking-improvement-poster.webp",
    "presentationDownload": "CBB_MapScore_Presentation.pptx",
}
SLIDES = [f"slides/slide-{i:02d}.webp" for i in range(1, 12)]
for f in list(ASSETS.values()) + SLIDES:
    assert (root / "assets/mapscore" / f).exists(), f


def fill(text, value_for, slide_value_for, indent=" " * 10):
    for key, path in ASSETS.items():
        token = f"'__A_{key}__'"
        assert text.count(token) == 1, key
        text = text.replace(token, value_for(path))
    slides = ("\n" + ",\n".join(indent + slide_value_for(p) for p in SLIDES) + "\n" + indent[:-2])
    assert text.count("__A_slides__") == 1
    return text.replace("__A_slides__", slides)


# Paste-ready block: GHL Media links from asset-urls.json; anything not
# uploaded yet stays '' with a note of the file it expects.
import json
urls = json.loads((root / "pages/mapscore/asset-urls.json").read_text(encoding="utf-8"))
by_path = {path: urls.get(key, "") for key, path in ASSETS.items()}
by_path.update({p: (urls.get("slides") or [""] * len(SLIDES))[i] for i, p in enumerate(SLIDES)})
# Settings filled the same way in both outputs (no local copy exists).
DIRECT = ["marketingVideo", "marketingVideoPoster"]
for v in list(by_path.values()) + [urls.get(k, "") for k in ["mapscoreLogo"] + DIRECT]:
    assert v == "" or (v.startswith("https://") and "'" not in v and " " not in v), v


def fill_direct(text):
    for k in DIRECT:
        if urls.get(k):
            token = f"      {k}: '',"
            assert text.count(token) == 1, k
            text = text.replace(token + " " * 12, token + "  ")  # long link: drop the column padding
            text = text.replace(token, f"      {k}: '{urls[k]}',")
    return text


def prod(p):
    u = by_path[p]
    return f"'{u}'" if u else f"''  /* upload: {Path(p).name} */"


block = fill_direct(fill(tpl, prod, prod))
if urls.get("mapscoreLogo"):
    block = block.replace("mapscoreLogo: '',", f"mapscoreLogo: '{urls['mapscoreLogo']}',", 1)
block = block.replace(" */  /* upload", " — upload")  # tidy double comments
out = root / "pages/mapscore/mapscore-main.html"
out.write_text(block, encoding="utf-8")

# Preview: local files
local = fill_direct(fill(tpl, lambda p: f"'../../assets/mapscore/{p}'", lambda p: f"'../../assets/mapscore/{p}'"))
header = (root / "sections/00-header.html").read_text(encoding="utf-8")
footer = (root / "sections/06-footer.html").read_text(encoding="utf-8")
page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CBB mapscore Preview</title>
<!-- Preview only: GHL loads these fonts itself. Images and media come from
     ../../assets/mapscore/ here; the GHL block uses GHL Media URLs instead. -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap">
<style>body {{ margin: 0; background: #0A0B0C; }}</style>
</head>
<body>
{header}
{local}
{footer}
</body>
</html>
"""
(root / "pages/mapscore/preview.html").write_text(page, encoding="utf-8")
print(f"Wrote {out.relative_to(root)} ({out.stat().st_size // 1024} KB) and pages/mapscore/preview.html")
