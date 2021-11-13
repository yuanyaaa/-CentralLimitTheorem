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
    e = n * p
    var = n * p * (1 - p)
    x_reality = np.arange(e - 9 * np.sqrt(var), e + 9 * np.sqrt(var))
    sample = []
    for x in x_reality:
        if x < 0:
            sample.append(0)
        else:
            sample.append(math.comb(n, int(x)) * pow(p, int(x)) * pow(1 - p, n - int(x)))
    # sample = [math.comb(n, i) * pow(p, i) * pow(1 - p, n - i) for i in x_reality]
    if isChecked:
        x_reality = [(x - e) / np.sqrt(var) for x in x_reality]
        # print("old sample:", sample)
        sample = [y * np.sqrt(var) for y in sample]
        # print("new sample", sample)
    # else:
    #     sample = [math.comb(n, i) * pow(p, i) * pow(1 - p, n - i) for i in x_reality]

    if isChecked:
        x = np.arange((e - 15 * np.sqrt(var) - e) / np.sqrt(var), (e + 15 * np.sqrt(var) - e) / np.sqrt(var), 0.1)
        y = norm_pdf(x, 0, 1)
    else:
        x = np.arange(e - 15 * np.sqrt(var), e + 15 * np.sqrt(var), 0.1)
        y = norm_pdf(x, e, np.sqrt(var))

    # print(x_reality, sample)
    return (x_reality, sample), (x, y)


def poisson(lambda_, isChecked):
    """绘制泊松分布的概率质量函数"""
    x_min = lambda_ - 9 * np.sqrt(lambda_)
    x_max = lambda_ + 9 * np.sqrt(lambda_)

    x_reality = np.linspace(x_min, x_max, int(9 * np.sqrt(lambda_)))
    sample = []
    for i_ in x_reality:
        tmp = np.exp(-lambda_)
        if i_ <= 0:
            sample.append(0)
        else:
            for index_ in range(1, int(i_)+1):
                tmp = tmp * lambda_ / index_
            sample.append(tmp)
    sample = np.array(sample).flatten()
    # sample = np.power(lambda_, x_reality) * np.exp(-lambda_) / factorial(x_reality)
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
    x_min = k - 9 * np.sqrt(2 * k)
    x_max = k + 9 * np.sqrt(2 * k)
    # 统计数据
    x_reality = np.linspace(x_min, x_max, int(18 * np.sqrt(2 * k)))
    sample = stats.chi2.pdf(x_reality, df=k)
    # 理想数据
    x = np.arange(x_min, x_max, 0.1)
    y = norm_pdf(x, k, np.sqrt(2 * k))
    if isChecked:
        # 对统计数据标准化
        x_reality = [(x_ - k) / np.sqrt(2 * k) for x_ in x_reality]
        sample_ = [y_ * np.sqrt(2 * k) for y_ in sample]
        # print("sample:", sample)
        sample = sample_
        # print(sample)
        # 对理想数据标准化
        x = np.arange((x_min - k) / np.sqrt(2 * k), (x_max - k) / np.sqrt(2 * k), 0.1)
        # print("chi2 x:", x)
        y = norm_pdf(x, 0, 1)

    return (x_reality, sample), (x, y)


def t(k, isChecked: bool):
    """绘制t分布的概率质量函数"""
    x_min = 0 - 9 * np.sqrt(k / (k - 2))
    x_max = 0 + 9 * np.sqrt(k / (k - 2))
    # 统计数据
    x_reality = np.arange(x_min, x_max, 0.1)
    sample = stats.t.pdf(x_reality, df=k)
    # 理想数据
    x = np.arange(x_min, x_max, 0.1)
    y = norm_pdf(x, 0, np.sqrt(k / (k - 2)))
    if isChecked:
        # 对统计数据标准化
        x_reality = [x_ / np.sqrt(k / (k - 2)) for x_ in x_reality]
        sample_ = [y_ * np.sqrt(k / (k - 2)) for y_ in sample]
        # print("sample:", sample)
        sample = sample_
        # print(sample)
        # 对理想数据标准化
        x = np.arange(x_min / np.sqrt(k / (k - 2)), x_max / np.sqrt(k / (k - 2)), 0.1)
        # print("chi2 x:", x)
        y = norm_pdf(x, 0, 1)

    return (x_reality, sample), (x, y)


def f(n1, n2, isChecked: bool):
    """绘制f分布的概率质量函数"""
    # n2 = 1000
    e = n2 / (n2 - 2)
    var = (2 * n2 * n2 * (n1 + n2 - 2)) / (n1 * (n2 - 2) * (n2 - 2) * (n2 - 4))
    x_min = e - 9 * np.sqrt(var)
    x_max = e + 9 * np.sqrt(var)
    # 统计数据
    x_reality = np.arange(x_min, x_max, 0.01)
    sample = stats.f.pdf(x_reality, n1, n2)
    # 理想数据
    x = np.arange(x_min, x_max, 0.01)
    y = norm_pdf(x, e, np.sqrt(var))
    if isChecked:
        # 对统计数据标准化
        x_reality = [(x_ - e) / np.sqrt(var) for x_ in x_reality]
        sample = [y_ * np.sqrt(var) for y_ in sample]

        # 对理想数据标准化
        x = np.arange((x_min - e) / np.sqrt(var), (x_max - e) / np.sqrt(var), 0.1)
        # print("chi2 x:", x)
        y = norm_pdf(x, 0, 1)

    return (x_reality, sample), (x, y)
