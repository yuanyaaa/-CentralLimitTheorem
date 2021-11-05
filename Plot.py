import matplotlib
from matplotlib.figure import Figure

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


# 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot lib的关键
class Figure_Canvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height),
                     dpi=dpi)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure

        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.setParent(parent)

        self.axes = fig.add_subplot(111)  # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

    def plot_self(self, reality, ideal):
        self.axes.hist(reality[1], bins=reality[0], align='left', density=True, rwidth=0.1)  # 绘制直方图
        self.axes.plot(ideal[0], ideal[1], color='orange', lw=3)
        # 设置标题和坐标
        # self.axes.title('Binomial PMF with n={}, p={}'.format(n, p))
        # self.axes.xlabel('number of successes')
        # self.axes.ylabel('probability')
