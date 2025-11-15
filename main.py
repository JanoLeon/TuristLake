import flet as ft
from views.index_view import view_index
from views.perfil_view import view_perfil
from views.mapa_view import view_mapa
from views.sos_view import view_sos
from views.actividades_view import view_actividad
from views.ajustes_view import view_ajustes

def route_resolver(page: ft.Page, route: str):
    page.clean()
    if route == "/perfil":
        view_perfil(page)
    elif route == "/mapa":
        view_mapa(page)
    elif route == "/sos":
        view_sos(page)
    elif route == "/actividad":
        view_actividad(page)
    elif route == "/ajustes":
        view_ajustes(page)
    else:
        # "/" y rutas desconocidas -> index
        view_index(page)

def main(page: ft.Page):
    # ---------- Configuración "mobile-like" ----------
    page.window_width = 420           # ancho típico móvil
    page.window_height = 820          # alto típico móvil
    page.window_resizable = False     # evitar redimensionar
    page.window_maximized = False     # no maximizar
    page.padding = 0                  # sin márgenes externos
    page.spacing = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # -----------------------------------------------

    page.scroll = ft.ScrollMode.ADAPTIVE
    page.theme_mode = ft.ThemeMode.SYSTEM

    # Idioma por defecto
    if page.client_storage.get("lang") not in ("es", "en"):
        page.client_storage.set("lang", "es")

    page.on_route_change = lambda e: route_resolver(page, e.route)
    route_resolver(page, page.route or "/")

if __name__ == "__main__":
    # Abrir en navegador con el tamaño configurado
    ft.app(target=main, view=ft.AppView.FLET_APP)
