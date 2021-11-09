import numpy as np
import math
from scipy import stats
import matplotlib
from scipy.special import factorial

matplotlib.use('Qt5Agg')


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
    x_min = lambda_ - 9 * np.sqrt(lambda_)
    x_max = lambda_ + 9 * np.sqrt(lambda_)

    x_reality = np.linspace(x_min, x_max, int(18 * np.sqrt(lambda_)))

    sample = np.power(lambda_, x_reality) * np.exp(-lambda_) / factorial(x_reality)
    # print(sample)
    if isChecked:
        x_reality = [(x - lambda_) / np.sqrt(lambda_) for x in x_reality]
        # print("old sample:", sample)
        sample = [y * np.sqrt(lambda_) for y in sample]
        # print("new sample", sample)

    if isChecked:
        x = np.arange((x_min - lambda_) / np.sqrt(lambda_), (x_max - lambda_) / np.sqrt(lambda_), 0.1)
        y = norm_pdf(x, 0, 1)
    else:
        x = np.arange(x_min, x_max, 0.1)
        y = norm_pdf(x, lambda_, np.sqrt(lambda_))

    # print(x_reality, sample)
    return (x_reality, sample), (x, y)


def chi2(k, isChecked: bool):
    """绘制卡方分布的概率质量函数"""
    # 坐标最大值
    k_max = 400
    x_min = k - 9 * np.sqrt(2 * k)
    x_max = k + 9 * np.sqrt(2 * k)
    # 统计数据
    x_reality = np.linspace(x_min, x_max, k_max//10)
    sample = stats.chi2.pdf(x_reality, df=k)
    # 理想数据
    x = np.arange(x_min, x_max, 0.1)
    y = norm_pdf(x, k, np.sqrt(2*k))
    if isChecked:
        # 对统计数据标准化
        x_reality = [(x_ - k) / np.sqrt(2*k) for x_ in x_reality]
        sample_ = [y_ * np.sqrt(2*k) for y_ in sample]
        # print("sample:", sample)
        sample = sample_
        # print(sample)
        # 对理想数据标准化
        x = np.arange((x_min - k) / np.sqrt(2*k), (x_max - k) / np.sqrt(2*k), 0.1)
        # print("chi2 x:", x)
        y = norm_pdf(x, 0, 1)

    return (x_reality, sample), (x, y)
