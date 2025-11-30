import flet as ft
from components.atoms.button_with_tokens import Button
from design_tokens.colors import Colors
from design_tokens.spacing import Spacing
from design_tokens.typography import Typography


def main(page: ft.Page):
    page.title = "Design Tokens Demo"
    page.bgcolor = Colors.BG_PRIMARY
    page.padding = Spacing.PAGE
    
    def button_clicked(e):
        print(f"Button clicked: {e.control}")
    
    page.add(
        ft.Column([
            # Header using typography tokens
            ft.Text(
                "Design Tokens System", 
                size=Typography.H1["size"],
                weight=Typography.H1["weight"],
                color=Colors.TEXT_PRIMARY
            ),
            
            ft.Container(height=Spacing.SECTION),  # Section spacing
            
            # Color Palette
            ft.Text(
                "Color Palette", 
                size=Typography.H3["size"],
                weight=Typography.H3["weight"],
                color=Colors.TEXT_PRIMARY
            ),
            
            ft.Row([
                ft.Container(
                    ft.Text("Primary", color=Colors.TEXT_INVERSE, size=12),
                    bgcolor=Colors.PRIMARY,
                    padding=Spacing.MD,
                    border_radius=4,
                    width=100,
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    ft.Text("Secondary", color=Colors.TEXT_PRIMARY, size=12),
                    bgcolor=Colors.SECONDARY,
                    padding=Spacing.MD,
                    border_radius=4,
                    width=100,
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    ft.Text("Success", color=Colors.TEXT_INVERSE, size=12),
                    bgcolor=Colors.SUCCESS,
                    padding=Spacing.MD,
                    border_radius=4,
                    width=100,
                    alignment=ft.alignment.center
                ),
                ft.Container(
                    ft.Text("Danger", color=Colors.TEXT_INVERSE, size=12),
                    bgcolor=Colors.DANGER,
                    padding=Spacing.MD,
                    border_radius=4,
                    width=100,
                    alignment=ft.alignment.center
                ),
            ], spacing=Spacing.SM),
            
            ft.Container(height=Spacing.SECTION),
            
            # Typography Scale
            ft.Text(
                "Typography Scale", 
                size=Typography.H3["size"],
                weight=Typography.H3["weight"],
                color=Colors.TEXT_PRIMARY
            ),
            
            ft.Column([
                ft.Text("Heading 1", size=Typography.H1["size"], weight=Typography.H1["weight"]),
                ft.Text("Heading 2", size=Typography.H2["size"], weight=Typography.H2["weight"]),
                ft.Text("Heading 3", size=Typography.H3["size"], weight=Typography.H3["weight"]),
                ft.Text("Body Large", size=Typography.BODY_LARGE["size"], weight=Typography.BODY_LARGE["weight"]),
                ft.Text("Body", size=Typography.BODY["size"], weight=Typography.BODY["weight"]),
                ft.Text("Body Small", size=Typography.BODY_SMALL["size"], weight=Typography.BODY_SMALL["weight"]),
                ft.Text("Caption", size=Typography.CAPTION["size"], weight=Typography.CAPTION["weight"]),
            ], spacing=Spacing.XS),
            
            ft.Container(height=Spacing.SECTION),
            
            # Buttons with Design Tokens
            ft.Text(
                "Buttons with Design Tokens", 
                size=Typography.H3["size"],
                weight=Typography.H3["weight"],
                color=Colors.TEXT_PRIMARY
            ),
            
            ft.Row([
                Button("Primary", variant="primary", on_click=button_clicked),
                Button("Secondary", variant="secondary", on_click=button_clicked),
                Button("Danger", variant="danger", on_click=button_clicked),
                Button("Ghost", variant="ghost", on_click=button_clicked),
            ], spacing=Spacing.SM),
            
            ft.Row([
                Button("Small", size="small", on_click=button_clicked),
                Button("Medium", size="medium", on_click=button_clicked),
                Button("Large", size="large", on_click=button_clicked),
            ], spacing=Spacing.SM),
            
            ft.Container(height=Spacing.SECTION),
            
            # Spacing Examples
            ft.Text(
                "Spacing System", 
                size=Typography.H3["size"],
                weight=Typography.H3["weight"],
                color=Colors.TEXT_PRIMARY
            ),
            
            ft.Column([
                ft.Container(
                    ft.Text("XS Padding", size=12),
                    bgcolor=Colors.GRAY_LIGHT,
                    padding=Spacing.XS,
                    border_radius=4
                ),
                ft.Container(
                    ft.Text("SM Padding", size=12),
                    bgcolor=Colors.GRAY_LIGHT,
                    padding=Spacing.SM,
                    border_radius=4
                ),
                ft.Container(
                    ft.Text("MD Padding", size=12),
                    bgcolor=Colors.GRAY_LIGHT,
                    padding=Spacing.MD,
                    border_radius=4
                ),
                ft.Container(
                    ft.Text("LG Padding", size=12),
                    bgcolor=Colors.GRAY_LIGHT,
                    padding=Spacing.LG,
                    border_radius=4
                ),
            ], spacing=Spacing.SM),
            
        ], spacing=Spacing.MD)
    )


ft.app(main)