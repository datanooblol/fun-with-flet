import flet as ft


def Input(placeholder="Enter text...", variant="default", size="medium", on_change=None, on_submit=None):
    """
    Atomic Input component with variants
    
    Variants:
    - default: Standard input
    - outlined: With border
    - filled: With background
    
    Sizes:
    - small: 32px height
    - medium: 40px height
    - large: 48px height
    """
    
    # Variant styles
    variant_styles = {
        "default": {
            "border": ft.InputBorder.UNDERLINE,
            "bgcolor": ft.Colors.TRANSPARENT
        },
        "outlined": {
            "border": ft.InputBorder.OUTLINE,
            "bgcolor": ft.Colors.TRANSPARENT
        },
        "filled": {
            "border": ft.InputBorder.NONE,
            "bgcolor": ft.Colors.GREY_100
        }
    }
    
    # Size styles
    size_styles = {
        "small": {"height": 32, "text_size": 12},
        "medium": {"height": 40, "text_size": 14},
        "large": {"height": 48, "text_size": 16}
    }
    
    style = variant_styles.get(variant, variant_styles["default"])
    size_style = size_styles.get(size, size_styles["medium"])
    
    return ft.TextField(
        hint_text=placeholder,
        border=style["border"],
        bgcolor=style["bgcolor"],
        height=size_style["height"],
        text_size=size_style["text_size"],
        on_change=on_change,
        on_submit=on_submit,
        border_radius=6
    )