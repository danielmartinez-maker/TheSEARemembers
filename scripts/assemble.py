#!/usr/bin/env python3
"""Assemble chapter Markdown files into the original reader-edition order."""
from pathlib import Path
import argparse
import hashlib
import json

parser = argparse.ArgumentParser()
parser.add_argument("--output", default="TheSeaRemembers_Full.md")
parser.add_argument("--verify", action="store_true", help="Check unchanged initial import against its original SHA-256")
args = parser.parse_args()

root = Path(__file__).resolve().parent.parent
manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
assembled = b"".join((root / path).read_bytes() for path in manifest["ordered_parts"])
if args.verify:
    actual = hashlib.sha256(assembled).hexdigest()
    if actual != manifest["source_sha256"]:
        raise SystemExit("Assembled manuscript differs from original import: " + actual)
Path(args.output).write_bytes(assembled)
print(f'Assembled {len(manifest["chapters"])} chapters and {len(manifest["bonus_interludes"])} bonus interludes ({len(assembled):,} bytes)')
if args.verify:
    print("Verified source SHA-256")
