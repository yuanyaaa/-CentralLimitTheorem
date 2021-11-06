import pandas as pd
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


def norm_pdf(x, mu, sigma):
    """正态分布概率密度函数"""
    pdf = np.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return pdf


def binomial(n, p, isChecked):
    """绘制二项分布的概率质量函数"""
    # sample = np.random.binomial(n, p, size=size)
    # bins = np.arange(n + 2)
    # plt.hist(sample, bins=bins, align='left', density=True, rwidth=0.1)  # 绘制直方图
    x_reality = np.arange(0, n + 1)
    sample = [math.comb(n, i) * pow(p, i) * pow(1 - p, n - i) for i in x_reality]
    if isChecked:
        x_reality = [(x - n * p) / np.sqrt(n * p * (1 - p)) for x in x_reality]
        print("old sample:", sample)
        sample = [y * np.sqrt(n * p * (1 - p)) for y in sample]
        print("new sample", sample)
    # else:
    #     sample = [math.comb(n, i) * pow(p, i) * pow(1 - p, n - i) for i in x_reality]

    if isChecked:
        x = np.arange((0 - n * p) / np.sqrt(n * p * (1 - p)), (n + 2 - n * p) / np.sqrt(n * p * (1 - p)), 0.1)
        y = norm_pdf(x, 0, 1)
    else:
        x = np.arange(0, n + 2, 0.1)
        y = norm_pdf(x, n * p, np.sqrt(n * p * (1 - p)))

    # print(x_reality, sample)
    return (x_reality, sample), (x, y)


def poisson(lambda_, isChecked):
    """绘制泊松分布的概率质量函数"""
    x_reality = np.arange(0, 21)
    sample = [pow(lambda_, i) * pow(np.e, -lambda_) / math.factorial(i) for i in x_reality]
    if isChecked:
        x_reality = [(x - lambda_) / np.sqrt(lambda_) for x in x_reality]
        # print("old sample:", sample)
        sample = [y * np.sqrt(lambda_) for y in sample]
        # print("new sample", sample)

    if isChecked:
        x = np.arange((0 - lambda_) / np.sqrt(lambda_), (21 - lambda_) / np.sqrt(lambda_), 0.1)
        y = norm_pdf(x, 0, 1)
    else:
        x = np.arange(0, 21, 0.1)
        y = norm_pdf(x, lambda_, np.sqrt(lambda_))

    # print(x_reality, sample)
    return (x_reality, sample), (x, y)
