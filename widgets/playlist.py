# Copyright (c) 2026, Motion-Craft Technology All rights reserved.
# Author: Subin. Gopi (subing85@gmail.com).
# Description: Review Player Qt Custom playlist widget module.
# WARNING! All changes made in this file will be lost when recompiling source file!

from __future__ import absolute_import


from PySide6 import QtCore
from PySide6 import QtWidgets

from widgets.layouts import VerticalLayout
from widgets.layouts import HorizontalLayout

from widgets.labels import ProjectIconLabel
from widgets.comboboxs import ProjectCombobox
from widgets.treewidgets import PlaylistTreewidget

class PlaylistGroup(QtWidgets.QGroupBox):

    def __init__(self, parent, *args, **kwargs):
        super(PlaylistGroup, self).__init__(parent)

        # self.setTitle("Playlist")

        self.setFlat(True)
        self.setMinimumSize(QtCore.QSize(200, 0))
        # self.setMaximumSize(QtCore.QSize(200, 16777215))

        self.verticallayout = VerticalLayout(self, space=10, margins=(0, 0, 0, 0))

        self.horizontallayout = HorizontalLayout(None, space=10, margins=(0, 0, 0, 0))
        self.verticallayout.addLayout(self.horizontallayout)

        self.projectIconLabel = ProjectIconLabel(self)
        self.projectIconLabel.setThumbnail("/run/media/batman/ALPHA/works/developments/review_player/resources/icons/unknown.png")
        self.horizontallayout.addWidget(self.projectIconLabel)

        self.projectCombobox = ProjectCombobox(self)
        self.horizontallayout.addWidget(self.projectCombobox)

        self.playlistTreewidget = PlaylistTreewidget(self)
        self.verticallayout.addWidget(self.playlistTreewidget)


if __name__ == "__main__":
    pass
