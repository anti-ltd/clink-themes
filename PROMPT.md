# Create a Clink theme

You are contributing one polished, data-only keyboard theme to this repository. First inspect `README.md`, a few nearby files in `Themes/`, and `tools/build-manifest.py`. Then create or update exactly one `.clinktheme` in `Themes/`.

Ask for the intended visual direction only if it is not already clear. Turn it into a coherent keyboard design, not just a palette swap: choose legible key and special-key contrast, an appropriate `isDark` value, material, typography, and—where useful—a restrained background effect. Start from the closest existing theme so every supported field and colour object remains valid. Give the file a unique permanent lowercase `id`, a clear human-readable `name`, and a kebab-case filename that matches the theme identity.

Repository themes must remain JSON data. Do not add `backgroundImageID` or `keyImageID`, image assets, executable code, or changes to the release workflow. Preserve colour components as numeric `r`, `g`, `b`, and `a` values in the 0–1 range. Prefer a complete, intentional theme over speculative unsupported properties.

Run:

```sh
python3 tools/build-manifest.py
python3 -m json.tool Themes/<your-file>.clinktheme >/dev/null
```

If a repository validator is added later, run it too. Include the generated `manifest.json` when its contents change. Finish by stating the theme file created, its design rationale, and validation result.
