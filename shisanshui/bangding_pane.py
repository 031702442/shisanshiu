from PyQt5.Qt import *
from bangding import Ui_Form

class BangDingPane(QWidget,Ui_Form):
    bd_exit_signal=pyqtSignal()
    bangding_signal=pyqtSignal(str,str)
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowTitle('欢乐十三水')
        self.setWindowIcon(QIcon('./1.png'))
    def bd_exit(self):
        self.bd_exit_signal.emit()
    def bangding(self):
        jw_account = self.jw_acount_le.text()
        jw_password = self.jw_pwd_le.text()
        self.bangding_signal.emit(jw_account,jw_password)



