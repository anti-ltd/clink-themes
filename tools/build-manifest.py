#!/usr/bin/env python3
"""Build the verified manifest for a Clink theme release."""
import hashlib
import json
import os
import pathlib

root = pathlib.Path(__file__).resolve().parents[1]
repository = os.environ.get("GITHUB_REPOSITORY", "anti-ltd/clink-themes")
files = []
for path in sorted((root / "Themes").glob("*.clinktheme")):
    # macOS can create AppleDouble sidecars on external volumes.
    if not path.name.startswith("."):
        files.append((path, path.read_bytes()))

# Each distinct set of bytes gets a permanent release URL. A cached manifest
# must never point at a newer file with a different checksum: an app that read
# the catalog before a release still installs the bytes it was promised.
identity = json.dumps([(path.name, hashlib.sha256(raw).hexdigest())
                       for path, raw in files], separators=(",", ":"))
version = "themes-" + hashlib.sha256(identity.encode()).hexdigest()
themes = []
for path, raw in files:
    theme = json.loads(raw)
    themes.append({
        "id": path.stem,
        "name": theme["name"],
        "version": version,
        "preview": theme,
        "asset": {
            "path": path.name,
            "url": f"https://github.com/{repository}/releases/download/{version}/{path.name}",
            "sha256": hashlib.sha256(raw).hexdigest(),
            "byteCount": len(raw),
        },
    })
(root / "manifest.json").write_text(json.dumps({"version": version, "themes": themes}, indent=2) + "\n")
print(f"{len(themes)} themes · {version}")
