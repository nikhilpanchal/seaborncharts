import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)


def plot():
    # The Figure (fig) is the final image that may contain 1 or more Axes.
    # The Axes represent an individual plot (don't confuse this with the word "axis", which refers to the x/y axis of a
    # plot).
    # We use an (or multiple) instances of matplotlib.axes.Axes to render one (or multiple) charts on an instance of
    # matplotlib.figure.Figure
    # The subplots function takes in a bunch of kwargs that help with layout and sizing. The params available are
    # visible on the pyplot.figure() call. subplots() passes them on to figure(). figsize is one example param
    # that takes width and height in inches
    fig, ax = plt.subplots(frameon=False, figsize=(10, 5))

    ax.bar(group_names, group_data)

    # setp will take a list (or many lists) of Matplotlib objects, and attempt to set some style element of each one.
    plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')

    # The Axes instance can be used directly to set properties on the individual chart using Axes.set()
    # The list of settable properties is visible here https://matplotlib.org/api/axes_api.html#the-axes-class
    ax.set(ylim=[0, 150000], ylabel='Total Revenue', xlabel='Company', title='Company Revenue')

    # Labels can be formatted using the FuncFormatter like so
    def currency(val, pos):
        """The two arguments are the value and the tick position"""
        if val >= 1e6:
            s = '${:1.1f}M'.format(val * 1e-6)
        else:
            s = '${:1.0f}K'.format(val * 1e-3)
        return s
    formatter = FuncFormatter(currency)

    # You use the ax object to pass the formatter to the right axis
    ax.yaxis.set_major_formatter(formatter)

    # To add another plot to this chart simple make a call to the ax object for the plot that you want
    # Add a horizontal line on the average revenue value
    ax.axhline(np.mean(group_data), ls='--')

    # Annotate new companies
    for group in [3, 5, 8]:
        ax.text(group, 140000, "New Company", fontsize=10, horizontalalignment="center")


if __name__ == '__main__':
    # plt.style is the way to set the Theme or color-scheme of the plot.
    print(plt.style.available)
    plt.style.use('seaborn-paper')

    # rcParams can be used to control the layout and many other styling features of the plot
    # The complete list of settable parameters is visible by listing out plt.rcParams.keys()
    # print(plt.rcParams.keys())

    plt.rcParams.update({'figure.autolayout': True})

    plot()
    plt.show()
