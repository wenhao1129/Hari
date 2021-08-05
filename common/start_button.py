# coding=UTF-8
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import time
import station.station as station
from UI.Ginger import *


class MyWin(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MyWin, self).__init__()
        self.setupUi(self)

    # 开始按钮触发时间和运行所选站位程序
    def onPushButtonClick_start(self):
        self.lineEdit_stop_time.clear()
        self.lineEdit_test_time.clear()
        testStatusText = ''
        model_name = self.lineEdit_modelName.text()
        station_name = self.lineEdit_stationName.text()
        robot_SN = self.lineEdit_RobotSN.text().upper()
        sn = self.lineEdit_detail_SN
        tester_name = self.lineEdit_tester.text()
        if model_name == '' or station_name == '' or robot_SN == '' or sn == '' or tester_name == '':
            QMessageBox.information(None, '输入确认', '请确认正确输入', QMessageBox.Yes | QMessageBox.No)
        else:
            testStatusText = '测试中'
            self.lineEdit_teststatus.setText(testStatusText)
            self.lineEdit_teststatus.setStyleSheet("background-color:yellow")
            startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            self.lineEdit_start_time.setText(startTime)
            time.sleep(1)
            station.MyWin.onChooseStation(self)
