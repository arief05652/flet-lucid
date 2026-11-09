import flet as ft

from .lucid_data import Icons


@ft.control("LucidIcon")
class Icon(ft.LayoutControl):
    """
    This library is based on flutter_lucide from flutter, and with this library, you can use over 2000 icons available on the lucide.dev website.

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

    size: ft.Number | None = None
    """Icon size in logical pixels. `None` uses the Flet default."""

    color: ft.ColorValue | None = None
    """Icon color (accepts `ft.Colors`, hex, etc.). `None` uses default."""

    blend_mode: ft.BlendMode | None = None
    """Blend mode when drawing over a background."""

    semantics_label: str | None = None
    """Semantic label for screen reader accessibility."""

    apply_text_scaling: bool | None = None
    """If `True`, icon size follows the system text scale."""

    fill: ft.Number | None = None
    """Variable-font fill level (0.0 = outline, 1.0 = solid)."""

    grade: ft.Number | None = None
    """Variable-font grade / optical thickness adjustment."""

    weight: ft.Number | None = None
    """Variable-font stroke weight (typical 100-700)."""

    optical_size: ft.Number | None = None
    """Variable-font optical size (`opsz`)."""

    shadows: ft.BoxShadowValue | None = None
    """Shadow(s) applied to the icon."""
