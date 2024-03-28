import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout, QMainWindow
from PyQt5 import Qt


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.init_ui()

    def init_ui(self):
        self.input_line = QLineEdit()
        self.input_line.setAlignment(Qt.AlignRight)
        self.input_line.setReadOnly(True)

        self.create_buttons()

        layout = QVBoxLayout()
        layout.addWidget(self.input_line)

        for row in self.buttons:
            button_row = QHBoxLayout()
            for button_text, button_slot in row:
                button = QPushButton(button_text)
                button.clicked.connect(button_slot)
                button_row.addWidget(button)
            layout.addLayout(button_row)

        self.central_widget.setLayout(layout)

    def create_buttons(self):
        self.buttons = [
            [("7", self.digit_pressed), ("8", self.digit_pressed), ("9", self.digit_pressed), ("+", self.operator_pressed)],
            [("4", self.digit_pressed), ("5", self.digit_pressed), ("6", self.digit_pressed), ("-", self.operator_pressed)],
            [("1", self.digit_pressed), ("2", self.digit_pressed), ("3", self.digit_pressed), ("*", self.operator_pressed)],
            [("0", self.digit_pressed), (".", self.digit_pressed), ("=", self.calculate_result), ("/", self.operator_pressed)]
        ]

    def digit_pressed(self):
        button = self.sender()
        digit = button.text()
        current_text = self.input_line.text()
        new_text = current_text + digit
        self.input_line.setText(new_text)

    def operator_pressed(self):
        button = self.sender()
        operator = button.text()
        current_text = self.input_line.text()
        new_text = current_text + " " + operator + " "
        self.input_line.setText(new_text)

    def calculate_result(self):
        expression = self.input_line.text()
        try:
            result = eval(expression)
            self.input_line.setText(str(result))
        except Exception as e:
            self.input_line.setText("Error")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
