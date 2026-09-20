# Gallery previews

These PNGs are captures of the repository theme JSON rendered by Clink's actual keyboard in an app-hosted iOS simulator. They use a 390 × 280 point English keyboard at 2× resolution, with the theme background enabled. Animations and press feedback are not represented in these still images.

To refresh the gallery:

1. Run `ThemeRepositoryGalleryTests` in the Clink iOS project with the Clink app as `TEST_HOST`.
2. Export the result bundle's attachments using `xcrun xcresulttool export attachments --path <result.xcresult> --output-path <attachments>`.
3. Install Pillow (`python3 -m pip install Pillow`) and run `python3 tools/update-readme-gallery.py <attachments>` in this repository. The script compresses the PNGs without changing their pixels.

`preview-manifest.json` records the source theme and preview hashes, so stale artwork can be identified after theme edits. The images are README assets only; they are not added to downloadable theme packs.
