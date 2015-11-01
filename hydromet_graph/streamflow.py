import seaborn as sns
from matplotlib import pyplot as plt

def hist_boxplot(data, obs = None):
    """
        Plot histograms and boxplots of supplied pandas.DataFrame of data.

        :param data: The data to be plotted, typically forecast and reference distributions.
        :type data: pandas.DataFrame
        :param obs: Observed value to plot as vertical line on histogram and boxplot subplots if not None. Defaults to None.
        :type obs: float

        :returns: (matplotlib.figure.Figure, matplotlib.axes.Axes)
    """

    fig, axes = plt.subplots(nrows=2, ncols=1)

    data.plot(kind='hist', bins=25, alpha=0.6, ax=axes[0])

    sns.boxplot(data = data, orient='h', ax = axes[1])

    if obs is not None:
        for ax in axes:
            obs_line = ax.vlines(obs, *ax.get_ylim(), linestyle='dashed')
            obs_line.set_label('Observed')
            ax.legend()

    fig.tight_layout()

    return fig, axes
