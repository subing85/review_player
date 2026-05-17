from PySide6 import QtGui
from PySide6 import QtCore
from PySide6 import QtWidgets


class PlaylistTreewidget(QtWidgets.QTreeWidget):
    def __init__(self, parent, **kwargs):
        super(PlaylistTreewidget, self).__init__(parent)

        self.setHeaderHidden(True)
        self.setAlternatingRowColors(True)
        self.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.SingleSelection)

        self.header().setStretchLastSection(True)

    def findChidItems(self, index=0, checkState=False):
        checkStates = {
            True: QtCore.Qt.CheckState.Checked,
            False: QtCore.Qt.CheckState.Unchecked,
        }

        widgetItem = self.invisibleRootItem()

        result = list()
        for count in range(widgetItem.childCount()):
            item = widgetItem.child(count)
            currentCheckState = item.checkState(index)
            if checkState and currentCheckState != QtCore.Qt.CheckState.Checked:
                continue
            result.append(item)

        return result

    def revised(self):
        self.clear()

    def removeItems(self, items):
        if not isinstance(items, list):
            items = [items]

        widgetItem = self.invisibleRootItem()
        for item in items:
            widgetItem.removeChild(item)
