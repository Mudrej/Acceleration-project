# -*- coding: cp1251 -*-

import matplotlib.pyplot as plt

def hist(data):
    keys = list(data.keys())
    values = list(data.values())

    fig, ax = plt.subplots()
    ax.bar(keys, values)
    plt.xticks(rotation=90)
    plt.grid(axis = 'y')

    plt.show()

