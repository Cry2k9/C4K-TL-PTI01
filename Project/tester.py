from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox, QWidget
from PyQt5 import uic
import re
import sys

email_pattern = re.compile(r"[^@]+@[^@]+\.[^@.]+")

class Login(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/login.ui", self)
        
        self.pbLogin.clicked.connect(self.check_login)
        self.pbRegister.clicked.connect(self.showRegister)
      
    def check_login(self):
        email = self.txtEmail.text()
        password = self.txtPassword.text()
        
        if not email: 
            msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
            msg_box.exec()
            return
        if not password:
            msg_box.setText("Vui lòng nhập mật khẩu!")
            msg_box.exec()
            return
        if not self.checkBox.isChecked():
            msg_box.setText("Vui lòng đồng ý để tiếp tục đăng nhập vào Sweet Love!")
            msg_box.exec()
            return
        
        if email == "admin@example.com" and password == "admin":
            self.close()
            # mainPage.show()  
        else:
            msg_box.setText("Email hoặc mật khẩu không đúng!")
            msg_box.exec()
            
    def showRegister(self):
        registerPage.show()
        self.close()


class Register(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/register.ui", self)
        self.name = ""
        
        self.pbRegister.clicked.connect(self.Register)
        self.pbLogin.clicked.connect(self.showLoginPage)
    
    def Register(self):
        self.name = self.txtFullName.text()
        email = self.txtEmail.text()
        password = self.txtPassword.text()
        
        if not self.name:
            msg_box.setText("Vui lòng nhập tên!")
            msg_box.exec()
            return
        if not email: 
            msg_box.setText("Vui lòng nhập email hoặc số điện thoại!")
            msg_box.exec()
            return
        if not email_pattern.match(email):
            msg_box.setText("Email không hợp lệ!")
            msg_box.exec()
        if not password:
            msg_box.setText("Vui lòng nhập mật khẩu!")
            msg_box.exec()
            return
        if not len(password) > 8:
            msg_box.setText("Mật khẩu không hợp lệ!")
            msg_box.exec()
        if not self.checkBox.isChecked():
            msg_box.setText("Vui lòng đọc và đồng ý các điều khoản của Sweet Love!")
            msg_box.exec()
            return
        
        # mainPage.lbUsername.setText(self.name)
        # mainPage.show()
        self.close()
    
    def showLoginPage(self):
        loginPage.show()
        self.close()

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)

    loginPage = Login()
    loginPage.show()
    registerPage = Register()

    msg_box = QMessageBox()
    msg_box.setWindowTitle("Error!")
    msg_box.setIcon(QMessageBox.Icon.Warning)
    msg_box.setStyleSheet("background-color: #F8F2EC; color: #356a9c")

    app.exec()