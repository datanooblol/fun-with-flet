"""
Border Design Tokens
Consistent border radius, width, and styles
"""

# Border Radius
RADIUS_NONE = 0
RADIUS_SM = 2
RADIUS_BASE = 4
RADIUS_MD = 6
RADIUS_LG = 8
RADIUS_XL = 12
RADIUS_2XL = 16
RADIUS_FULL = 9999  # Fully rounded

# Border Width
BORDER_0 = 0
BORDER_1 = 1
BORDER_2 = 2
BORDER_4 = 4
BORDER_8 = 8

# Semantic Border Tokens
class Borders:
    # Radius
    RADIUS_BUTTON = RADIUS_MD      # 6px
    RADIUS_INPUT = RADIUS_BASE     # 4px
    RADIUS_CARD = RADIUS_LG        # 8px
    RADIUS_MODAL = RADIUS_XL       # 12px
    RADIUS_PILL = RADIUS_FULL      # Fully rounded
    
    # Width
    WIDTH_THIN = BORDER_1          # 1px
    WIDTH_THICK = BORDER_2         # 2px
    WIDTH_FOCUS = BORDER_2         # 2px for focus states