import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel , QGridLayout, QWidget 
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3rd app")
        self.setGeometry(500,150,1080,720)
        self.setWindowIcon(QIcon("icon.jpg"))
        self.initializeUI()
    

    def initializeUI(self):
        label=QLabel("Hello")
        label2=QLabel("Janagan")
        label3=QLabel("Welcome to PyQt5")

        QLabel.setStyleSheet(label,""" 
            font-size: 50px;
            color: red;
            width: 200px;
            height: 100px;           
            """)
        QLabel.setStyleSheet(label2,""" 
            font-size: 50px;
            color: blue;
            width: 200px;
            height: 100px;           
            """)
        QLabel.setStyleSheet(label3,""" 
            font-size: 50px;
            color: green;
            width: 400px;
            height: 100px;           
            """)

        central_widget=QWidget()
        self.setCentralWidget(central_widget)
        grid=QGridLayout()

        grid.addWidget(label,1,1)
        grid.addWidget(label2,1,0)
        grid.addWidget(label3,0,0)
        central_widget.setLayout(grid)





def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
    

if __name__=="__main__":
    main()