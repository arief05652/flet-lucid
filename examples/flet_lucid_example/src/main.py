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
