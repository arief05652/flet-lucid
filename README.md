# Flet Lucid

Lucide icons for [Flet](https://flet.dev) — 2,000+ icons exposed as a native Flutter control.

[![PyPI - Version](https://img.shields.io/pypi/v/flet-lucid)](https://pypi.org/project/flet-lucid/)
[![PyPI - Downloads](https://img.shields.io/pypi/dw/flet-lucid)](https://pypi.org/project/flet-lucid/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Flet](https://img.shields.io/badge/flet-%3E%3D1.1.2-blue)](https://flet.dev/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow)](LICENSE)

## Features

- **2,000+ icons** — the full [Lucide](https://lucide.dev) icon set.
- **Native control** — rendered with Flutter, not text or image assets.
- **Works everywhere** — Android, Linux, macOS, and web.
- **Zero asset setup** — the icon font is bundled with the extension.
- **No extra dependencies** — nothing beyond Flet.

## Requirements

- Python 3.10 or newer.
- Flet 1.1.2 or newer.

## Installation

With [uv](https://docs.astral.sh/uv/):

```bash
uv add flet-lucid
```

With pip:

```bash
pip install flet-lucid
```

## Quick Start

```python
import flet as ft

from flet_lucid import Icon, Icons


def main(page: ft.Page):
    page.add(
        Icon(Icons.AIRPLAY, size=48, color=ft.Colors.BLUE),
    )


ft.run(main)
```

> [!IMPORTANT]
> Build your Flet project before running it. Flet must register the package in its Flutter dependencies.

```bash
flet build linux   # or: flet build web, flet build apk
```

## Usage

### Basic icon

```python
Icon(Icons.ALIGN_VERTICAL_DISTRIBUTE_START, size=100)
```

### Color and accessibility

```python
Icon(
    Icons.SHIELD_CHECK,
    size=32,
    color=ft.Colors.GREEN,
    semantics_label="Verified",
)
```

### Icon properties

| Property | Type | Description |
| --- | --- | --- |
| `icon` | `Icons` | Icon to render. Required. |
| `size` | `Number` | Icon size in logical pixels. |
| `color` | `ColorValue` | Icon color. Accepts `ft.Colors`, hex, etc. |
| `blend_mode` | `BlendMode` | Blend mode used when drawing the icon. |
| `semantics_label` | `str` | Accessibility label for screen readers. |
| `apply_text_scaling` | `bool` | Follow the system text scale. |
| `fill` | `Number` | Variable-font fill level (`0.0` outline, `1.0` solid). |
| `grade` | `Number` | Variable-font grade adjustment. |
| `weight` | `Number` | Variable-font stroke weight. |
| `optical_size` | `Number` | Variable-font optical size. |
| `shadows` | `BoxShadowValue` | Shadow applied to the icon. |

## Finding Icons

Browse all available icons at [lucide.dev/icons](https://lucide.dev/icons). Enum names follow the icon name in uppercase with underscores:

```python
Icons.APP_WINDOW_MAC   # app-window-mac
Icons.ARROW_UP_RIGHT   # arrow-up-right
```

## Platform Support

| Platform | Status |
| --- | --- |
| Android | Supported |
| Linux | Supported |
| macOS | Supported |
| Web | Supported |
| iOS | Untested |
| Windows | Untested |

## Development

```bash
git clone https://github.com/arief05652/flet-lucid.git
cd flet-lucid
just sync
just run
```

Useful commands:

```bash
just generate      # regenerate the Icons enum and Dart map
just run web       # run the example on web
just build linux   # build the example
```

## Built With

- [flutter_lucide](https://pub.dev/packages/flutter_lucide) — Flutter package for Lucide icons.
- [Lucide](https://lucide.dev) — open-source icon set.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
