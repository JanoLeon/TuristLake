import flet as ft
from core.i18n import t
from ui.navbar import build_appbar
from core.ui_helpers import text_title, text_body


def view_perfil(page: ft.Page):
    page.appbar = build_appbar(page)
    page.title = f"{t(page, 'app_title')} · {t(page, 'profile')}"

    # Nombre ya guardado (modo sin cuenta), si existe
    guest_name = page.client_storage.get("guest_name") or ""

    # --------- Controles sección "Iniciar sesión" (con cuenta) ---------
    usuario_field = ft.TextField(
        label="Usuario o correo",
        width=320,
    )
    password_field = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=320,
    )

    def on_login(e):
        username = (usuario_field.value or "").strip()

        if not username or not password_field.value:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Ingresa usuario y contraseña."),
            )
            page.snack_bar.open = True
            page.update()
            return

        # Aquí iría la validación real contra backend, por ahora asumimos que es válido
        page.client_storage.set("account_username", username)

        page.snack_bar = ft.SnackBar(
            content=ft.Text(f"Sesión iniciada como: {username}"),
        )
        page.snack_bar.open = True

        # Ir a la vista de perfil con cuenta
        page.go("/perfil_cuenta")
        page.update()

    login_button = ft.ElevatedButton("Iniciar sesión", on_click=on_login)

    login_card = ft.Card(
        content=ft.Container(
            padding=16,
            content=ft.Column(
                spacing=8,
                controls=[
                    text_body(page, "Iniciar sesión con cuenta", base_size=15),
                    usuario_field,
                    password_field,
                    login_button,
                ],
            ),
        )
    )

    # --------- Controles sección "Usar sin cuenta" (solo nombre) ---------
    nombre_field = ft.TextField(
        label="Nombre para usar sin cuenta",
        width=320,
        value=guest_name,
    )

    saludo_label = ft.Text(
        f"Hola {guest_name}" if guest_name else "",
        size=14,
        weight=ft.FontWeight.W_600 if guest_name else None,
    )

    def guardar_nombre(e):
        name = (nombre_field.value or "").strip()

        if not name:
            page.snack_bar = ft.SnackBar(
                content=ft.Text("Escribe un nombre para continuar.")
            )
            page.snack_bar.open = True
        else:
            page.client_storage.set("guest_name", name)
            saludo_label.value = f"Hola {name}"
            page.snack_bar = ft.SnackBar(
                content=ft.Text(f"Nombre guardado: {name}")
            )
            page.snack_bar.open = True

        page.update()

    guest_button = ft.OutlinedButton("Usar sin cuenta", on_click=guardar_nombre)

    guest_card = ft.Card(
        content=ft.Container(
            padding=16,
            content=ft.Column(
                spacing=8,
                controls=[
                    text_body(page, "Usar aplicación sin cuenta", base_size=15),
                    nombre_field,
                    guest_button,
                    saludo_label,
                ],
            ),
        )
    )

    # --------- Layout general de la vista ---------
    page.add(
        ft.Container(
            expand=True,
            alignment=ft.alignment.top_center,
            padding=20,
            content=ft.Column(
                controls=[
                    text_title(page, t(page, "profile")),
                    text_body(page, t(page, "profile_desc")),
                    ft.Divider(),

                    login_card,
                    guest_card,

                    ft.ElevatedButton(
                        t(page, "back_home"),
                        on_click=lambda e: page.go("/"),
                    ),
                ],
                spacing=16,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )
    )

    page.update()
