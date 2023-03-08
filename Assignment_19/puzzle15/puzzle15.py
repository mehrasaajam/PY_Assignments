
import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_mainwindow import Ui_MainWindow

def non_repeating_random_2d_list(n, m):
    global total_list

    total_list = [[0 for i in range(n)] for j in range(m)]
    num_list = []

    for i in range(n):

        for j in range(m):

            while True:
                x = random.randint(1, 16)

                if x not in num_list:
                    total_list[i][j] = x
                    for row in total_list:
                        for num in row:
                            num_list.append(num)
                    break
    
    print(total_list)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.btns = [[self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4],
                    [self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btn_8],
                    [self.ui.btn_9, self.ui.btn_10, self.ui.btn_11, self.ui.btn_12],
                    [self.ui.btn_13, self.ui.btn_14, self.ui.btn_15, self.ui.btn_16]]

        non_repeating_random_2d_list(4, 4)
        print(total_list)
        for i in range(4):
            for j in range(4):
                r = total_list[i][j]
                self.btns[i][j].setText(str(r))
                self.btns[i][j].clicked.connect(partial(self.play, i, j))
                if r == 16:
                    self.btns[i][j].setVisible(False)
                    self.empty_i = i
                    self.empty_j = j

    def play(self, i, j):

        # if (i == self.empty_i and (j == self.empty_j -1 or j == self.empty_j + 1)) or (j == self.empty_j and (i == self.empty_i -1 or j == self.empty_i + 1)):
        if i == self.empty_i and abs(j - self.empty_j) == 1 or j == self.empty_j and abs(i - self.empty_i) == 1:
            self.btns[self.empty_i][self.empty_j].setText(self.btns[i][j].text())
            self.btns[i][j].setText("16")

            self.btns[self.empty_i][self.empty_j].setVisible(True)
            self.btns[i][j].setVisible(False)

            self.empty_i = i
            self.empty_j = j
        else:
            ...

        if self.check_win() == true:
            msg_box = QMessageBox()
            msg_box.setText("You Win!")
            msg_box.exec()

    def check_win(self):
        index = 1
        for i in range(4):
            for j in range(4):
                if int(self.btns[i][j].text()) != index:
                    return True
                index += 1

        return True


app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()