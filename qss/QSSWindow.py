# coding=utf-8
""" 测试qss文件 """
import sys


from qss.qsswindow_Fm import *
from PyQt5.QtWidgets import QApplication

class Example(QtWidgets.QMainWindow, Ui_QSSWindow):
    """ 测试用例 """
    def __init__(self):
        super().__init__()
        self.loadQSS()
        self.setupUi(self)
        self.connectSign()
        self.initData()
        self.show()

    def loadQSS(self):
        """ 加载QSS """
        file = 'window.qss'
        with open(file, 'rt', encoding='utf8') as f:
            styleSheet = f.read()
        self.setStyleSheet(styleSheet)
        f.close()

    def initData(self):
        # 初始化常用组件
        self.lineEdit.setText("一别两宽，各生欢喜~")
        self.comboBox.addItems(['Item1', 'Item2', 'Item3', 'Item4', 'Item5', 'Item6', 'Item7', 'Item2', 'Item3', 'Item4', 'Item5', 'Item6', 'Item7'])
        self.horizontalSlider.setValue(50)
        self.updateProgressBar()
        self.textEdit.setText("忠于理想，面对现实。 \n      -- 这杯可乐有点甜")
        pass

    def connectSign(self):
        """ 连接信号 """
        self.horizontalSlider.valueChanged.connect(self.updateProgressBar)
        pass

    def updateProgressBar(self):
        self.progressBar.setValue(self.horizontalSlider.value())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())