import flet as ft
from design_tokens.colors import Colors
from design_tokens.spacing import Spacing
from design_tokens.typography import Typography
from design_tokens.borders import Borders


def Button(text="Button", variant="primary", size="medium", on_click=None, icon=None):
    """
    Button component using Design Tokens
    Demonstrates how to use centralized design system
    """
    
    # Variant styles using design tokens
    variant_styles = {
        "primary": {
            "bgcolor": Colors.PRIMARY,
            "color": Colors.TEXT_INVERSE,
            "border": None
        },
        "secondary": {
            "bgcolor": Colors.SECONDARY_LIGHT,
            "color": Colors.TEXT_PRIMARY,
            "border": None
        },
        "danger": {
            "bgcolor": Colors.DANGER,
            "color": Colors.TEXT_INVERSE,
            "border": None
        },
        "ghost": {
            "bgcolor": Colors.WHITE,
            "color": Colors.PRIMARY,
            "border": ft.border.all(Borders.WIDTH_THIN, Colors.PRIMARY)
        }
    }
    
    # Size styles using design tokens
    size_styles = {
        "small": {
            "height": 32,
            "padding": ft.padding.symmetric(
                horizontal=Spacing.SM, 
                vertical=Spacing.XS
            ),
            "text_size": Typography.CAPTION["size"]
        },
        "medium": {
            "height": 40,
            "padding": ft.padding.symmetric(
                horizontal=Spacing.MD, 
                vertical=Spacing.SM
            ),
            "text_size": Typography.BUTTON["size"]
        },
        "large": {
            "height": 48,
            "padding": ft.padding.symmetric(
                horizontal=Spacing.LG, 
                vertical=Spacing.MD
            ),
            "text_size": Typography.BODY["size"]
        }
    }
    
    style = variant_styles.get(variant, variant_styles["primary"])
    size_style = size_styles.get(size, size_styles["medium"])
    
    # Build row content
    row_content = []
    if icon:
        row_content.append(ft.Icon(icon, size=16, color=style["color"]))
    row_content.append(
        ft.Text(
            text, 
            weight=Typography.BUTTON["weight"],
            size=size_style["text_size"],
            color=style["color"]
        )
    )
    
    return ft.Container(
        ft.Row(
            row_content,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=Spacing.SM
        ),
        bgcolor=style["bgcolor"],
        border=style.get("border"),
        border_radius=Borders.RADIUS_BUTTON,
        padding=size_style["padding"],
        height=size_style["height"],
        on_click=on_click,
        ink=True
    )