import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QCheckBox, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import os

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

class CreateWindow(BaseWindow):
    def __init__(self):
        super().__init__("Create New Project", "Welcome to the Create Window!")

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
