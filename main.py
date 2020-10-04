import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from worker import Worker
import time

from MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.threadpool = QThreadPool()
        self.assignInput()
    
    def assignInput(self):
        '''
        Assign callbacks to the user input
        '''
        self.pushButton.clicked.connect(self.loadBar)

    def loadBar(self):
        '''
        Simulate loading
        '''
        worker = Worker(self._loadBarHelper)
        worker.signals.progress.connect(lambda value: self.progressBar.setValue(value))
        self.threadpool.start(worker) 

    def _loadBarHelper(self, progress_callback):
        value = 0

        while value < 100:
            value += 1
            progress_callback.emit(value)
            time.sleep(0.01)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec()