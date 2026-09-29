#!/usr/bin/env bash
# Builds review-only preview pages. Paste the individual blocks into
# GoHighLevel, never these preview files.
#   preview.html                  home page (every file in sections/)
#   pages/<name>/preview.html     each page listed in pages/<name>/blocks.txt
set -euo pipefail
cd "$(dirname "$0")/.."

write_page() { # $1 = output file, $2 = title, remaining args = block files
  local out=$1 title=$2; shift 2
  {
    cat <<HEAD
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${title}</title>
<!-- Preview only: GHL loads these fonts itself -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap">
<style>body { margin: 0; background: #0A0B0C; }</style>
</head>
<body>
HEAD
    for f in "$@"; do
      cat "$f"
      printf '\n'
    done
    printf '</body>\n</html>\n'
  } > "$out"
  echo "Wrote $out"
}

write_page preview.html "CBB Home Preview" sections/*.html

for list in pages/*/blocks.txt; do
  [ -e "$list" ] || continue
  dir=$(dirname "$list")
  mapfile -t blocks < <(grep -v '^\s*#' "$list" | grep -v '^\s*$')
  write_page "$dir/preview.html" "CBB $(basename "$dir") Preview" "${blocks[@]}"
done
