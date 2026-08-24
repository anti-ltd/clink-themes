# Verify this Clink themes repository

Read `README.md`, `PROMPT.md`, representative files in `Themes/`, and `tools/build-manifest.py`. Audit the repository; do not modify files unless asked to fix a specific issue.

For every `Themes/*.clinktheme`, parse and pretty-print the JSON:

```sh
python3 -m json.tool Themes/<file>.clinktheme >/dev/null
```

Then run `python3 tools/build-manifest.py`. Confirm every theme has a unique permanent lowercase id, clear visible name, matching kebab-case filename, valid `isDark` intent, and only supported data fields demonstrated by existing themes. Colour components must be numeric `r`, `g`, `b`, and `a` values from 0 to 1. Review key, special-key, and text contrast for legibility; flag incoherent material/type/background choices. Repository themes must not include `backgroundImageID`, `keyImageID`, image assets, executable code, or speculative properties.

Verify the regenerated `manifest.json` exactly represents the themes and that the release workflow is unchanged. Report every theme checked, JSON and manifest results, visual/contrast concerns (as review findings, not measured claims), and exact paths with recommended fixes. Do not claim device-level visual testing unless it occurred.
