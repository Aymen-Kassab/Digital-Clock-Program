import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
# From this module we will import time, timer and Qt classes that we will need for our application
from PyQt5.QtCore import QTime, QTimer, Qt
# To work with fonts
from PyQt5.QtGui import QFont, QFontDatabase

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Digital Clock")
        self.setWindowIcon(QIcon("./logo.png"))
        self.time_label = QLabel(self) # This is the label that will display the time
        self.timer = QTimer(self)
        self.update_time()
        self.initUI()
    def initUI(self):
        self.setGeometry(500, 300, 800, 300)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        # Let's centre the label horizontally
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: hsl(111, 100%, 50%);")
        self.setStyleSheet("background-color: black;")

        # YES ALL OF THIS TO SET UP A FONT OF YOUR CHOOSING!
        font_id = QFontDatabase.addApplicationFont("./DS-DIGIB.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time() # To update the time

        # If you want to import a specific font do have to import TTF file (True Type Font)

    def update_time(self):
        current = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()