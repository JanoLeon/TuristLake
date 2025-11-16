import flet as ft

def get_font_settings(page: ft.Page):
    font_scale = float(page.client_storage.get("font_scale") or 1.0)
    easy_read = (page.client_storage.get("easy_read") or "0") == "1"
    return font_scale, easy_read

def text_title(page: ft.Page, text: str) -> ft.Text:
    font_scale, easy_read = get_font_settings(page)
    return ft.Text(
        text,
        size=24 * font_scale,
        weight=ft.FontWeight.BOLD if easy_read else ft.FontWeight.BOLD,
    )

def text_body(page: ft.Page, text: str, base_size: float = 14, opacity: float = 1.0) -> ft.Text:
    font_scale, easy_read = get_font_settings(page)
    return ft.Text(
        text,
        size=base_size * font_scale,
        weight=ft.FontWeight.W_600 if easy_read else None,
        opacity=opacity,
    )
