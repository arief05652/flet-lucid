import flet as ft

from flet_lucid import Icon, Icons, WebIcons


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.always_on_top = True

    page.fonts = {"lucide": "/fonts/lucide.ttf"}

    page.add(
        # ft.Text(
        #     value=WebIcons.APP_WINDOW_MAC.value,
        #     style=ft.TextStyle(
        #         size=100,
        #         font_family="lucide",
        #     ),
        # ),
        Icon(Icons.ALIGN_VERTICAL_DISTRIBUTE_START, size=100)
    )


ft.run(main, assets_dir="assets")
