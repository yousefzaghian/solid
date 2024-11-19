import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QComboBox, QCheckBox, QRadioButton, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.create_window()
        self.create_title()
        self.create_label_1()
        self.create_radio_button_1()
        self.create_radio_button_2()
        self.create_label_1()
        self.create_label_2()
        self.create_label_3()
        self.create_label_4()
        self.create_label_5()
        self.create_label_6()
        self.create_line_edit_1()
        self.create_line_edit_2()
        self.create_line_edit_3()
        self.create_check_box_1()
        self.create_check_box_2()
        self.create_check_box_3()
        self.create_check_box_4()
        self.create_combo_box()
        self.create_button()
        self.design()
        self.button.clicked.connect(self.is_clicked)
        
    def create_window(self):
        self.setGeometry(200, 200, 500, 500)
        
    def create_title(self):
        self.setWindowTitle("Information")
        
    def design(self):
        self.layout = QVBoxLayout()
        self.elayout = QHBoxLayout()
        self.glayout = QHBoxLayout()
        self.label_7 = QLabel(self)
        self.label_7.setText("description : ")
        self.label_7.move(10, 280)
        self.textEdit = QTextEdit(self)
        self.textEdit.move(90, 280)
        self.layout.addWidget(self.label_1)
        self.layout.addWidget(self.label_2)
        self.layout.addWidget(self.label_3)
        self.layout.addWidget(self.label_4)
        self.layout.addWidget(self.label_5)
        self.layout.addWidget(self.label_6)
        self.layout.addWidget(self.label_7)
        self.layout.addWidget(self.textEdit)
        self.layout.addWidget(self.line_edit_1)
        self.layout.addWidget(self.line_edit_2)
        self.layout.addWidget(self.line_edit_3)
        self.elayout.addWidget(self.check_box_1)
        self.elayout.addWidget(self.check_box_2)
        self.elayout.addWidget(self.check_box_3)
        self.elayout.addWidget(self.check_box_4)
        self.layout.addLayout(self.elayout)
        self.glayout.addWidget(self.radio_button_1)
        self.glayout.addWidget(self.radio_button_2)
        self.layout.addLayout(self.glayout)
        # self.setLayout(self.layout)
        
       
    def create_label_1(self):
        self.label_1 = QLabel(self)
        self.label_1.setText("gender : ")
        self.label_1.move(10, 10)
        
    def create_label_2(self):
        self.label_2 = QLabel(self)
        self.label_2.setText("Name : ")
        self.label_2.move(10, 70)
        
    def create_label_3(self):
        self.label_3 = QLabel(self)
        self.label_3.setText("Last Name : ")
        self.label_3.move(10, 100)
        
    def create_label_4(self):
        self.label_4 = QLabel(self)
        self.label_4.setText("Student Number : ") 
        self.label_4.move(10, 130)
        
    def create_label_5(self):
        self.label_5 = QLabel(self)
        self.label_5.setText("What is your degree ? ")  
        self.label_5.move(10, 160)
        
    def create_label_6(self):
        self.label_6 = QLabel(self)
        self.label_6.setText("What is your field of study in university ? ")
        self.label_6.move(10, 220)
               
    def create_line_edit_1(self):
        self.line_edit_1 = QLineEdit(self)
        self.line_edit_1.move(70, 70)
        
    def create_line_edit_2(self):
        self.line_edit_2 = QLineEdit(self)
        self.line_edit_2.move(90, 100)
        
    def create_line_edit_3(self):
        self.line_edit_3 = QLineEdit(self)
        self.line_edit_3.move(130, 130)
        
    def create_check_box_1(self):
        self.check_box_1 = QCheckBox(self)
        self.check_box_1.setText("Associate")
        self.check_box_1.move(10, 190)
    
    def create_check_box_2(self):
        self.check_box_2 = QCheckBox(self)
        self.check_box_2.setText("bachelor")
        self.check_box_2.move(90, 190)
        
    def create_check_box_3(self):
        self.check_box_3 = QCheckBox(self)
        self.check_box_3.setText("Master")
        self.check_box_3.move(170, 190)
        
    def create_check_box_4(self):
        self.check_box_4 = QCheckBox(self)
        self.check_box_4.setText("Ph.D")
        self.check_box_4.move(250, 190)
        
    
    def create_combo_box(self):
        self.combo_box = QComboBox(self)
        self.combo_box.addItem("Computer engineering")
        self.combo_box.addItem("Chemical engineering")
        self.combo_box.addItem("Mechanical engineering")
        self.combo_box.addItem("Electrical engineering")
        self.combo_box.addItem("Petroleum engineering")
        self.combo_box.move(10, 250)
    
    def create_radio_button_1(self):
        self.radio_button_1 = QRadioButton(self)
        self.radio_button_1.setText("male")
        self.radio_button_1.setGeometry(10, 10 , 65, 65)
        
    def create_radio_button_2(self):
        self.radio_button_2 = QRadioButton(self)
        self.radio_button_2.setText("female")
        self.radio_button_2.setGeometry(90, 10, 65, 65)
        
    def create_button(self):
        self.button = QPushButton(self)
        self.button.setText("Save")
        self.button.move(170, 470)
        
    def is_clicked(self):
        name = self.line_edit_1.text()
        last_name = self.line_edit_2.text()
        student_number = self.line_edit_3.text()
        combo_box = self.combo_box.currentText()
        description = self.textEdit.toPlainText()
        gender = "unknown"
        if self.radio_button_1.isChecked():
            gender = "male"
        elif self.radio_button_2.isChecked():
            gender = "female"
        degree = "unknown"    
        if self.check_box_1.isChecked():
            degree = "Associate"
        elif self.check_box_2.isChecked():
            degree = "bachelor"
        elif self.check_box_3.isChecked():
            degree = "Master"
        elif self.check_box_4.isChecked():
            degree = "Ph.D"
        
        f = open("information.txt", "w")
        f.write(f"gender : {gender}\n")
        f.write(f"name : {name}\n")
        f.write(f"last name : {last_name}\n")
        f.write(f"student number : {student_number}\n")
        f.write(f"degree : {degree}\n")
        f.write(f"field of study : {combo_box}\n")
        f.write(f"description : {description}\n")
                 

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())    