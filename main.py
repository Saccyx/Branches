import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QCheckBox, QWidget, 
    QVBoxLayout, QHBoxLayout, QToolBar, QAction
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

ICON_PATH = "Planet_Logo.png"

class CreateWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Window")
        self.setGeometry(600, 300, 300, 200)

        self.Add_Branch_Button = QPushButton("Add Branch")
        self.button.setFixedSize(200, 50)  
        self.button.setStyleSheet("background-color: lightblue; font-size: 16px;")

        self.button.clicked.connect(self.open_new_window)

        layout = QVBoxLayout()
        layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(layout)

        layout = QVBoxLayout()
        
        self.setLayout(layout)
        





        

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setWindowIcon(QIcon(ICON_PATH))
        self.setGeometry(350, 150, 1200, 800) 

        self.button = QPushButton("Open Creation Window")
        self.button.setFixedSize(200, 50)  
        self.button.setStyleSheet("background-color: lightblue; font-size: 16px;")

        self.button.clicked.connect(self.open_new_window)

        layout = QVBoxLayout()
        layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def open_new_window(self):
        self.second_window = CreateWindow()
        self.second_window.show() 





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())