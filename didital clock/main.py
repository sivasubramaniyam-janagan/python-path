import sys
from PyQt5.QtWidgets import QApplication , QMainWindow ,QTimeEdit, QVBoxLayout, QWidget,QLabel 
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont , QIcon

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Digital Clock')
        self.setGeometry(100, 100, 300, 150)

        self.label= QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('Arial', 30))

        vbox = QVBoxLayout()
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        self.update_time()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  

    def update_time(self):
        current_time = QTime.currentTime().toString('hh:mm:ss AP')
        self.label.setText(current_time)
        
      


if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())