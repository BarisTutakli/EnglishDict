import sys
from PyQt5.QtWidgets import QDialog,QApplication
import szlk1
from szlk1 import Ui_demoszlk
import json
from difflib import get_close_matches

class MainWindow(QDialog,szlk1.Ui_demoszlk):
    def __init__(self, app=None):
        super(MainWindow, self).__init__()
        self.app = app
        self.setupUi(self)
        self.show()
        self.veriler = json.load(open("data.json"))


    def clear(self):
        self.label.clear()
        self.ldt_input.clear()
        self.lbl_geribildirm.clear()
    def kapat(self):
        ret = app.exec_()
        app.exit()
        sys.exit(ret)

    def kontrol_et(self):
        self.w = self.ldt_input.text()
        if self.w in self.veriler:
            self.lbl_geribildirm.setText("kelime bulundu translate i tıklayınız")
            #self.btn_cevir.isEnabled()= True
        elif(len(get_close_matches(self.w, self.veriler.keys())) > 0):
            print("şunu mu {} demek istedin? öyle ise tekrar deneyiniz ".format(get_close_matches(self.w, self.veriler.keys())))
            self.lbl_geribildirm.setText("{} şunlardan birini mi demek istedin? öyle ise tekrar deneyiniz ".format(get_close_matches(self.w, self.veriler.keys())))
            self.ldt_input.clear()
            #self.btn_cevir.isEnabled() = True
        else:
            print("aradığınız kelime bulunmamaktadır .Lütfen kontrol ediniz")
            self.lbl_geribildirm.setText("aradığınız kelime bulunmamaktadır .Lütfen kontrol ediniz")

    def ceviri_yap(self):
        self.w = self.ldt_input.text()
        print("çalıştı")
        str1=""
        for i in self.veriler[self.w]:
            str1=str1 + i+ "\n"
        self.label.appendPlainText(str1)

if __name__ == "__main__":
 app = QApplication(sys.argv)
 mainWin = MainWindow(app)
 ret = app.exec_()
 app.exit()
 sys.exit(ret)








