# 🎨 FLET LUCID

[![PyPI - Downloads](https://img.shields.io/pypi/dw/flet-lucid)](https://pypi.org/project/flet-lucid/)
[![PyPI - Version](https://img.shields.io/pypi/v/flet-lucid)](https://pypi.org/project/flet-lucid/)
[![Python](https://img.shields.io/badge/python-3.12%2B-blue)](https://www.python.org/)
[![Flet](https://img.shields.io/badge/flet-%3E%3D0.80.0-blue)](https://flet.dev/)

---

## ✨ Features

- ✅ **Easy to use** — plug directly into your Flet project
- 🎯 **1600+ icons** — full Lucide icon collection
- 📦 **Zero extra dependencies** — lightweight & fast

---

## 📱 Platform Compatibility

![Android](https://img.shields.io/badge/Android-supported-brightgreen)
![Linux](https://img.shields.io/badge/Linux-supported-brightgreen)
![macOS](https://img.shields.io/badge/macOS-supported-brightgreen)
![iOS](https://img.shields.io/badge/iOS-untested-yellow)
![Windows](https://img.shields.io/badge/Windows-untested-yellow)
![Web](https://img.shields.io/badge/Web-not_supported-red)

---

## 📋 Requirements

> [!TIP]
> Make sure you are using **Flet 0.85.0 or above** and **Python 3.12 or above**.

### Install with UV

```bash
uv add flet-lucid
```

### Install with pip

```bash
pip install flet-lucid
```

---

## 🚀 Usage

> [!NOTE]
> Make sure to **build** your project first before running it. Flet needs to register the package into its Flutter dependencies.

```python
import flet as ft
from flet_lucid import Icon, Icons


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.always_on_top = True

    page.add(
        Icon(Icons.AIRPLAY, size=100),
    )

ft.run(main)
```

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
