from PyQt5.Qt import *
from history import Ui_Form
from s1 import history,gameend
from PyQt5 import QtWidgets

class HistoryPane(QWidget, Ui_Form):
    show_search_exit_signal = pyqtSignal()
    show_nexthistory_exit_signal = pyqtSignal()
    show_uppagehistory_exit_signal = pyqtSignal()
    history_exit_signal=pyqtSignal()
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        self.setWindowTitle('欢乐十三水')
        self.setWindowIcon(QIcon('./1.png'))
    def history(self,token,user_id):
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(True)
        self.label_7.setText('战局id：')
        self.label_16.setText('战局id：')
        self.label_17.setText('战局id：')
        self.label_21.setText('战局id：')
        self.page = 1
        self.res = history(token,user_id)
        self.res = self.res['data']
        self.long = len(self.res) / 4
        self.id_label_1.setText(str(self.res[(self.page - 1)*4]['id']))
        self.score_label_1.setText(str(self.res[(self.page - 1)*4]['score']))
        self.card_label_1.setText(str(self.res[(self.page - 1)*4]['card']))
        self.id_label_2.setText(str(self.res[(self.page - 1)*4+1]['id']))
        self.score_label_2.setText(str(self.res[(self.page - 1)*4+1]['score']))
        self.card_label_2.setText(str(self.res[(self.page - 1)*4+1]['card']))
        self.id_label_3.setText(str(self.res[(self.page - 1)*4+2]['id']))
        self.score_label_3.setText(str(self.res[(self.page - 1)*4+2]['score']))
        self.card_label_3.setText(str(self.res[(self.page - 1)*4+2]['card']))
        self.id_label_4.setText(str(self.res[(self.page - 1)*4+3]['id']))
        self.score_label_4.setText(str(self.res[(self.page - 1)*4+3]['score']))
        self.card_label_4.setText(str(self.res[(self.page - 1)*4+3]['card']))
    def previewhistory(self,token,user_id):
        if self.page >= 2:
            self.page = self.page - 1
            self.long = len(self.res) / 4
            self.id_label_1.setText(str(self.res[(self.page - 1) * 4]['id']))
            self.score_label_1.setText(str(self.res[(self.page - 1) * 4]['score']))
            self.card_label_1.setText(str(self.res[(self.page - 1) * 4]['card']))
            self.id_label_2.setText(str(self.res[(self.page - 1) * 4 + 1]['id']))
            self.score_label_2.setText(str(self.res[(self.page - 1) * 4 + 1]['score']))
            self.card_label_2.setText(str(self.res[(self.page - 1) * 4 + 1]['card']))
            self.id_label_3.setText(str(self.res[(self.page - 1) * 4 + 2]['id']))
            self.score_label_3.setText(str(self.res[(self.page - 1) * 4 + 2]['score']))
            self.card_label_3.setText(str(self.res[(self.page - 1) * 4 + 2]['card']))
            self.id_label_4.setText(str(self.res[(self.page - 1) * 4 + 3]['id']))
            self.score_label_4.setText(str(self.res[(self.page - 1) * 4 + 3]['score']))
            self.card_label_4.setText(str(self.res[(self.page - 1) * 4 + 3]['card']))
        else:
            msg_box = QtWidgets.QMessageBox
            msg_box.question(self, '温馨提醒', '当前已是第一页', msg_box.Yes | msg_box.Yes, msg_box.No)
    def nexthistory(self,token,user_id):
        if self.page<self.long-1:
            self.page = self.page +1
            self.long = len(self.res) / 4
            self.id_label_1.setText(str(self.res[(self.page - 1) * 4]['id']))
            self.score_label_1.setText(str(self.res[(self.page - 1) * 4]['score']))
            self.card_label_1.setText(str(self.res[(self.page - 1) * 4]['card']))
            self.id_label_2.setText(str(self.res[(self.page - 1) * 4 + 1]['id']))
            self.score_label_2.setText(str(self.res[(self.page - 1) * 4 + 1]['score']))
            self.card_label_2.setText(str(self.res[(self.page - 1) * 4 + 1]['card']))
            self.id_label_3.setText(str(self.res[(self.page - 1) * 4 + 2]['id']))
            self.score_label_3.setText(str(self.res[(self.page - 1) * 4 + 2]['score']))
            self.card_label_3.setText(str(self.res[(self.page - 1) * 4 + 2]['card']))
            self.id_label_4.setText(str(self.res[(self.page - 1) * 4 + 3]['id']))
            self.score_label_4.setText(str(self.res[(self.page - 1) * 4 + 3]['score']))
            self.card_label_4.setText(str(self.res[(self.page - 1) * 4 + 3]['card']))
        else:
            msg_box = QtWidgets.QMessageBox
            msg_box.question(self, '温馨提醒', '当前已是最后一页', msg_box.Yes | msg_box.Yes, msg_box.No)
    def search_id(self,token):
        id=self.search_le.text()
        print(id)
        self.label_7.setText('Name:')
        self.label_16.setText('Name:')
        self.label_17.setText('Name:')
        self.label_21.setText('Name:')
        self.res=gameend(token,id)
        print(self.res['status'])
        if self.res['status'] == 0:
            self.res = self.res['data']
            self.res = self.res['detail']
            self.id_label_1.setText(str(self.res[0]['name']))
            self.score_label_1.setText(str(self.res[0]['score']))
            self.card_label_1.setText(str(self.res[0]['card']))
            self.id_label_2.setText(str(self.res[1]['name']))
            self.score_label_2.setText(str(self.res[1]['score']))
            self.card_label_2.setText(str(self.res[1]['card']))
            self.id_label_3.setText(str(self.res[2]['name']))
            self.score_label_3.setText(str(self.res[2]['score']))
            self.card_label_3.setText(str(self.res[2]['card']))
            self.id_label_4.setText(str(self.res[3]['name']))
            self.score_label_4.setText(str(self.res[3]['score']))
            self.card_label_4.setText(str(self.res[3]['card']))
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(False)



    def search(self):
        search_id=self.search_le.text()

        self.show_search_exit_signal.emit()
    def uppage(self):
        self.show_uppagehistory_exit_signal.emit()
    def nextpage(self):
        self.show_nexthistory_exit_signal.emit()

    def exit(self):
        self.history_exit_signal.emit()



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = HistoryPane()  # 创建控件
    window.show()
    sys.exit(app.exec_())