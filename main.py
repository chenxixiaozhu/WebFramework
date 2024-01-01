import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import json


class MainWindow(QMainWindow):
    def __init__(self):
        josn = json.loads(open("package.json", "r").read())
        mun = [josn["name"], josn["version"],josn["size_width"],josn["size_height"], josn["main_html"]]
        print(mun)
        super(MainWindow, self).__init__()
        self.setWindowTitle(mun[0])
        self.setWindowIcon(QIcon("./test.ico"))
        self.setGeometry(70,70,int(mun[2]),int(mun[3]))
        self.browser=QWebEngineView()
        self.browser.load(QUrl(QFileInfo(mun[4]).absoluteFilePath()))
        self.setCentralWidget(self.browser)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec_())