import flet as ft
from core.i18n import t
from ui.navbar import build_appbar


def view_mapa(page: ft.Page):
    page.appbar = build_appbar(page)
    page.title = f"{t(page, 'app_title')} · {t(page, 'map')}"

    # --- elegir control de mapa según plataforma ---
    if page.platform == ft.PagePlatform.WEB:
        # En web, WebView NO está soportado
        mapa_control = ft.Container(
            height=500,
            border_radius=10,
            bgcolor=ft.Colors.RED_400,
            alignment=ft.alignment.center,
            content=ft.Text(
                "El mapa interactivo solo está disponible en la app de escritorio.",
                size=14,
                color=ft.Colors.WHITE,
                text_align=ft.TextAlign.CENTER,
            ),
        )
    else:
        # En app Flet (desktop/mobile) usamos WebView con el asset HTML
        map_url = page.get_asset_url("map_llanquihue.html")

        mapa_control = ft.Container(
            height=500,
            border_radius=10,
            bgcolor=ft.Colors.BLACK12,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            content=ft.WebView(
                url=map_url,
                expand=True,
            ),
        )

    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.top_center,
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Text(t(page, "map"), size=24, weight=ft.FontWeight.BOLD),
                    ft.Text(t(page, "map_desc"), size=14),
                    mapa_control,
                    ft.ElevatedButton(t(page, "back_home"), on_click=lambda e: page.go("/")),
                ],
                spacing=12,
            ),
        )
    )
    page.update()
