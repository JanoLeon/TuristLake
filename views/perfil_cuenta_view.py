import flet as ft
from core.i18n import t
from ui.navbar import build_appbar
from core.ui_helpers import text_body


def view_perfil_cuenta(page: ft.Page):
    page.appbar = build_appbar(page)
    page.title = f"{t(page, 'app_title')} · {t(page, 'profile')}"

    # Nombre del usuario con cuenta
    username = (page.client_storage.get("account_username") or "").strip()
    if not username:
        username = "Invitado"

    # Nombre visual en mayúsculas
    display_name = username.upper()

    # Iniciales para el avatar
    initials = "".join([p[0].upper() for p in username.split() if p])[:2]

    avatar_size = 96

    avatar = ft.Stack(
        controls=[
            ft.CircleAvatar(
                content=ft.Text(
                    initials,
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.WHITE,
                ),
                radius=avatar_size / 2,
                bgcolor=ft.Colors.BLUE_GREY_400,
            ),
            ft.Container(
                width=avatar_size + 10,
                height=avatar_size + 10,
                border_radius=avatar_size,
                border=ft.border.all(2, ft.Colors.BLUE_GREY_200),
            ),
            ft.Container(
                alignment=ft.alignment.bottom_right,
                width=avatar_size + 10,
                height=avatar_size + 10,
                content=ft.Container(
                    width=28,
                    height=28,
                    border_radius=16,
                    bgcolor=ft.Colors.WHITE,
                    alignment=ft.alignment.center,
                    content=ft.Icon(
                        ft.Icons.CAMERA_ALT,
                        size=16,
                        color=ft.Colors.BLUE_GREY_700,
                    ),
                ),
            ),
        ],
        width=avatar_size + 10,
        height=avatar_size + 10,
        alignment=ft.alignment.center,
    )

    subtitle = ft.Text(
        "Explorando TuristLake",
        size=14,
        color=ft.Colors.GREY_600,
    )

    def on_edit_profile(e):
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Edición de perfil aún no implementada."),
        )
        page.snack_bar.open = True
        page.update()

    edit_icon = ft.IconButton(
        icon=ft.Icons.EDIT,
        icon_size=18,
        tooltip="Editar perfil",
        on_click=on_edit_profile,
    )

    profile_header = ft.Column(
        spacing=8,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            avatar,
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=4,
                controls=[
                    ft.Text(
                        display_name,
                        size=18,
                        weight=ft.FontWeight.W_700,
                    ),
                    edit_icon,
                ],
            ),
            subtitle,
        ],
    )

    def on_logout(e):
        page.client_storage.remove("account_username")
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Has cerrado sesión."),
        )
        page.snack_bar.open = True
        page.go("/perfil")
        page.update()

    logout_button = ft.ElevatedButton(
        text="Cerrar sesión",
        icon=ft.Icons.LOGOUT,
        on_click=on_logout,
    )

    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.top_center,
            padding=20,
            content=ft.Column(
                spacing=24,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    profile_header,
                    ft.Divider(),
                    text_body(
                        page,
                        "Aquí podrás ver y administrar tu información personal mientras exploras la zona del Lago Llanquihue.",
                        base_size=13,
                    ),
                    logout_button,
                    ft.ElevatedButton(
                        t(page, "back_home"),
                        on_click=lambda e: page.go("/"),
                    ),
                ],
            ),
        )
    )
    page.update()
