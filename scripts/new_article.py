#!/usr/bin/env python3
"""templates/article/ をコピーして新しい記事フォルダを作る。

使い方:
    python scripts/new_article.py bigquery-cost-tips
    → articles/YYYY/YYYYMMDD-bigquery-cost-tips/ ができる
"""

import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = ROOT / "templates" / "article"

if len(sys.argv) != 2:
    sys.exit("使い方: python scripts/new_article.py <slug>")

slug = sys.argv[1]
today = date.today()
dest = ROOT / "articles" / f"{today:%Y}" / f"{today:%Y%m%d}-{slug}"

if dest.exists():
    sys.exit(f"既にあります: {dest.relative_to(ROOT)}")

shutil.copytree(TEMPLATE_DIR, dest)

# index.md の日付だけ今日の日付に置き換える
index = dest / "index.md"
if index.exists():
    text = index.read_text(encoding="utf-8").replace("YYYY-MM-DD", today.isoformat())
    index.write_text(text, encoding="utf-8")

print(f"作成しました: {dest.relative_to(ROOT)}/")
