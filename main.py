import sys
from PyQt5.QtWidgets import QApplication

from lib.main_window import main_window

if __name__=='__main__':
    app = QApplication(sys.argv)
    m=main_window()
    sys.exit(app.exec_())