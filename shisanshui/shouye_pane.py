from PyQt5.Qt import *
from shouye import Ui_Form

class shouyePane(QWidget,Ui_Form):
    show_login_signal_1 = pyqtSignal()
    show_register_signal_1 = pyqtSignal()
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.setWindowTitle('欢乐十三水')
        self.setWindowIcon(QIcon('./1.png'))
    def register_show(self):
        self.show_register_signal_1.emit()
    def login_show(self):
        self.show_login_signal_1.emit()

if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=shouyePane()#创建控件
    window.show()
    sys.exit(app.exec_())
