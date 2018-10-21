import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


seaborn_styles = ['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']

pd.set_option('display.max_columns', 200)
pd.set_option('display.width', 1000)


def load_data():
    df = pd.read_csv('../resources/Pokemon.csv', index_col=0)
    print(df.head(10))

    return df


def scatter(df):
    # lmplot produces a regression of two data variables
    # X and y arguments hold the column names in the dataframe that hold the x and y axis data
    # the data argument takes the dataframe (which contains all the data)
    # hue takes in a column name in the dataframe that tells seaborn to use a different color for each value in that
    # column. This allows us to render a different dimension of information using color
    sns.lmplot(x='Attack', y='Defense', fit_reg=False, hue='Stage', data=df)
    plt.ylim(0, None)
    plt.xlim(0, None)


def box_plot(df):
    sns.set_style(seaborn_styles[1])

    # Renders a box plot of the dataframe data
    # Its much easier to format data in the dataframe rather than use seaborn to selectively plot certain columns
    sns.boxplot(df.drop(['Total', 'Stage', 'Legendary'], axis=1))


def heatmap(df):
    df_numeric = df.drop(['Total', 'Stage', 'Legendary'], axis=1)

    # The heatmap is good to show a plot of matrix data
    # Here we show a plot of the correlation of the different numeric columns with each other
    sns.heatmap(data=df_numeric.corr())


def histogram(df):
    sns.set_style(seaborn_styles[2])
    # plot a histogram that shows the distribution of data by segregating points into buckets
    sns.distplot(df['Attack'], kde=False, hist=True)


def bar(df):
    # Takes in a hue parameter which is the name of a column in the data
    # Passing in the hue parameter produces a grouped bar chart with a bar in each group holding a different color based
    # on the value of the column
    # Side tidbit to note: Colors are a lot nicer without hue specified.
    sns.barplot(x='Type 2', y='Total', data=df)


def factor_plot(df):
    """Demonstrates how you can use seaborn to plot different points, each in its own sub-plot"""

    # col is the key parameter here that determines what column values to use to separate the plots into different
    # subplots
    # Here, all rows with the same value of the Stage column are grouped together. And then each group is plotted in its
    # own sub-plot
    # So instead of using hue to create a grouped bar chart, you can use factorplot and the col param, to create a
    # separate graph for each bar type.
    # You can also change bar to line to plot a line chart in different sub-plots
    sns.factorplot(x='Name', y='Total', data=df, col='Stage', kind='bar')


def line(df):
    sns.set_style(seaborn_styles[0])
    sns.lineplot(x='Stage', y='Speed', data=df.head(3))
    plt.xlim(0, None)
    plt.ylim(0, None)
    plt.xticks(range(1,8))


def plot_subplots(df):
    sns.set_style(seaborn_styles[0])

    fig, axes = plt.subplots(ncols=2, nrows=2)
    sns.lineplot(x='Stage', y='Speed', data=df.head(3), ax=axes[0,0])
    sns.lineplot(x='Stage', y='Attack', data=df.head(3), ax=axes[0,1])
    sns.barplot(x='Type 2', y='Total', data=df,  ax=axes[1,0])

    axes[1,1] = None


if __name__ == '__main__':
    df = load_data()
    # scatter(df)
    # box_plot(df)
    # heatmap(df)
    # histogram(df)
    # bar(df)
    # factor_plot(df)
    # line(df)

    plot_subplots(df)

    plt.show()
