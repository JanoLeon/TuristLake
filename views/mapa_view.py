import flet as ft
from core.i18n import t
from ui.navbar import build_appbar
from core.ui_helpers import text_title, text_body


def view_mapa(page: ft.Page):
    page.appbar = build_appbar(page)
    page.title = f"{t(page, 'app_title')} · {t(page, 'map')}"

    # --- DIMENSIONES DEL RECTÁNGULO TIPO CELULAR ---
    CELL_WIDTH = 280
    CELL_HEIGHT = 520

    # --- DIMENSIONES REALES DE LA IMAGEN (AJÚSTALAS SEGÚN TU PNG) ---
    IMG_WIDTH = 634
    IMG_HEIGHT = 464

    # 🔥 Calcular escala mínima para que la imagen SIEMPRE llene el rectángulo
    min_scale_w = CELL_WIDTH / IMG_WIDTH
    min_scale_h = CELL_HEIGHT / IMG_HEIGHT
    MIN_SCALE = max(min_scale_w, min_scale_h)   # evita imágenes más chicas que el contenedor

    # --- INTERACTIVE VIEWER CONFIGURADO CORRECTAMENTE ---
    mapa_interactivo = ft.InteractiveViewer(
        min_scale=MIN_SCALE,
        max_scale=5.0,
        scale_enabled=True,
        pan_enabled=True,
        boundary_margin=ft.Margin(0, 0, 0, 0),  # 🔥 evita salirte del contenedor
        constrained=False,  # 🔥 permite mantener el tamaño de la imagen
        content=ft.Container(
            width=IMG_WIDTH,
            height=IMG_HEIGHT,
            content=ft.Image(
                src="map_llanquihue_offline.png",
                fit=ft.ImageFit.FILL,   # llena el espacio correctamente
            ),
        ),
    )

    rectangulo_mapa = ft.Container(
        width=CELL_WIDTH,
        height=CELL_HEIGHT,
        border_radius=20,
        border=ft.border.all(2, ft.Colors.BLUE_GREY_200),
        bgcolor=ft.Colors.BLACK12,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        content=mapa_interactivo,
    )

    boton_volver = ft.ElevatedButton(
        text=t(page, "back_home"),
        icon=ft.Icons.HOME,
        on_click=lambda e: page.go("/"),
    )

    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.top_center,
            padding=20,
            content=ft.Column(
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    text_title(page, t(page, "map")),
                    text_body(page, t(page, "map_desc"), base_size=13, opacity=0.9),
                    rectangulo_mapa,
                    boton_volver,
                ],
            ),
        )
    )

    page.update()
