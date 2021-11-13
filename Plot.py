import matplotlib
from matplotlib.figure import Figure

matplotlib.use("Qt5Agg")  # 声明使用QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


# 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot lib的关键
class Figure_Canvas(FigureCanvas):

    def __init__(self, parent=None, width=8.5, height=5.18, dpi=100):
        fig = Figure(figsize=(width, height),
                     dpi=dpi)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure

        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.setParent(parent)

        self.axes = fig.add_subplot(111)  # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

    def plot_self(self, reality, ideal, distribution: str, isChecked: bool):
        # if distribution == "Chi2" or distribution == "T" or distribution == 'F':
        #     self.axes.plot(reality[0], reality[1], color='blue', lw=4, label="Reality Data")
        # else:
        #     self.axes.bar(x=reality[0], height=reality[1])  # 绘制直方图
        # self.axes.plot(ideal[0], ideal[1], color='orange', lw=3, label="Ideal Data")

        if distribution == 'Binomial':
            self.axes.bar(x=reality[0], height=reality[1])
            if isChecked:
                self.axes.plot(ideal[0], ideal[1], color='orange', lw=3, label="N(0, 1)")
            else:
                self.axes.plot(ideal[0], ideal[1], color='orange', lw=3, label="N(np, np(1-p))")
            self.axes.set_title("B(n,p) with n increasing")
            self.axes.set_xlabel("x")
            self.axes.set_ylabel("p(x)")
        elif distribution == 'Poisson':
            self.axes.bar(x=reality[0], height=reality[1])
            if isChecked:
                self.axes.plot(ideal[0], ideal[1], color='orange', lw=3, label=r"$N(0, 1)$")
            else:
                self.axes.plot(ideal[0], ideal[1], color='orange', lw=3, label=r"$N(\lambda, \lambda)$")
            self.axes.set_title("P(\u03bb) with \u03bb increasing")
            self.axes.set_xlabel("x")
            self.axes.set_ylabel("p(x)")
        elif distribution == 'Chi2':
            if isChecked:
                self.axes.plot(reality[0], reality[1], color='blue', lw=4, label=r"$f((\chi^2-n)/\sqrt{2n})$")
                self.axes.plot(ideal[0], ideal[1], color='orange', lw=3, label=r"$N(0, 1)$")
            else:
                self.axes.plot(reality[0], reality[1], color='blue', lw=4, label="chi2")
                self.axes.plot(ideal[0], ideal[1], color='orange', lw=3, label="N(n, 2n))")
            self.axes.set_title("Chi2(n) with n increasing")
            self.axes.set_xlabel("x")
            self.axes.set_ylabel("p(x)")
        elif distribution == 'T':
            if isChecked:
                self.axes.plot(reality[0], reality[1], color='blue', lw=4, label=r"$f((T-0)/\sqrt{n/(n-2)}$")
                self.axes.plot(ideal[0], ideal[1], color='orange', lw=3, label=r"$N(0, 1)$")
            else:
                self.axes.plot(reality[0], reality[1], color='blue', lw=4, label=r"$T(n)$")
                self.axes.plot(ideal[0], ideal[1], color='orange', lw=3, label=r"$N(0, \sqrt{n/(n-2)})$")
            self.axes.set_title("T(n) with n increasing")
            self.axes.set_xlabel("x")
            self.axes.set_ylabel("p(x)")
        elif distribution == 'F':
            if isChecked:
                self.axes.plot(reality[0], reality[1], color='blue', lw=4, label=r"$f(\frac{F-\alpha}{\sqrt{\beta}})(\alpha=\frac{n_2}{n_2-2}, \beta=\frac{2n_2^2(n_1+n_2-2)}{n_1(n_2)^2(n_2-4)})$")
                self.axes.plot(ideal[0], ideal[1], color='orange', lw=3, label=r"$N(0, 1)$")
            else:
                self.axes.plot(reality[0], reality[1], color='blue', lw=4, label=r"$F(n_1,n_2)$")
                self.axes.plot(ideal[0], ideal[1], color='orange', lw=3, label=r"$N(\alpha, \beta)(\alpha=\frac{n_2}{n_2-2}, \beta=\frac{2n_2^2(n_1+n_2-2)}{n_1(n_2)^2(n_2-4)})$")
            self.axes.set_title("F(n1,n2) with n increasing")
            self.axes.set_xlabel("x")
            self.axes.set_ylabel("p(x)")
        self.axes.legend()
        # 设置标题和坐标
        # self.axes.title('Binomial PMF with n={}, p={}'.format(n, p))
        # self.axes.xlabel('number of successes')
        # self.axes.ylabel('probability')