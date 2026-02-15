import sys
import segno

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import (QPushButton, QApplication,
                            QLineEdit, QVBoxLayout,
                            QWidget, QLabel)

version = 1.0

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SURFACE | QR-GENERATOR  -v" + str(version))
        self.setGeometry(500, 500, 500, 500)
        self.setWindowIcon(QIcon("logo.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.title_label = QLabel("SURFACE | QR", self)
        self.version_label = QLabel(str(version))
        self.value_entry = QLineEdit(self)
        self.convert_btn = QPushButton("Convert to QR", self)
        self.qr_label = QLabel(self)

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()

        vbox.addWidget(self.title_label)
        vbox.addWidget(self.value_entry)
        vbox.addWidget(self.convert_btn)
        vbox.addWidget(self.qr_label)
        vbox.setAlignment(Qt.AlignTop)

        self.title_label.setAlignment(Qt.AlignLeft)
        self.value_entry.setAlignment(Qt.AlignHCenter)
        self.qr_label.setAlignment(Qt.AlignTop)
        self.qr_label.setAlignment(Qt.AlignHCenter)

        self.setLayout(vbox)
        
        self.setStyleSheet("""
                QWidget{
                            background-color: #1B262C;
                }
                QLabel{
                            font-family: Cascadia Code;
                            font-size: 35px;
                            color: white;
                            font-weight: bold;
                }
                QLineEdit{
                            font-size: 25px;
                            font-family: Cascadia Code;
                            background-color: #0F4C75;
                            color: #BBE1FA;
                            border-radius: 8px;
                            padding: 9 9 9 9;
                }
                QPushButton{
                            font-size: 35px;
                            background-color: #0F4C75;
                            border-radius: 8px;
                            color: #BBE1FA;
                            font-family: Cascadia Code;
                            padding: 7 7 7 7;
                }
                QPushButton:hover,
                QPushButton:focus {
                            background-color: #3282B8;
                            border: 3px solid #9ac3fe;
                            color: #1B262C;
                }
        """)

        self.convert_btn.clicked.connect(self.create_qr_code)

    def create_qr_code(self):
        qrcode = segno.make_qr(self.value_entry.text())
        qrcode.save("qrcode.png", scale=10)

        self.pixmap = QPixmap("qrcode.png")
        self.qr_label.setPixmap(self.pixmap)

        print("QR code saved!")


if __name__ == "__main__":
    qrapp = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(qrapp.exec_())