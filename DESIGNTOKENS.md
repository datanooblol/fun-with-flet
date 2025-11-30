# Design Tokens in Flet

## 📚 Table of Contents
- [🎯 What You'll Learn](#-what-youll-learn)
- [🎨 What are Design Tokens?](#-what-are-design-tokens)
- [🏗️ Our Implementation](#️-our-implementation)
- [🎨 1. Color Tokens](#-1-color-tokens)
- [📏 2. Spacing Tokens](#-2-spacing-tokens)
- [🔤 3. Typography Tokens](#-3-typography-tokens)
- [🔲 4. Border Tokens](#-4-border-tokens)
- [🌆 5. Shadow Tokens](#-5-shadow-tokens)
- [📝 Implementation Example: Button with Design Tokens](#-implementation-example-button-with-design-tokens)
- [✅ Benefits Achieved](#-benefits-achieved)
- [📝 Usage Patterns](#-usage-patterns)
- [🚀 Advanced Patterns](#-advanced-patterns)
- [⚖️ Comparison with Other Frameworks](#️-comparison-with-other-frameworks)
- [✅ Best Practices](#-best-practices)
- [🚀 Future Enhancements](#-future-enhancements)
- [🎆 Conclusion](#-conclusion)

---

## 🎯 What You'll Learn
Design Tokens are like a **style guide for your code** - they keep everything looking consistent and professional!

### 🚀 For Complete Beginners
Imagine you're painting a house:
- **Without Design Tokens**: You mix paint colors by eye each time → inconsistent results
- **With Design Tokens**: You have exact paint formulas → perfect consistency every time

### 📚 Learning Path
1. **Understand the Problem** - Why we need design tokens
2. **See the Solution** - How tokens solve consistency issues
3. **Learn the Categories** - Colors, spacing, typography, etc.
4. **Practice Implementation** - Use tokens in real components

### 💡 Real-World Example
**Netflix, Spotify, Airbnb** all use design tokens to ensure their apps look consistent across web, mobile, and TV platforms!

---

## Overview

Design Tokens are the **single source of truth** for design decisions in your application. They are named entities that store visual design attributes like colors, spacing, typography, and more. This document explains how we implemented a complete Design Token system in Flet.

## What are Design Tokens? 🎨

### 📚 Simple Analogy
Design Tokens are like a **recipe book for your app's appearance**:

**Without Tokens** (Bad):
```python
# Scattered colors everywhere
bgcolor="#3182CE"  # What blue is this?
bgcolor="#2C5282"  # Is this the same blue?
bgcolor="#4299E1"  # Another blue? Which one is right?
```

**With Tokens** (Good):
```python
# Clear, meaningful names
bgcolor=Colors.PRIMARY        # Obviously the main brand color
bgcolor=Colors.PRIMARY_DARK   # Clearly a darker version
bgcolor=Colors.SUCCESS        # Obviously for success states
```

### 🎯 Professional Benefits
Design Tokens bridge the gap between **design and development** by:
- **Centralizing design decisions** (colors, spacing, typography)
- **Ensuring consistency** across the entire application
- **Enabling easy theming** and design system changes
- **Improving maintainability** (change once, update everywhere)

### 💡 Real-World Impact
- **Designer says**: "Make the primary blue darker"
- **Without tokens**: Find and change 50+ hardcoded colors 😱
- **With tokens**: Change `Colors.PRIMARY` once → entire app updates! 🎉

## Our Implementation

### Project Structure

```
src/design_tokens/
├── __init__.py
├── colors.py         # Color palette & semantic colors
├── spacing.py        # Spacing scale & layout tokens
├── typography.py     # Font sizes, weights, line heights
├── borders.py        # Border radius & width tokens
└── shadows.py        # Elevation & shadow system
```

## 1. Color Tokens (`colors.py`)

### Color Scale System

**Primary Colors (Blue Scale):**
```python
PRIMARY_50 = "#EBF8FF"    # Lightest
PRIMARY_100 = "#BEE3F8"
PRIMARY_500 = "#3182CE"   # Main primary color
PRIMARY_600 = "#2C5282"
PRIMARY_900 = "#1A365D"   # Darkest
```

**Semantic Color Categories:**
- **Primary**: Main brand colors
- **Secondary**: Supporting colors
- **Success**: Green tones for positive actions
- **Warning**: Orange tones for caution
- **Danger**: Red tones for errors/destructive actions
- **Neutral**: Gray scale for text and backgrounds

### Semantic Color Mapping

```python
class Colors:
    # Brand Colors
    PRIMARY = PRIMARY_500
    PRIMARY_LIGHT = PRIMARY_50
    PRIMARY_DARK = PRIMARY_900
    
    # Semantic Colors
    SUCCESS = SUCCESS_500
    WARNING = WARNING_500
    DANGER = DANGER_500
    
    # Text Colors
    TEXT_PRIMARY = GRAY_900      # Main text
    TEXT_SECONDARY = GRAY_600    # Secondary text
    TEXT_MUTED = GRAY_400        # Muted text
    TEXT_INVERSE = WHITE         # Text on dark backgrounds
    
    # Background Colors
    BG_PRIMARY = WHITE           # Main background
    BG_SECONDARY = GRAY_50       # Secondary background
    BG_DARK = GRAY_900          # Dark theme background
```

### Usage Examples

```python
# Instead of hardcoded colors:
bgcolor=ft.Colors.BLUE

# Use semantic tokens:
bgcolor=Colors.PRIMARY

# For different contexts:
bgcolor=Colors.SUCCESS      # Success button
color=Colors.TEXT_MUTED     # Secondary text
bgcolor=Colors.BG_SECONDARY # Card background
```

## 2. Spacing Tokens (`spacing.py`)

### 4px Grid System

**Base Unit:** 4px (ensures consistent spacing across all screen densities)

```python
BASE_UNIT = 4

SPACE_1 = 4px    # BASE_UNIT * 1
SPACE_2 = 8px    # BASE_UNIT * 2
SPACE_3 = 12px   # BASE_UNIT * 3
SPACE_4 = 16px   # BASE_UNIT * 4
SPACE_6 = 24px   # BASE_UNIT * 6
SPACE_8 = 32px   # BASE_UNIT * 8
```

### Semantic Spacing

```python
class Spacing:
    # Component Internal Spacing
    XS = 4px     # Tight spacing
    SM = 8px     # Small spacing
    MD = 16px    # Medium spacing (most common)
    LG = 24px    # Large spacing
    XL = 32px    # Extra large spacing
    
    # Layout Spacing
    SECTION = 48px    # Between major sections
    PAGE = 64px       # Page margins
    
    # Component-Specific
    BUTTON_PADDING_X = 16px
    BUTTON_PADDING_Y = 8px
    INPUT_PADDING_X = 12px
    CARD_PADDING = 24px
```

### Usage Examples

```python
# Instead of hardcoded values:
padding=16

# Use semantic tokens:
padding=Spacing.MD

# For specific contexts:
padding=ft.padding.symmetric(
    horizontal=Spacing.BUTTON_PADDING_X,
    vertical=Spacing.BUTTON_PADDING_Y
)
```

## 3. Typography Tokens (`typography.py`)

### Font Size Scale

**Modular Scale (1.25 ratio):**
```python
FONT_SIZE_XS = 12px
FONT_SIZE_SM = 14px
FONT_SIZE_BASE = 16px    # Base font size
FONT_SIZE_LG = 18px
FONT_SIZE_XL = 20px
FONT_SIZE_2XL = 24px
FONT_SIZE_3XL = 30px
FONT_SIZE_4XL = 36px
FONT_SIZE_5XL = 48px
```

### Typography Styles

```python
class Typography:
    # Headings
    H1 = {
        "size": 48,
        "weight": ft.FontWeight.W_700,
        "line_height": 1.25
    }
    
    H2 = {
        "size": 36,
        "weight": ft.FontWeight.W_700,
        "line_height": 1.25
    }
    
    # Body Text
    BODY = {
        "size": 16,
        "weight": ft.FontWeight.W_400,
        "line_height": 1.5
    }
    
    # UI Elements
    BUTTON = {
        "size": 14,
        "weight": ft.FontWeight.W_500,
        "line_height": 1.25
    }
```

### Usage Examples

```python
# Instead of hardcoded typography:
ft.Text("Title", size=24, weight=ft.FontWeight.BOLD)

# Use typography tokens:
ft.Text(
    "Title", 
    size=Typography.H2["size"],
    weight=Typography.H2["weight"]
)
```

## 4. Border Tokens (`borders.py`)

### Border Radius Scale

```python
RADIUS_NONE = 0
RADIUS_SM = 2px
RADIUS_BASE = 4px
RADIUS_MD = 6px
RADIUS_LG = 8px
RADIUS_XL = 12px
RADIUS_FULL = 9999px    # Fully rounded (pills)
```

### Semantic Borders

```python
class Borders:
    RADIUS_BUTTON = 6px     # Standard button radius
    RADIUS_INPUT = 4px      # Input field radius
    RADIUS_CARD = 8px       # Card radius
    RADIUS_MODAL = 12px     # Modal radius
    
    WIDTH_THIN = 1px        # Standard border
    WIDTH_THICK = 2px       # Emphasis border
    WIDTH_FOCUS = 2px       # Focus state border
```

## 5. Shadow Tokens (`shadows.py`)

### Elevation System

```python
class Shadows:
    LEVEL_1 = "0 1px 2px rgba(0,0,0,0.05)"     # Buttons
    LEVEL_2 = "0 1px 3px rgba(0,0,0,0.1)"      # Cards
    LEVEL_3 = "0 4px 6px rgba(0,0,0,0.1)"      # Dropdowns
    LEVEL_4 = "0 10px 15px rgba(0,0,0,0.1)"    # Modals
    LEVEL_5 = "0 20px 25px rgba(0,0,0,0.1)"    # High priority overlays
```

## Implementation Example: Button with Design Tokens

### Before (Hardcoded Values)

```python
def Button(text, variant="primary"):
    return ft.Container(
        ft.Text(text, color="#FFFFFF", size=14, weight=ft.FontWeight.W_500),
        bgcolor="#3182CE",
        padding=ft.padding.symmetric(horizontal=16, vertical=8),
        border_radius=6,
        height=40
    )
```

### After (Using Design Tokens)

```python
from design_tokens.colors import Colors
from design_tokens.spacing import Spacing
from design_tokens.typography import Typography
from design_tokens.borders import Borders

def Button(text, variant="primary"):
    variant_styles = {
        "primary": {
            "bgcolor": Colors.PRIMARY,
            "color": Colors.TEXT_INVERSE
        },
        "secondary": {
            "bgcolor": Colors.SECONDARY,
            "color": Colors.TEXT_PRIMARY
        }
    }
    
    style = variant_styles[variant]
    
    return ft.Container(
        ft.Text(
            text, 
            color=style["color"],
            size=Typography.BUTTON["size"],
            weight=Typography.BUTTON["weight"]
        ),
        bgcolor=style["bgcolor"],
        padding=ft.padding.symmetric(
            horizontal=Spacing.BUTTON_PADDING_X,
            vertical=Spacing.BUTTON_PADDING_Y
        ),
        border_radius=Borders.RADIUS_BUTTON,
        height=40
    )
```

## Benefits Achieved

### 1. **Consistency**
- All components use the same color palette
- Consistent spacing throughout the app
- Unified typography scale

### 2. **Maintainability**
- Change primary color once, updates everywhere
- Easy to adjust spacing system globally
- Typography changes propagate automatically

### 3. **Scalability**
- Easy to add new color variants
- Simple to extend spacing scale
- New components inherit design system

### 4. **Design-Development Sync**
- Tokens match design system exactly
- Designers and developers speak same language
- Easy to implement design changes

### 5. **Theming Support**
- Easy to create dark/light themes
- Brand customization becomes simple
- A/B testing different design variations

## Usage Patterns

### 1. **Import Tokens**
```python
from design_tokens.colors import Colors
from design_tokens.spacing import Spacing
from design_tokens.typography import Typography
```

### 2. **Use Semantic Names**
```python
# Good - Semantic meaning
bgcolor=Colors.PRIMARY
padding=Spacing.MD
size=Typography.H2["size"]

# Bad - Hardcoded values
bgcolor="#3182CE"
padding=16
size=24
```

### 3. **Component-Specific Tokens**
```python
# Create specific tokens for common patterns
BUTTON_HEIGHT_SM = 32
BUTTON_HEIGHT_MD = 40
BUTTON_HEIGHT_LG = 48

INPUT_HEIGHT = 40
CARD_MIN_HEIGHT = 120
```

### 4. **Contextual Usage**
```python
# Different contexts use appropriate tokens
success_button = Colors.SUCCESS
error_message = Colors.DANGER
muted_text = Colors.TEXT_MUTED
page_background = Colors.BG_PRIMARY
```

## Advanced Patterns

### 1. **Token Composition**
```python
def create_card_style():
    return {
        "bgcolor": Colors.BG_PRIMARY,
        "padding": Spacing.CARD_PADDING,
        "border_radius": Borders.RADIUS_CARD,
        "border": ft.border.all(Borders.WIDTH_THIN, Colors.GRAY_200)
    }
```

### 2. **Responsive Tokens**
```python
# Different tokens for different screen sizes
class ResponsiveSpacing:
    MOBILE_PADDING = Spacing.SM
    TABLET_PADDING = Spacing.MD
    DESKTOP_PADDING = Spacing.LG
```

### 3. **State-Based Tokens**
```python
class ButtonStates:
    DEFAULT = Colors.PRIMARY
    HOVER = Colors.PRIMARY_DARK
    DISABLED = Colors.GRAY_300
    FOCUS_BORDER = Colors.PRIMARY
```

## Comparison with Other Frameworks

### React/Next.js (CSS Variables)
```css
:root {
  --color-primary: #3182CE;
  --spacing-md: 16px;
  --font-size-lg: 18px;
}

.button {
  background: var(--color-primary);
  padding: var(--spacing-md);
  font-size: var(--font-size-lg);
}
```

### Flet (Python Constants)
```python
Colors.PRIMARY = "#3182CE"
Spacing.MD = 16
Typography.BODY_LG["size"] = 18

ft.Container(
    bgcolor=Colors.PRIMARY,
    padding=Spacing.MD,
    child=ft.Text(size=Typography.BODY_LG["size"])
)
```

### Tailwind CSS
```html
<button class="bg-blue-500 px-4 py-2 text-lg">
  Button
</button>
```

### Flet Equivalent
```python
Button(
    bgcolor=Colors.PRIMARY,
    padding=ft.padding.symmetric(
        horizontal=Spacing.MD,
        vertical=Spacing.SM
    ),
    text_size=Typography.BODY_LG["size"]
)
```

## Best Practices

### 1. **Naming Conventions**
- Use semantic names: `PRIMARY`, `SUCCESS`, `DANGER`
- Avoid implementation details: `BLUE_500` → `PRIMARY`
- Be consistent: `SM`, `MD`, `LG` for all scales

### 2. **Token Organization**
- Group by category (colors, spacing, typography)
- Use hierarchical naming (TEXT_PRIMARY, TEXT_SECONDARY)
- Create component-specific tokens when needed

### 3. **Documentation**
- Document token purpose and usage
- Provide examples for each token
- Show before/after comparisons

### 4. **Validation**
- Use consistent scales (4px grid for spacing)
- Ensure sufficient color contrast
- Test tokens across different components

## Future Enhancements

### 1. **Theme System**
```python
class LightTheme:
    BG_PRIMARY = Colors.WHITE
    TEXT_PRIMARY = Colors.BLACK

class DarkTheme:
    BG_PRIMARY = Colors.BLACK
    TEXT_PRIMARY = Colors.WHITE
```

### 2. **Animation Tokens**
```python
class Animations:
    DURATION_FAST = "150ms"
    DURATION_NORMAL = "300ms"
    DURATION_SLOW = "500ms"
    
    EASING_EASE_OUT = "cubic-bezier(0, 0, 0.2, 1)"
```

### 3. **Breakpoint Tokens**
```python
class Breakpoints:
    MOBILE = 480
    TABLET = 768
    DESKTOP = 1024
    WIDE = 1280
```

## 🎆 Conclusion

### 📝 What You've Accomplished
Congratulations! You now understand Design Tokens - a **professional-grade system** used by major tech companies.

### 🚀 Key Benefits You've Learned
- **Consistency** - Your app looks professional and unified
- **Speed** - Build new features faster with existing tokens
- **Maintainability** - Easy updates and changes
- **Collaboration** - Designers and developers speak the same language

### 📚 Your Learning Journey
1. ✅ **Components** - You learned how to build reusable UI pieces
2. ✅ **Atomic Design** - You learned how to organize components systematically
3. ✅ **Design Tokens** - You learned how to maintain consistent styling

### 🚀 Next Steps for Beginners
1. **Practice**: Build a small app using all three concepts
2. **Experiment**: Try creating your own design token system
3. **Explore**: Look at how real companies use these patterns
4. **Build**: Create a portfolio project showcasing your skills

### 💡 Pro Tips
- Start small - even 3-4 color tokens make a huge difference
- Be consistent with naming (PRIMARY, SECONDARY, SUCCESS)
- Document your tokens so others can use them
- Remember: Professional apps are built with these exact patterns!

### 🌟 You're Ready!
You now have the same foundational knowledge used to build apps at **Netflix, Spotify, Airbnb, and Google**. The concepts are identical - just different tools!

By implementing Design Tokens, you've learned a foundation that makes building and maintaining consistent, professional UIs much easier - just like modern design systems in React, Vue, or other frameworks! 🎨✨