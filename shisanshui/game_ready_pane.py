from PyQt5.Qt import *
from game_ready import Ui_Form

class GameReadyPane(QWidget,Ui_Form):
    show_game_exit_signal=pyqtSignal()
    show_ready_signal = pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.setWindowTitle('欢乐十三水')
        self.setWindowIcon(QIcon('./1.png'))

    def game_exit(self):
        self.show_game_exit_signal.emit()
    def ready(self):
        self.show_ready_signal.emit()

