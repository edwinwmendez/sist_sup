# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'position_cursor_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 70)
        MainWindow.setStyleSheet("color: rgb(253, 253, 253);\n"
"background-color: rgb(14, 22, 33);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 20, 500, 40))
        self.frame.setStyleSheet("QPushButton{\n"
"color:rgb(69, 78, 121);\n"
"background-color: rgb(255, 255, 255)\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spn_seconds = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spn_seconds.setMaximumSize(QtCore.QSize(35, 16777215))
        self.spn_seconds.setMinimum(2)
        self.spn_seconds.setMaximum(10)
        self.spn_seconds.setObjectName("spn_seconds")
        self.horizontalLayout.addWidget(self.spn_seconds)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.btn_ok = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_ok.setMinimumSize(QtCore.QSize(30, 25))
        self.btn_ok.setMaximumSize(QtCore.QSize(40, 30))
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout.addWidget(self.btn_ok)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lbl_coord_x = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_coord_x.setText("")
        self.lbl_coord_x.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_coord_x.setObjectName("lbl_coord_x")
        self.horizontalLayout_3.addWidget(self.lbl_coord_x)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(1, 0))
        self.label_5.setMaximumSize(QtCore.QSize(2, 16777215))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lbl_coord_y = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_coord_y.setText("")
        self.lbl_coord_y.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_coord_y.setObjectName("lbl_coord_y")
        self.horizontalLayout_3.addWidget(self.lbl_coord_y)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 500, 20))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 501, 22))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_close = QtWidgets.QToolButton(self.horizontalLayoutWidget_2)
        self.btn_close.setMinimumSize(QtCore.QSize(10, 10))
        self.btn_close.setMaximumSize(QtCore.QSize(10, 10))
        self.btn_close.setText("...")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/ciricle_red.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setIconSize(QtCore.QSize(10, 10))
        self.btn_close.setPopupMode(QtWidgets.QToolButton.DelayedPopup)
        self.btn_close.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.btn_close.setAutoRaise(True)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_4.addWidget(self.btn_close)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Obtener posición del cursor despues de"))
        self.label_2.setText(_translate("MainWindow", "Segundos"))
        self.btn_ok.setText(_translate("MainWindow", "Ok"))
        self.label_3.setText(_translate("MainWindow", "X"))
        self.label_4.setText(_translate("MainWindow", "Y"))
        self.label_5.setText(_translate("MainWindow", ":"))
        self.btn_close.setShortcut(_translate("MainWindow", "Esc"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
