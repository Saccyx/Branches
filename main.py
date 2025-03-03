import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Branches")
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon("Planet_Logo.png"))
        self.button1 = QPushButton("Home", self)
        self.button2 = QPushButton("Create", self)
        self.button3 = QPushButton("Import", self)
        self.initUI()

    def initUI(self):

        # Homepage button setup
        self.button1.setGeometry(0, 0, 200, 100)
        self.button1.setStyleSheet("font-size: 30px;")
        self.button1.clicked.connect(self.button1_clicked)

        # Create button setup
        self.button2.setGeometry(200, 0, 200, 100)
        self.button2.setStyleSheet("font-size: 30px;")
        self.button2.clicked.connect(self.button2_clicked)

        # Import button setup
        self.button3.setGeometry(400, 0, 200, 100)
        self.button3.setStyleSheet("font-size: 30px;")
        self.button3.clicked.connect(self.button3_clicked)

    def button1_clicked(self):
        print("Button 1 clicked")

    def button2_clicked(self):
        print("Button 2 clicked")

    def button3_clicked(self):
        print("Button 3 clicked")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



