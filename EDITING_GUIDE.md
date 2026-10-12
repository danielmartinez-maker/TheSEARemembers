# Editing guide

This is a **work in progress**, not a continuity-corrected or line-edited manuscript. The import preserves the source text; editorial criticism belongs in issues or pull requests until a change is agreed.

1. Find the chapter in [CHAPTER_INDEX.md](CHAPTER_INDEX.md).
2. Edit that chapter only, ideally in a focused pull request; note any continuity impacts on adjacent chapters.
3. Review character ages, timelines, cabin affiliations, relationship changes, and plot setup before merging.
4. Run `python scripts/assemble.py` from the repository root to regenerate the reader manuscript.
5. The `--verify` option checks the *initial import*, and will intentionally fail after valid content edits.

The original manuscript was split without prose edits. `manifest.json` records reading order and the original full-text SHA-256 so future revisions can be compared precisely.
