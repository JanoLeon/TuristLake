import flet as ft
from core.i18n import t
from ui.navbar import build_appbar
from core.ui_helpers import text_title, text_body


def view_actividad(page: ft.Page):
    page.appbar = build_appbar(page)
    page.title = f"{t(page, 'app_title')} · {t(page, 'activity')}"

    actividades = [
        {
            "nombre": "Navegación por el Lago Llanquihue",
            "lugar": "Puerto Varas — Muelle",
            "clp": 15000,
            "contacto": "+56 9 9534 9980",
        },
        {
            "nombre": "Kayak en Ensenada",
            "lugar": "Playa Niklitschek, Ensenada",
            "clp": 20000,
            "contacto": "+56 9 7734 2218",
        },
        {
            "nombre": "Recorrido en bicicleta",
            "lugar": "Ruta Puerto Varas – Frutillar",
            "clp": 25000,
            "contacto": "+56 9 7402 8360",
        },
        {
            "nombre": "Cabalgata frente al volcán Osorno",
            "lugar": "Ensenada",
            "clp": 30000,
            "contacto": "+56 9 9151 8723",
        },
        {
            "nombre": "Rafting Río Petrohué",
            "lugar": "Entrada a Parque Vicente Pérez Rosales",
            "clp": 40000,
            "contacto": "+56 9 9534 9101",
        },
        {
            "nombre": "Pesca recreativa en el lago",
            "lugar": "Puerto Octay — Bahía",
            "clp": 35000,
            "contacto": "+56 9 9650 1123",
        },
        {
            "nombre": "Canopy y tirolesa",
            "lugar": "Camino a Ensenada — Volcán Osorno",
            "clp": 25000,
            "contacto": "+56 9 9473 8822",
        },
        {
            "nombre": "Ascenso teleférico Volcán Osorno",
            "lugar": "Centro de Ski Volcán Osorno",
            "clp": 28000,
            "contacto": "+56 9 9640 5101",
        },
        {
            "nombre": "Stand Up Paddle (SUP)",
            "lugar": "Playa Niklitschek, Puerto Varas",
            "clp": 18000,
            "contacto": "+56 9 5693 7346",
        },
        {
            "nombre": "Tour fotográfico del lago",
            "lugar": "Costanera Puerto Varas",
            "clp": 20000,
            "contacto": "+56 9 8899 1210",
        },
    ]

    USD_RATE = 960
    for a in actividades:
        a["usd"] = round(a["clp"] / USD_RATE, 2)

    tarjetas = []
    for a in actividades:
        tarjeta = ft.Container(
            bgcolor=ft.Colors.AMBER_50,
            border_radius=12,
            padding=12,
            content=ft.Column(
                spacing=6,
                controls=[
                    ft.Text(a["nombre"], size=14, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        f"{t(page, 'activity_location')}: {a['lugar']}",
                        size=12,
                        color=ft.Colors.GREY_700,
                    ),
                    ft.Text(
                        f"{t(page, 'activity_price')}: ${a['clp']:,} CLP",
                        size=12,
                        color=ft.Colors.BLUE_900,
                    ),
                    ft.Text(
                        f"{t(page, 'activity_price_usd')}: ${a['usd']} USD",
                        size=12,
                        color=ft.Colors.BLUE_700,
                    ),
                    ft.Text(
                        f"{t(page, 'activity_contact')}: {a['contacto']}",
                        size=12,
                        color=ft.Colors.GREEN_900,
                    ),
                    ft.ElevatedButton(
                        t(page, "activity_call"),
                        icon=ft.Icons.PHONE,
                        on_click=lambda e, tel=a["contacto"]: _reservar(page, tel),
                        height=34,
                    ),
                ],
            ),
        )
        tarjetas.append(tarjeta)

    grid = ft.GridView(
        expand=True,
        runs_count=1,
        max_extent=500,
        spacing=12,
        run_spacing=12,
        controls=tarjetas,
    )

    page.add(
        ft.Container(
            expand=True,
            padding=20,
            content=ft.Column(
                spacing=16,
                controls=[
                    text_title(page, t(page, "activity")),
                    text_body(page, t(page, "activity_lake_intro")),
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


def _reservar(page: ft.Page, telefono: str):
    msg = t(page, "activity_contacting").format(phone=telefono)
    page.snack_bar = ft.SnackBar(
        content=ft.Text(msg),
    )
    page.snack_bar.open = True
    page.update()
