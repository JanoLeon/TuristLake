import flet as ft
from core.i18n import t


def _set_lang_and_reload(page: ft.Page, lang: str, sheet: ft.BottomSheet | None = None):
    page.client_storage.set("lang", lang)

    if sheet is not None:
        sheet.open = False

    from views.index_view import view_index
    page.clean()
    view_index(page)
    page.update()


def _build_lang_sheet(page: ft.Page) -> ft.BottomSheet:
    sheet = ft.BottomSheet(
        show_drag_handle=True,
        content=ft.Container(
            width=360,
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
                        on_click=lambda e: _set_lang_and_reload(page, "es", sheet),
                        width=320,
                    ),
                    ft.ElevatedButton(
                        t(page, "english"),
                        on_click=lambda e: _set_lang_and_reload(page, "en", sheet),
                        width=320,
                    ),
                    ft.ElevatedButton(
                        t(page, "chinese"),
                        on_click=lambda e: _set_lang_and_reload(page, "zh", sheet),
                        width=320,
                    ),

                    ft.Row(
                        controls=[
                            ft.TextButton(
                                t(page, "close"),
                                on_click=lambda e: _close_sheet(page, sheet),
                            )
                        ],
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

    # --- Colores según tema ---
    if page.theme_mode == ft.ThemeMode.DARK:
        appbar_color = ft.Colors.INDIGO_900
        icon_color = ft.Colors.WHITE
        text_color = ft.Colors.WHITE
        circle_color = ft.Colors.WHITE24
    else:
        appbar_color = ft.Colors.INDIGO_900
        icon_color = ft.Colors.GREY_300
        text_color = ft.Colors.GREY_200
        circle_color = ft.Colors.WHITE24
    # ---------------------------

    def open_lang_dialog(e):
        bs = _build_lang_sheet(page)
        page.open(bs)

    return ft.AppBar(
        title=ft.Row(
            spacing=8,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    width=44,
                    height=44,
                    border_radius=999,     # círculo detrás
                    bgcolor=circle_color,  # semitransparente, se ve bien en ambos temas
                    alignment=ft.alignment.center,
                    padding=4,
                    content=ft.Image(
                        src="assets/logo.png",
                        width=34,
                        height=34,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                ),
                ft.Text(
                    t(page, "app_title"),
                    color=text_color,
                    weight=ft.FontWeight.W_600,
                ),
            ],
        ),
        center_title=False,
        bgcolor=appbar_color,
        leading=ft.IconButton(
            icon=ft.Icons.PERSON,
            icon_color=icon_color,
            tooltip=t(page, "profile"),
            on_click=lambda e: page.go("/perfil"),
        ),
        actions=[
            ft.IconButton(
                icon=ft.Icons.LANGUAGE,
                icon_color=icon_color,
                tooltip=t(page, "select_lang"),
                on_click=open_lang_dialog,
            )
        ],
    )
