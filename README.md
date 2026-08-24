<p align="center">
  <img src="https://raw.githubusercontent.com/anti-ltd/clink-language-packs/main/icon-1024.png" width="96" alt="Clink app icon">
</p>

<h1 align="center">Clink themes</h1>

<p align="center">Open keyboard themes for Clink.</p>

Themes change the keyboard's colours, materials, type treatment, and gradients. They are ordinary JSON data, so you can read every setting before publishing a theme.

## Official Clink repositories

[Language packs](https://github.com/anti-ltd/clink-language-packs) · [Layouts](https://github.com/anti-ltd/clink-layouts) · [Profiles](https://github.com/anti-ltd/clink-profiles) · [Themes](https://github.com/anti-ltd/clink-themes) · [Panels](https://github.com/anti-ltd/clink-panels) · [Actions](https://github.com/anti-ltd/clink-actions) · [Fonts](https://github.com/anti-ltd/clink-fonts) · [Sounds](https://github.com/anti-ltd/clink-sounds)

## Included themes

The official repository includes a broad collection of themes, including:

- **Amethyst**, a dark violet theme with luminous accents.
- **Bauhaus**, a geometric light theme with a Futura typeface.
- **Dracula**, a dark theme with high-contrast purple and pink accents.
- **Liquid Mint**, a light Liquid Glass theme with mint accents.
- **Nebula**, a dark theme with an animated background effect.

The complete collection is published under [`Themes/`](Themes). The generated [`manifest.json`](manifest.json) describes every release asset.

## Make your first theme

You do not need to build Clink or write a manifest.

1. Fork this repository.
2. In Clink, make a theme and choose **Export** from the theme menu. This gives you a `.clinktheme` file.
3. Put the file in [`Themes/`](Themes), for example `Themes/my-theme.clinktheme`.
4. Open the file in a text editor. Give it a permanent lowercase `id` and a clear visible `name`.
5. Do not include `backgroundImageID` or `keyImageID`. Repository themes can contain colours, gradients, materials, and fonts, but not image files.
6. Run these commands:

   ```sh
   python3 tools/build-manifest.py
   python3 tools/validate-manifest.py
   ```

7. Push to `main`. GitHub Actions publishes the themes and manifest to the `latest` release.

## Add your repository to Clink

Open **General → Repositories** in Clink and add `owner/repository`, for example:

```text
your-name/my-clink-themes
```

Then open **Customize → Look**, choose your repository's chip, and download a theme. Downloaded themes remain available offline. They stay read-only, but anyone can make an editable copy.

## Make a theme with an AI agent

This repository includes [`PROMPT.md`](PROMPT.md), a ready-to-use brief for an AI coding agent. Fork the repository, open the fork in your agent, and say:

```text
Read PROMPT.md and create a [describe the visual direction] theme.
```

The prompt tells the agent which existing themes to inspect, which fields are safe to use, and how to regenerate the manifest. Review the resulting JSON and import it into Clink before publishing.

## What Clink verifies

Clink accepts only public HTTPS GitHub release manifests. Each theme must come from that repository's release, be a `.clinktheme` JSON file no larger than 128 KB, and match the SHA-256 hash and byte count in the manifest.

Clink downloads each file into a temporary directory, verifies its checksum and safe data-only structure, and only then installs it. Themes cannot contain photos or executable code.

Adding a repository is a trust decision. Only add repositories whose release contents you trust.

## Publishing is automatic

Keep `Themes/`, `tools/`, and `.github/workflows/` in your fork. Add or update a theme, regenerate the manifest, and push to `main`. GitHub Actions validates the files and refreshes the `latest` release so Clink can download them.
