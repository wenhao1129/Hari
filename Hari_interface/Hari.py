#coding=UTF-8
import sys
from PyQt5.Qt import QThread,QMutex,pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI.Ginger import *
import time
import common.stop_button as stop_button
import common.total_time as total_time
import data_local.count_testresult as count_testresult
import data_local.save_csv as save_csv
from selenium import webdriver
import Hari_interface.BOSS as BOSS
import Hari_interface.RDP as RDP
import Hari_interface.ROC as ROC
import configparser
config = configparser.ConfigParser()
config.read("../config/config.ini", encoding="utf-8-sig")
#edge_browser = webdriver.Edge()


#建立新的线程,用来监控外部程序运行,并且会生成tmp.txt
class TextBrowser_thred(QThread):
    signal = pyqtSignal(str)

    def __init__(self, TextBrowser_win, data):
        self.data = data
        self.TextBrowser_win = TextBrowser_win
        super().__init__()

    def run(self):
        while self.data.poll is not None:
            template = self.data.stdout.readline()
            outputs = bytes.decode(template)
            self.signal.emit(str(outputs))
            if outputs == '':
               break


class MyWin(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MyWin, self).__init__()
        self.setupUi(self)

    def hari_setup_action(self):
        boss_result = BOSS.MyWin.boss_action(self)
        if boss_result == 'PASS':
            time.sleep(3)
            roc_result = ROC.MyWin.roc_action(self)
            if roc_result == 'PASS':
                time.sleep(3)
                rdp_result = RDP.MyWin.rdp_action(self)
                if rdp_result == 'PASS':
                    time.sleep(3)
                else:
                    pass
            else:
                pass
        else:
            pass
        stop_button.MyWin.onPushButtonClick_stop(self)
        total_time.MyWin.Total_Test_time(self)
        testStatusText = 'PASS'
        testresult = 'PASS'
        errorcode = 'Hari_st_PASS'
        self.lineEdit_teststatus.setText(testStatusText)
        self.lineEdit_teststatus.setStyleSheet("background-color:green")
        count_testresult.MyWin.sum_testreslut(self, testresult)
        save_csv.MyWin.local_csv(self, errorcode, testresult)


    #定义信号和槽,调用时触发
    def start_button_click(self):
        self.TextBrowser_show = TextBrowser_thred(self.textBrowser, self.data)
        self.TextBrowser_show.signal.connect(self.TextBrowser_show_text)
        self.TextBrowser_show.start()

    #定义槽函数,接受外部程序运行结果,生成tmp.txt
    def TextBrowser_show_text(self, msg):
        self.textBrowser.append(msg)
        try:
            f = open('tmp.txt', 'a', encoding='utf-8')
            f.write(msg)
            f.close()
        except Exception as e:
            print(e)

