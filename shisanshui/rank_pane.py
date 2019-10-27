from PyQt5.Qt import *
from rank import Ui_Form
from s1 import rank
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
class RankPane(QWidget,Ui_Form):
    show_previewrank_exit_signal=pyqtSignal()
    show_nextrank_exit_signal= pyqtSignal()
    rank_exit_signal=pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.setWindowTitle('欢乐十三水')
        self.setWindowIcon(QIcon('./1.png'))
        self.page = 1
        self.res = rank()
        self.long = len(self.res) / 5
        quece = (self.page - 1) * 5 + 1
        self.label_1_1.setText('No.{}'.format(quece))
        self.label_2_1.setText('No.{}'.format(quece + 1))
        self.label_3_1.setText('No.{}'.format(quece + 2))
        self.label_4_1.setText('No.{}'.format(quece + 3))
        self.label_5_1.setText('No.{}'.format(quece + 4))
        self.label_1_2.setText(str(self.res[(self.page - 1) * 5]['name']))
        self.label_2_2.setText(str(self.res[(self.page - 1) * 5 + 1]['name']))
        self.label_3_2.setText(str(self.res[(self.page - 1) * 5 + 2]['name']))
        self.label_4_2.setText(str(self.res[(self.page - 1) * 5 + 3]['name']))
        self.label_5_2.setText(str(self.res[(self.page - 1) * 5 + 4]['name']))
        self.label_1_3.setText(str(self.res[(self.page - 1) * 5]['score']))
        self.label_2_3.setText(str(self.res[(self.page - 1) * 5 + 1]['score']))
        self.label_3_3.setText(str(self.res[(self.page - 1) * 5 + 2]['score']))
        self.label_4_3.setText(str(self.res[(self.page - 1) * 5 + 3]['score']))
        self.label_5_3.setText(str(self.res[(self.page - 1) * 5 + 4]['score']))

    def preview(self):
        self.show_previewrank_exit_signal.emit()


    def next(self):
        self.show_nextrank_exit_signal.emit()

    def previewpage(self):
        if self.page >= 2:
            self.page = self.page - 1
            self.long = len(self.res) / 5


            quece = (self.page - 1) * 5 + 1
            self.label_1_1.setText('No.{}'.format(quece))
            self.label_2_1.setText('No.{}'.format(quece + 1))
            self.label_3_1.setText('No.{}'.format(quece + 2))
            self.label_4_1.setText('No.{}'.format(quece + 3))
            self.label_5_1.setText('No.{}'.format(quece + 4))
            self.label_1_2.setText(str(self.res[(self.page - 1) * 5]['name']))
            self.label_2_2.setText(str(self.res[(self.page - 1) * 5 + 1]['name']))
            self.label_3_2.setText(str(self.res[(self.page - 1) * 5 + 2]['name']))
            self.label_4_2.setText(str(self.res[(self.page - 1) * 5 + 3]['name']))
            self.label_5_2.setText(str(self.res[(self.page - 1) * 5 + 4]['name']))
            self.label_1_3.setText(str(self.res[(self.page - 1) * 5]['score']))
            self.label_2_3.setText(str(self.res[(self.page - 1) * 5 + 1]['score']))
            self.label_3_3.setText(str(self.res[(self.page - 1) * 5 + 2]['score']))
            self.label_4_3.setText(str(self.res[(self.page - 1) * 5 + 3]['score']))
            self.label_5_3.setText(str(self.res[(self.page - 1) * 5 + 4]['score']))
        else:
            msg_box = QtWidgets.QMessageBox
            msg_box.question(self, '温馨提醒', '当前已是第一页', msg_box.Yes | msg_box.Yes, msg_box.No)

    def nextpage(self):
        if self.page < self.long-1:
            self.page=self.page+1
            quece = (self.page - 1) * 5 + 1
            self.label_1_1.setText('No.{}'.format(quece))
            self.label_2_1.setText('No.{}'.format(quece + 1))
            self.label_3_1.setText('No.{}'.format(quece + 2))
            self.label_4_1.setText('No.{}'.format(quece + 3))
            self.label_5_1.setText('No.{}'.format(quece + 4))
            self.label_1_2.setText(str(self.res[(self.page - 1) * 5]['name']))
            self.label_2_2.setText(str(self.res[(self.page - 1) * 5 + 1]['name']))
            self.label_3_2.setText(str(self.res[(self.page - 1) * 5 + 2]['name']))
            self.label_4_2.setText(str(self.res[(self.page - 1) * 5 + 3]['name']))
            self.label_5_2.setText(str(self.res[(self.page - 1) * 5 + 4]['name']))
            self.label_1_3.setText(str(self.res[(self.page - 1) * 5]['score']))
            self.label_2_3.setText(str(self.res[(self.page - 1) * 5 + 1]['score']))
            self.label_3_3.setText(str(self.res[(self.page - 1) * 5 + 2]['score']))
            self.label_4_3.setText(str(self.res[(self.page - 1) * 5 + 3]['score']))
            self.label_5_3.setText(str(self.res[(self.page - 1) * 5 + 4]['score']))
        else:
            msg_box = QtWidgets.QMessageBox
            msg_box.question(self, '温馨提醒', '当前已是最后一页', msg_box.Yes | msg_box.Yes, msg_box.No)
    def exit(self):
        self.rank_exit_signal.emit()
if __name__ == '__main__':
    import sys
    app=QApplication(sys.argv)
    window=RankPane()#创建控件
    window.show()
    sys.exit(app.exec_())