import flet as ft
from core.i18n import t
from ui.navbar import build_appbar

def view_perfil(page: ft.Page):
    page.appbar = build_appbar(page)
    page.title = f"{t(page, 'app_title')} · {t(page, 'profile')}"
    page.add(
        ft.Container(
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Text(t(page, "profile"), size=24, weight=ft.FontWeight.BOLD),
                    ft.Text(t(page, "profile_desc"), size=14),
                    ft.ElevatedButton(t(page, "back_home"), on_click=lambda e: page.go("/")),
                ],
                spacing=12,
            ),
        )
    )
    page.update()
