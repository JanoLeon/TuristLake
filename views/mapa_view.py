import flet as ft
from core.i18n import t
from ui.navbar import build_appbar
from core.ui_helpers import text_title, text_body

def view_mapa(page: ft.Page):
    page.appbar = build_appbar(page)
    page.title = f"{t(page, 'app_title')} · {t(page, 'map')}"
    page.add(
        ft.Container(
            padding=20,
            content=ft.Column(
                controls=[
                    text_title(page, t(page, "map")),
                    text_body(page, t(page, "map_desc")),
                    ft.ElevatedButton(t(page, "back_home"), on_click=lambda e: page.go("/")),
                ],
                spacing=12,
            ),
        )
    )
    page.update()
