from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
import serial
import sys
import threading

serialPort = "COM4"  # serial port
baudRate = 115200  # baud rate


class SerialPort:
    message = ''

    def __init__(self, port, buand):
        super(SerialPort, self).__init__()
        self.port = serial.Serial(port, buand)
        self.port.close()
        if not self.port.isOpen():
            self.port.open()

    def port_open(self):
        if not self.port.isOpen():
            self.port.open()  # Open Serial Port

    def port_close(self):
        self.port.close()

    def send_data(self, data):
        n = self.port.write(data.encode())  # send data

    def read_data(self):  # receive data
        while True:
            self.message = self.port.readline()  # receive data
            print(self.message)


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Arduino Piano"
        self.top = 150
        self.left = 150
        self.width = 600
        self.height = 500

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))

        for i in range(0, 8):
            painter.drawRect(100 + i * 50, 100, 50, 200)

        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        painter.drawRect(135, 100, 30, 125)
        painter.drawRect(135 + 50, 100, 30, 125)
        painter.drawRect(135 + 150, 100, 30, 125)
        painter.drawRect(135 + 200, 100, 30, 125)
        painter.drawRect(135 + 250, 100, 30, 125)

    def keyPressEvent(self, input):
        if input.key() == Qt.Key_Q:
            print("DO-Keyboard")
            mSerial.send_data('1')
        elif input.key() == Qt.Key_W:
            print("RE-Keyboard")
            mSerial.send_data('3')
        elif input.key() == Qt.Key_E:
            print("MI-Keyboard")
            mSerial.send_data('5')
        elif input.key() == Qt.Key_R:
            print("FA-Keyboard")
            mSerial.send_data('6')
        elif input.key() == Qt.Key_T:
            print("SOL-Keyboard")
            mSerial.send_data('8')
        elif input.key() == Qt.Key_Y:
            print("LA-Keyboard")
            mSerial.send_data('10')
        elif input.key() == Qt.Key_U:
            print("SI-Keyboard")
            mSerial.send_data('12')
        elif input.key() == Qt.Key_I:
            print("DO!-Keyboard")
            mSerial.send_data('13')
        elif input.key() == Qt.Key_2:
            print("DO#-Keyboard")
            mSerial.send_data('2')
        elif input.key() == Qt.Key_3:
            print("RE#-Keyboard")
            mSerial.send_data('4')
        elif input.key() == Qt.Key_5:
            print("FA#-Keyboard")
            mSerial.send_data('7')
        elif input.key() == Qt.Key_6:
            print("SOL#-Keyboard")
            mSerial.send_data('9')
        elif input.key() == Qt.Key_7:
            print("LA#-Keyboard")
            mSerial.send_data('11')
        elif input.key() == Qt.Key_Escape:
            self.close()

    def keyReleaseEvent(self, event) :
        mSerial.send_data('0')

    def mouseReleaseEvent(self, event):
        #  print("released")
        mSerial.send_data('0')

    def mousePressEvent(self, event):
        x = event.x()
        y = event.y()
        # print(f"x = {x} | y = {y}")

        if 100 < x < 250 and 100 < y < 300:
            if 135 < x < 165 and 100 < y < 225:
                print("DO#")
                mSerial.send_data('2')
            elif 135 + 50 < x < 165 + 50 and 100 < y < 225:
                print("RE#")
                mSerial.send_data('4')
            elif x < 150:
                print("DO")
                mSerial.send_data('1')
            elif 150 < x < 200:
                print("RE")
                mSerial.send_data('3')
            elif x > 200:
                print("MI")
                mSerial.send_data('5')

        elif 250 < x < 500 and 100 < y < 300:
            if 135 + 150 < x < 165 + 150 and 100 < y < 225:
                print("FA#")
                mSerial.send_data('7')
            elif 135 + 200 < x < 165 + 200 and 100 < y < 225:
                print("SOL#")
                mSerial.send_data('9')
            elif 135 + 250 < x < 165 + 250 and 100 < y < 225:
                print("LA#")
                mSerial.send_data('11')
            elif 250 < x < 300:
                print("FA")
                mSerial.send_data('6')
            elif 300 < x < 350:
                print("SOL")
                mSerial.send_data('8')
            elif 350 < x < 400:
                print("LA")
                mSerial.send_data('10')
            elif 400 < x < 450:
                print("SI")
                mSerial.send_data('12')
            elif 450 < x < 500:
                print("DO!")
                mSerial.send_data('13')


if __name__ == '__main__':
    serialPort = "COM" + input("Please enter the COM (1-12) : ")
    baudRate = input("Please enter the BaudRate : ")
    input("\nPlease wait 3 second after starting program\n"
          "Keyboard Control : Q 2 W 3 E R 5 T 6 Y 7 U I\n"
          "Click Control : Click the tuts\n"
          "Enter to Continue...\n")
    input("Created by Araaf Ario...")
    print("GUI Starting")

    mSerial = SerialPort(serialPort, baudRate)
    t1 = threading.Thread(target=mSerial.read_data)
    t1.start()
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
