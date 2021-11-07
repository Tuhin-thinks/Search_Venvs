from typing import List, Union, Any

from PySide2.QtWidgets import QFileDialog
from PySide2.QtCore import QUrl


def openDir(parent, caption_str: str, current_dir_str: Union[Any, str]):
    options = QFileDialog.Options()
    options |= QFileDialog.ShowDirsOnly

    file_dialog: QUrl = QFileDialog.getExistingDirectoryUrl(parent, caption=caption_str, dir=current_dir_str,
                                                            options=options)
    if file_dialog:
        return file_dialog.toLocalFile()
    return None


def saveFile(parent, caption: str, current_dir__str: Union[None, str]):
    options = QFileDialog.Options()
    options |= QFileDialog.AcceptSave
    cur_dir__url = QUrl(current_dir__str)
    file_dialog, _ = QFileDialog.getSaveFileUrl(parent, caption, dir=cur_dir__url, options=options)

    if file_dialog and _:
        file_dialog: 'QUrl'
        return file_dialog.toLocalFile()
    return None
