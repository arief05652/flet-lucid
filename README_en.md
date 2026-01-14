# FLET LUCID

![PyPI - Downloads](https://img.shields.io/pypi/dw/flet-lucid)
![PyPI - Version](https://img.shields.io/pypi/v/flet-lucid)

#### [id_translate](README.md)

## Features

* **Easy to use**
* Supports over **1600+ icons**
* **Supported Devices:**

> [!NOTE]
> **🟢 Green**: Build successful / Running \
> **🟡 Yellow**: Not yet tested \
> **🔴 Red**: Not supported

| Device | Status |
| --- | --- |
| Android | 🟢 |
| Linux | 🟢 |
| MacOS | 🟢 |
| Web | 🔴 |
| IOS | 🟡 |
| Windows | 🟡 |

---

## Requirements

> [!TIP]
> Make sure you are using **flet version 0.80.0 or above** and also using **Python version 3.12 or above**.

### Using UV

```bash
uv add flet-lucid
```

## How to Use

> [!NOTE]
> Ensure you **build** the project before running it. Why? Because Flet needs to register the package to the Flutter dependencies first.

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
