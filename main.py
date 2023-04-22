import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        # Hesap makinesi penceresi ayarları
        self.setWindowTitle("Hesap Makinesi")
        self.setGeometry(0, 0, 500, 300)

        # Widget'lar oluşturuluyor
        widget = QWidget(self)
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.display = QLineEdit()

        # Widget'lar özellikleri ayarlanıyor
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)

        # Widget'lar layoutlara ekleniyor
        vbox.addWidget(self.display)

        for i in range(1, 10):
            button = QPushButton(str(i))
            button.clicked.connect(lambda _, num=i: self.add_to_display(num))
            hbox.addWidget(button)
            if i % 3 == 0:
                vbox.addLayout(hbox)
                hbox = QHBoxLayout()

        button_zero = QPushButton('0')
        button_zero.clicked.connect(lambda: self.add_to_display(0))
        hbox.addWidget(button_zero)

        button_add = QPushButton('+')
        button_add.clicked.connect(lambda: self.add_operator('+'))
        hbox.addWidget(button_add)

        vbox.addLayout(hbox)

        hbox = QHBoxLayout()

        button_clear = QPushButton('C')
        button_clear.clicked.connect(lambda: self.display.setText(''))
        hbox.addWidget(button_clear)

        button_subtract = QPushButton('-')
        button_subtract.clicked.connect(lambda: self.add_operator('-'))
        hbox.addWidget(button_subtract)

        vbox.addLayout(hbox)

        hbox = QHBoxLayout()

        button_multiply = QPushButton('*')
        button_multiply.clicked.connect(lambda: self.add_operator('*'))
        hbox.addWidget(button_multiply)

        button_divide = QPushButton('/')
        button_divide.clicked.connect(lambda: self.add_operator('/'))
        hbox.addWidget(button_divide)

        vbox.addLayout(hbox)

        hbox = QHBoxLayout()

        button_equals = QPushButton('=')
        button_equals.clicked.connect(self.calculate_result)
        hbox.addWidget(button_equals)

        vbox.addLayout(hbox)

        # Widget'lar layouta ekleniyor
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.current_operator = None
        self.current_value = None
        self.new_value = False

    def add_to_display(self, num):
        if self.new_value:
            self.display.setText(str(num))
            self.new_value = False
        else:
            self.display.setText(self.display.text() + str(num))

    def add_operator(self, operator):
        self.current_operator = operator
        self.current_value = float(self.display.text())
        self.new_value = True

    def calculate_result(self):
        if self.current_operator is None:
            return
        value = float(self.display.text())
        if self.current_operator == '+':
            result = self.current_value + value
        elif self.current_operator == '-':
            result = self.current_value - value
        elif self.current_operator == '*':
            result = self.current_value * value
        else:
            result = self.current_value / value

        self.display.setText(str(result))
        self.current_operator = None
        self.new_value = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
