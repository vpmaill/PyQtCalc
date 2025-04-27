import sys
from math import sqrt
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QPushButton, QLabel, QGridLayout, QWidget, QSizePolicy)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.res = '0'
        self.first = '0'
        self.second = '0'
        self.currentSight = ''
        self.littleWindowDiv = ''
        self.firstTime = False

        self.setWindowTitle("Калькулятор")
        self.setGeometry(300, 70, 850, 850)

        param = self.size()

        self.littleWindow = QLabel(self.littleWindowDiv)
        self.littleWindow.setMinimumHeight(30)
        self.littleWindow.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.littleWindow.setStyleSheet("font-size: 15px; color: grey")
        self.littleWindow.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)

        self.mainLabel = QLabel(str(self.res))
        self.mainLabel.setStyleSheet("font-size: 80px")
        self.mainLabel.setMinimumHeight(150)
        self.mainLabel.setMaximumHeight(200)
        self.mainLabel.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.mainLabel.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignCenter)

        self.listLabel = QLabel(" Журнал")
        self.listLabel.setFixedWidth(300)
        self.listLabel.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.CreateButtons()

    def CreateButtons(self):
        button0 = QPushButton("0")
        button1 = QPushButton("1")
        button2 = QPushButton("2")
        button3 = QPushButton("3")
        button4 = QPushButton("4")
        button5 = QPushButton("5")
        button6 = QPushButton("6")
        button7 = QPushButton("7")
        button8 = QPushButton("8")
        button9 = QPushButton("9")
        buttonPercent = QPushButton("%")
        buttonCE = QPushButton("CE")
        buttonC = QPushButton("C")
        buttonBackspace = QPushButton("Backspace")
        buttonRecip = QPushButton("1/x")
        buttonPow = QPushButton("x^2")
        buttonRoot = QPushButton("sqrt(x)")
        buttonDivision = QPushButton(chr(247))
        buttonMul = QPushButton("x")
        buttonSub = QPushButton("-")
        buttonSum = QPushButton("+")
        buttonRes = QPushButton("=")
        buttonSig = QPushButton("+/-")
        buttonComa = QPushButton(",")

        Buttons = [button0, button1, button2, button3, button4,
                   button5, button6, button7, button8, button9,
                   buttonSig, buttonComa, buttonPercent, buttonCE,
                   buttonC, buttonBackspace, buttonRecip, buttonPow,
                   buttonRoot, buttonDivision, buttonMul, buttonSub,
                   buttonSum, buttonRes]

        for a in Buttons:
            a.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        for i in range(12):
            Buttons[i].setStyleSheet('QPushButton {font-size: 30px; background-color: #3b3b3b}')
        for i in range(12, len(Buttons)):
            Buttons[i].setStyleSheet('QPushButton {font-size: 25px; background-color: #323232}')
        buttonRes.setStyleSheet('QPushButton {font-size: 30px; color: black; background-color: #db9ee5}')

        layout = QGridLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.littleWindow, 0, 0, 1, 4)
        layout.addWidget(self.listLabel, 0, 4, 6, 1)
        layout.addWidget(self.mainLabel, 1, 0, 1, 4)
        layout.addWidget(buttonPercent, 2, 0)
        layout.addWidget(buttonCE, 2, 1)
        layout.addWidget(buttonC, 2, 2)
        layout.addWidget(buttonBackspace, 2, 3)
        layout.addWidget(buttonRecip, 3, 0)
        layout.addWidget(buttonPow, 3, 1)
        layout.addWidget(buttonRoot, 3, 2)
        layout.addWidget(buttonDivision, 3, 3)
        layout.addWidget(button7, 4, 0)
        layout.addWidget(button8, 4, 1)
        layout.addWidget(button9, 4, 2)
        layout.addWidget(buttonMul, 4, 3)
        layout.addWidget(button4, 5, 0)
        layout.addWidget(button5, 5, 1)
        layout.addWidget(button6, 5, 2)
        layout.addWidget(buttonSub, 5, 3)
        layout.addWidget(button1, 6, 0)
        layout.addWidget(button2, 6, 1)
        layout.addWidget(button3, 6, 2)
        layout.addWidget(buttonSum, 6, 3)
        layout.addWidget(buttonSig, 7, 0)
        layout.addWidget(button0, 7, 1)
        layout.addWidget(buttonComa, 7, 2)
        layout.addWidget(buttonRes, 7, 3)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        for i in range(10):
            Buttons[i].clicked.connect(lambda _, num=Buttons[i].text(): self.printNum(num))

        buttonSum.clicked.connect(self.SumBut)
        buttonSub.clicked.connect(self.SubBut)
        buttonDivision.clicked.connect(self.DivBut)
        buttonMul.clicked.connect(self.MulBut)
        buttonPow.clicked.connect(self.PowBut)
        buttonRoot.clicked.connect(self.SqrtBut)
        buttonRes.clicked.connect(self.ResBut)
        buttonC.clicked.connect(self.CBut)
        buttonCE.clicked.connect(self.CEBut)
        buttonSig.clicked.connect(self.SigBut)
        buttonComa.clicked.connect(self.ComaBut)
        buttonBackspace.clicked.connect(self.BackBut)
        buttonPercent.clicked.connect(self.PercBut)

    def SumBut(self):
        self.currentSight = "+"
        self.first = self.res
        self.res = "0"
        self.littleWindow.setText(f'{self.first} +')

    def SubBut(self):
        self.currentSight = "-"
        self.first = self.res
        self.res = "0"
        self.littleWindow.setText(f'{self.first} -')

    def DivBut(self):
        self.currentSight = "/"
        self.first = self.res
        self.res = "0"
        self.littleWindow.setText(f'{self.first} {chr(247)}')

    def MulBut(self):
        self.currentSight = "x"
        self.first = self.res
        self.res = "0"
        self.littleWindow.setText(f'{self.first} x')

    def PowBut(self):
        self.res **= 2
        self.littleWindow.setText(f"sqr({self.res})")

    def SqrtBut(self):
        if float(self.res) < 0:
            TempValue = self.res
            self.CBut()
            self.littleWindow.setText(f"sqrt({TempValue})")
            self.mainLabel.setText("Неверный ввод")
        else:
            self.res = sqrt(self.res)
            self.littleWindow.setText(f"sqrt({self.res})")

    def printNum(self, num):
        if self.currentSight == '':
            if self.res == '0':
                self.res = num
            else:
                self.res += num
            self.mainLabel.setText(self.res)
            self.first = self.res
        else:
            if self.res == '0':
                self.res = num
            else:
                self.res += num
            self.mainLabel.setText(self.res)
            self.second = self.res

    def ResBut(self):
        if self.currentSight == "+":
            if float(self.first) + float(self.second) != int(float(self.first) + float(self.second)):
                self.mainLabel.setText(str(float(self.first) + float(self.second)))
                self.littleWindow.setText(f'{self.first} + {self.second} =')
                self.first = str(float(self.first) + float(self.second))
            else:
                self.mainLabel.setText(str(int(float(self.first) + float(self.second))))
                self.littleWindow.setText(f'{self.first} + {self.second} =')
                self.first = str(int(float(self.first) + float(self.second)))
        elif self.currentSight == "-":
            if float(self.first) - float(self.second) != int(float(self.first) - float(self.second)):
                self.mainLabel.setText(str(float(self.first) - float(self.second)))
                self.littleWindow.setText(f'{self.first} - {self.second} =')
                self.first = str(float(self.first) - float(self.second))
            else:
                self.mainLabel.setText(str(int(float(self.first) - float(self.second))))
                self.littleWindow.setText(f'{self.first} - {self.second} =')
                self.first = str(int(float(self.first) - float(self.second)))
        elif self.currentSight == "/":
            if self.second != '0':
                if float(self.first) / float(self.second) != int(float(self.first) / float(self.second)):
                    self.mainLabel.setText(str(float(self.first) / float(self.second)))
                    self.littleWindow.setText(f'{self.first} {chr(247)} {self.second} =')
                    self.first = str(float(self.first) / float(self.second))
                else:
                    self.mainLabel.setText(str(int(float(self.first) / float(self.second))))
                    self.littleWindow.setText(f'{self.first} {chr(247)} {self.second} =')
                    self.first = str(int(float(self.first) / float(self.second)))
            else:
                tempValue = self.first
                self.mainLabel.setText("Деление на ноль невозможно")
                self.littleWindow.setText(f'{tempValue} {chr(247)}')
        elif self.currentSight == "x":
            if float(self.first) * float(self.second) != int(float(self.first) * float(self.second)):
                self.mainLabel.setText(str(float(self.first) * float(self.second)))
                self.littleWindow.setText(f'{self.first} x {self.second} =')
                self.first = str(float(self.first) * float(self.second))
            else:
                self.mainLabel.setText(str(int(float(self.first) * float(self.second))))
                self.littleWindow.setText(f'{self.first} x {self.second} =')
                self.first = str(int(float(self.first) * float(self.second)))
        self.res = self.first
        # self.first = '0'
        # self.currentSight = ''

    def CBut(self):
        self.res = '0'
        self.first = '0'
        self.second = '0'
        self.currentSight = ''
        self.littleWindowDiv = ''
        self.firstTime = False
        self.mainLabel.setText('0')
        self.littleWindow.setText('')

    def CEBut(self):
        self.res = '0'
        self.second = '0'
        self.mainLabel.setText('0')

    def SigBut(self):
        if self.currentSight == '':
            self.res = -1 * float(self.res)
            if int(self.res) == float(self.res):
                self.mainLabel.setText(str(int(self.res)))
                self.res = str(int(self.res))
            else:
                self.mainLabel.setText(str(self.res))
                self.res = str(self.res)
        else:
            self.second = -1 * float(self.second)
            if int(self.second) == float(self.second):
                self.mainLabel.setText(str(int(self.second)))
                self.second = str(int(self.second))
            else:
                self.mainLabel.setText(str(self.second))
                self.second = str(self.second)

    def ComaBut(self):
        self.res = self.res + "."
        self.mainLabel.setText(self.res)

    def BackBut(self):
        if len(self.res) == 1:
            self.res = '0'
            self.mainLabel.setText(self.res)
        else:
            self.res = self.res[:-1]
            self.mainLabel.setText(self.res)

    def PercBut(self):
        a = 1
        if self.currentSight == "x":
            if self.second == '0':
                self.second = self.first
                self.second = float(self.second) / 100
                if self.second.is_integer():
                    self.second = str(int(self.second))
                self.littleWindow.setText(f'{self.first} x {self.second}')
                self.res = float(self.second) * float(self.first)
                if self.res.is_integer():
                    self.res = str(int(self.res))
                self.mainLabel.setText(self.res)
            else:
                self.second = float(self.second) / 100
                if self.second.is_integer():
                    self.second = str(int(self.second))
                self.littleWindow.setText(f'{self.first} x {self.second}')
                self.res = float(self.second) * float(self.first)
                if self.res.is_integer():
                    self.res = str(int(self.res))
                self.mainLabel.setText(self.res)
            self.res = self.first
            self.first = '0'
            self.currentSight = ''
            self.second = "0"
        else:
            self.res = '0'
            self.first = '0'
            self.littleWindow.setText(self.res)
            self.mainLabel.setText(self.res)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
