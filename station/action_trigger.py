#coding=UTF-8
from PyQt5.QtWidgets import QMainWindow
import station.choose_station as choose
import common.sfis as sfis
import common.start_button as start_button
import common.stop_button as stop_button
from UI.Ginger import *


class MyWin(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MyWin, self).__init__()
        self.setupUi(self)

    def action_connect(self):
        #绑定按钮触发机种选择
        self.actionGinger1_0.triggered.connect(lambda: choose.MyWin.onChooseModel_1_0(self))
        self.actionGinger1_1.triggered.connect(lambda: choose.MyWin.onChooseModel_1_1(self))
        self.actionGinger1_1_1.triggered.connect(lambda: choose.MyWin.onChooseModel_1_1_1(self))
        self.actionGinger1_1_2.triggered.connect(lambda: choose.MyWin.onChooseModel_1_1_2(self))
        #self.actionGinger1_1_0_Plus.triggered.connect(lambda: choose.MyWin.onChooseModel_1_1_Plus(self))
        #绑定按钮触发站位选择
        #self.action_dance.triggered.connect(lambda: self.onChoosedance_wireless(self))
        self.actionUpgrade.triggered.connect(lambda: choose.MyWin.onChoose_trash_back(self))
        self.actionOTA.triggered.connect(lambda: choose.MyWin.onChooseCCUOTA(self))
        self.actionBOSS_setup.triggered.connect(lambda:choose.MyWin.onChooseBOSS_setup(self))
        self.actionRDP_setup.triggered.connect(lambda: choose.MyWin.onChooseRDP_setup(self))
        self.actionROC_setup.triggered.connect(lambda: choose.MyWin.onChooseROC_setup(self))
        self.actionHari_setup.triggered.connect(lambda: choose.MyWin.onChooseHari_setup(self))
        self.actionHari.triggered.connect(lambda: choose.MyWin.onChooseHari(self))
        #开始按钮触发选择
        self.pushbutton_SFIS_ON.clicked.connect(lambda:sfis.MyWin.onPushButton_SFIS_ON(self))
        self.pushButton_start.clicked.connect(lambda:start_button.MyWin.onPushButtonClick_start(self))
        self.pushButton_stop.clicked.connect(lambda:stop_button.MyWin.onPushButtonClick_stop(self))
        #self.pushButton_stop.clicked.connect(self.saveLogfile)
