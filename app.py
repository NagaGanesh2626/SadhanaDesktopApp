import os.path
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFormLayout
from PyQt5.QtGui import QPalette, QBrush, QLinearGradient, QPixmap, QTransform
from PyQt5.QtCore import Qt, QTimer
from pymongo import MongoClient

#Changes required:
def changes():
    """
    0) Make the entire code in a simple and understandable way by making it in OOPS format! (Done!)
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


class login_page(QWidget):
    def __init__(self):
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
        label1.setStyleSheet("""
            QLabel {
                background: transparent;
                qproperty-alignment: 'AlignCenter';
                font-family: Arial;
                font-weight: bold;
                font-size: 20px;
                color: black;
            }
        """)
        name_ = QLineEdit(self)
        name_.setStyleSheet("""
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
        password_ = QLineEdit(self)
        password_.setEchoMode(QLineEdit.Password)
        password_.setStyleSheet("""
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
        submit = QPushButton("Submit", self)
        submit.setStyleSheet("""
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
        imagelabel = QLabel(self)
        image1 = QPixmap("feaether.png")
        imagelabel.setPixmap(image1)
        transform = QTransform()
        rotated_image = image1.transformed(transform, Qt.SmoothTransformation)
        imagelabel.setPixmap(rotated_image)
        imagelabel.setStyleSheet("background: transparent;")
        scaled_image = image1.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        imagelabel.setPixmap(scaled_image)
        imagelabel.resize(scaled_image.width(), scaled_image.height())
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
        layout = QFormLayout()
        layout.addRow(label1)
        layout.addRow(name_)
        layout.addRow(password_)
        layout.addRow(submit)
        self.setLayout(layout)

    def page1submit(self):
        ...


class main_page(QWidget):
    def __init__(self):
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

    def forReturnButton(self):
        ...

    def forLogoutButton(self):
        ...


class RegisterPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sadhana Register Page")
        self.setGeometry(300, 300, 500, 500)
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

# Main Function:
def main():
    app = QApplication(sys.argv)
    loginPage = login_page()
    loginPage.show()

    mainpage = main_page()
    # mainpage.show()

    registerPage = RegisterPage()
    # registerPage.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


# Functions
# def is_logged_in():
#     return os.path.exists(SESSION_FILE)
#
# def set_logged_in():
#     with open(SESSION_FILE, 'w') as f:
#         f.write('logged_in')
# def set_logged_out():
#     if os.path.exists(SESSION_FILE):
#         os.remove(SESSION_FILE)
# # This temporary messages I have to change it in such a way that I can use it whenever I want for whatever variable
# def temporarymessages(message, duration):
#     text = label1.text()
#     style = label1.styleSheet()
#     label1.setText(message)
#     label1.setStyleSheet("""
#         QLabel {
#             background: transparent;
#             qproperty-alignment: 'AlignCenter';
#             font-family: Arial;
#             font-weight: bold;
#             font-size: 20px;
#             color: red;
#         }
#     """)
#
#     QTimer.singleShot(duration, lambda: (label1.setText(text), label1.setStyleSheet(style)))
# def forRegisterButtonfun():
#     page1.hide()
#     page3.show()
# forRegisterButton.clicked.connect(forRegisterButtonfun)
# def onPushButton1():
#     page2.hide()
#     page1.show()
# ReturnButton.clicked.connect(onPushButton1)
# def regPushButton():
#     res = collection_1.find_one({"Name": registerAcc.text()})
#     if registerAcc.text() != "":
#         if res is None:
#             user = {
#                 "Name": registerAcc.text(),
#                 "Password": registerPass.text(),
#             }
#             result = collection_1.insert_one(user)
#             page3.hide()
#             page1.show()
#             temporarymessages("Please enter the Registered Data here: ", 10000)
#         else:
#             registerLabel.setText("The username is Already Taken")
#     else:
#         registerLabel.setText("Enter a valid text!")
# registerSubmit.clicked.connect(regPushButton)
#
# def forlogoutButton():
#     set_logged_out()
# def onPushButton():
#     name = name_.text().title()
#     password = password_.text()
#     if name != "":
#         result = collection_1.find_one({"Name": name, "Password": password})
#         if result != None:
#             set_logged_in()
#             label2.setText(f" Hare Krishna! Welcome {name} to Sadhana App!")
#             page1.hide()
#             page2.show()
#         else:
#             temporarymessages("Please Register to the App!", 2000)
#     else:
#         temporarymessages("Please Enter a valid Text!", 2000)
#
# submit.clicked.connect(onPushButton)
# name_.returnPressed.connect(onPushButton)
