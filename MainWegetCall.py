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
from PyQt5.QtGui import QIntValidator, QDoubleValidator


# import pyqtgraph as pg


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # TODO Range from 2 to 100, but still has bug
        self.rangemin.setValidator(QIntValidator(2, 100, self))
        self.rangemax.setValidator(QIntValidator(2, 100, self))
        self.rangemax.textChanged.connect(self.setSliderMax)
        self.rangemin.textChanged.connect(self.setSliderMin)
        # TODO Still has bug
        self.pro.setValidator(
            QDoubleValidator(0.0,  1.0, 3, notation=QDoubleValidator.StandardNotation))
        # self.continue_.clicked.connect(self.simulateSecrete)
        self.horizontalSlider.sliderMoved.connect(self.simulateSecrete)
        self.horizontalSlider.sliderMoved.connect(self.setnValue)

    def simulateSecrete(self):
        if self.chooseDistribution.currentText() == 'Binomial':
            print(self.horizontalSlider.value(), float(self.pro.text()))
            reality, ideal = binomial(self.horizontalSlider.value(), float(self.pro.text()))
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

    def setnValue(self):
        self.n_value.setText(str(self.horizontalSlider.value()))

    def setSliderMin(self):
        self.sliderMin.setText(self.rangemin.text())
        self.horizontalSlider.setMinimum(int(self.rangemin.text()))

    def setSliderMax(self):
        self.sliderMax.setText(self.rangemax.text())
        self.horizontalSlider.setMaximum(int(self.rangemax.text()))


if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
