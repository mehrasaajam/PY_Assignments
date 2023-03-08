
import random
import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader


def play_1():
    global user_score
    global com1_score
    global com2_score
    main_window.btn_user.setText("✋")
    com1_choice = int(random.randint(0, 1))
    com2_choice = int(random.randint(0, 1))

    if com1_choice == 0 and com2_choice == 0:
        main_window.btn_com1.setText("🤚")
        main_window.btn_com2.setText("🤚")
        user_score += 1
    elif com1_choice == 0 and com2_choice == 1:
        main_window.btn_com1.setText("🤚")
        main_window.btn_com2.setText("✋")
        com1_score += 1
    elif com1_choice == 1 and com2_choice == 0:
        main_window.btn_com1.setText("✋")
        main_window.btn_com2.setText("🤚")
        com2_score += 1
    main_window.btn_user_score.setText("Score : " + str(user_score))
    main_window.btn_com1_score.setText("Score : " + str(com1_score))
    main_window.btn_com2_score.setText("Score : " + str(com2_score))
    check()

def play_0():
    global user_score
    global com1_score
    global com2_score
    main_window.btn_user.setText("🤚")
    com1_choice = int(random.randint(0, 1))
    com2_choice = int(random.randint(0, 1))

    if com1_choice == 1 and com2_choice == 1:
        main_window.btn_com1.setText("✋")
        main_window.btn_com2.setText("✋")
        user_score += 1
    elif com1_choice == 1 and com2_choice == 0:
        main_window.btn_com1.setText("✋")
        main_window.btn_com2.setText("🤚")
        com1_score += 1
    elif com1_choice == 0 and com2_choice == 1:
        main_window.btn_com1.setText("🤚")
        main_window.btn_com2.setText("✋")
        com2_score += 1
    main_window.btn_user_score.setText("Score : " + str(user_score))
    main_window.btn_com1_score.setText("Score : " + str(com1_score))
    main_window.btn_com2_score.setText("Score : " + str(com2_score))
    check()
    
def check():
    global i
    i += 1
    if i == 5:
        if user_score > com1_score and user_score > com2_score:
            msg_box = QMessageBox(text="You win!")
            msg_box.exec()
        elif com1_score > user_score and com1_score > com2_score:
            msg_box = QMessageBox(text="Computer 1 win!")
            msg_box.exec()
        elif com2_score > user_score and com2_score > com1_score:
            msg_box = QMessageBox(text="Computer 2 win!")
            msg_box.exec()
        else:
            msg_box = QMessageBox(text="Draw!")
            msg_box.exec()
    

app = QApplication(sys.argv)

loader = QUiLoader()
main_window = loader.load("palam_polom_pilish.ui")
main_window.show()

i = 0
user_score = 0
com1_score = 0
com2_score = 0
main_window.btn_user_score.setText("Score : " + str(user_score))
main_window.btn_com1_score.setText("Score : " + str(com1_score))
main_window.btn_com2_score.setText("Score : " + str(com2_score))

main_window.btn_1.setText("✋")
main_window.btn_0.setText("🤚")

main_window.btn_1.clicked.connect(play_1)
main_window.btn_0.clicked.connect(play_0)

app.exec()
