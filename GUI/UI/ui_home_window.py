# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(829, 524)
        MainWindow.setMinimumSize(QSize(385, 0))
        self.actionPreferences = QAction(MainWindow)
        self.actionPreferences.setObjectName(u"actionPreferences")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_pafe_1 = QFrame(self.page)
        self.frame_pafe_1.setObjectName(u"frame_pafe_1")
        self.frame_pafe_1.setFrameShape(QFrame.NoFrame)
        self.frame_pafe_1.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_pafe_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.frame_pafe_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"URW Gothic")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet(u"\n"
"	font: 11pt \"URW Gothic\";")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_searchPath = QLineEdit(self.frame)
        self.lineEdit_searchPath.setObjectName(u"lineEdit_searchPath")
        self.lineEdit_searchPath.setMinimumSize(QSize(0, 30))
        self.lineEdit_searchPath.setStyleSheet(u"#lineEdit_searchPath{\n"
"	border: none;\n"
"	border-bottom: 1px solid blue;\n"
"	font: 11pt \"URW Gothic\";\n"
"	padding: 2px 10px;\n"
"}\n"
"#lineEdit_searchPath::hover:!pressed{\n"
"	border: none;\n"
"	border-bottom: 2px solid blue;\n"
"}")

        self.horizontalLayout.addWidget(self.lineEdit_searchPath)

        self.pushButton_open = QPushButton(self.frame)
        self.pushButton_open.setObjectName(u"pushButton_open")
        self.pushButton_open.setMinimumSize(QSize(100, 30))
        self.pushButton_open.setStyleSheet(u"#pushButton_open{\n"
"	background-color: rgb(186, 189, 182);\n"
"	border: 1px solid none;\n"
"	font: 11pt \"URW Gothic\";\n"
"	border-radius: 2px;\n"
"}\n"
"#pushButton_open::hover:!pressed{\n"
"	border: 2px solid blue;\n"
"	font: 11pt \"URW Gothic\";\n"
"}\n"
"#pushButton_open::pressed{\n"
"	border: none;\n"
"	font: 11pt \"URW Gothic\";\n"
"	padding: 2px;\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton_open)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.frame_pafe_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"\n"
"	font: 11pt \"URW Gothic\";")
        self.label_2.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_saveAs = QLineEdit(self.frame_2)
        self.lineEdit_saveAs.setObjectName(u"lineEdit_saveAs")
        self.lineEdit_saveAs.setMinimumSize(QSize(0, 30))
        self.lineEdit_saveAs.setStyleSheet(u"#lineEdit_saveAs{\n"
"	border: none;\n"
"	border-bottom: 1px solid blue;\n"
"	font: 11pt \"URW Gothic\";\n"
"	padding: 2px 10px;\n"
"}\n"
"#lineEdit_saveAs::hover:!pressed{\n"
"	border: none;\n"
"	border-bottom: 2px solid blue;\n"
"}")

        self.horizontalLayout_2.addWidget(self.lineEdit_saveAs)

        self.pushButton_saveAs = QPushButton(self.frame_2)
        self.pushButton_saveAs.setObjectName(u"pushButton_saveAs")
        self.pushButton_saveAs.setMinimumSize(QSize(100, 30))
        self.pushButton_saveAs.setStyleSheet(u"#pushButton_saveAs{\n"
"	background-color: rgb(186, 189, 182);\n"
"	border: 1px solid none;\n"
"	font: 11pt \"URW Gothic\";\n"
"	border-radius: 2px;\n"
"}\n"
"#pushButton_saveAs::hover:!pressed{\n"
"	border: 2px solid blue;\n"
"	font: 11pt \"URW Gothic\";\n"
"}\n"
"#pushButton_saveAs::pressed{\n"
"	border: none;\n"
"	font: 11pt \"URW Gothic\";\n"
"	padding: 2px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_saveAs)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_pafe_1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.pushButton_startFinding = QPushButton(self.frame_4)
        self.pushButton_startFinding.setObjectName(u"pushButton_startFinding")
        self.pushButton_startFinding.setMinimumSize(QSize(100, 50))
        self.pushButton_startFinding.setMaximumSize(QSize(195, 16777215))
        self.pushButton_startFinding.setStyleSheet(u"#pushButton_startFinding{\n"
"	background-color: rgb(186, 189, 182);\n"
"	border: 1px solid none;\n"
"	font: 11pt \"URW Gothic\";\n"
"	border-radius: 2px;\n"
"}\n"
"#pushButton_startFinding::hover:!pressed{\n"
"	border: 2px solid blue;\n"
"	font: 11pt \"URW Gothic\";\n"
"}\n"
"#pushButton_startFinding::pressed{\n"
"	border: none;\n"
"	font: 11pt \"URW Gothic\";\n"
"	padding: 2px;\n"
"}")

        self.gridLayout_2.addWidget(self.pushButton_startFinding, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)


        self.gridLayout.addWidget(self.frame_4, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_pafe_1, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_delete_venv_header = QFrame(self.page_2)
        self.frame_delete_venv_header.setObjectName(u"frame_delete_venv_header")
        self.frame_delete_venv_header.setMaximumSize(QSize(16777215, 50))
        self.frame_delete_venv_header.setFrameShape(QFrame.StyledPanel)
        self.frame_delete_venv_header.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_delete_venv_header)

        self.frame_del_venv_tableframe = QFrame(self.page_2)
        self.frame_del_venv_tableframe.setObjectName(u"frame_del_venv_tableframe")
        self.frame_del_venv_tableframe.setFrameShape(QFrame.StyledPanel)
        self.frame_del_venv_tableframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_del_venv_tableframe)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_2.addWidget(self.frame_del_venv_tableframe)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_4.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.frame_page_header = QFrame(self.centralwidget)
        self.frame_page_header.setObjectName(u"frame_page_header")
        self.frame_page_header.setFrameShape(QFrame.NoFrame)
        self.frame_page_header.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_page_header)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.pushButton_changeMode = QPushButton(self.frame_page_header)
        self.pushButton_changeMode.setObjectName(u"pushButton_changeMode")
        self.pushButton_changeMode.setMinimumSize(QSize(121, 41))
        self.pushButton_changeMode.setMaximumSize(QSize(121, 41))
        self.pushButton_changeMode.setStyleSheet(u"#pushButton_changeMode{\n"
"	background-color: rgb(186, 189, 182);\n"
"	border: 1px solid none;\n"
"	font: 11pt \"URW Gothic\";\n"
"	border-radius: 2px;\n"
"}\n"
"#pushButton_changeMode::hover:!pressed{\n"
"	border: 2px solid blue;\n"
"	font: 11pt \"URW Gothic\";\n"
"}\n"
"#pushButton_changeMode::pressed{\n"
"	border: none;\n"
"	font: 11pt \"URW Gothic\";\n"
"	padding: 2px;\n"
"}")

        self.gridLayout_5.addWidget(self.pushButton_changeMode, 0, 0, 1, 1)

        self.label_curr_window_name = QLabel(self.frame_page_header)
        self.label_curr_window_name.setObjectName(u"label_curr_window_name")

        self.gridLayout_5.addWidget(self.label_curr_window_name, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_page_header, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 829, 20))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pushButton_changeMode, self.lineEdit_searchPath)
        QWidget.setTabOrder(self.lineEdit_searchPath, self.pushButton_open)
        QWidget.setTabOrder(self.pushButton_open, self.lineEdit_saveAs)
        QWidget.setTabOrder(self.lineEdit_saveAs, self.pushButton_saveAs)
        QWidget.setTabOrder(self.pushButton_saveAs, self.pushButton_startFinding)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionPreferences)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SearchVenvs", None))
        self.actionPreferences.setText(QCoreApplication.translate("MainWindow", u"&Preferences", None))
#if QT_CONFIG(shortcut)
        self.actionPreferences.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+P", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"*Select directory to search from", None))
        self.lineEdit_searchPath.setText("")
        self.pushButton_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"*File name to save output results", None))
        self.lineEdit_saveAs.setText("")
        self.pushButton_saveAs.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.pushButton_startFinding.setText(QCoreApplication.translate("MainWindow", u"Start finding", None))
        self.pushButton_changeMode.setText(QCoreApplication.translate("MainWindow", u"Change Mode", None))
        self.label_curr_window_name.setText("")
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

