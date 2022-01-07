import typing

from PySide2 import QtWidgets, QtGui

from UI.Models import Model__venv


class VenvView(QtWidgets.QTableView):
    def __init__(self):
        super(VenvView, self).__init__()

        self._model = Model__venv.EnvViewmodel()
        self.setModel(self._model)

    def reset_model(self, venv_path_list: typing.List[str]):
        self.model().reset_model([[x, 0] for x in venv_path_list])

    def resizeEvent(self, event:QtGui.QResizeEvent) -> None:
        tot_width = self.visibleRegion().boundingRect().width() - 10
        self.setColumnWidth(0, int(tot_width * 0.8))
        self.setColumnWidth(1, int(tot_width * 0.2))
