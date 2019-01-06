
from PyQt5.QtWidgets import QLabel, QFrame
class dialog_label(QLabel):
    def __init__(self,centralwidget):
        super().__init__(centralwidget)
        self.setFrameShape(QFrame.Box)
        self.setStyleSheet('border-width: 1px;border-style: solid;border-color: rgb(255, 170, 0);'+
                           'background-color: rgb(100,149,237);color:rgb(255,255,255);'+
                            'border-radius:15px; border-left:20px;padding-left:20px;'

                           )
        print('dialog_label')