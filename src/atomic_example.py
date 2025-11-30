import flet as ft
from components.atoms.button import Button
from components.atoms.input import Input
from components.molecules.input_with_button import InputWithButton


def main(page: ft.Page):
    page.title = "Atomic Design Demo"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 20
    
    def button_clicked(e):
        print(f"Button clicked: {e.control}")
    
    def input_changed(e):
        print(f"Input changed: {e.control.value}")
    
    page.add(
        ft.Column([
            ft.Text("Atomic Design Components", size=24, weight=ft.FontWeight.BOLD),
            
            ft.Divider(),
            ft.Text("Atoms - Buttons", size=18),
            ft.Row([
                Button("Primary", variant="primary", on_click=button_clicked),
                Button("Secondary", variant="secondary", on_click=button_clicked),
                Button("Danger", variant="danger", on_click=button_clicked),
                Button("Ghost", variant="ghost", on_click=button_clicked),
            ], spacing=10),
            
            ft.Row([
                Button("Small", size="small", on_click=button_clicked),
                Button("Medium", size="medium", on_click=button_clicked),
                Button("Large", size="large", on_click=button_clicked),
            ], spacing=10),
            
            ft.Divider(),
            ft.Text("Atoms - Inputs", size=18),
            ft.Column([
                Input(placeholder="Default input", variant="default", on_change=input_changed),
                Input(placeholder="Outlined input", variant="outlined", on_change=input_changed),
                Input(placeholder="Filled input", variant="filled", on_change=input_changed),
            ], spacing=10),
            
            ft.Divider(),
            ft.Text("Molecules - Input with Button", size=18),
            InputWithButton(
                placeholder="Type a message...",
                button_text="Send",
                on_send=button_clicked,
                on_submit=input_changed
            ),
            
        ], spacing=20)
    )


ft.app(main)