import flet as ft


def ChatInput(on_send, on_submit):
    return ft.Row([
        ft.TextField(
            hint_text="Type a message...",
            expand=True,
            on_submit=on_submit
        ),
        ft.IconButton(
            icon=ft.Icons.SEND,
            on_click=on_send
        )
    ])