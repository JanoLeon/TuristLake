import flet as ft
from core.i18n import t
from ui.navbar import build_appbar
from core.ui_helpers import text_title, text_body, get_font_settings

def view_ajustes(page: ft.Page):
    page.appbar = build_appbar(page)
    page.title = f"{t(page, 'app_title')} · {t(page, 'settings')}"

    # Leer valores guardados
    current_theme = page.client_storage.get("theme") or "system"
    font_scale, easy_read = get_font_settings(page)

    # Handlers
    def on_theme_change(e):
        value = e.control.value
        page.client_storage.set("theme", value)

        if value == "light":
            page.theme_mode = ft.ThemeMode.LIGHT
        elif value == "dark":
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.SYSTEM

        # 🔥 volver a construir el navbar con el nuevo tema
        page.appbar = build_appbar(page)
        page.update()

    def on_font_change(e):
        value = e.control.value
        page.client_storage.set("font_scale", value)
        # Reconstruye la vista actual con el nuevo tamaño
        page.go(page.route or "/ajustes")

    def on_easy_read_change(e):
        value = e.control.value
        page.client_storage.set("easy_read", "1" if value else "0")
        page.go(page.route or "/ajustes")

    theme_dropdown = ft.Dropdown(
        label=t(page, "theme_mode"),
        value=current_theme,
        options=[
            ft.dropdown.Option("light", t(page, "theme_light")),
            ft.dropdown.Option("dark", t(page, "theme_dark")),
            ft.dropdown.Option("system", t(page, "theme_system")),
        ],
        on_change=on_theme_change,
        width=250,
    )

    font_slider = ft.Slider(
        min=0.8,
        max=1.2,
        divisions=2,
        value=font_scale,
        label="{value:.1f}x",
        on_change=on_font_change,
    )

    easy_read_switch = ft.Switch(
        label=t(page, "easy_reading_option"),
        value=easy_read,
        on_change=on_easy_read_change,
    )

    page.add(
        ft.Container(
            padding=20,
            content=ft.Column(
                controls=[
                    text_title(page, t(page, "settings")),
                    text_body(page, t(page, "settings_desc")),
                    ft.Divider(),

                    # Tema
                    theme_dropdown,

                    # Tamaño de fuente
                    ft.Column(
                        controls=[
                            text_body(page, t(page, "font_size"), base_size=13),
                            font_slider,
                            ft.Row(
                                controls=[
                                    text_body(page, t(page, "font_small"), base_size=12, opacity=0.6),
                                    text_body(page, t(page, "font_medium"), base_size=12, opacity=0.6),
                                    text_body(page, t(page, "font_large"), base_size=12, opacity=0.6),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                        ],
                        spacing=4,
                    ),

                    # Opción de fácil lectura
                    ft.Column(
                        controls=[
                            easy_read_switch,
                            text_body(page, t(page, "easy_reading_desc"), base_size=12, opacity=0.8),
                        ],
                        spacing=4,
                    ),

                    ft.ElevatedButton(t(page, "back_home"), on_click=lambda e: page.go("/")),
                ],
                spacing=16,
            ),
        )
    )
    page.update()
