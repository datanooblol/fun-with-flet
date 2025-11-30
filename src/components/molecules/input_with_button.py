import flet as ft
from ..atoms.input import Input
from ..atoms.button import Button


def InputWithButton(placeholder="Type here...", button_text="Send", on_send=None, on_submit=None):
    """
    Molecule: Input field combined with a button
    Uses atomic Input and Button components
    """
    
    input_field = Input(
        placeholder=placeholder,
        variant="outlined",
        on_submit=on_submit
    )
    
    send_button = Button(
        text=button_text,
        variant="primary",
        icon=ft.Icons.SEND,
        on_click=on_send
    )
    
    return ft.Row([
        ft.Container(input_field, expand=True),
        send_button
    ], spacing=8)