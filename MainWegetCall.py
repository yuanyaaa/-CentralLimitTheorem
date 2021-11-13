# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
# 导入程序运行必须模块
import sys
import time
# PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# 导入designer工具生成的login模块
from CentralLimitWeget import Ui_MainWindow
from CentralLimitTheorem import *
from Plot import Figure_Canvas
from PyQt5.QtGui import QIntValidator, QDoubleValidator


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        # TODO Range from 2 to 100, but still has bug
        self.rangemin.setValidator(QIntValidator(2, 100, self))
        self.rangemax.setValidator(QIntValidator(2, 200, self))
        self.step.setValidator(QIntValidator(2, 100, self))
        self.chooseDistribution.activated[str].connect(self.chooseDis)

        self.rangemax.textChanged.connect(self.setSliderValue)
        self.rangemin.textChanged.connect(self.setSliderValue)
        # TODO Still has bug
        # self.pro.setValidator(
        #     QDoubleValidator(0.0, 1.0, 3, notation=QDoubleValidator.StandardNotation))
        self.horizontalSlider.sliderMoved.connect(self.simulateSecrete)
        self.horizontalSlider.sliderMoved.connect(self.setnValue)
        self.continue_.clicked.connect(self.simulateContinue)
        # self.work = WorkThread()

    def simulateSecrete(self):
        if self.rangemin.text() == '' or self.rangemax.text() == '' or self.step.text() == '' or (
                self.pro.text() == '' and self.chooseDistribution.currentText() == "Binomial") or (
                self.pro.text() == '' and self.chooseDistribution.currentText() == "F"):
            # print("Error!!!")
            self.reportError("请输入完整数据")
        else:
            if self.chooseDistribution.currentText() == 'Binomial':
                if float(self.pro.text()) > 1 or float(self.pro.text()) <= 0:
                    self.reportError("P的值超出范围")
                    return
                else:
                    reality, ideal = binomial(self.horizontalSlider.value(), float(self.pro.text()),
                                              self.normalization.isChecked())
            elif self.chooseDistribution.currentText() == 'Poisson':
                reality, ideal = poisson(self.horizontalSlider.value(), self.normalization.isChecked())
            elif self.chooseDistribution.currentText() == 'Chi2':
                reality, ideal = chi2(self.horizontalSlider.value(), self.normalization.isChecked())
            elif self.chooseDistribution.currentText() == 'T':
                if self.horizontalSlider.value() <= 2:
                    self.reportError("n的值必须大于2！")
                    return
                else:
                    reality, ideal = t(self.horizontalSlider.value(), self.normalization.isChecked())
            elif self.chooseDistribution.currentText() == 'F':
                if float(self.pro.text()) <= 4:
                    self.reportError("n2必须大于4")
                    return
                else:
                    # print('horizontalSlider', self.horizontalSlider.value())
                    reality, ideal = f(self.horizontalSlider.value(), int(self.pro.text()), self.normalization.isChecked())
            dr = Figure_Canvas()
            # 实例化一个FigureCanvas
            dr.plot_self(reality, ideal, self.chooseDistribution.currentText(), self.normalization.isChecked())  # 画图
            graphicscene = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
            graphicscene.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
            self.graphicsView.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
            self.graphicsView.show()  # 最后，调用show方法呈现图形！Voila!!

    def simulateContinue(self):
        if self.rangemin.text() == '' or self.rangemax.text() == '' or self.step.text() == '' or (
                self.pro.text() == '' and self.chooseDistribution.currentText() == 'Binomial') or (
                self.pro.text() == '' and self.chooseDistribution.currentText() == 'F'):
            # print("Error!!!")
            self.reportError("请输入完整数据")
        else:
            valueMin = int(self.rangemin.text())
            valueMax = int(self.rangemax.text())
            step = int(self.step.text())
            # print(type(valueMin), type(valueMax), type(step))
            for n in range(valueMin, valueMax + 1, step):
                print("the value of current value n:", n)

                if self.chooseDistribution.currentText() == 'Binomial':
                    if float(self.pro.text()) > 1 or float(self.pro.text()) <= 0:
                        self.reportError("P的值超出范围")
                        return
                    else:
                        reality, ideal = binomial(n, float(self.pro.text()), self.normalization.isChecked())
                elif self.chooseDistribution.currentText() == 'Poisson':
                    reality, ideal = poisson(n, self.normalization.isChecked())
                elif self.chooseDistribution.currentText() == 'Chi2':
                    reality, ideal = chi2(n, self.normalization.isChecked())
                elif self.chooseDistribution.currentText() == 'T':
                    if n <= 2:
                        self.reportError("n的值必须大于2！")
                        return
                    else:
                        reality, ideal = t(n, self.normalization.isChecked())
                elif self.chooseDistribution.currentText() == 'F':
                    if float(self.pro.text()) <= 4:
                        self.reportError("n2必须大于4")
                        return
                    else:
                        reality, ideal = f(n, float(self.pro.text()), self.normalization.isChecked())
                dr = Figure_Canvas()
                # 实例化一个FigureCanvas
                dr.plot_self(reality, ideal, self.chooseDistribution.currentText(), self.normalization.isChecked())  # 画图
                graphicscene = QtWidgets.QGraphicsScene()  # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
                graphicscene.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
                self.graphicsView.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
                self.graphicsView.show()  # 最后，调用show方法呈现图形！Voila!!
                QtWidgets.QApplication.processEvents()
                time.sleep(.7)

    def setnValue(self):
        self.n_value.setText(str(self.horizontalSlider.value()))

    # def setSliderMin(self):
    #     if self.rangemin.text() != '':
    #         print("Min:", self.rangemin.text())
    #         self.sliderMin.setText(self.rangemin.text())
    #         self.horizontalSlider.setMinimum(int(self.rangemin.text()))
    #         self.horizontalSlider.setMaximum(int(self.rangemax.text()))

    def setSliderValue(self):
        if self.rangemax.text() != '':
            self.sliderMax.setText(self.rangemax.text())
            self.horizontalSlider.setMaximum(int(self.rangemax.text()))

        if self.rangemin.text() != '':
            self.sliderMin.setText(self.rangemin.text())
            self.horizontalSlider.setMinimum(int(self.rangemin.text()))

    def chooseDis(self, text):
        if text == 'Binomial':
            self.label.setText("The range of n:")
            self.label_4.setText("P")
            self.label_4.show()
            self.pro.show()

        elif text == 'Poisson':
            self.label.setText(u"The range of \u03bb:")
            self.label_4.hide()
            self.pro.hide()

        elif text == 'Chi2':
            self.label.setText("The range of n:")
            self.label_4.hide()
            self.pro.hide()
        elif text == 'T':
            self.label.setText("The range of n:")
            self.label_4.hide()
            self.pro.hide()
        elif text == 'F':
            self.label.setText("The range of n1:")
            self.label_4.setText("n2")
            self.label_4.show()
            self.pro.show()

    def reportError(self, error):
        msgBox = QMessageBox()
        msgBox.setWindowTitle('错误')
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText(error)
        msgBox.exec()


if __name__ == "__main__":
    # 固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    # 初始化
    myWin = MyMainForm()
    # 将窗口控件显示在屏幕上
    myWin.show()
    # 程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
