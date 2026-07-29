"""
Design System and Theme for WeebCentral Downloader.
Neon Noir aesthetic: dark backgrounds with cyan/magenta neon accents.
"""

# =============================================================================
# COLOR PALETTE
# =============================================================================

class Colors:
    """Color constants for the dark purple theme."""
    
    # Backgrounds (layered depth)
    BG_DARKEST = "#393028"      # Window background
    BG_DARK = "#3D332C"         # Panel background
    BG_MEDIUM = "#483B34"       # Card background
    BG_LIGHT = "#53493F"        # Input/elevated background
    BG_HOVER = "#50443B"        # Hover states
    
    # Accent colors
    ACCENT = "#B2A667"          # Primary highlight
    ACCENT_SOFT = "#C3B684"     # Lighter highlight
    SUCCESS = "#8AA16A"         # Success
    WARNING = "#C78E44"         # Warning
    ERROR = "#C15E5E"           # Error
    
    # Backward-compatible legacy color names
    NEON_CYAN = ACCENT
    NEON_MAGENTA = ACCENT
    NEON_VIOLET = ACCENT_SOFT
    NEON_GREEN = SUCCESS
    NEON_ORANGE = WARNING
    NEON_RED = ERROR
    
    # Text colors
    TEXT_PRIMARY = "#F1E3C2"
    TEXT_SECONDARY = "#D9C9A7"
    TEXT_MUTED = "#A38F6F"
    TEXT_DISABLED = "#7B6D5B"
    
    # Borders
    BORDER_DEFAULT = "#5A5244"
    BORDER_HOVER = "#6D6350"
    BORDER_FOCUS = ACCENT
    
    # Gradients (as QSS format)
    GRADIENT_PRIMARY = f"qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {ACCENT_SOFT}, stop:1 {ACCENT})"
    GRADIENT_SUCCESS = f"qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {SUCCESS}, stop:1 {ACCENT})"
    GRADIENT_BG = f"qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 {BG_DARK}, stop:1 {BG_DARKEST})"


# =============================================================================
# TYPOGRAPHY
# =============================================================================

class Fonts:
    """Font specifications."""
    
    FAMILY_DISPLAY = "Outfit, Segoe UI, Arial, sans-serif"
    FAMILY_BODY = "Inter, Segoe UI, Arial, sans-serif"
    
    SIZE_HERO = 48
    SIZE_H1 = 24
    SIZE_H2 = 20
    SIZE_H3 = 16
    SIZE_BODY = 14
    SIZE_SMALL = 12
    SIZE_TINY = 10


# =============================================================================
# SPACING & SIZING
# =============================================================================

class Spacing:
    """Spacing and sizing constants."""
    
    XS = 4
    SM = 8
    MD = 12
    LG = 16
    XL = 24
    XXL = 32
    
    RADIUS_SM = 6
    RADIUS_MD = 10
    RADIUS_LG = 16
    RADIUS_XL = 24
    RADIUS_FULL = 9999


# =============================================================================
# STYLESHEET
# =============================================================================

