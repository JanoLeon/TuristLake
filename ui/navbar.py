# ui/navbar.py
import flet as ft
from core.i18n import t

def _set_lang_and_reload(page: ft.Page, lang: str, sheet: ft.BottomSheet | None = None):
    page.client_storage.set("lang", lang)
    if sheet is not None:
        sheet.open = False
        page.update()
    # Fuerza reconstrucción de la vista actual (router)
    page.go(page.route or "/")

def _build_lang_sheet(page: ft.Page) -> ft.BottomSheet:
    # Hoja inferior estilo móvil con tres opciones en su idioma nativo
    sheet = ft.BottomSheet(
        show_drag_handle=True,
        content=ft.Container(
            width=360,  # ancho “móvil”
            padding=20,
            content=ft.Column(
                tight=True,
                spacing=12,
                controls=[
                    ft.Text(t(page, "lang_dialog_title"), size=20, weight=ft.FontWeight.W_600),
                    ft.Text(t(page, "lang_dialog_subtitle"), size=13, opacity=0.8),
                    ft.Divider(opacity=0.2),

                    ft.ElevatedButton(
                        t(page, "spanish"),
                        on_click=lambda e, s=sheet: _set_lang_and_reload(page, "es", s),
                        width=320,
                    ),
                    ft.ElevatedButton(
                        t(page, "english"),
                        on_click=lambda e, s=sheet: _set_lang_and_reload(page, "en", s),
                        width=320,
                    ),
                    ft.ElevatedButton(
                        t(page, "chinese"),
                        on_click=lambda e, s=sheet: _set_lang_and_reload(page, "zh", s),
                        width=320,
                    ),

                    ft.Row(
                        controls=[ft.TextButton(t(page, "close"), on_click=lambda e: _close_sheet(page, sheet))],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
            ),
        ),
    )
    return sheet

def _close_sheet(page: ft.Page, sheet: ft.BottomSheet):
    sheet.open = False
    page.update()

def build_appbar(page: ft.Page) -> ft.AppBar:
    # Color dinámico según tema
    if page.theme_mode == ft.ThemeMode.DARK:
        appbar_color = ft.Colors.SURFACE_VARIANT  # clarito en oscuro
    else:
        appbar_color = ft.Colors.INDIGO_900       # azul oscuro en claro

    def open_lang_dialog(e):
        # Ventana emergente estilo móvil
        bs = _build_lang_sheet(page)
        page.open(bs)

    return ft.AppBar(
        title=ft.Text(t(page, "app_title")),
        center_title=False,
        bgcolor=appbar_color,
        leading=ft.IconButton(
            icon=ft.Icons.PERSON,
            tooltip=t(page, "profile"),
            on_click=lambda e: page.go("/perfil"),
        ),
        actions=[
            ft.IconButton(
                icon=ft.Icons.LANGUAGE,
                tooltip=t(page, "select_lang"),
                on_click=open_lang_dialog,
            )
        ],
    )
