import hashlib
import os.path
import sys

import bcrypt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout, \
    QStackedWidget
from PyQt5.QtGui import QPalette, QBrush, QLinearGradient, QPixmap, QTransform
from PyQt5.QtCore import Qt, QTimer
from pymongo import MongoClient


#Changes required:
def changes():
    """
    0) Make the entire code in a simple and understandable way by making it in OOPS format! (Done!)
    0.1) Hide the Important folders and files that are not required to open source.
    1) Complete the hashing of the passwords
    2) Work on the UI so that the peacock feather is oriented and positioned in the corned at 37degrees
    3) Complete the login sessions and logout sessions
    4) Make the functions more reliable
    5) Complete the page2, which questions about the sadhana chart of the respective person
    6) Complete the notes page where the person can write his important notes.
    7) Make the app global with global databases.
    8) Make the people use it, and make a leaderboard for the people who daily report.
    9) Make the entire project into a git repository and post it in github
    """


connection = MongoClient('localhost', 27017)
db = connection['SadhanaChart']
collection_1 = db['Users']
SESSION_FILE = 'session.txt'


def hashPasswords(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def checkPasswords(password, a_password):
    return bcrypt.checkpw(password.encode('utf-8'), a_password.encode('utf-8'))


def temporaryWarnings(name, Text, time):
    temp = name.text()
    temp_style = name.StyleSheet()

    name.setText(Text)
    name.setStyleSheet("color: red;", "font-family: Arial;", "font-size: 16px;", "font-weight: bold;")

    QTimer.singleShot(time, lambda: (name.setText(temp), name.setStyleSheet(temp_style)))


class login_page(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Sadhana App")
        self.setGeometry(300, 300, 500, 500)
        self.label1 = QLabel('Welcome to Sadhana App! ', self)
        self.name_ = QLineEdit(self)
        self.name_.setPlaceholderText('Enter Username: ')
        self.password_ = QLineEdit(self)
        self.submit = QPushButton(self)
        self.password_.setPlaceholderText("Enter Password")
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                spread: pad, x1:0, y1:0, x2:1, y2:1,
                stop: 0 rgba(0,0,255,0.3), stop:1 rgba(255,255,255,0.5)
                );
            }
        """)
        self.initUi()

    def initUi(self):

        self.label1.setStyleSheet("""
            QLabel {
                background: transparent;
                qproperty-alignment: 'AlignCenter';
                font-family: Arial;
                font-weight: bold;
                font-size: 20px;
                color: black;
            }
        """)

        self.name_.setStyleSheet("""
            QLineEdit {
                background-color: rgba(255,255,255,50);
                qproperty-alignment: 'AlignCenter'; /* Center text horizontally and vertically */
                color: black;
                font-family: Arial;
                font-size: 12px;
                border: none;
                border-radius: 13px;
            }
        """)

        self.password_.setEchoMode(QLineEdit.Password)
        self.password_.setStyleSheet("""
            QLineEdit {
                background-color: rgba(255,255,255,50);
                qproperty-alignment: 'AlignCenter'; /* Center text horizontally and vertically */
                color: black;
                font-family: Arial;
                font-size: 12px;
                border: none;
                border-radius: 13px;
            }
        """)

        self.submit.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: white;
                font-family: Arial;
                font-weight: bold;
                padding: 10px;
                border: none;
                border-radius: 13px;
                qproperty-alignment: 'AlignCenter';
            }
            QPushButton:hover {
                background-color: rgba(0,255,0,0.2);
            }
        """)
        forRegisterButton = QPushButton("Register Here")
        forRegisterButton.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: white;
                font-family: Arial;
                font-weight: bold;
                padding: 10px;
                border: none;
                border-radius: 13px;
                qproperty-alignment: 'AlignCenter';
            }
            QPushButton:hover {
                background-color: rgba(0,255,0,0.2);
            }
        """)
        forRegisterButton.clicked.connect(self.show_register_page)
        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.name_)
        layout.addWidget(self.password_)
        layout.addWidget(forRegisterButton)
        layout.addWidget(self.submit)
        self.setLayout(layout)

    def loginButton(self):
        username = self.name_.text()
        password = self.password_.text()

        user_find = collection_1.find_one({'Name': username})
        if user_find is not None and checkPasswords(user_find['Password'], password):
            with open(SESSION_FILE, 'w') as session_file:
                session_file.write('Logged-In')
            self.submit.clicked.connect(self.show_main_page)
        else:
            temporaryWarnings(self.label1, "Please Register to the Application", 5000)

    def show_main_page(self):
        self.app.show_main_page()
    def show_register_page(self):
        self.app.show_register_page()

class main_page(QWidget):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Sadhana App")
        self.setGeometry(300, 300, 500, 500)
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    spread: pad, x1:0, y1:0, x2:1, y2:1,
                    stop: 0 rgba(0,0,255,0.3), stop:1 rgba(255,255,255,0.5)
                );
            }
        """)
        label1 = QLabel('Enter your username here: ', self)
        label1.setStyleSheet("background: transparent;"
                             "color: black;"
                             "font-family: Arial;"
                             "font-size: 20px;"
                             "font-weight: bold;")
        ReturnButton = QPushButton("<<")
        ReturnButton.setStyleSheet("color: black;")
        logoutButton = QPushButton("Logout")
        layout = QFormLayout()
        layout.addRow(label1)
        layout.addRow(ReturnButton)
        layout.addRow(logoutButton)
        self.setLayout(layout)

    def logout(self):
        if os.path.exists(SESSION_FILE):
            os.remove(SESSION_FILE)
        self.app.show_login_page()


