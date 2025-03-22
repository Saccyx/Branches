import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QCheckBox, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Branches")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("Planet_Logo.png"))

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        # Homepage button setup
        self.button1 = QPushButton("Home")
        self.button1.setStyleSheet("font-size: 30px;")
        self.button1.clicked.connect(self.button1_clicked)

        # Create button setup
        self.button2 = QPushButton("Create")
        self.button2.setStyleSheet("font-size: 30px;")
        self.button2.clicked.connect(self.button2_clicked)

        # Import button setup
        self.button3 = QPushButton("Import")
        self.button3.setStyleSheet("font-size: 30px;")
        self.button3.clicked.connect(self.button3_clicked)

        # Dark Mode checkbox
        self.checkDarkMode = QCheckBox("Dark Mode")
        self.checkDarkMode.setStyleSheet("font-size: 20px; padding: 10px;")
        self.checkDarkMode.stateChanged.connect(self.toggle_dark_mode)

        # Add widgets to layout
        button_layout.addWidget(self.button1)
        button_layout.addWidget(self.button2)
        button_layout.addWidget(self.button3)
        button_layout.addWidget(self.checkDarkMode)

        layout.addLayout(button_layout)
        central_widget.setLayout(layout)

    def button1_clicked(self):
        print("Button 1 clicked")
        self.window = HomeWindow()
        self.window.show()

    def button2_clicked(self):
        print("Button 2 clicked")
        self.window = CreateWindow()
        self.window.show()

    def button3_clicked(self):
        print("Button 3 clicked")
        self.window = ImportWindow()
        self.window.show()

    def toggle_dark_mode(self, state):
        if state == Qt.Checked:
            self.setStyleSheet("background-color: #333; color: white;")
        else:
            self.setStyleSheet("")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
