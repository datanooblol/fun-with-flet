import flet as ft


def ChatContainer(children):
    return ft.Container(
        ft.Container(
            ft.Column(children),
            width=700,
        ),
        alignment=ft.alignment.center,
        expand=True
    )