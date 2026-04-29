import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Example")
        self.setGeometry(100, 100, 700, 700)

        self.text=QLineEdit(self)
        self.text.setGeometry(50, 50, 200, 30)
        self.text.setPlaceholderText("Enter text here")
        self.text.setStyleSheet(""" 
            background-color: lightgray;
            border: 1px solid black;
            border-radius: 5px;
        """)


        self.button = QPushButton("Click Me", self)
        self.button.setGeometry(50, 100, 100, 30)
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        input_text = self.text.text()
        print(f"Button clicked! You entered: {input_text}")







def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

main()