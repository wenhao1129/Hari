#coding=UTF-8
from PyQt5.QtWidgets import QMainWindow
import time
from UI.Ginger import *
#import Hari_interface.BOSS as BOSS
import Hari.BOSS as BOSS
#import Hari_interface.ROC as ROC
import Hari.ROC as ROC
import Hari_interface.RDP as RDP
#import Hari.RDP as RDP
import Hari_interface.Hari as Hari
#import Hari.Hari as Hari
#import Hari_interface.Hari_test as Hari_test
import Hari.Hari_test as Hari_test

class MyWin(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MyWin, self).__init__()
        self.setupUi(self)

    #选择站位,运行对应程序
    def onChooseStation(self):
        robotSN = self.lineEdit_RobotSN.text().upper()
        chooseStation = self.lineEdit_stationName.text()
        model_name = self.lineEdit_modelName.text()
        while chooseStation == '回收':
              #upgradeCCU.MyWin.upgradeCCU(self)
              time.sleep(1)
              break
        while chooseStation == 'BOSS_setup':
              BOSS.MyWin.boss_action(self)
              time.sleep(1)
              break
        while chooseStation == 'RDP_setup':
              RDP.MyWin.rdp_action(self)
              time.sleep(1)
              break
        while chooseStation == 'ROC_setup':
              ROC.MyWin.roc_action(self)
              time.sleep(1)
              break
        while chooseStation == 'Hari_setup':
              Hari.MyWin.hari_setup_action(self)
              time.sleep(1)
              break
        while chooseStation == 'Hari':
              Hari_test.MyWin.hari_test_action(self)
              time.sleep(1)
              break





