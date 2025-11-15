# views/index_view.py
import flet as ft
from core.i18n import t
from ui.navbar import build_appbar

def _square_button(text: str, icon_name: str, on_click=None) -> ft.Container:
    return ft.Container(
        width=150,
        height=150,
        bgcolor=ft.Colors.SURFACE,
        border_radius=ft.border_radius.all(20),
        border=ft.border.all(2, ft.Colors.ON_SURFACE),
        ink=True,
        on_click=on_click,
        padding=20,
        content=ft.Column(
            controls=[ft.Icon(icon_name, size=42), ft.Text(text, size=16, weight=ft.FontWeight.W_600)],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
        ),
    )

def view_index(page: ft.Page):
    page.appbar = build_appbar(page)
    page.title = t(page, "app_title")

    fila_superior = ft.Row(
        controls=[
            _square_button(t(page, "map"),      ft.Icons.MAP,        on_click=lambda e: page.go("/mapa")),
            _square_button(t(page, "sos"),      ft.Icons.SOS,        on_click=lambda e: page.go("/sos")),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
    )

    fila_inferior = ft.Row(
        controls=[
            _square_button(t(page, "activity"), ft.Icons.SHOW_CHART, on_click=lambda e: page.go("/actividad")),
            _square_button(t(page, "settings"), ft.Icons.SETTINGS,   on_click=lambda e: page.go("/ajustes")),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=16,
    )

    # Contenedor centrado, con un poco de margen superior para “bajar” los botones
    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.center,  # centra en ambos ejes
            padding=ft.padding.only(top=40, left=20, right=20, bottom=20),
            content=ft.Column(
                controls=[
                    ft.Text(t(page, "home_desc"), size=14, opacity=0.8),
                    fila_superior,
                    fila_inferior,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=16,
            ),
        )
    )
    page.update()
