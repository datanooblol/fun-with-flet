import flet as ft

"""
Typography Design Tokens
Consistent text sizing, weights, and line heights
"""

# Font Sizes (based on modular scale)
FONT_SIZE_XS = 12
FONT_SIZE_SM = 14
FONT_SIZE_BASE = 16
FONT_SIZE_LG = 18
FONT_SIZE_XL = 20
FONT_SIZE_2XL = 24
FONT_SIZE_3XL = 30
FONT_SIZE_4XL = 36
FONT_SIZE_5XL = 48

# Line Heights
LINE_HEIGHT_TIGHT = 1.25
LINE_HEIGHT_NORMAL = 1.5
LINE_HEIGHT_RELAXED = 1.75

# Font Weights (Flet equivalents)
FONT_WEIGHT_LIGHT = ft.FontWeight.W_300
FONT_WEIGHT_NORMAL = ft.FontWeight.W_400
FONT_WEIGHT_MEDIUM = ft.FontWeight.W_500
FONT_WEIGHT_SEMIBOLD = ft.FontWeight.W_600
FONT_WEIGHT_BOLD = ft.FontWeight.W_700

# Typography Scale
class Typography:
    # Headings
    H1 = {
        "size": FONT_SIZE_5XL,
        "weight": FONT_WEIGHT_BOLD,
        "line_height": LINE_HEIGHT_TIGHT
    }
    
    H2 = {
        "size": FONT_SIZE_4XL,
        "weight": FONT_WEIGHT_BOLD,
        "line_height": LINE_HEIGHT_TIGHT
    }
    
    H3 = {
        "size": FONT_SIZE_3XL,
        "weight": FONT_WEIGHT_SEMIBOLD,
        "line_height": LINE_HEIGHT_TIGHT
    }
    
    H4 = {
        "size": FONT_SIZE_2XL,
        "weight": FONT_WEIGHT_SEMIBOLD,
        "line_height": LINE_HEIGHT_NORMAL
    }
    
    # Body Text
    BODY_LARGE = {
        "size": FONT_SIZE_LG,
        "weight": FONT_WEIGHT_NORMAL,
        "line_height": LINE_HEIGHT_RELAXED
    }
    
    BODY = {
        "size": FONT_SIZE_BASE,
        "weight": FONT_WEIGHT_NORMAL,
        "line_height": LINE_HEIGHT_NORMAL
    }
    
    BODY_SMALL = {
        "size": FONT_SIZE_SM,
        "weight": FONT_WEIGHT_NORMAL,
        "line_height": LINE_HEIGHT_NORMAL
    }
    
    # UI Text
    BUTTON = {
        "size": FONT_SIZE_SM,
        "weight": FONT_WEIGHT_MEDIUM,
        "line_height": LINE_HEIGHT_TIGHT
    }
    
    CAPTION = {
        "size": FONT_SIZE_XS,
        "weight": FONT_WEIGHT_NORMAL,
        "line_height": LINE_HEIGHT_NORMAL
    }
    
    LABEL = {
        "size": FONT_SIZE_SM,
        "weight": FONT_WEIGHT_MEDIUM,
        "line_height": LINE_HEIGHT_NORMAL
    }