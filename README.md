<p align="center">
  <img src="https://raw.githubusercontent.com/anti-ltd/clink-language-packs/main/icon-1024.png" width="96" alt="Clink app icon">
</p>

<h1 align="center">Clink themes</h1>

<p align="center">Open keyboard themes for Clink.</p>

Themes change the keyboard's colours, materials, type treatment, and gradients. They are ordinary JSON, so you can read every setting before you publish it.

## Official Clink repositories

[Language packs](https://github.com/anti-ltd/clink-language-packs) · [Layouts](https://github.com/anti-ltd/clink-layouts) · [Profiles](https://github.com/anti-ltd/clink-profiles) · [Themes](https://github.com/anti-ltd/clink-themes) · [Panels](https://github.com/anti-ltd/clink-panels) · [Actions](https://github.com/anti-ltd/clink-actions)

## Included themes

| Theme | Look |
|---|---|
| ✨ Nebula | A deep violet keyboard with luminous lavender accents. |
| 🎨 Clink collection | The full former in-app preset collection, now available on demand. |

## Make your first theme

You do not need to build an app or write a manifest.

1. Fork this repository.
2. In Clink, make a theme you like and use **Export** from the theme menu. This gives you a `.clinktheme` file.
3. Put that file in `Themes/`, for example `Themes/my-theme.clinktheme`.
4. Open the file in a text editor. Give it a permanent lowercase `id`, and a clear visible `name`.
5. Do not include `backgroundImageID` or `keyImageID`. A repository theme can contain colours, gradients, materials, and fonts, but not image files.
6. Push to `main`.

The included GitHub Action reads every file, calculates its SHA-256 hash and byte size, writes `manifest.json`, and publishes the `latest` release for you. You never need to make a tag or release by hand.

## Add your repository to Clink

In Clink, open **General → Repositories** and add `owner/repository`, for example `your-name/my-clink-themes`. Open **Customize → Look**, then choose your repository's tab. Downloaded themes remain available offline and can be used for free. They stay read-only, but anyone can make an editable copy.

## What Clink verifies

Clink accepts only public HTTPS GitHub release manifests. Each theme must come from that same repository's release, be a `.clinktheme` JSON file no larger than 128 KB, and match the SHA-256 hash and byte count in the manifest. Clink downloads to a temporary folder, verifies the file and its safe data-only structure, then installs it. Themes cannot contain photos or executable code.
