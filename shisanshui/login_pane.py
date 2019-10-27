from PyQt5.Qt import *
from login import Ui_Form

class LoginPane(QWidget,Ui_Form):
    show_login_exit_signal=pyqtSignal()
    show_room_signal=pyqtSignal(str,str)
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.setWindowTitle('欢乐十三水')
        self.setWindowIcon(QIcon('./1.png'))
    def login_exit(self):
        self.show_login_exit_signal.emit()
    def show_room(self):
        account_txt = self.acount_le.text()
        password_txt = self.password_le.text()
        self.show_room_signal.emit(account_txt,password_txt)
    def enable_login(self):
        account_txt = self.acount_le.text()
        password_txt = self.password_le.text()
        if len(account_txt) > 0 and len(password_txt) > 0:
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=LoginPane()#创建控件
    window.show()
    sys.exit(app.exec_())
