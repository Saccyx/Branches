import sys
import os
import Base_Branch
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QCheckBox, QWidget, 
    QVBoxLayout, QHBoxLayout, QToolBar, QAction,QLineEdit, QComboBox, QTableWidget, QTableWidgetItem, QGridLayout, QFrame
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

ICON_PATH = "Planet_Logo.png"




class CreateWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Window")
        self.setGeometry(600, 300, 300, 250)

        # Input field
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter text")
        self.input_field.setFixedSize(200, 30)
        self.input_field.setStyleSheet("font-size: 14px;")

        # Add Branch Button
        self.Add_Branch_Button = QPushButton("Add Branch")
        self.Add_Branch_Button.setFixedSize(200, 50)  
        self.Add_Branch_Button.setStyleSheet("background-color: lightblue; font-size: 16px;")
        self.Add_Branch_Button.clicked.connect(self.handle_add_branch)

        # New Story Button
        self.New_Story_Button = QPushButton("New Story")
        self.New_Story_Button.setFixedSize(200, 50)  
        self.New_Story_Button.setStyleSheet("background-color: lightgreen; font-size: 16px;")
        self.New_Story_Button.clicked.connect(self.handle_new_story)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input_field, alignment=Qt.AlignCenter)
        layout.addWidget(self.Add_Branch_Button, alignment=Qt.AlignCenter)
        layout.addWidget(self.New_Story_Button, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def handle_add_branch(self):
        branch_name = self.input_field.text()
        print(f"Branch name entered: {branch_name}")

    def handle_new_story(self):
        print("New story button clicked")



        

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