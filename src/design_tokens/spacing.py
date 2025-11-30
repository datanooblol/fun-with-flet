"""
Spacing Design Tokens
Consistent spacing system for padding, margin, and layout
"""

# Base spacing unit (4px)
BASE_UNIT = 4

# Spacing Scale (based on 4px grid)
SPACE_0 = 0
SPACE_1 = BASE_UNIT * 1      # 4px
SPACE_2 = BASE_UNIT * 2      # 8px
SPACE_3 = BASE_UNIT * 3      # 12px
SPACE_4 = BASE_UNIT * 4      # 16px
SPACE_5 = BASE_UNIT * 5      # 20px
SPACE_6 = BASE_UNIT * 6      # 24px
SPACE_8 = BASE_UNIT * 8      # 32px
SPACE_10 = BASE_UNIT * 10    # 40px
SPACE_12 = BASE_UNIT * 12    # 48px
SPACE_16 = BASE_UNIT * 16    # 64px
SPACE_20 = BASE_UNIT * 20    # 80px
SPACE_24 = BASE_UNIT * 24    # 96px
SPACE_32 = BASE_UNIT * 32    # 128px

# Semantic Spacing
class Spacing:
    # Component Internal Spacing
    XS = SPACE_1    # 4px
    SM = SPACE_2    # 8px
    MD = SPACE_4    # 16px
    LG = SPACE_6    # 24px
    XL = SPACE_8    # 32px
    
    # Layout Spacing
    SECTION = SPACE_12    # 48px
    PAGE = SPACE_16       # 64px
    
    # Component Specific
    BUTTON_PADDING_X = SPACE_4    # 16px
    BUTTON_PADDING_Y = SPACE_2    # 8px
    
    INPUT_PADDING_X = SPACE_3     # 12px
    INPUT_PADDING_Y = SPACE_2     # 8px
    
    CARD_PADDING = SPACE_6        # 24px
    MODAL_PADDING = SPACE_8       # 32px