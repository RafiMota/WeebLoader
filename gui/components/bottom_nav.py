"""
Bottom Navigation Bar.
Centered pill-shaped navigation bar replacing the sidebar.
"""

from PyQt6.QtWidgets import QFrame, QHBoxLayout, QPushButton, QButtonGroup
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QCursor

from gui.theme import Spacing


class BottomNavBar(QFrame):
    """
    Centered pill-shaped bottom navigation bar.
    Displays a row of text tabs; the active tab is highlighted with a pill.
    """

    tabChanged = pyqtSignal(int)

    def __init__(self, labels, parent=None):
        super().__init__(parent)
        self.setObjectName("bottom-nav")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(Spacing.XS, Spacing.XS, Spacing.XS, Spacing.XS)
        layout.setSpacing(Spacing.XS)

        self._group = QButtonGroup(self)
        self._group.setExclusive(True)
        self._buttons = []

        for index, label in enumerate(labels):
            button = QPushButton(label)
            button.setObjectName("bottom-nav-item")
            button.setCheckable(True)
            button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
            self._group.addButton(button, index)
            layout.addWidget(button)
            self._buttons.append(button)

        if self._buttons:
            self._buttons[0].setChecked(True)

        self._group.idClicked.connect(self.tabChanged.emit)

    def set_current(self, index: int):
        """Programmatically set the active tab without emitting tabChanged."""
        if 0 <= index < len(self._buttons):
            self._buttons[index].setChecked(True)
