#!/usr/bin/env bash
# Stitches every section into preview.html so the full page can be viewed
# locally. preview.html is for review only — paste the files in sections/
# into GoHighLevel, not this file.
set -euo pipefail
cd "$(dirname "$0")/.."

{
  cat <<'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CBB Home Preview</title>
<!-- Preview only: GHL loads these fonts itself -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap">
<style>body { margin: 0; background: #0A0B0C; }</style>
</head>
<body>
EOF
  for f in sections/*.html; do
    cat "$f"
    printf '\n'
  done
  printf '</body>\n</html>\n'
} > preview.html

echo "Wrote preview.html"
