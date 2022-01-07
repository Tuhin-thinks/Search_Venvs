import typing
from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import Qt


class EnvViewmodel(QtCore.QAbstractTableModel):
    def __init__(self):
        super(EnvViewmodel, self).__init__()

        self._model_data = []
        self.header_labels = ["Venv Name", "Keep?"]

    def reset_model(self, venv_path_list: typing.List[typing.List[str]]):
        self.beginResetModel()
        self._model_data = venv_path_list
        print(f"reset done with data: {self._model_data}")
        self.endResetModel()

    def data(self, index: QtCore.QModelIndex, role: int = ...) -> typing.Any:
        row, col = index.row(), index.column()
        if role == Qt.DisplayRole:
            _data = str(self._model_data[row][col])
            return _data

    def rowCount(self, parent: QtCore.QModelIndex = ...) -> int:
        return len(self._model_data)

    def columnCount(self, parent: QtCore.QModelIndex = ...) -> int:
        return len(self.header_labels)

    def headerData(self, section: int, orientation: QtCore.Qt.Orientation, role: int = ...) -> typing.Any:
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
                return str(self.header_labels[section])
