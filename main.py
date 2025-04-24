import sys
import os
import pickle
from Base_Branch import Base_Branch

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
        self.base_branch_instance = None 
        self.saved_branches = []  

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

        # Export Button
        self.Export_Button = QPushButton("Export Branches")
        self.Export_Button.setFixedSize(200, 50)
        self.Export_Button.setStyleSheet("background-color: lightcoral; font-size: 16px;")
        self.Export_Button.clicked.connect(self.handle_export)


        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.input_field, alignment=Qt.AlignCenter)
        layout.addWidget(self.Add_Branch_Button, alignment=Qt.AlignCenter)
        layout.addWidget(self.New_Story_Button, alignment=Qt.AlignCenter)
        layout.addWidget(self.Export_Button, alignment=Qt.AlignCenter)
        self.setLayout(layout)

    def handle_add_branch(self):
        if self.base_branch_instance is None:
            print("No story exists. Please create a story first.")
            return

        text_to_add = self.input_field.text().strip()
        if not text_to_add:
            print("No text entered. Please enter dialogue to add.")
            return

        self.base_branch_instance.edit_add(text_to_add)
        self.input_field.clear()


       

    def handle_new_story(self):
        branch_name = self.input_field.text().strip()
        if not branch_name:
            print("Branch name is empty. Please enter a name.")
            return
        self.base_branch_instance = Base_Branch(name=branch_name, type="story scene")
        self.saved_branches.append(self.base_branch_instance)
        print(f"Created Base_Branch: name={self.base_branch_instance.name}, type={self.base_branch_instance.type}")
        self.input_field.clear()

    def handle_export(self):
        if not self.saved_branches:
            print("No branches to export.")
            return

        with open("branches.pkl", "wb") as f:
            pickle.dump(self.saved_branches, f)
            print(f"Exported {len(self.saved_branches)} branches to 'branches.pkl'")


        

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