import flet as ft

from flet_lucid import Icon, Icons


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.always_on_top = True

    # Works on desktop and web. The font is bundled by flutter_lucide,
    # so no asset copy or page.fonts is needed.
    page.add(
        ft.Text("Icon (desktop + web)", size=16),
        Icon(Icons.AMPHORA, size=100),
    )


ft.run(main)
