# coding=utf-8
import collections
import codecs
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import style
style.use('ggplot')
from pylab import mpl

#mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
mpl.rcParams['axes.unicode_minus'] = False

def draw_bar_chart(dict):

    # fig, ax = plt.subplots(figsize=(15,8))
    fig = plt.figure()
    ax = fig.add_subplot(211)
    width = 0.3

    keys = dict.keys()
    values = dict.values()
    ind = np.arange(len(keys))  # the x locations for the groups
    cab = ax.bar(ind, values, width)

    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(keys)
    plt.show()

if __name__ == '__main__':
    with codecs.open('./text/japanese.txt', 'r','utf-8') as f:
        text = f.read()
    frequency = collections.Counter(text)
    print(frequency.most_common())
    draw_bar_chart(dict(frequency.most_common(100)))
