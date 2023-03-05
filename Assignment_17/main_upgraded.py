
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import math

def backspace():
    text_1 = main_window.text_box.text()
    text_2 = text_1[:-1]
    main_window.text_box.setText(text_2)

def c():
    main_window.text_box.setText("")

def num(x):
    main_window.text_box.setText(main_window.text_box.text() + x)

def plus():
    global op
    op = "+"
    global a
    a = int(main_window.text_box.text())
    main_window.text_box.setText("")

def sub():
    global op
    op = "-"
    global a
    a = int(main_window.text_box.text())
    main_window.text_box.setText("")

def mul():
    global op
    op = "*"
    global a
    a = int(main_window.text_box.text())
    main_window.text_box.setText("")

def div():
    global op
    op = "/"
    global a
    a = int(main_window.text_box.text())
    main_window.text_box.setText("")

def sin():
    global op
    op = "sin"

def cos():
    global op
    op = "cos"

def tan():
    global op
    op = "tan"

def cot():
    global op
    op = "cot"

def sqrt():
    global op
    op = "sqrt"

def log():
    global op
    op = "log"

def result():
    b = int(main_window.text_box.text())

    if op == "+":      
        c = a + b
        main_window.text_box.setText(str(c))
    elif op == "-":
        c = a - b
        main_window.text_box.setText(str(c))
    elif op == "*":
        c = a * b
        main_window.text_box.setText(str(c))
    elif op == "/":
        if b == 0:
            c = "Error"
            main_window.text_box.setText(c)
        else:
            c = a / b
            main_window.text_box.setText(str(c)) 

    elif op == "sin": 
        c = math.sin(b*math.pi/180)
        main_window.text_box.setText(str(c))
    elif op == "cos":   
        c = math.cos(b*math.pi/180)
        main_window.text_box.setText(str(c))
    elif op == "tan":   
        c = math.tan(b*math.pi/180)
        main_window.text_box.setText(str(c))
    elif op == "cot":   
        c = 1 / (math.tan(b*math.pi/180))
        main_window.text_box.setText(str(c))
    elif op == "sqrt":

        if b < 0:
            c = "Error"
            main_window.text_box.setText(c)
        else:
            c = math.sqrt(b)
            main_window.text_box.setText(str(c)) 

    elif op == "log":   
        c = math.log(b, 10)
        main_window.text_box.setText(str(c))

app = QApplication([])
loader = QUiLoader()
main_window = loader.load("Calculator_upgraded.ui")
main_window.show()

main_window.btn_backspace.clicked.connect(backspace)
main_window.btn_c.clicked.connect(c)
main_window.btn_dot.clicked.connect(partial(num, "."))
main_window.btn_0.clicked.connect(partial(num, "0"))
main_window.btn_1.clicked.connect(partial(num, "1"))
main_window.btn_2.clicked.connect(partial(num, "2"))
main_window.btn_3.clicked.connect(partial(num, "3"))
main_window.btn_4.clicked.connect(partial(num, "4"))
main_window.btn_5.clicked.connect(partial(num, "5"))
main_window.btn_6.clicked.connect(partial(num, "6"))
main_window.btn_7.clicked.connect(partial(num, "7"))
main_window.btn_8.clicked.connect(partial(num, "8"))
main_window.btn_9.clicked.connect(partial(num, "9"))
main_window.btn_plus.clicked.connect(plus)
main_window.btn_sub.clicked.connect(sub)
main_window.btn_mul.clicked.connect(mul)
main_window.btn_div.clicked.connect(div)
main_window.btn_sin.clicked.connect(sin)
main_window.btn_cos.clicked.connect(cos)
main_window.btn_tan.clicked.connect(tan)
main_window.btn_cot.clicked.connect(cot)
main_window.btn_sqrt.clicked.connect(sqrt)
main_window.btn_log.clicked.connect(log)
main_window.btn_result.clicked.connect(result)

app.exec()