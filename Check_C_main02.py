import os
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from Check_Continuity_04 import Ui_Dialog

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
        # 更新上面每次打开的默认路径
        self.lineEdit.setText("".join(fileName))
        return

    def Check_consecutive_files(self):
        path = self.lineEdit.text()
        start = self.lineEdit_2.text()
        end = self.lineEdit_3.text()
        #print(start)
        #print(end)

        files = os.listdir(path)
        if not files:
            self.plainTextEdit.setPlainText("No files in fold!")
            return

        # sort the files by name
        files.sort()

        # get the starting index
        if not start:
            self.plainTextEdit.setPlainText("Please input Start and End.")
            return
        else:
            start_index = int(start)
            end_index = int(end)
            count = len(files)
            count_index = end_index-start_index
            if count != count_index:
                self.plainTextEdit.setPlainText("Missing Number: "+
                                                str(count_index-count+1))

        # check if the files are consecutive
        missing_files = []
        previous_index = start_index
        for j in range(count):
            file = files[j]
            file_index = int(file.split('.')[0])
            if file_index != previous_index + 1:
                for i in range(previous_index + 1, file_index):
                    missing_files.append(f"{i}.{file.split('.')[1]}")
            previous_index = file_index

        # if there are missing files
        if missing_files:
            self.plainTextEdit.appendPlainText("Missing files:")
            for missing_file in missing_files:
                self.plainTextEdit.appendPlainText(missing_file)
        else:
            self.plainTextEdit.setPlainText("No missing!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_Dialog()
    ex.show()
    sys.exit(app.exec_())
