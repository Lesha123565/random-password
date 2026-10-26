from PyQt6.QtWidgets import QMainWindow, QFrame, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QComboBox, QLineEdit
from modules.app import app
from PyQt6.QtCore import Qt
import random



main_window = QMainWindow()



WIDTH_WINDOW = 1000
HEIGHT_WINDOW = 800

primary_screen = app.primaryScreen()
screen_size = primary_screen.size()
width_screen = screen_size.width()
height_screen = screen_size.height()


main_window.setGeometry(
    (width_screen // 2) - (WIDTH_WINDOW // 2), 
    (height_screen // 2) - (HEIGHT_WINDOW // 2), 
    WIDTH_WINDOW, 
    HEIGHT_WINDOW
)






main_frame = QFrame(parent= main_window)
main_frame.setStyleSheet("background-color: #D8B4F8")
main_frame.setFixedSize(WIDTH_WINDOW, HEIGHT_WINDOW)



main_layout = QHBoxLayout()
main_frame.setLayout(main_layout)






menu = QComboBox(parent = main_frame)
menu.setStyleSheet("background-color: #90C7FF; border 2px solid")
menu.setFixedSize(120, 20)
menu.addItems(["6", "8", "12", "16"])



menu2 = QComboBox(parent= main_frame)
menu2.setStyleSheet("background-color:  #90C7FF; border 2px solid")
menu2.setFixedSize(120, 20)
menu2.addItems(["Тільки цифри", "Літери та цифри", "Усі символи"])



frame2 = QFrame(parent= main_frame)
frame2.setStyleSheet("background-color:#D8B4F8; border: 1px solid")
frame2.setFixedSize(200, 50)
layout2 = QHBoxLayout()
frame2.setLayout(layout2)


delete = QPushButton(parent= main_frame, text = "Очистити")
delete.setFixedSize(170,20)
delete.setStyleSheet("background-color: #FFB7B2; color: white; ")




button = QPushButton(parent= main_frame, text = "Згенерувати")
main_layout.addWidget(button)
button.setFixedSize(150,20)
button.setStyleSheet("background-color: #A3E4D7; color: white")







main_layout.addWidget(menu)
main_layout.addWidget(menu2)
main_layout.addWidget(button)
main_layout.addWidget(frame2)
main_layout.addWidget(delete)








random_letter = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"


random_symbol = "!@#$%^&*()_+-=[]{};:',<>/?| ~ "

def click():
    if menu.currentText() == "6":
        if menu2.currentText() == "Тільки цифри":
            passw = ""
            for i in range(6):
                passw += str(random.randint(0,9))
            password.setText(passw)
        elif menu2.currentText() == "Літери та цифри":
            passw = ""
            for i in range(6):
                list_1 = [random.choice(random_letter), str(random.randint(0,9)),]
                num = random.randint(0,1)
                if num == 0:
                    passw += list_1[num]
                else:
                    passw += list_1[num] 
                password.setText(passw)
        else:
            passw = ""
            for i in range(6):
                list_2 = [random.choice(random_letter), str(random.randint(0,9)), random.choice(random_symbol)]
                num = random.randint(0,2)
                if num == 0:
                    passw += list_2[num]
                elif num == 1:
                    passw += list_2[num] 
                else:
                    passw += list_2[num]
                password.setText(passw)       
    elif menu.currentText() == "8":
        if menu2.currentText() == "Тільки цифри":
            passw = ""
            for i in range(8):
                passw += str(random.randint(0,9))
            password.setText(passw)
        elif menu2.currentText() == "Літери та цифри":
                    passw = ""
                    for i in range(8):
                        list_1 = [random.choice(random_letter), str(random.randint(0,9)),]
                        num = random.randint(0,1)
                        if num == 0:
                            passw += list_1[num]
                        else:
                            passw += list_1[num] 
                        password.setText(passw)
        else:
            passw = ""
            for i in range(8):
                list_2 = [random.choice(random_letter), str(random.randint(0,9)), random.choice(random_symbol)]
                num = random.randint(0,2)
                if num == 0:
                    passw += list_2[num]
                elif num == 1:
                    passw += list_2[num] 
                else:
                    passw += list_2[num]
                password.setText(passw) 



    elif menu.currentText() == "12":
            if menu2.currentText() == "Тільки цифри":
                passw = ""
                for i in range(12):
                    passw += str(random.randint(0,9))
                password.setText(passw)
            elif menu2.currentText() == "Літери та цифри":
                        passw = ""
                        for i in range(12):
                            list_1 = [random.choice(random_letter), str(random.randint(0,9)),]
                            num = random.randint(0,1)
                            if num == 0:
                                passw += list_1[num]
                            else:
                                passw += list_1[num] 
                            password.setText(passw)
            else:
                passw = ""
                for i in range(12):
                    list_2 = [random.choice(random_letter), str(random.randint(0,9)), random.choice(random_symbol)]
                    num = random.randint(0,2)
                    if num == 0:
                        passw += list_2[num]
                    elif num == 1:
                        passw += list_2[num] 
                    else:
                        passw += list_2[num]
                    password.setText(passw) 


    elif menu.currentText() == "16":
                if menu2.currentText() == "Тільки цифри":
                    passw = ""
                    for i in range(16):
                        passw += str(random.randint(0,9))
                    password.setText(passw)
                elif menu2.currentText() == "Літери та цифри":
                            passw = ""
                            for i in range(16):
                                list_1 = [random.choice(random_letter), str(random.randint(0,9)),]
                                num = random.randint(0,1)
                                if num == 0:
                                    passw += list_1[num]
                                else:
                                    passw += list_1[num] 
                                password.setText(passw)
                else:
                        passw = ""
                        for i in range(16):
                            list_2 = [random.choice(random_letter), str(random.randint(0,9)), random.choice(random_symbol)]
                            num = random.randint(0,2)
                            if num == 0:
                                passw += list_2[num]
                            elif num == 1:
                                passw += list_2[num] 
                            else:
                                passw += list_2[num]
                            password.setText(passw) 

    

    
                
button.clicked.connect(click)
password = QLabel(parent= frame2 )
password.setStyleSheet("background-color: #D8B4F8; border: None")
layout2.addWidget(password)


def delete_clicked():
        password.setText("")
delete.clicked.connect(delete_clicked)











