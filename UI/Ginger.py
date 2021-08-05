# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ginger.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(1695, 983)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image_logo/logo_data.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_base = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_base.setGeometry(QtCore.QRect(0, 0, 1691, 131))
        self.groupBox_base.setObjectName("groupBox_base")
        self.label = QtWidgets.QLabel(self.groupBox_base)
        self.label.setGeometry(QtCore.QRect(140, 40, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_base)
        self.label_2.setGeometry(QtCore.QRect(140, 80, 61, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit_modelName = QtWidgets.QLineEdit(self.groupBox_base)
        self.lineEdit_modelName.setGeometry(QtCore.QRect(220, 30, 151, 41))
        self.lineEdit_modelName.setObjectName("lineEdit_modelName")
        self.lineEdit_stationName = QtWidgets.QLineEdit(self.groupBox_base)
        self.lineEdit_stationName.setGeometry(QtCore.QRect(220, 80, 151, 41))
        self.lineEdit_stationName.setObjectName("lineEdit_stationName")
        self.label_3 = QtWidgets.QLabel(self.groupBox_base)
        self.label_3.setGeometry(QtCore.QRect(380, 40, 101, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_base)
        self.label_4.setGeometry(QtCore.QRect(380, 90, 101, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_tester = QtWidgets.QLineEdit(self.groupBox_base)
        self.lineEdit_tester.setGeometry(QtCore.QRect(490, 30, 121, 41))
        self.lineEdit_tester.setObjectName("lineEdit_tester")
        self.lineEdit_RobotSN = QtWidgets.QLineEdit(self.groupBox_base)
        self.lineEdit_RobotSN.setGeometry(QtCore.QRect(490, 80, 121, 41))
        self.lineEdit_RobotSN.setObjectName("lineEdit_RobotSN")
        self.label_11 = QtWidgets.QLabel(self.groupBox_base)
        self.label_11.setGeometry(QtCore.QRect(1250, 40, 111, 51))
        self.label_11.setObjectName("label_11")
        self.lineEdit_teststatus = QtWidgets.QLineEdit(self.groupBox_base)
        self.lineEdit_teststatus.setGeometry(QtCore.QRect(1370, 20, 191, 101))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lineEdit_teststatus.setFont(font)
        self.lineEdit_teststatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_teststatus.setObjectName("lineEdit_teststatus")
        self.label_14 = QtWidgets.QLabel(self.groupBox_base)
        self.label_14.setGeometry(QtCore.QRect(1020, 80, 41, 41))
        self.label_14.setObjectName("label_14")
        self.lineEdit_MO = QtWidgets.QLineEdit(self.groupBox_base)
        self.lineEdit_MO.setGeometry(QtCore.QRect(1060, 80, 181, 41))
        self.lineEdit_MO.setText("")
        self.lineEdit_MO.setObjectName("lineEdit_MO")
        self.pushButton_start = QtWidgets.QPushButton(self.groupBox_base)
        self.pushButton_start.setGeometry(QtCore.QRect(10, 30, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop = QtWidgets.QPushButton(self.groupBox_base)
        self.pushButton_stop.setGeometry(QtCore.QRect(1570, 20, 121, 101))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.pushbutton_SFIS_ON = QtWidgets.QPushButton(self.groupBox_base)
        self.pushbutton_SFIS_ON.setGeometry(QtCore.QRect(1020, 30, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushbutton_SFIS_ON.setFont(font)
        self.pushbutton_SFIS_ON.setObjectName("pushbutton_SFIS_ON")
        self.lineEdit_scan_barcode = QtWidgets.QLineEdit(self.groupBox_base)
        self.lineEdit_scan_barcode.setGeometry(QtCore.QRect(1140, 30, 101, 41))
        self.lineEdit_scan_barcode.setObjectName("lineEdit_scan_barcode")
        self.label_16 = QtWidgets.QLabel(self.groupBox_base)
        self.label_16.setGeometry(QtCore.QRect(630, 80, 41, 41))
        self.label_16.setObjectName("label_16")
        self.lineEdit_detail_SN = QtWidgets.QLineEdit(self.groupBox_base)
        self.lineEdit_detail_SN.setGeometry(QtCore.QRect(680, 80, 331, 41))
        self.lineEdit_detail_SN.setText("")
        self.lineEdit_detail_SN.setObjectName("lineEdit_detail_SN")
        self.label_15 = QtWidgets.QLabel(self.groupBox_base)
        self.label_15.setGeometry(QtCore.QRect(620, 30, 61, 41))
        self.label_15.setObjectName("label_15")
        self.lineEdit_IMEI = QtWidgets.QLineEdit(self.groupBox_base)
        self.lineEdit_IMEI.setGeometry(QtCore.QRect(680, 30, 331, 41))
        self.lineEdit_IMEI.setText("")
        self.lineEdit_IMEI.setObjectName("lineEdit_IMEI")
        self.groupBox_information = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_information.setGeometry(QtCore.QRect(10, 130, 1381, 901))
        self.groupBox_information.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_information.setObjectName("groupBox_information")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_information)
        self.textBrowser.setGeometry(QtCore.QRect(10, 30, 1371, 581))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_testtime = QtWidgets.QGroupBox(self.groupBox_information)
        self.groupBox_testtime.setGeometry(QtCore.QRect(650, 620, 421, 151))
        self.groupBox_testtime.setObjectName("groupBox_testtime")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_testtime)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_testtime)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_start_time = QtWidgets.QLineEdit(self.groupBox_testtime)
        self.lineEdit_start_time.setObjectName("lineEdit_start_time")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_start_time)
        self.lineEdit_stop_time = QtWidgets.QLineEdit(self.groupBox_testtime)
        self.lineEdit_stop_time.setObjectName("lineEdit_stop_time")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_stop_time)
        self.label_7 = QtWidgets.QLabel(self.groupBox_testtime)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_5 = QtWidgets.QLabel(self.groupBox_testtime)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_test_time = QtWidgets.QLineEdit(self.groupBox_testtime)
        self.lineEdit_test_time.setObjectName("lineEdit_test_time")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_test_time)
        self.groupBox_programversion = QtWidgets.QGroupBox(self.groupBox_information)
        self.groupBox_programversion.setGeometry(QtCore.QRect(10, 620, 401, 151))
        self.groupBox_programversion.setObjectName("groupBox_programversion")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_programversion)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.groupBox_programversion)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_programversion)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)
        self.groupBox_testresult = QtWidgets.QGroupBox(self.groupBox_information)
        self.groupBox_testresult.setGeometry(QtCore.QRect(420, 620, 221, 151))
        self.groupBox_testresult.setObjectName("groupBox_testresult")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_testresult)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_18 = QtWidgets.QLabel(self.groupBox_testresult)
        self.label_18.setObjectName("label_18")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.lineEdit_testresult_pass = QtWidgets.QLineEdit(self.groupBox_testresult)
        self.lineEdit_testresult_pass.setObjectName("lineEdit_testresult_pass")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_testresult_pass)
        self.label_19 = QtWidgets.QLabel(self.groupBox_testresult)
        self.label_19.setObjectName("label_19")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.lineEdit_testresult_fail = QtWidgets.QLineEdit(self.groupBox_testresult)
        self.lineEdit_testresult_fail.setObjectName("lineEdit_testresult_fail")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_testresult_fail)
        self.label_20 = QtWidgets.QLabel(self.groupBox_testresult)
        self.label_20.setObjectName("label_20")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.lineEdit_testresult_rate = QtWidgets.QLineEdit(self.groupBox_testresult)
        self.lineEdit_testresult_rate.setObjectName("lineEdit_testresult_rate")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_testresult_rate)
        self.label_9 = QtWidgets.QLabel(self.groupBox_information)
        self.label_9.setGeometry(QtCore.QRect(1070, 650, 311, 111))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../image_logo/cloudminds666.png"))
        self.label_9.setObjectName("label_9")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1400, 130, 291, 801))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../image_logo/Robot.png"))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1695, 37))
        self.menuBar.setObjectName("menuBar")
        self.Model = QtWidgets.QMenu(self.menuBar)
        self.Model.setObjectName("Model")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuCCU = QtWidgets.QMenu(self.menuBar)
        self.menuCCU.setObjectName("menuCCU")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")
        self.actionAuthor = QtWidgets.QAction(MainWindow)
        self.actionAuthor.setObjectName("actionAuthor")
        self.actionStart_Service = QtWidgets.QAction(MainWindow)
        self.actionStart_Service.setObjectName("actionStart_Service")
        self.actionStop_Service = QtWidgets.QAction(MainWindow)
        self.actionStop_Service.setObjectName("actionStop_Service")
        self.actionIP128 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setItalic(False)
        self.actionIP128.setFont(font)
        self.actionIP128.setObjectName("actionIP128")
        self.actionIP200 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionIP200.setFont(font)
        self.actionIP200.setObjectName("actionIP200")
        self.action_start_service = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.action_start_service.setFont(font)
        self.action_start_service.setObjectName("action_start_service")
        self.action_stop_service = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.action_stop_service.setFont(font)
        self.action_stop_service.setObjectName("action_stop_service")
        self.action_5 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.action_5.setFont(font)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.action_6.setFont(font)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(MainWindow)
        self.action_7.setObjectName("action_7")
        self.action_8 = QtWidgets.QAction(MainWindow)
        self.action_8.setObjectName("action_8")
        self.action_setup = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.action_setup.setFont(font)
        self.action_setup.setObjectName("action_setup")
        self.action_pcsetup = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.action_pcsetup.setFont(font)
        self.action_pcsetup.setObjectName("action_pcsetup")
        self.action_unit = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.action_unit.setFont(font)
        self.action_unit.setObjectName("action_unit")
        self.actionSuperNode = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionSuperNode.setFont(font)
        self.actionSuperNode.setObjectName("actionSuperNode")
        self.actionUltraSonic = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionUltraSonic.setFont(font)
        self.actionUltraSonic.setObjectName("actionUltraSonic")
        self.actionDance = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionDance.setFont(font)
        self.actionDance.setObjectName("actionDance")
        self.actionNavigation = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionNavigation.setFont(font)
        self.actionNavigation.setObjectName("actionNavigation")
        self.actionGinger1_0 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(18)
        self.actionGinger1_0.setFont(font)
        self.actionGinger1_0.setObjectName("actionGinger1_0")
        self.actionGinger1_1 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionGinger1_1.setFont(font)
        self.actionGinger1_1.setObjectName("actionGinger1_1")
        self.actionGravity = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionGravity.setFont(font)
        self.actionGravity.setObjectName("actionGravity")
        self.actionIMU = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionIMU.setFont(font)
        self.actionIMU.setObjectName("actionIMU")
        self.action_dance = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.action_dance.setFont(font)
        self.action_dance.setObjectName("action_dance")
        self.action_grasp = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.action_grasp.setFont(font)
        self.action_grasp.setObjectName("action_grasp")
        self.actionversion = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionversion.setFont(font)
        self.actionversion.setObjectName("actionversion")
        self.action_map = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.action_map.setFont(font)
        self.action_map.setObjectName("action_map")
        self.action_zero = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.action_zero.setFont(font)
        self.action_zero.setObjectName("action_zero")
        self.actionsetup = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionsetup.setFont(font)
        self.actionsetup.setObjectName("actionsetup")
        self.actionpcsetup = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionpcsetup.setFont(font)
        self.actionpcsetup.setObjectName("actionpcsetup")
        self.actionUpgrade = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionUpgrade.setFont(font)
        self.actionUpgrade.setObjectName("actionUpgrade")
        self.actionOTA = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionOTA.setFont(font)
        self.actionOTA.setObjectName("actionOTA")
        self.action_navigation = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.action_navigation.setFont(font)
        self.action_navigation.setObjectName("action_navigation")
        self.action_ultrasonic = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.action_ultrasonic.setFont(font)
        self.action_ultrasonic.setObjectName("action_ultrasonic")
        self.action_supernode = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.action_supernode.setFont(font)
        self.action_supernode.setObjectName("action_supernode")
        self.action_IMU = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.action_IMU.setFont(font)
        self.action_IMU.setObjectName("action_IMU")
        self.action_gravity = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.action_gravity.setFont(font)
        self.action_gravity.setObjectName("action_gravity")
        self.action_device = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.action_device.setFont(font)
        self.action_device.setObjectName("action_device")
        self.action_versionCompare = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.action_versionCompare.setFont(font)
        self.action_versionCompare.setObjectName("action_versionCompare")
        self.action_head_calibration = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.action_head_calibration.setFont(font)
        self.action_head_calibration.setObjectName("action_head_calibration")
        self.action_head_verify = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.action_head_verify.setFont(font)
        self.action_head_verify.setObjectName("action_head_verify")
        self.action_head_calibrate = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.action_head_calibrate.setFont(font)
        self.action_head_calibrate.setObjectName("action_head_calibrate")
        self.action_head_veri = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.action_head_veri.setFont(font)
        self.action_head_veri.setObjectName("action_head_veri")
        self.action_9 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.action_9.setFont(font)
        self.action_9.setObjectName("action_9")
        self.actionLED = QtWidgets.QAction(MainWindow)
        self.actionLED.setObjectName("actionLED")
        self.action_10 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.action_10.setFont(font)
        self.action_10.setObjectName("action_10")
        self.action_11 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.action_11.setFont(font)
        self.action_11.setObjectName("action_11")
        self.actionGinger1_1_1 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionGinger1_1_1.setFont(font)
        self.actionGinger1_1_1.setObjectName("actionGinger1_1_1")
        self.action_hari_IP128 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.action_hari_IP128.setFont(font)
        self.action_hari_IP128.setObjectName("action_hari_IP128")
        self.action_write_document = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.action_write_document.setFont(font)
        self.action_write_document.setObjectName("action_write_document")
        self.action_gatherparam = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.action_gatherparam.setFont(font)
        self.action_gatherparam.setObjectName("action_gatherparam")
        self.actionGinger1_1_2 = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionGinger1_1_2.setFont(font)
        self.actionGinger1_1_2.setObjectName("actionGinger1_1_2")
        self.actionGinger1_1_0_Plus = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.actionGinger1_1_0_Plus.setFont(font)
        self.actionGinger1_1_0_Plus.setObjectName("actionGinger1_1_0_Plus")
        self.actionBOSS_setup = QtWidgets.QAction(MainWindow)
        self.actionBOSS_setup.setObjectName("actionBOSS_setup")
        self.actionROC_setup = QtWidgets.QAction(MainWindow)
        self.actionROC_setup.setObjectName("actionROC_setup")
        self.actionRDP_setup = QtWidgets.QAction(MainWindow)
        self.actionRDP_setup.setObjectName("actionRDP_setup")
        self.actionHari_setup = QtWidgets.QAction(MainWindow)
        self.actionHari_setup.setObjectName("actionHari_setup")
        self.actionHari = QtWidgets.QAction(MainWindow)
        self.actionHari.setObjectName("actionHari")
        self.Model.addAction(self.actionGinger1_0)
        self.Model.addAction(self.actionGinger1_1)
        self.Model.addAction(self.actionGinger1_1_1)
        self.Model.addAction(self.actionGinger1_1_2)
        self.menuAbout.addAction(self.actionversion)
        self.menuCCU.addAction(self.actionUpgrade)
        self.menu.addAction(self.actionBOSS_setup)
        self.menu.addAction(self.actionROC_setup)
        self.menu.addAction(self.actionRDP_setup)
        self.menu.addAction(self.actionHari_setup)
        self.menu.addAction(self.actionHari)
        self.menuBar.addAction(self.Model.menuAction())
        self.menuBar.addAction(self.menuCCU.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ginger Test Program"))
        self.groupBox_base.setTitle(_translate("MainWindow", "基本信息"))
        self.label.setText(_translate("MainWindow", "机种："))
        self.label_2.setText(_translate("MainWindow", "站位："))
        self.label_3.setText(_translate("MainWindow", "测试员："))
        self.label_4.setText(_translate("MainWindow", "RobotSN:"))
        self.label_11.setText(_translate("MainWindow", "测试状态："))
        self.label_14.setText(_translate("MainWindow", "MO："))
        self.pushButton_start.setText(_translate("MainWindow", "开始"))
        self.pushButton_stop.setText(_translate("MainWindow", "停止"))
        self.pushbutton_SFIS_ON.setText(_translate("MainWindow", "SFIS ON"))
        self.label_16.setText(_translate("MainWindow", "SN："))
        self.label_15.setText(_translate("MainWindow", "IMEI："))
        self.groupBox_information.setTitle(_translate("MainWindow", "测试信息"))
        self.groupBox_testtime.setTitle(_translate("MainWindow", "测试时间"))
        self.label_8.setText(_translate("MainWindow", "结束："))
        self.label_7.setText(_translate("MainWindow", "开始："))
        self.label_5.setText(_translate("MainWindow", "test time:"))
        self.groupBox_programversion.setTitle(_translate("MainWindow", "程式版本"))
        self.label_10.setText(_translate("MainWindow", "Ginger Test Program version 2.0"))
        self.label_12.setText(_translate("MainWindow", "NPI TE Terry Li "))
        self.groupBox_testresult.setTitle(_translate("MainWindow", "测试结果统计"))
        self.label_18.setText(_translate("MainWindow", "PASS："))
        self.label_19.setText(_translate("MainWindow", "FAIL:"))
        self.label_20.setText(_translate("MainWindow", "Rate:"))
        self.Model.setTitle(_translate("MainWindow", "机种"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuCCU.setTitle(_translate("MainWindow", "回收用户"))
        self.menu.setTitle(_translate("MainWindow", "Hari"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))
        self.actionAuthor.setText(_translate("MainWindow", "Author"))
        self.actionStart_Service.setText(_translate("MainWindow", "Start Service"))
        self.actionStop_Service.setText(_translate("MainWindow", "Stop Service"))
        self.actionIP128.setText(_translate("MainWindow", "IP128"))
        self.actionIP200.setText(_translate("MainWindow", "IP200"))
        self.action_start_service.setText(_translate("MainWindow", "开启服务"))
        self.action_stop_service.setText(_translate("MainWindow", "停止服务"))
        self.action_5.setText(_translate("MainWindow", "自起服务"))
        self.action_6.setText(_translate("MainWindow", "停止自起服务"))
        self.action_7.setText(_translate("MainWindow", "版本"))
        self.action_8.setText(_translate("MainWindow", "作者"))
        self.action_setup.setText(_translate("MainWindow", "setup"))
        self.action_pcsetup.setText(_translate("MainWindow", "pcsetup"))
        self.action_unit.setText(_translate("MainWindow", "单元测试"))
        self.actionSuperNode.setText(_translate("MainWindow", "超节点"))
        self.actionUltraSonic.setText(_translate("MainWindow", "超声波"))
        self.actionDance.setText(_translate("MainWindow", "跳舞"))
        self.actionNavigation.setText(_translate("MainWindow", "导航"))
        self.actionGinger1_0.setText(_translate("MainWindow", "Ginger1.0.x"))
        self.actionGinger1_1.setText(_translate("MainWindow", "Ginger1.1.0"))
        self.actionGravity.setText(_translate("MainWindow", "重力补偿"))
        self.actionIMU.setText(_translate("MainWindow", "IMU"))
        self.action_dance.setText(_translate("MainWindow", "跳舞"))
        self.action_grasp.setText(_translate("MainWindow", "抓取"))
        self.actionversion.setText(_translate("MainWindow", "version"))
        self.action_map.setText(_translate("MainWindow", "导入地图"))
        self.action_zero.setText(_translate("MainWindow", "丢零"))
        self.actionsetup.setText(_translate("MainWindow", "setup"))
        self.actionpcsetup.setText(_translate("MainWindow", "pcsetup"))
        self.actionUpgrade.setText(_translate("MainWindow", "回收"))
        self.actionOTA.setText(_translate("MainWindow", "OTA"))
        self.action_navigation.setText(_translate("MainWindow", "导航"))
        self.action_ultrasonic.setText(_translate("MainWindow", "超声波"))
        self.action_supernode.setText(_translate("MainWindow", "超节点"))
        self.action_IMU.setText(_translate("MainWindow", "IMU校准"))
        self.action_gravity.setText(_translate("MainWindow", "重力补偿"))
        self.action_device.setText(_translate("MainWindow", "device文件"))
        self.action_versionCompare.setText(_translate("MainWindow", "版本比对"))
        self.action_head_calibration.setText(_translate("MainWindow", "标定"))
        self.action_head_verify.setText(_translate("MainWindow", "校准"))
        self.action_head_calibrate.setText(_translate("MainWindow", "标定"))
        self.action_head_veri.setText(_translate("MainWindow", "校准"))
        self.action_9.setText(_translate("MainWindow", "雷达"))
        self.actionLED.setText(_translate("MainWindow", "LED"))
        self.action_10.setText(_translate("MainWindow", "执行器"))
        self.action_11.setText(_translate("MainWindow", "执行器"))
        self.actionGinger1_1_1.setText(_translate("MainWindow", "Ginger1.1.1"))
        self.action_hari_IP128.setText(_translate("MainWindow", "IP128"))
        self.action_write_document.setText(_translate("MainWindow", "文件写入"))
        self.action_gatherparam.setText(_translate("MainWindow", "参数采集"))
        self.actionGinger1_1_2.setText(_translate("MainWindow", "Ginger1.1.2"))
        self.actionGinger1_1_0_Plus.setText(_translate("MainWindow", "Ginger1.1.0 Plus"))
        self.actionBOSS_setup.setText(_translate("MainWindow", "BOSS_setup"))
        self.actionROC_setup.setText(_translate("MainWindow", "ROC_setup"))
        self.actionRDP_setup.setText(_translate("MainWindow", "RDP_setup"))
        self.actionHari_setup.setText(_translate("MainWindow", "Hari_setup"))
        self.actionHari.setText(_translate("MainWindow", "Hari"))
