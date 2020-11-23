import sys
import PyQt5
import PyQt5.QtWidgets
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from . import io

class Sn(PyQt5.QtWidgets.QWidget):
    def __init__(self, root, config):
        super().__init__()
        self.title = config['window']['title']
        self.top = int(config['window']['top'])
        self.left = int(config['window']['left'])
        self.width = int(config['window']['width'])
        self.height = int(config['window']['height'])
        self.previous_view = None
        self.current_view = None

        self.init_window()

        self.populate(path=root)

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setMouseTracking(True)

        self.list = PyQt5.QtWidgets.QListWidget()
        self.list.clicked.connect(self.click_handler)

        vbox = PyQt5.QtWidgets.QVBoxLayout()
        vbox.addWidget(self.list)
        self.setLayout(vbox)

        self.show()

    def populate(self, path):
        # save the previous view
        self.previous_view = self.current_view

        # generate the new view
        self.current_view = io.DirView(path)

        # modify the list
        self.redraw_list(self.current_view)

    def redraw_list(self, view):
        for idx, entry in enumerate(view):
            item = PyQt5.QtWidgets.QListWidgetItem(entry.path)
            # todo clean this
            item.setIcon(QtGui.QIcon('resources/folder-ico.svg'))
            self.list.insertItem(idx, item)
            
    def click_handler(self):
        selected_path = self.list.currentItem().text()
        self.list.clear()
        self.populate(path=selected_path)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Backspace: 
            self.redraw_list(self.previous_view)