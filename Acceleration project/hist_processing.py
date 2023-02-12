# -*- coding: cp1251 -*-

import matplotlib.pyplot as plt

def hist(data):
    values = [list(data.values())[i][0] for i in range(len(data.keys()))]

    fig, ax = plt.subplots()
    ax.bar(data.keys(), values)
    plt.xticks(rotation=90)
    plt.grid(axis = 'y')

    plt.show()

