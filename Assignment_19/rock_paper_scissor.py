
import random
import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader


def play_rock():
    global player
    global player_score
    global computer_score
   
    if player == 1:
        main_window.btn_ply_choice.setText("👊")
        player = 2

    if player == 2:
        cpu()
        player = 1

    check()


def play_paper():
    global player
    global player_score
    global computer_score
   
    if player == 1:
        main_window.btn_ply_choice.setText("✋")
        player = 2

    if player == 2:
        cpu()
        player = 1

    check()


def play_scissor():
    global player
    global player_score
    global computer_score
   
    if player == 1:
        main_window.btn_ply_choice.setText("🤞")
        player = 2

    if player == 2:
        cpu()
        player = 1

    check()


def cpu():
    x = random.randint(1, 3)

    if x == 1:
        main_window.btn_com_choice.setText("👊")
    elif x == 2:
        main_window.btn_com_choice.setText("✋")
    elif x == 3:
        main_window.btn_com_choice.setText("🤞")


def check():
    global player
    global player_score
    global computer_score

    if main_window.btn_com_choice.text() == "👊" and main_window.btn_ply_choice.text() == "✋":
        player_score += 1
    elif main_window.btn_com_choice.text() == "👊" and main_window.btn_ply_choice.text() == "🤞":
       computer_score += 1
    elif main_window.btn_com_choice.text() == "✋" and main_window.btn_ply_choice.text() == "👊":
        computer_score += 1
    elif main_window.btn_com_choice.text() == "✋" and main_window.btn_ply_choice.text() == "🤞":
        player_score += 1
    elif main_window.btn_com_choice.text() == "🤞" and main_window.btn_ply_choice.text() == "👊":
        player_score += 1
    elif main_window.btn_com_choice.text() == "🤞" and main_window.btn_ply_choice.text() == "✋":
        computer_score += 1

    main_window.btn_ply_score.setText("Your score : " + str(player_score))
    main_window.btn_com_score.setText("Computer score : " + str(computer_score))

    if player_score == 3:
        msg_box = QMessageBox(text="You win!")
        msg_box.exec()

    if computer_score == 3:
        msg_box = QMessageBox(text="Computer wins!")
        msg_box.exec()


app = QApplication(sys.argv)

loader = QUiLoader()
main_window = loader.load("rock_paper_scissor.ui")
main_window.show()

player = 1
player_score = 0
computer_score = 0
main_window.btn_ply_score.setText("Your score : " + str(player_score))
main_window.btn_com_score.setText("Computer score : " + str(computer_score))

main_window.btn_rock.setText("👊")
main_window.btn_paper.setText("✋")
main_window.btn_scissor.setText("🤞")

main_window.btn_rock.clicked.connect(play_rock)
main_window.btn_paper.clicked.connect(play_paper)
main_window.btn_scissor.clicked.connect(play_scissor)

app.exec()
