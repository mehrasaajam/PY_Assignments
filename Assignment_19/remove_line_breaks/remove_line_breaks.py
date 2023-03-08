
import sys
import re
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

def run():
    edited = main_window.first_txt.toPlainText().replace("\n", " ")
    main_window.second_txt.setPlainText(edited)

app = QApplication(sys.argv)

loader = QUiLoader()
main_window = loader.load("remove_line_breaks.ui")
main_window.show()

main_window.btn_run.clicked.connect(run)

app.exec()
