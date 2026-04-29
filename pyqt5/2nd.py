import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton ,QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2nd app")
        self.setGeometry(500,150,1080,720)
        self.initializeUI()
        self.label=QLabel("Hello",self)
        self.label.setGeometry(20,150,200,100)
        

    def initializeUI(self):
        self.button=QPushButton("Click me",self)
        self.button.setGeometry(20,20,200,100)
        self.button.setStyleSheet("""
            font-size: 50px;
            color: red;
            width: 200px;
            height: 100px;  
            """)
        self.button.clicked.connect(self.buttonClicked)
        
    def buttonClicked(self):
        print("Button clicked")
        self.button.setText("Clicked")
        self.label.setText("Button clicked")


def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()