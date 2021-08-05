#coding=UTF-8
from PyQt5.QtWidgets import QMainWindow,QMessageBox
from UI.Ginger import *


class MyWin(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MyWin, self).__init__()
        self.setupUi(self)

    #机种选择按钮
    def onChooseModel_1_0(self):
        self.lineEdit_modelName.setText("Ginger1.0.x")

    def onChooseModel_1_1(self):
        self.lineEdit_modelName.setText("Ginger1.1.0")

    def onChooseModel_1_1_1(self):
        self.lineEdit_modelName.setText("Ginger1.1.1")

    def onChooseModel_1_1_2(self):
        self.lineEdit_modelName.setText("Ginger1.1.2")

    def onChoose_trash_back(self):
        self.lineEdit_stationName.setText("回收")

    def onChooseBOSS_setup(self):
        self.lineEdit_stationName.setText("BOSS_setup")

    def onChooseRDP_setup(self):
        self.lineEdit_stationName.setText("RDP_setup")

    def onChooseROC_setup(self):
        self.lineEdit_stationName.setText("ROC_setup")

    def onChooseHari_setup(self):
        self.lineEdit_stationName.setText("Hari_setup")

    def onChooseHari(self):
        self.lineEdit_stationName.setText("Hari")

    def version(self):
        QMessageBox.information(None, '版本信息', '请参考README', QMessageBox.Ok)
