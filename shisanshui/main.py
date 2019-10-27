import os
import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from login_pane import LoginPane
from shouye_pane import shouyePane
from register_pane import RegisterPane
from room_pane import RoomPane
from rank_pane import RankPane
from history_pane import HistoryPane
from bangding_pane import  BangDingPane
from game_ready_pane import GameReadyPane
from game_open_pane import GameOpenPane
from PyQt5.Qt import *
from s1 import register,login,regiseterAndBind
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app=QApplication(sys.argv)
    shouye_pane = shouyePane()
    register_pane=RegisterPane()
    login_pane=LoginPane()
    room_pane=RoomPane()
    rank_pane=RankPane()
    history_pane=HistoryPane()
    bangding_pane=BangDingPane()
    game_ready_pane=GameReadyPane()
    game_open_pane=GameOpenPane()
    token=''
    user_id=''
    account=''
    password=''

    #创建控件
    def show_shouye_pane_1():
        print("登入到首页")
        shouye_pane.show()
        login_pane.hide()
    def show_shouye_pane_2():
        print("注册到首页")
        shouye_pane.show()
        room_pane.hide()
    def show_shouye_pane_3():
        print("房间到首页")
        shouye_pane.show()
        room_pane.hide()
    def show_login_pane_1():
        print("首页到登入")
        login_pane.show()
        shouye_pane.hide()
    def show_bangding_pane(a,p):
        global account,password
        account=a
        password=p
        print("注册到绑定")
        bangding_pane.show()
        register_pane.hide()

    def show_login_pane_2(jw_a,jw_p):
        pid=regiseterAndBind(account,password,jw_a,jw_p)
        if pid=='0':
            print("绑定到登入")
            login_pane.show()
            bangding_pane.hide()
        else:
            msg_box = QtWidgets.QMessageBox
            msg_box.question(bangding_pane, '温馨提醒', '绑定的教务处帐号或密码错误', msg_box.Yes | msg_box.Yes, msg_box.No)
            #QMessageBox.about(,"消息框标题", "这是关于软件的说明", QMessageBox.Yes | QMessageBox.No)
            print("学生号或密码错误")
    def show_register_pane_2():
        print("绑定到注册")
        register_pane.show()
        bangding_pane.hide()

    def show_register_pane_1():
        print("首页到注册")
        register_pane.show()
        shouye_pane.hide()
    def show_room_pane(a,p):
        global pid, token,user_id
        try:
            pid, token,user_id = login(a,p)
        except ValueError:
            pid = login(a,p)
        print(pid)
        if pid=='0':
            print("登入到房间")
            room_pane.show()
            login_pane.hide()
        else:
            msg_box = QtWidgets.QMessageBox
            msg_box.question(login_pane, '温馨提醒', '账号或密码错误', msg_box.Yes | msg_box.Yes, msg_box.No)
    def show_rank_pane():
        print("房间到排行榜")
        rank_pane.show()
        room_pane.hide()
    def show_nextrank_pane():

        rank_pane.nextpage()
        rank_pane.show()
    def show_previewrank_pane():

        rank_pane.previewpage()
        rank_pane.show()

    def show_history_pane():
        history_pane.history(token,user_id)
        history_pane.show()
        room_pane.hide()

    def show_nexthistory_pane():

        history_pane.nexthistory(token,user_id)
        history_pane.show()
    def show_previewhistory_pane():

        history_pane.previewhistory(token,user_id)
        history_pane.show()

    def rank_exit():
        room_pane.show()
        rank_pane.hide()
    def history_exit():
        room_pane.show()
        history_pane.hide()

    def search_id():
        history_pane.search_id(token)
        history_pane.show()

    def game_open():
        room_pane.hide()
        game_ready_pane.show()

    def game_exit():
        room_pane.show()
        game_ready_pane.hide()
    def game_ready():
        game_open_pane.game_open(token)
        game_open_pane.show()
        game_ready_pane.hide()
    def game_play():
        game_open_pane.play_game(token)
        game_open_pane.show()
    def game_jiesuan():
        game_open_pane.game_jiesuan(token)
        game_open_pane.show()
    def open_game_exit():
        room_pane.show()
        game_open_pane.hide()


    login_pane.show_login_exit_signal.connect(show_shouye_pane_1)
    login_pane.show_room_signal.connect(show_room_pane)
    register_pane.show_register_exit_signal.connect(show_shouye_pane_2)
    register_pane.show_login_signal.connect(show_bangding_pane)
    bangding_pane.bangding_signal.connect(show_login_pane_2)
    bangding_pane.bd_exit_signal.connect(show_register_pane_2)
    shouye_pane.show_login_signal_1.connect(show_login_pane_1)
    shouye_pane.show_register_signal_1.connect(show_register_pane_1)
    room_pane.show_room_exit_signal.connect(show_shouye_pane_3)
    room_pane.show_rank_signal.connect(show_rank_pane)
    rank_pane.show_nextrank_exit_signal.connect(show_nextrank_pane)
    rank_pane.show_previewrank_exit_signal.connect(show_previewrank_pane)
    rank_pane.rank_exit_signal.connect(rank_exit)
    room_pane.show_history_signal.connect(show_history_pane)
    history_pane.show_nexthistory_exit_signal.connect(show_nexthistory_pane)
    history_pane.show_uppagehistory_exit_signal.connect(show_previewhistory_pane)
    history_pane.history_exit_signal.connect(history_exit)
    history_pane.show_search_exit_signal.connect(search_id)

    room_pane.show_gmae_signal.connect(game_open)
    game_ready_pane.show_game_exit_signal.connect(game_exit)
    game_ready_pane.show_ready_signal.connect(game_ready)
    game_open_pane.play_game_signal.connect(game_play)
    game_open_pane.jiesuan_game_signal.connect(game_jiesuan)
    game_open_pane.open_game_exit_signal.connect(open_game_exit)


    shouye_pane.show()
    sys.exit(app.exec_())
