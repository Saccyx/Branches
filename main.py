import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QCheckBox, QWidget, 
    QVBoxLayout, QHBoxLayout, QToolBar, QAction
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

ICON_PATH = "Planet_Logo.png"

class BaseWindow(QWidget):
    def __init__(self, title, message):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(200, 200, 400, 300)
        if os.path.exists(ICON_PATH):
            self.setWindowIcon(QIcon(ICON_PATH))

        layout = QVBoxLayout()
        label = QLabel(message)
        label.setStyleSheet("font-size: 20px; padding: 10px;")
        layout.addWidget(label)
        self.setLayout(layout)

class HomeWindow(BaseWindow):
    def __init__(self):
        super().__init__("Home Window", "Welcome to the Home Window!")

class ImportWindow(BaseWindow):
    def __init__(self):
        super().__init__("Import Project", "Welcome to the Import Window!")

class CreateWindow(QMainWindow):  # Changed to QMainWindow to support a taskbar
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create New Project")
        self.setGeometry(200, 200, 400, 300)
        if os.path.exists(ICON_PATH):
            self.setWindowIcon(QIcon(ICON_PATH))

        # Central Widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        label = QLabel("Welcome to the Create Window!")
        label.setStyleSheet("font-size: 20px; padding: 10px;")
        layout.addWidget(label)

        self.central_widget.setLayout(layout)

        # Taskbar (Toolbar)
        self.toolbar = QToolBar("Taskbar")
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

        # Adding actions to the taskbar
        self.add_taskbar_actions()

    def add_taskbar_actions(self):
        new_action = QAction(QIcon("new_icon.png"), "New", self)
        open_action = QAction(QIcon("open_icon.png"), "Open", self)
        save_action = QAction(QIcon("save_icon.png"), "Save", self)
        exit_action = QAction(QIcon("exit_icon.png"), "Exit", self)
        
        exit_action.triggered.connect(self.close)

        self.toolbar.addAction(new_action)
        self.toolbar.addAction(open_action)
        self.toolbar.addAction(save_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(exit_action)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Branches")
        self.setGeometry(100, 100, 800, 600)
        if os.path.exists(ICON_PATH):
            self.setWindowIcon(QIcon(ICON_PATH))

        # Store references to sub-windows
        self.windows = {}

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        # Buttons
        self.buttons = {
            "Home": HomeWindow,
            "Create": CreateWindow,
            "Import": ImportWindow
        }

        for name, window_class in self.buttons.items():
            button = QPushButton(name)
            button.setStyleSheet("font-size: 30px;")
            button.clicked.connect(lambda checked, w=window_class: self.open_window(w))
            button_layout.addWidget(button)

        # Dark Mode checkbox
        self.checkDarkMode = QCheckBox("Dark Mode")
        self.checkDarkMode.setStyleSheet("font-size: 20px; padding: 10px;")
        self.checkDarkMode.stateChanged.connect(self.toggle_dark_mode)

        button_layout.addWidget(self.checkDarkMode)
        layout.addLayout(button_layout)
        central_widget.setLayout(layout)

        # Taskbar (Toolbar)
        self.toolbar = QToolBar("Taskbar")
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)

        # Adding actions to the taskbar
        self.add_taskbar_actions()

    def add_taskbar_actions(self):
        new_action = QAction(QIcon("new_icon.png"), "New", self)
        open_action = QAction(QIcon("open_icon.png"), "Open", self)
        save_action = QAction(QIcon("save_icon.png"), "Save", self)
        exit_action = QAction(QIcon("exit_icon.png"), "Exit", self)

        exit_action.triggered.connect(self.close)

        self.toolbar.addAction(new_action)
        self.toolbar.addAction(open_action)
        self.toolbar.addAction(save_action)
        self.toolbar.addSeparator()
        self.toolbar.addAction(exit_action)

    def open_window(self, window_class):
        window_name = window_class.__name__
        if window_name not in self.windows or not self.windows[window_name].isVisible():
            self.windows[window_name] = window_class()
            self.windows[window_name].show()

    def toggle_dark_mode(self, state):
        if state == Qt.Checked:
            app.setStyleSheet("background-color: #333; color: white;")
        else:
            app.setStyleSheet("")

def main():
    global app
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
