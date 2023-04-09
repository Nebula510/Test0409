import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QDialog,QMainWindow,QFileDialog,QAction,QMessageBox
from PyQt5.QtGui import QIcon
from Check_Continuuty3 import Ui_Dialog
import xlsxwriter as xw

class Ui_Dialog(QDialog,Ui_Dialog):

    def __init__(self,parent=None):
        super(Ui_Dialog, self).__init__(parent)
        self.setupUi(self)

        # 设置敲击响应
        self.btn_sps_file.clicked.connect(self.open_sps_file)
        self.btn_ok.clicked.connect(self.Check_consecutive_files)

        self.lineEdit.setText("E:\\2023\\py_work\\shalik_CheckName\\check")

    def open_sps_file(self):
        fileName = QFileDialog.getExistingDirectory(self,
            "Choose Fold", self.lineEdit.text())
        print("".join(fileName))
        print(type(fileName))
        # 更新上面每次打开的默认路径
        self.lineEdit.setText("".join(fileName))
        return

    def Check_consecutive_files(self):
        path = self.lineEdit.text()
        files = os.listdir(path)
        if not files:
            print("No files found in the directory.")
            return

        # sort the files by name
        files.sort()

        # get the starting index
        start_index = int(files[0].split('.')[0])

        # check if the files are consecutive
        missing_files = []
        previous_index = start_index
        for file in files:
            file_index = int(file.split('.')[0])
            if file_index != previous_index + 1:
                for i in range(previous_index + 1, file_index):
                    missing_files.append(f"{i}.{file.split('.')[1]}")
            previous_index = file_index

        # if there are missing files
        if missing_files:
            print("Missing files:")
            self.plainTextEdit.setPlainText("Missing files:")
            for missing_file in missing_files:
                print(missing_file)
                self.plainTextEdit.appendPlainText(missing_file)

        else:
            print("No missing!")
            self.plainTextEdit.setPlainText("No missing!")


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Ui_Dialog()
    ex.show()
    sys.exit(app.exec_())
