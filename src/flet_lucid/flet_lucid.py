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
    """The icon name from the `Icons` enum (Lucide-based)."""

    size: Optional[ft.Number] = None
    """Icon size in logical pixels. `None` uses the Flet default."""

    color: Optional[ft.ColorValue] = None
    """Icon color (accepts `ft.Colors`, hex, etc.). `None` uses default."""

    blend_mode: Optional[ft.BlendMode] = None
    """Blend mode when drawing over a background."""

    semantics_label: Optional[str] = None
    """Semantic label for screen reader accessibility."""

    apply_text_scaling: Optional[bool] = None
    """If `True`, icon size follows the system text scale."""

    fill: Optional[ft.Number] = None
    """Variable-font fill level (0.0 = outline, 1.0 = solid)."""

    grade: Optional[ft.Number] = None
    """Variable-font grade / optical thickness adjustment."""

    weight: Optional[ft.Number] = None
    """Variable-font stroke weight (typical 100-700)."""

    optical_size: Optional[ft.Number] = None
    """Variable-font optical size (`opsz`)."""

    shadows: Optional[ft.BoxShadowValue] = None
    """Shadow(s) applied to the icon."""