class RegisterPage(QWidget):
    def __init__(self, app):
        super().__init__()
        self.setWindowTitle("Sadhana Register Page")
        self.setGeometry(300, 300, 500, 500)
        self.initUi()

    def initUi(self):
        self.setStyleSheet("""
                QWidget {
                background: qlineargradient(
                    spread: pad, x1:0, y1:0, x2:1, y2:1,
                    stop: 0 rgba(0,0,255,0.3), stop:1 rgba(255,255,255,0.5)
                );
            }
        """)
        registerLabel = QLabel("Register Your Account", self)
        registerLabel.setStyleSheet("""
            QLabel {
                background: transparent;
                qproperty-alignment: 'AlignCenter';
                font-family: Arial;
                font-weight: bold;
                font-size: 20px;
                color: white;
            }
        """)
        registerAcc = QLineEdit()
        registerAcc.setStyleSheet("""
            QLineEdit {
                background-color: rgba(255,255,255,50);
                qproperty-alignment: 'AlignCenter'; /* Center text horizontally and vertically */
                color: white;
                font-family: Arial;
                font-size: 12px;
                border: none;
                border-radius: 13px;
            }
        """)
        registerPass = QLineEdit()
        registerPass.setStyleSheet("""
            QLineEdit {
                background-color: rgba(255,255,255,50);
                qproperty-alignment: 'AlignCenter'; 
                color: white;
                font-family: Arial;
                font-size: 12px;
                border: none;
                border-radius: 13px;
            }
        """)
        registerSubmit = QPushButton("Submit")
        registerSubmit.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: white;
                font-family: Arial;
                font-weight: bold;
                padding: 10px;
                border: none;
                border-radius: 13px;
                qproperty-alignment: 'AlignCenter';
            }
            QPushButton:hover {
                background-color: rgba(0,255,0,0.2);
            }
        """)
        layout = QFormLayout()
        layout.addRow(registerLabel)
        layout.addRow(registerAcc)
        layout.addRow(registerPass)
        layout.addRow(registerSubmit)
        self.setLayout(layout)


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)
        self.stack = QStackedWidget(self)

        self.login_page = login_page(self)
        self.main_page = main_page(self)
        self.register_page = RegisterPage(self)

        self.stack.addWidget(self.login_page)
        self.stack.addWidget(self.main_page)

        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)
        if os.path.exists(SESSION_FILE):
            self.show_main_page()
        else:
            self.show_login_page()

    def show_login_page(self):
        self.stack.setCurrentWidget(self.login_page)
    def show_main_page(self):
        self.stack.setCurrentWidget(self.main_page)
    def show_register_page(self):
        self.stack.setCurrentWidget(self.register_page)
# Main Function:
def main():
    app = QApplication(sys.argv)
    my_app = Application()
    my_app.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()