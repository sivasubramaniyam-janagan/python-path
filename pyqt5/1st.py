import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("1st app")
        self.setGeometry(500,150,1080,720)
        self.setWindowIcon(QIcon("icon.jpg"))
        label=QLabel("Hello",self)
        label.setGeometry(20,20,200,100)
        label.setStyleSheet(""" 
            font-size: 50px;
            color: red;
            width: 200px;
            height: 100px;           
            """)
        label1=QLabel("Janagan",self)
        label1.setGeometry(20,150,1080,200)
        label1.setStyleSheet(""" 
            font-size: 50px;
            color: blue;
            font-family: Arial;  
            background-color: yellow;
            """)
        label1.setAlignment(Qt.AlignCenter)
        label1.setFont(QFont("Arial",50))



def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
    




if __name__=="__main__":
    main()