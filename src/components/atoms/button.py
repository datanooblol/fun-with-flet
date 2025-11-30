import flet as ft


def Button(text="Button", variant="primary", size="medium", on_click=None, icon=None):
    """
    Atomic Button component with variants
    
    Variants:
    - primary: Blue background
    - secondary: Grey background  
    - danger: Red background
    - ghost: Transparent with border
    
    Sizes:
    - small: 32px height
    - medium: 40px height
    - large: 48px height
    """
    
    # Variant styles
    variant_styles = {
        "primary": {
            "bgcolor": ft.Colors.BLUE,
            "color": ft.Colors.WHITE,
            "border": None
        },
        "secondary": {
            "bgcolor": ft.Colors.GREY_300,
            "color": ft.Colors.BLACK,
            "border": None
        },
        "danger": {
            "bgcolor": ft.Colors.RED,
            "color": ft.Colors.WHITE,
            "border": None
        },
        "ghost": {
            "bgcolor": ft.Colors.TRANSPARENT,
            "color": ft.Colors.BLUE,
            "border": ft.border.all(1, ft.Colors.BLUE)
        }
    }
    
    # Size styles
    size_styles = {
        "small": {"height": 32, "padding": ft.padding.symmetric(horizontal=12)},
        "medium": {"height": 40, "padding": ft.padding.symmetric(horizontal=16)},
        "large": {"height": 48, "padding": ft.padding.symmetric(horizontal=20)}
    }
    
    style = variant_styles.get(variant, variant_styles["primary"])
    size_style = size_styles.get(size, size_styles["medium"])
    
    # Build row content, filtering out None values
    row_content = []
    if icon:
        row_content.append(ft.Icon(icon, size=16))
    row_content.append(ft.Text(text, weight=ft.FontWeight.W_500))
    
    return ft.Container(
        ft.Row(
            row_content,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=8
        ),
        bgcolor=style["bgcolor"],
        border=style.get("border"),
        border_radius=6,
        padding=size_style["padding"],
        height=size_style["height"],
        on_click=on_click,
        ink=True
    )