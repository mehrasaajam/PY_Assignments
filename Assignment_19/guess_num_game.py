
import random
import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader


def play():
    user_num = int(main_window.btn_num.text())

    if computer_num == user_num:
        main_window.btn_msg.setText("")
        msg_box = QMessageBox(text="you win 🎊")
        msg_box.exec()
        # print("you win in try", i)      
    elif computer_num > user_num:
        main_window.btn_msg.setText("go up ↑")
    elif computer_num < user_num:
        main_window.btn_msg.setText("go down ↓")

    # if computer_num != user_num and i == 9:
    #     msg_box = QMessageBox(text="you failed ☹")
    #     msg_box.exec()


app = QApplication(sys.argv)

loader = QUiLoader()
main_window = loader.load("guess_num_game.ui")
main_window.show()

computer_num = random.randint(0, 1000)

main_window.btn_check.clicked.connect(play)

app.exec()
