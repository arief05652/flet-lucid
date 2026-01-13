# FLET LUCID

![PyPI - Downloads](https://img.shields.io/pypi/dw/flet-lucid)
![PyPI - Version](https://img.shields.io/pypi/v/flet-lucid)


## Features

- Mudah dipakai
- mendukung sampai 1600++ macam icon
- device yang didukung:

> [!NOTE]
> **🟢 Green**: berarti bisa di build/dapat berjalan \
> **🟡 Yellow**: belum di test \
> **🔴 Red**: tidak di dukung

| Device  | Status |
| --- | --- |
| Android | 🟢 |
| Linux | 🟢 |
| Web | 🔴 |
| Ios | 🟡 |
| Windows | 🟡 |

## Requirements

### Use UV
```bash
uv add flet-lucid
```

## How to Use

> [!NOTE]
> sebelum dijalankan pastikan kamu build terlebih dahulu, kenapa? karna flet harus mendaftarkan terlebih dahulu ke depedensi flutter nya


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
