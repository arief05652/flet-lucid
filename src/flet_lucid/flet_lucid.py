from typing import Optional

import flet as ft

from .lucid_data import Icons


@ft.control("LucidIcon")
class Icon(ft.LayoutControl):
    """
    This library is based on flutter_lucid from flutter, and with this library, you can use over 1600 icons available on the lucide.dev website.

    You can visit the official website to find the icon you want.
    Lucide Website: https://lucide.dev/

    Example:
        ```python
        from flet_lucid import Icon, Icons

        Icon(Icons.AIRPLAY)
        ```
    """

    icon: Icons
    size: Optional[ft.Number] = None
    color: Optional[ft.ColorValue] = None
    blend_mode: Optional[ft.BlendMode] = None
    semantics_label: Optional[str] = None
    apply_text_scaling: Optional[bool] = None
    fill: Optional[ft.Number] = None
    grade: Optional[ft.Number] = None
    weight: Optional[ft.Number] = None
    optical_size: Optional[ft.Number] = None
    shadows: Optional[ft.BoxShadowValue] = None
