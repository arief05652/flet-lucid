# 🎨 FLET LUCID

[![PyPI - Downloads](https://img.shields.io/pypi/dw/flet-lucid)](https://pypi.org/project/flet-lucid/)
[![PyPI - Version](https://img.shields.io/pypi/v/flet-lucid)](https://pypi.org/project/flet-lucid/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![Flet](https://img.shields.io/badge/flet-%3E%3D0.80.0-blue)](https://flet.dev/)

---

## Features

- ✅ **Easy to use** — plug directly into your Flet project
- 🎯 **1600+ icons** — full Lucide icon collection
- 📦 **Zero extra dependencies** — lightweight & fast

## Platform Compatibility

![Android](https://img.shields.io/badge/Android-supported-brightgreen)
![Linux](https://img.shields.io/badge/Linux-supported-brightgreen)
![macOS](https://img.shields.io/badge/macOS-supported-brightgreen)
![Web](https://img.shields.io/badge/Web-supported-brightgreen)
![iOS](https://img.shields.io/badge/iOS-untested-yellow)
![Windows](https://img.shields.io/badge/Windows-untested-yellow)

## Requirements

> [!TIP]
> Make sure you are using **Flet 0.80.0 or above** and **Python 3.10 or above**.

### Install with UV

```bash
uv add flet-lucid
```

### Install with pip

```bash
pip install flet-lucid
```

## How to Use

> [!NOTE]
> Make sure to **build** your project first before running it. Flet needs to register the package into its Flutter dependencies.

1. **Import the package**

```python
from flet_lucid import Icon, Icons
```

2. **For non-web apps (Android, Linux, macOS, Windows)** — use it directly:

```python
Icon(Icons.AIRPLAY)
```

3. **For web apps** — include the Lucide font. You can download it [here](https://github.com/arief05652/flet-lucid/tree/main/examples/flet_lucid_example/src/assets/fonts/lucide.ttf).

```python
import flet as ft

from flet_lucid import WebIcons


def main(page: ft.Page):
    page.fonts = {"lucide": "/fonts/lucide.ttf"}

    page.add(
        ft.Text(
            value=WebIcons.APP_WINDOW_MAC.value,
            style=ft.TextStyle(
                size=100,
                font_family="lucide",
            ),
        ),
    )


ft.run(main, assets_dir="assets")
```

## Built With

This repository is built on top of [flutter_lucide](https://pub.dev/packages/flutter_lucide)

- **Website**: [https://lucide.dev](https://lucide.dev)
- **Repository**: [https://github.com/lucide-icons/lucide](https://github.com/lucide-icons/lucide)

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
