import sys

from PySide2.QtWidgets import QApplication, QMainWindow

from UI import ui_home_window
from UI_Utils import FileHandling as FH


class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()

        self.ui = ui_home_window.Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_open.clicked.connect(self.openDirLocation)
        self.ui.pushButton_saveAs.clicked.connect(self.saveFileLocation)

    def openDirLocation(self):
        dir_path = FH.openDir(self, caption_str='Select Search directory', current_dir_str=None)
        if dir_path:
            self.ui.lineEdit_searchPath.setText(dir_path)

    def saveFileLocation(self):
        save_path = FH.saveFile(self, "Select save file location", None)
        if save_path:
            self.ui.lineEdit_saveAs.setText(save_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = HomeWindow()
    w.show()
    sys.exit(app.exec_())
