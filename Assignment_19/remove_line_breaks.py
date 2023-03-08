
import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

def run():
    first_txt = main_window.text_edit.text()
    second_txt = first_txt.replace(r'\n', ' ').replace(r'\r', '')
    main_window.text_first.setText(second_txt)

app = QApplication(sys.argv)

loader = QUiLoader()
main_window = loader.load("remove_line_breaks.ui")
main_window.show()

main_window.btn_run.clicked.connect(run)

app.exec()
