import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def norm_pdf(x, mu, sigma):
    """正态分布概率密度函数"""
    pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return pdf


def binomial(n, p, size):
    """绘制二项分布的概率质量函数"""
    sample = np.random.binomial(n, p, size=size)  # 产生10000个符合二项分布的随机数
    bins = np.arange(n + 2)
    plt.hist(sample, bins=bins, align='left', density=True, rwidth=0.1)  # 绘制直方图
    x = np.arange(0, n+2, 0.1)
    y = norm_pdf(x, n*p, np.sqrt(n*p*(1-p)))
    return (bins, sample), (x, y)
    # fig = plt.figure()
    # plt.plot(x, y, color='orange', lw=3)
    # # 设置标题和坐标
    # plt.title('Binomial PMF with n={}, p={}'.format(n, p))
    # plt.xlabel('number of successes')
    # plt.ylabel('probability')
    # cavans = FigureCanvas(fig)
    # plt.show()
    # return cavans

binomial(10, 0.5, 10000)
