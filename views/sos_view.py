import flet as ft
from core.i18n import t
from ui.navbar import build_appbar
from core.ui_helpers import text_title, text_body


def view_sos(page: ft.Page):
    page.appbar = build_appbar(page)
    page.title = f"{t(page, 'app_title')} · {t(page, 'sos')}"

    contactos = [
        {"nombre": "Carabineros Los Lagos", "tel": "132"},
        {"nombre": "Tenencia Puerto Varas", "tel": "+56 65 227 1220"},
        {"nombre": "Retén Ensenada", "tel": "+56 65 221 2030"},
        {"nombre": "SAMU Emergencias", "tel": "131"},
        {"nombre": "Bomberos Puerto Varas", "tel": "132"},
        {"nombre": "Bomberos Puerto Octay", "tel": "+56 64 246 1166"},
        {"nombre": "Capitanía de Puerto (Lago)", "tel": "+56 65 234 4300"},
    ]

    grid_items = []
    for c in contactos:
        card = ft.Container(
            bgcolor=ft.Colors.BLUE_50,
            border_radius=12,
            padding=12,
            content=ft.Column(
                spacing=4,
                controls=[
                    ft.Text(c["nombre"], size=14, weight=ft.FontWeight.W_600),
                    ft.Text(c["tel"], size=13, color=ft.Colors.BLUE_900),
                    ft.ElevatedButton(
                        t(page, "sos_call"),
                        icon=ft.Icons.PHONE,
                        on_click=lambda e, tel=c["tel"]: _llamar(page, tel),
                        height=36,
                    ),
                ],
            ),
        )
        grid_items.append(card)

    grid = ft.GridView(
        expand=True,
        runs_count=2,
        max_extent=200,
        child_aspect_ratio=0.9,
        spacing=12,
        run_spacing=12,
        controls=grid_items,
    )

    page.add(
        ft.Container(
            expand=True,
            padding=20,
            content=ft.Column(
                spacing=16,
                controls=[
                    text_title(page, t(page, "sos")),
                    text_body(page, t(page, "sos_lake_intro")),
                    ft.Divider(),
                    grid,
                    ft.ElevatedButton(
                        t(page, "back_home"),
                        on_click=lambda e: page.go("/"),
                    ),
                ],
            ),
        )
    )
    page.update()


def _llamar(page: ft.Page, telefono: str):
    msg = t(page, "sos_calling").format(phone=telefono)
    page.snack_bar = ft.SnackBar(
        content=ft.Text(msg),
    )
    page.snack_bar.open = True
    page.update()
