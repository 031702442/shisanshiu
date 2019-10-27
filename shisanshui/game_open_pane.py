from PyQt5.Qt import *
from game_open import Ui_Form
import re
from s1 import gameopen,PlayGame,getjson,getcard,gameend,submit

class GameOpenPane(QWidget,Ui_Form):
    play_game_signal=pyqtSignal()
    jiesuan_game_signal=pyqtSignal()
    open_game_exit_signal = pyqtSignal()

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setAttribute(Qt.WA_StyledBackground,True)
        self.setupUi(self)
        self.setWindowTitle('欢乐十三水')
        self.setWindowIcon(QIcon('./1.png'))

    def play(self):
        self.play_game_signal.emit()
    def jiesuan(self):
        self.jiesuan_game_signal.emit()
    def open_game_exit(self):
        self.open_game_exit_signal.emit()
    def game_open(self,token):
        self.data=gameopen(token)
        mycard = self.data[1].split(' ')
        mycard=str(mycard)
        self.textEdit.setText(mycard)
    def play_game(self,token):
        res=PlayGame(self.data,token)
        self.id =res['id']
        h1=res['card'][0]
        h2=res['card'][1]
        h3=res['card'][2]
        self.textEdit.setText('前墩：'+h1+'\n'+'中墩：'+h2+'\n'+'后墩：'+h3+'\n')
    def game_jiesuan(self,token):
        res=gameend(token,self.id)
        pid=res['status']
        print(pid)
        if pid==0:
            res=res['data']
            res=res['detail']
            print(res)
            print(res[1]['name'])
            print(res[2]['score'])
            print(res[3]['card'])
            self.textEdit.setText('玩家一:'+'\n'+'Name:'+res[0]['name']+'      Score:'+str(res[0]['score'])+'\n'+'Card:'+str(res[0]['card'])+'\n'+'玩家二:'+'\n'+'Name:'+res[1]['name']+'      Score:'+str(res[1]['score'])+'\n'+'Card:'+str(res[1]['card'])+'\n'+'玩家三:'+'\n'+'Name:'+res[2]['name']+'      Score:'+str(res[2]['score'])+'\n'+'Card:'+str(res[2]['card'])+'\n'+'玩家四:'+'\n'+'Name:'+res[3]['name']+'      Score:'+str(res[3]['score'])+'\n'+'Card:'+str(res[3]['card']))
        else:
            self.textEdit.setText("战局尚未结束，请稍等一会再结算！")






