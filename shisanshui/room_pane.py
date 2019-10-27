from PyQt5.Qt import *
from room import Ui_Form

class RoomPane(QWidget,Ui_Form):
    show_room_exit_signal=pyqtSignal()
    show_history_signal=pyqtSignal()
    show_rank_signal = pyqtSignal()
    show_gmae_signal= pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.setWindowTitle('欢乐十三水')
        self.setWindowIcon(QIcon('./1.png'))
    def room_exit(self):
        self.show_room_exit_signal.emit()
    def history(self):
        self.show_history_signal.emit()
    def rank(self):
        self.show_rank_signal.emit()
    def game(self):
        self.show_gmae_signal.emit()
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=RoomPane()#创建控件
    window.show()
    sys.exit(app.exec_())