def get_stylesheet() -> str:
    """Generate the complete QSS stylesheet."""
    
    return f"""
/* ==========================================================================
   GLOBAL STYLES
   ========================================================================== */

QWidget {{
    background-color: {Colors.BG_DARKEST};
    color: {Colors.TEXT_PRIMARY};
    font-family: {Fonts.FAMILY_BODY};
    font-size: {Fonts.SIZE_BODY}px;
}}

/* ==========================================================================
   MAIN WINDOW
   ========================================================================== */

QMainWindow {{
    background-color: {Colors.BG_DARKEST};
}}

/* ==========================================================================
   LABELS
   ========================================================================== */

QLabel {{
    color: {Colors.TEXT_PRIMARY};
    background: transparent;
}}

QLabel#title {{
    font-family: {Fonts.FAMILY_DISPLAY};
    font-size: {Fonts.SIZE_HERO}px;
    font-weight: bold;
    color: {Colors.TEXT_PRIMARY};
}}

QLabel#subtitle {{
    font-size: {Fonts.SIZE_H2}px;
    color: {Colors.TEXT_SECONDARY};
}}

QLabel#section-header {{
    font-family: {Fonts.FAMILY_DISPLAY};
    font-size: {Fonts.SIZE_H3}px;
    font-weight: bold;
    color: {Colors.TEXT_PRIMARY};
    padding: {Spacing.SM}px 0;
}}

QLabel#muted {{
    color: {Colors.TEXT_MUTED};
    font-size: {Fonts.SIZE_SMALL}px;
}}

/* ==========================================================================
   BUTTONS
   ========================================================================== */

QPushButton {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(241, 227, 194, 0.08), stop:1 rgba(241, 227, 194, 0.04));
    color: {Colors.TEXT_PRIMARY};
    border: 1px solid rgba(241, 227, 194, 0.18);
    border-radius: {Spacing.RADIUS_MD}px;
    padding: {Spacing.MD}px {Spacing.LG}px;
    font-size: {Fonts.SIZE_BODY}px;
    font-weight: 500;
    min-height: 20px;

}}

QPushButton:hover {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(241, 227, 194, 0.14), stop:1 rgba(241, 227, 194, 0.08));
    border-color: rgba(241, 227, 194, 0.28);
}}

QPushButton:pressed {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgba(241, 227, 194, 0.20), stop:1 rgba(241, 227, 194, 0.12));
}}

QPushButton:disabled {{
    background-color: rgba(112, 98, 79, 0.35);
    color: {Colors.TEXT_DISABLED};
    border-color: rgba(112, 98, 79, 0.25);
}}

QPushButton#primary {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(178, 166, 103, 0.42), stop:1 rgba(178, 166, 103, 0.24));
    border: 1px solid rgba(178, 166, 103, 0.35);
    color: {Colors.TEXT_PRIMARY};
    font-weight: bold;
}}

QPushButton#primary:hover {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(178, 166, 103, 0.58), stop:1 rgba(178, 166, 103, 0.34));
}}

QPushButton#primary:pressed {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(178, 166, 103, 0.50), stop:1 rgba(178, 166, 103, 0.30));
}}

QPushButton#danger {{
    background-color: {Colors.ERROR};
    border: 1px solid rgba(193, 94, 94, 0.5);
    color: {Colors.TEXT_PRIMARY};
}}

QPushButton#success {{
    background: {Colors.GRADIENT_SUCCESS};
    border: 1px solid rgba(138, 161, 106, 0.45);
    color: {Colors.TEXT_PRIMARY};
}}

/* ==========================================================================
   BOTTOM NAVIGATION BAR
   ========================================================================== */

/* Note: Qt's style engine doesn't clamp border-radius like CSS does -
   a radius larger than ~half the widget's height renders square corners
   instead of a capsule, so these use a radius sized to the actual height
   rather than Spacing.RADIUS_FULL. */
QFrame#bottom-nav {{
    background-color: {Colors.BG_DARK};
    border: 1px solid {Colors.BORDER_DEFAULT};
    border-radius: 28px;
}}

QPushButton#bottom-nav-item {{
    background: transparent;
    border: none;
    border-radius: 22px;
    padding: {Spacing.MD}px {Spacing.XL}px;
    color: {Colors.TEXT_MUTED};
    font-size: {Fonts.SIZE_BODY}px;
    font-weight: 500;
}}

QPushButton#bottom-nav-item:hover {{
    color: {Colors.TEXT_PRIMARY};
    background-color: rgba(241, 227, 194, 0.06);
}}

QPushButton#bottom-nav-item:checked {{
    background-color: {Colors.BG_LIGHT};
    color: {Colors.TEXT_PRIMARY};
    font-weight: 600;
}}

/* ==========================================================================
   INPUTS
   ========================================================================== */

QLineEdit {{
    background-color: {Colors.BG_LIGHT};
    color: {Colors.TEXT_PRIMARY};
    border: 2px solid {Colors.BORDER_DEFAULT};
    border-radius: {Spacing.RADIUS_MD}px;
    padding: {Spacing.MD}px {Spacing.LG}px;
    font-size: {Fonts.SIZE_BODY}px;
    selection-background-color: rgba(178, 166, 103, 0.28);
}}

QLineEdit:hover {{
    border-color: {Colors.BORDER_HOVER};
}}

QLineEdit:focus {{
    border-color: {Colors.ACCENT};
}}

QLineEdit:disabled {{
    background-color: {Colors.BG_DARK};
    color: {Colors.TEXT_DISABLED};
}}

/* Placeholder text */
QLineEdit[echoMode="2"] {{
    lineedit-password-character: 9679;
}}

/* ==========================================================================
   SPINBOXES
   ========================================================================== */

QSpinBox, QDoubleSpinBox {{
    background-color: {Colors.BG_LIGHT};
    color: {Colors.TEXT_PRIMARY};
    border: 2px solid {Colors.BORDER_DEFAULT};
    border-radius: {Spacing.RADIUS_MD}px;
    padding: {Spacing.SM}px {Spacing.MD}px;
}}

QSpinBox:focus, QDoubleSpinBox:focus {{
    border-color: {Colors.NEON_CYAN};
}}

QSpinBox::up-button, QDoubleSpinBox::up-button,
QSpinBox::down-button, QDoubleSpinBox::down-button {{
    background-color: {Colors.BG_HOVER};
    border: none;
    width: 20px;
}}

/* ==========================================================================
   CHECKBOXES & RADIO BUTTONS
   ========================================================================== */

QCheckBox, QRadioButton {{
    color: {Colors.TEXT_PRIMARY};
    spacing: {Spacing.SM}px;
}}

QCheckBox::indicator, QRadioButton::indicator {{
    width: 20px;
    height: 20px;
    border: 2px solid {Colors.BORDER_DEFAULT};
    background-color: {Colors.BG_LIGHT};
}}

QCheckBox::indicator {{
    border-radius: {Spacing.RADIUS_SM}px;
}}

QRadioButton::indicator {{
    border-radius: 10px;
}}

QCheckBox::indicator:hover, QRadioButton::indicator:hover {{
    border-color: {Colors.NEON_CYAN};
}}

QCheckBox::indicator:checked {{
    background-color: {Colors.NEON_CYAN};
    border-color: {Colors.NEON_CYAN};
}}

QRadioButton::indicator:checked {{
    background-color: {Colors.NEON_CYAN};
    border-color: {Colors.NEON_CYAN};
}}

/* ==========================================================================
   PROGRESS BARS
   ========================================================================== */

QProgressBar {{
    background-color: {Colors.BG_LIGHT};
    border: none;
    border-radius: {Spacing.RADIUS_SM}px;
    text-align: center;
    color: {Colors.TEXT_PRIMARY};
    font-weight: bold;
    font-size: {Fonts.SIZE_SMALL}px;
    min-height: 20px;
}}

QProgressBar::chunk {{
    background: {Colors.GRADIENT_PRIMARY};
    border-radius: {Spacing.RADIUS_SM}px;
}}

/* ==========================================================================
   SCROLL AREAS & LISTS
   ========================================================================== */

QScrollArea {{
    background-color: transparent;
    border: none;
}}

QScrollArea > QWidget > QWidget {{
    background-color: transparent;
}}

QListWidget {{
    background-color: {Colors.BG_MEDIUM};
    border: 1px solid {Colors.BORDER_DEFAULT};
    border-radius: {Spacing.RADIUS_MD}px;
    padding: {Spacing.SM}px;
    outline: none;
}}

QListWidget::item {{
    background-color: transparent;
    color: {Colors.TEXT_PRIMARY};
    padding: {Spacing.SM}px {Spacing.MD}px;
    border-radius: {Spacing.RADIUS_SM}px;
    margin: 2px 0;
}}

QListWidget::item:hover {{
    background-color: {Colors.BG_HOVER};
}}

QListWidget::item:selected {{
    background: {Colors.GRADIENT_PRIMARY};
}}

/* ==========================================================================
   SCROLLBARS
   ========================================================================== */

QScrollBar:vertical {{
    background-color: {Colors.BG_DARK};
    width: 12px;
    border-radius: 6px;
    margin: 0;
}}

QScrollBar::handle:vertical {{
    background-color: {Colors.BG_HOVER};
    border-radius: 6px;
    min-height: 30px;
}}

QScrollBar::handle:vertical:hover {{
    background-color: {Colors.NEON_CYAN};
}}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0;
}}

QScrollBar:horizontal {{
    background-color: {Colors.BG_DARK};
    height: 12px;
    border-radius: 6px;
    margin: 0;
}}

QScrollBar::handle:horizontal {{
    background-color: {Colors.BG_HOVER};
    border-radius: 6px;
    min-width: 30px;
}}

QScrollBar::handle:horizontal:hover {{
    background-color: {Colors.NEON_CYAN};
}}

QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
    width: 0;
}}

/* ==========================================================================
   FRAMES & CARDS
   ========================================================================== */

QFrame#card {{
    background-color: {Colors.BG_MEDIUM};
    border: 1px solid {Colors.BORDER_DEFAULT};
    border-radius: {Spacing.RADIUS_LG}px;
}}

QFrame#glass-card {{
    background-color: rgba(26, 26, 37, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: {Spacing.RADIUS_LG}px;
}}

/* ==========================================================================
   TAB WIDGET
   ========================================================================== */

QTabWidget::pane {{
    background-color: {Colors.BG_DARK};
    border: none;
}}

QTabBar::tab {{
    background-color: {Colors.BG_MEDIUM};
    color: {Colors.TEXT_SECONDARY};
    padding: {Spacing.MD}px {Spacing.XL}px;
    border: none;
    border-top-left-radius: {Spacing.RADIUS_MD}px;
    border-top-right-radius: {Spacing.RADIUS_MD}px;
    margin-right: 2px;
}}

QTabBar::tab:hover {{
    background-color: {Colors.BG_HOVER};
    color: {Colors.TEXT_PRIMARY};
}}

QTabBar::tab:selected {{
    background: {Colors.GRADIENT_PRIMARY};
    color: {Colors.TEXT_PRIMARY};
}}

/* ==========================================================================
   SLIDERS
   ========================================================================== */

QSlider::groove:horizontal {{
    background-color: {Colors.BG_LIGHT};
    height: 8px;
    border-radius: 4px;
}}

QSlider::handle:horizontal {{
    background: {Colors.GRADIENT_PRIMARY};
    width: 20px;
    height: 20px;
    margin: -6px 0;
    border-radius: 10px;
}}

QSlider::handle:horizontal:hover {{
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 rgba(178, 166, 103, 0.72), stop:1 rgba(178, 166, 103, 0.42));
}}

QSlider::sub-page:horizontal {{
    background: {Colors.GRADIENT_PRIMARY};
    border-radius: 4px;
}}

/* ==========================================================================
   COMBOBOXES
   ========================================================================== */

QComboBox {{
    background-color: {Colors.BG_LIGHT};
    color: {Colors.TEXT_PRIMARY};
    border: 2px solid {Colors.BORDER_DEFAULT};
    border-radius: {Spacing.RADIUS_MD}px;
    padding: {Spacing.SM}px {Spacing.MD}px;
    min-height: 20px;
}}

QComboBox:hover {{
    border-color: {Colors.BORDER_HOVER};
}}

QComboBox:focus {{
    border-color: {Colors.NEON_CYAN};
}}

QComboBox::drop-down {{
    border: none;
    width: 30px;
}}

QComboBox QAbstractItemView {{
    background-color: {Colors.BG_MEDIUM};
    border: 1px solid {Colors.BORDER_DEFAULT};
    border-radius: {Spacing.RADIUS_MD}px;
    selection-background-color: {Colors.NEON_CYAN};
    outline: none;
    padding: {Spacing.XS}px;
}}

/* ==========================================================================
   TOOLTIPS
   ========================================================================== */

QToolTip {{
    background-color: {Colors.BG_MEDIUM};
    color: {Colors.TEXT_PRIMARY};
    border: 1px solid {Colors.NEON_CYAN};
    border-radius: {Spacing.RADIUS_SM}px;
    padding: {Spacing.SM}px {Spacing.MD}px;
}}

/* ==========================================================================
   MESSAGE BOX
   ========================================================================== */

QMessageBox {{
    background-color: {Colors.BG_DARK};
}}

QMessageBox QLabel {{
    color: {Colors.TEXT_PRIMARY};
}}

QMessageBox QPushButton {{
    min-width: 80px;
}}
"""
