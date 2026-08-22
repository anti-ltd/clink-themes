#!/usr/bin/env python3
"""Build the verified manifest for a Clink theme release."""
import hashlib
import json
import os
import pathlib

root = pathlib.Path(__file__).resolve().parents[1]
repository = os.environ.get("GITHUB_REPOSITORY", "anti-ltd/clink-themes")
themes = []
for path in sorted((root / "Themes").glob("*.clinktheme")):
    raw = path.read_bytes()
    theme = json.loads(raw)
    themes.append({
        "id": path.stem,
        "name": theme["name"],
        "version": "latest",
        "preview": theme,
        "asset": {
            "path": path.name,
            "url": f"https://github.com/{repository}/releases/download/latest/{path.name}",
            "sha256": hashlib.sha256(raw).hexdigest(),
            "byteCount": len(raw),
        },
    })
(root / "manifest.json").write_text(json.dumps({"version": "latest", "themes": themes}, indent=2) + "\n")
