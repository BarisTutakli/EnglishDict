# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'szlk1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_demoszlk(object):
    def setupUi(self, demoszlk):
        demoszlk.setObjectName("demoszlk")
        demoszlk.resize(787, 453)
        self.verticalLayout = QtWidgets.QVBoxLayout(demoszlk)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(demoszlk)
        self.frame.setStyleSheet("#frame{\n"
"background:#3a4055;\n"
"\n"
"\n"
"\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ldt_input = QtWidgets.QLineEdit(self.frame)
        self.ldt_input.setGeometry(QtCore.QRect(120, 90, 119, 20))
        self.ldt_input.setStyleSheet("#ldt_input{\n"
"    background-color: #eeffdd;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
" \n"
"    \n"
"    border-radius: 4px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 7em;\n"
"\n"
"\n"
"\n"
"}")
        self.ldt_input.setObjectName("ldt_input")
        self.btn_kontrol = QtWidgets.QPushButton(self.frame)
        self.btn_kontrol.setGeometry(QtCore.QRect(260, 90, 93, 23))
        self.btn_kontrol.setStyleSheet("#btn_kontrol{\n"
"    background-color: #eeffdd;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 3px;\n"
"    \n"
"\n"
"\n"
"}")
        self.btn_kontrol.setObjectName("btn_kontrol")
        self.btn_cevir = QtWidgets.QPushButton(self.frame)
        self.btn_cevir.setEnabled(True)
        self.btn_cevir.setGeometry(QtCore.QRect(500, 90, 93, 23))
        self.btn_cevir.setStyleSheet("#btn_cevir{\n"
"    background-color: #eeffdd;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 3px;\n"
"    \n"
"\n"
"\n"
"}")
        self.btn_cevir.setObjectName("btn_cevir")
        self.cikis = QtWidgets.QPushButton(self.frame)
        self.cikis.setGeometry(QtCore.QRect(630, 380, 93, 23))
        self.cikis.setStyleSheet("#cikis{\n"
"    background-color: #eeffdd;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 3px;\n"
"    \n"
"\n"
"\n"
"}")
        self.cikis.setObjectName("cikis")
        self.btn_temizle = QtWidgets.QPushButton(self.frame)
        self.btn_temizle.setGeometry(QtCore.QRect(380, 90, 93, 21))
        self.btn_temizle.setStyleSheet("#btn_temizle{\n"
"    background-color: #eeffdd;\n"
"    font: 10pt \"MS Shell Dlg 2\";\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 10px;\n"
"    border-color: beige;\n"
"    font: bold 14px;\n"
"    min-width: 5em;\n"
"    padding: 3px;\n"
"    \n"
"\n"
"\n"
"}")
        self.btn_temizle.setObjectName("btn_temizle")
        self.btm_frame = QtWidgets.QFrame(self.frame)
        self.btm_frame.setGeometry(QtCore.QRect(110, 150, 551, 211))
        self.btm_frame.setStyleSheet("#btm_frame{\n"
"    background:white;\n"
"    position:relative;\n"
"    min-height:200px;\n"
"    min-width:500px;\n"
"\n"
"}")
        self.btm_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btm_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btm_frame.setObjectName("btm_frame")
        self.lbl_geribildirm = QtWidgets.QLabel(self.btm_frame)
        self.lbl_geribildirm.setGeometry(QtCore.QRect(0, 0, 551, 36))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl_geribildirm.setFont(font)
        self.lbl_geribildirm.setStyleSheet("#lbl_geribildirm{\n"
"   background-color: #b4ffc7;\n"
"\n"
"   \n"
"\n"
"    font: bold 14px;\n"
"    min-width: 20em;\n"
"    min-height:2em;\n"
"   \n"
"}")
        self.lbl_geribildirm.setFrameShape(QtWidgets.QFrame.Box)
        self.lbl_geribildirm.setText("")
        self.lbl_geribildirm.setObjectName("lbl_geribildirm")
        self.label = QtWidgets.QPlainTextEdit(self.btm_frame)
        self.label.setGeometry(QtCore.QRect(0, 40, 551, 171))
        self.label.setStyleSheet("#label{\n"
"    min-width:450;\n"
"    min-height:50;\n"
"\n"
"}")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(demoszlk)
        self.btn_cevir.clicked.connect(demoszlk.ceviri_yap)
        self.btn_temizle.clicked.connect(demoszlk.clear)
        self.btn_kontrol.clicked.connect(demoszlk.kontrol_et)
        self.cikis.clicked.connect(demoszlk.kapat)
        QtCore.QMetaObject.connectSlotsByName(demoszlk)

    def retranslateUi(self, demoszlk):
        _translate = QtCore.QCoreApplication.translate
        demoszlk.setWindowTitle(_translate("demoszlk", "Form"))
        self.btn_kontrol.setText(_translate("demoszlk", "kontrol et"))
        self.btn_cevir.setText(_translate("demoszlk", "translate"))
        self.cikis.setText(_translate("demoszlk", "Çıkış"))
        self.btn_temizle.setText(_translate("demoszlk", "Temizle"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    demoszlk = QtWidgets.QWidget()
    ui = Ui_demoszlk()
    ui.setupUi(demoszlk)
    demoszlk.show()
    sys.exit(app.exec_())

