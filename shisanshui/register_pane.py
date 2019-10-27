from PyQt5.Qt import *
from register import Ui_Form

class RegisterPane(QWidget,Ui_Form):
    show_register_exit_signal=pyqtSignal()
    show_login_signal = pyqtSignal(str,str)

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.setWindowTitle('欢乐十三水')
        self.setWindowIcon(QIcon('./1.png'))
    def shouye_show(self):
        print("注册界面返回首页")
        self.show_register_exit_signal.emit()
    def login_show(self):
        print("注册界面到登录界面")
        account_txt = self.acount_le.text()
        password_txt = self.password_le.text()
        self.show_login_signal.emit(account_txt,password_txt)
    def enable_register(self):
        #print("判断")
        account_txt=self.acount_le.text()
        password_txt=self.password_le.text()
        password_txt2=self.count_le_3.text()
        if len(account_txt)>0 and len(password_txt)>0 and len(password_txt2)>0 and password_txt==password_txt2:
            self.login_btn.setEnabled(True)
        else:
            self.login_btn.setEnabled(False)
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=RegisterPane()#创建控件
    window.show()
    sys.exit(app.exec_())
