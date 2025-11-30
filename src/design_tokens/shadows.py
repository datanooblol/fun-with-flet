"""
Shadow Design Tokens
Consistent elevation and shadow system
"""

# Shadow Definitions (CSS-like for reference)
# Note: Flet has limited shadow support, but we define them for future use

SHADOW_NONE = "none"
SHADOW_SM = "0 1px 2px 0 rgba(0, 0, 0, 0.05)"
SHADOW_BASE = "0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)"
SHADOW_MD = "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)"
SHADOW_LG = "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)"
SHADOW_XL = "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)"
SHADOW_2XL = "0 25px 50px -12px rgba(0, 0, 0, 0.25)"

# Semantic Shadows
class Shadows:
    BUTTON = SHADOW_SM
    CARD = SHADOW_BASE
    MODAL = SHADOW_LG
    DROPDOWN = SHADOW_MD
    TOOLTIP = SHADOW_SM
    
    # Elevation levels
    LEVEL_1 = SHADOW_SM    # Buttons, small cards
    LEVEL_2 = SHADOW_BASE  # Cards, inputs
    LEVEL_3 = SHADOW_MD    # Dropdowns, popovers
    LEVEL_4 = SHADOW_LG    # Modals, drawers
    LEVEL_5 = SHADOW_XL    # High-priority overlays