from PyQt5.QtCore import QThread, pyqtSignal
import time


class WorkThread:
    trigger = pyqtSignal()

    def __init__(self):
        super(WorkThread, self).__init__()

    def run(self):
        time.sleep(0.5)
        self.trigger.emit()
