#!/usr/bin/env python3
"""Import Clink's repository gallery captures and refresh the README gallery.

Run ThemeRepositoryGalleryTests in an app-hosted iOS simulator, export its
xcresult attachments, then pass that export directory to this script.
"""
import argparse
import hashlib
import html
import json
from pathlib import Path
import re
from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('attachments', type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
repository = root.name
sources = {json.loads(p.read_text())['id']: p for p in (root/'Themes').glob('*.clinktheme')
           if not p.name.startswith('.')}
themes = sorted((json.loads(p.read_text()) for p in sources.values()),
                key=lambda t: t['name'].casefold())
attachments = json.loads((args.attachments/'manifest.json').read_text())
exports = {}
for test in attachments:
    for item in test.get('attachments', []):
        name = item['suggestedHumanReadableName']
        if name.startswith(repository+'--'):
            key = re.sub(r'_\d+_[A-Fa-f0-9-]+\.png$', '', name[len(repository)+2:])
            exports[key] = args.attachments/item['exportedFileName']
missing = {t['id'] for t in themes} - exports.keys()
if missing:
    raise SystemExit(f'Missing captures: {sorted(missing)}')
preview_dir = root/'README-assets/previews'
preview_dir.mkdir(parents=True,exist_ok=True)
checksums = {}
for theme in themes:
    dest=preview_dir/f'{theme["id"]}.png'
    with Image.open(exports[theme['id']]) as image:
        metadata = {k: image.info[k] for k in ('icc_profile', 'dpi') if k in image.info}
        image.save(dest, optimize=True, **metadata)
    source=sources[theme['id']]
    checksums[theme['id']]={'themeSHA256':hashlib.sha256(source.read_bytes()).hexdigest(),
                            'previewSHA256':hashlib.sha256(dest.read_bytes()).hexdigest()}
(root/'README-assets/preview-manifest.json').write_text(json.dumps(checksums,indent=2)+'\n')

def cell(theme):
    if theme is None: return ''
    key=theme['id'];name=html.escape(theme['name']);image=f'README-assets/previews/{key}.png'
    return f'<a href="Themes/{sources[key].name}"><strong>{name}</strong></a><br><a href="{image}"><img src="{image}" width="400" alt="{name} keyboard preview"></a>'

lines=['<!-- theme-gallery:start -->','## Included themes','']
if repository.endswith('-unofficial'):
    lines += [f'{len(themes)} unofficial themes, with light and dark versions shown together. These themes are inspired by the named brands and are not affiliated with or endorsed by them.','', '| Light | Dark |','| --- | --- |']
    pairs={}
    for t in themes:
        family,variant=t['id'].rsplit('-',1)
        pairs.setdefault(family,{})[variant]=t
    for family in sorted(pairs):
        variants=pairs[family]
        lines.append(f'| {cell(variants.get("light"))} | {cell(variants.get("dark"))} |')
else:
    lines += [f'{len(themes)} keyboard themes. Select a name to open its theme file, or a preview to see it at full size.','']
    styles=[('solid','Solid'),('3d','3D'),('liquidGlass','Liquid Glass'),('liquidIce','Ice'),('metal','Metal'),('classic','Classic'),('gamepad','Gamepad'),('molten','Molten')]
    assert set(t['material'] for t in themes) <= {s[0] for s in styles}
    for kind,title in styles:
        group=[t for t in themes if t['material']==kind]
        if not group: continue
        lines += [f'### {title}', '', '| | |','| --- | --- |']
        for i in range(0,len(group),2):
            lines.append(f'| {cell(group[i])} | {cell(group[i+1] if i+1<len(group) else None)} |')
        lines.append('')
lines += ['', 'The complete collection is published under [`Themes/`](Themes). The generated [`manifest.json`](manifest.json) describes every release asset.', '', '<!-- theme-gallery:end -->','']
p=root/'README.md';s=p.read_text()
if '<!-- theme-gallery:start -->' in s:
    s=re.sub(r'<!-- theme-gallery:start -->.*?<!-- theme-gallery:end -->\n', '\n'.join(lines),s,flags=re.S)
else:
    a=s.index('## Included themes');b=s.index('## Make your first theme',a)
    s=s[:a]+'\n'.join(lines)+'\n'+s[b:]
p.write_text(s)
print(f'{repository}: {len(themes)} previews and README entries updated')
