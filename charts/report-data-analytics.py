import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import string


seaborn_styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']

pd.set_option('display.max_columns', 200)
pd.set_option('display.width', 1000)


def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def get_random_bus(count):
    return [random_word(6) for i in range(0, count)]


def get_random_percentage(count):
    return np.random.rand(count)*100


def get_bar_data(count):
    return pd.DataFrame(
        data={
            'client_accuracy': get_random_percentage(count),
            'benchmark_accuracy': get_random_percentage(count)
        },
        index=get_random_bus(count)
    )


def get_time_date(count):
    return pd.DataFrame({
            '0%': get_random_percentage(count),
            '10%': get_random_percentage(count),
            '20%': get_random_percentage(count),
            '30%': get_random_percentage(count),
            '40%': get_random_percentage(count),
            '50%': get_random_percentage(count),
            '60%': get_random_percentage(count),
            '70%': get_random_percentage(count),
            '80%': get_random_percentage(count),
            '90%': get_random_percentage(count)
        },
        index=pd.date_range(start='10/1/2018', end='10/10/2018')
    )


def plot_histogram(column, axis):
    data = get_bar_data(100)
    bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90,100]
    ax = sns.distplot(data[column], bins=bins, hist=True, kde=False, rug=False, ax=axis)
    ax.set_xticks(bins)

    return ax


def plot_line(axis):
    data = get_time_date(10)
    data.plot(kind='line', ax=axis)
    # sns.lineplot(x=data.index, y=['0%', '10%'], data=data)


def plot_multiple_sub_plots():
    grid = plt.GridSpec(2, 2, wspace=0.1)

    plot_histogram('client_accuracy', plt.subplot(grid[0, 0]))
    plot_histogram('benchmark_accuracy', plt.subplot(grid[0, 1]))
    plot_line(plt.subplot(grid[1, :]))


if __name__ == '__main__':
    sns.set_style(seaborn_styles[4])
    plot_multiple_sub_plots()
    # plot_line(None)

    plt.show()
