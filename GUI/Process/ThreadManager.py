from PySide2 import QtCore
from PySide2.QtCore import QObject

from . import detect_venv


class ScanDir(QObject):
    found_signal = QtCore.Signal(str)
    path_signal = QtCore.Signal(str)
    completed = QtCore.Signal()

    def __init__(self, start_path, save_loc=None):
        QObject.__init__(self)
        self.start_path = start_path
        self.save_loc = save_loc

    def run(self):
        print("started scan")
        file_saved_as = detect_venv.begin_scan(self.start_path, self.found_signal, self.path_signal, self.save_loc)
        self.found_signal.emit(file_saved_as)

        self.completed.emit()
