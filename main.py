import os
import flet as ft
from views.index_view import view_index
from views.perfil_view import view_perfil
from views.mapa_view import view_mapa
from views.sos_view import view_sos
from views.actividades_view import view_actividad
from views.ajustes_view import view_ajustes
from views.perfil_cuenta_view import view_perfil_cuenta


def apply_theme_from_storage(page: ft.Page):
    theme = page.client_storage.get("theme") or "system"
    if theme == "light":
        page.theme_mode = ft.ThemeMode.LIGHT
    elif theme == "dark":
        page.theme_mode = ft.ThemeMode.DARK
    else:
        page.theme_mode = ft.ThemeMode.SYSTEM


def route_resolver(page: ft.Page, route: str):
    page.clean()
    if route == "/perfil":
        view_perfil(page)
    elif route == "/perfil_cuenta":
        view_perfil_cuenta(page)
    elif route == "/mapa":
        view_mapa(page)
    elif route == "/sos":
        view_sos(page)
    elif route == "/actividad":
        view_actividad(page)
    elif route == "/ajustes":
        view_ajustes(page)
    else:
        view_index(page)


def main(page: ft.Page):
    # ---------- Icono de la ventana (solo Desktop Windows) ----------
    base_dir = os.path.dirname(__file__)
    icon_path = os.path.join(base_dir, "assets", "logo.ico")
    page.window.icon = icon_path  # << aquí se cambia el icono
    # ---------------------------------------------------------------

    # ---------- Configuración VENTANA TIPO CELULAR ----------
    page.window_maximized = False
    page.window_full_screen = False
    page.window_resizable = False

    page.window_width = 380
    page.window_height = 760

    page.window_min_width = 380
    page.window_min_height = 760

    page.update()
    # --------------------------------------------------------

    page.padding = 0
    page.spacing = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.scroll = ft.ScrollMode.ADAPTIVE

    # Idioma por defecto
    if page.client_storage.get("lang") not in ("es", "en", "zh"):
        page.client_storage.set("lang", "es")

    # Tema desde storage
    apply_theme_from_storage(page)

    # Valores por defecto de lectura
    if page.client_storage.get("font_scale") is None:
        page.client_storage.set("font_scale", 1.0)
    if page.client_storage.get("easy_read") is None:
        page.client_storage.set("easy_read", "0")

    page.on_route_change = lambda e: route_resolver(page, e.route)
    route_resolver(page, page.route or "/")

if __name__ == "__main__":
    ft.app(
        target=main,
        view=ft.AppView.FLET_APP,
        assets_dir="assets",
    )
