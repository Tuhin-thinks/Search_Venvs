import os.path
import sys

from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow

from Process import ThreadManager
from UI import ui_home_window
from UI.CustomWidgets import TableView__venv
from UI_Utils import FileHandling as File_handling


class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()

        self.scan_start_location = None
        self.ui = ui_home_window.Ui_MainWindow()
        self.ui.setupUi(self)

        self.path_list = []

        # thread to handle scanning of directories
        self.scan_thread = QtCore.QThread()
        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.pushButton_open.clicked.connect(self.openDirLocation)
        self.ui.pushButton_saveAs.clicked.connect(self.saveFileLocation)

        self.ui.pushButton_startFinding.clicked.connect(self.start_file_scan)
        self.ui.pushButton_changeMode.clicked.connect(self.change_page)

        self.venv_table_view = TableView__venv.VenvView()
        self.ui.frame_del_venv_tableframe.layout().addWidget(self.venv_table_view)

    def change_page(self):
        to_index = int(not self.ui.stackedWidget.currentIndex())
        self.ui.stackedWidget.setCurrentIndex(to_index)

    def start_and_create_scan_object(self, save_loc):
        self.scan_object = ThreadManager.ScanDir(self.scan_start_location, save_loc)
        self.scan_object.found_signal.connect(self.display_status)
        self.scan_object.path_signal.connect(self.venv_found)
        self.scan_object.completed.connect(self.destroy_thread)
        self.scan_object.completed.connect(self.enable_research)
        self.scan_thread.started.connect(self.scan_object.run)
        self.scan_object.moveToThread(self.scan_thread)
        self.scan_thread.start()

    def destroy_thread(self):
        self.scan_thread.quit()
        while True:
            try:
                self.scan_object.disconnect()  # disconnect all connection
            except (TypeError, AttributeError, RuntimeError):
                break
        try:
            self.scan_object.deleteLater()
        except Exception as e:
            print(f"Err:: {e.__str__()}")

    def reset_model_data(self):
        self.venv_table_view.reset_model(self.path_list[:])
        # self.path_list.clear()

    def enable_research(self):
        self.ui.pushButton_startFinding.setDisabled(False)  # enable scan button after 'search' is completed
        self.reset_model_data()

    def venv_found(self, path_str: str):
        self.path_list.append(path_str)

    def display_status(self, message, *args):
        self.ui.statusbar.showMessage(message, 2 * 1000)  # show message for 2 seconds

    def start_file_scan(self):
        """check if the required data are provided and start the directory scan"""
        if self.scan_start_location is not None and os.path.exists(self.scan_start_location):
            save_location = self.ui.lineEdit_saveAs.text()
            self.start_and_create_scan_object(save_loc=save_location)
            self.ui.pushButton_startFinding.setDisabled(True)  # disable scan button (when scan already running)
        else:
            self.ui.statusbar.showMessage("scan directory not set, please select the scanning directory", 2 * 1000)

    def openDirLocation(self):
        dir_path = File_handling.openDir(self, caption_str='Select Search directory', current_dir_str=None)
        if dir_path:
            self.ui.lineEdit_searchPath.setText(dir_path)
            self.scan_start_location = dir_path  # store the scan start directory location

    def saveFileLocation(self):
        save_path = File_handling.saveFile(self, "Select save file location", None)
        if save_path:
            self.ui.lineEdit_saveAs.setText(save_path)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.destroy_thread()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = HomeWindow()
    w.show()
    sys.exit(app.exec_())
