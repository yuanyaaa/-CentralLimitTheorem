# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
# 导入程序运行必须模块
import sys
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
# 导入designer工具生成的login模块
from CentralLimitWeget import Ui_MainWindow
from CentralLimitTheorem import *
from Plot import Figure_Canvas
import pyqtgraph as pg


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # 添加登录按钮信号和槽。注意display函数不加小括号()
        self.pushButton_2.clicked.connect(self.simulate)
        # pg.setConfigOptions(leftButtonPan=False)
        # self.setCentralWidget(self.widget)

    def simulate(self):
        if self.comboBox.currentText() == 'Binomial':
            print(self.horizontalSlider.value())
            reality, ideal = binomial(self.horizontalSlider.value(), self.horizontalSlider_2.value() / 100, 10000)
            dr = Figure_Canvas()
            # 实例化一个FigureCanvas
            dr.plot_self(reality, ideal)  # 画图
            graphicscene = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
            graphicscene.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
            self.graphicsView.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
            self.graphicsView.show()  # 最后，调用show方法呈现图形！Voila!!
            # self.setCentralWidget(self.graphicsView)
            # self.graphicsView.setFixedSize(800, 600)
            # self.pw = pg.PlotWidget(self.graphicsView)
            # self.plot_data = self.pw.plot(ideal[0], ideal[1], pen=None)
            # self.pw.show()
            # cavans = binomial(self.horizontalSlider.value(), self.horizontalSlider_2.value()/100, 10000)
            # layout = QMainWindow.QVBoxLayout()
            # layout.addWidget(self.canvas)
            # self.setCentralWidget(cavans)

    # def plot(self):


if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
