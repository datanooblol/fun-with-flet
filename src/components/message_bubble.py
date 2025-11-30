import flet as ft


def MessageBubble(message, sender="You", is_user=True):
    return ft.Container(
        ft.Text(f"{sender}: {message}", color=ft.Colors.WHITE),
        bgcolor=ft.Colors.BLUE if is_user else ft.Colors.GREY,
        padding=10,
        border_radius=10,
        alignment=ft.alignment.center_right if is_user else ft.alignment.center_left
    )