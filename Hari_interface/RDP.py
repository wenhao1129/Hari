#coding=UTF-8
import sys
from PyQt5.Qt import QThread,QMutex,pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI.Ginger import *
import time
import common.stop_button as stop_button
import common.total_time as total_time
import data_local.count_testresult as count_testresult
import Hari_interface.RDP_log as RDP_log
from selenium import webdriver
import configparser
config = configparser.ConfigParser()
config.read("../config/config.ini", encoding='UTF-8')
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

    def rdp_action(self):
        robot_sn = self.lineEdit_RobotSN.text().upper()
        detail_SN = self.lineEdit_detail_SN.text()
        IMEI = self.lineEdit_IMEI.text()
        RDP_log.TestMyLog.print_log(self, robot_sn, detail_SN, IMEI)
        testresult = 'PASS'

        '''''
        stop_button.MyWin.onPushButtonClick_stop(self)
        total_time.MyWin.Total_Test_time(self)
        testStatusText = 'PASS'        
        self.lineEdit_teststatus.setText(testStatusText)
        self.lineEdit_teststatus.setStyleSheet("background-color:green")
        count_testresult.MyWin.sum_testreslut(self,testresult)
        '''''

        return testresult


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

