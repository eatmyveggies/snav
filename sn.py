import sys
import PyQt5
from pathlib import Path

import configparser

from core import sn

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('sn.ini')
    config.sections()
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = sn.Sn(
        root=str(Path.home()),
        config=config
        )
    sys.exit(app.exec())
