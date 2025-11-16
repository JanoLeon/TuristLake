import flet as ft
from core.i18n import t
from ui.navbar import build_appbar
from core.ui_helpers import text_title, text_body

def view_perfil(page: ft.Page):
    page.appbar = build_appbar(page)
    page.title = f"{t(page, 'app_title')} · {t(page, 'profile')}"
    page.add(
        ft.Container(
            padding=20,
            content=ft.Column(
                controls=[
                    text_title(page, t(page, "profile")),
                    text_body(page, t(page, "profile_desc")),
                    ft.ElevatedButton(t(page, "back_home"), on_click=lambda e: page.go("/")),
                ],
                spacing=12,
            ),
        )
    )
    page.update()
