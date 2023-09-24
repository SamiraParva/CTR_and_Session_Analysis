import pandas as pd
import numpy as np
import functools as ft
import seaborn as sns
import matplotlib.pyplot as plt

class Vissulizer:

    def frequency_distribution(self, df:pd.DataFrame, col:str):
        """
        A user-defined function to plot histogram of input column of dataframe

        Parameters:
            df (pd.dataFrame): a dataFrame that is a source for calculating.
            col : column name to plot histogram
        Output:

        Returns:
            None
        """
        x = df[col][df[col] >= 0].to_numpy()
        ax = sns.kdeplot(x, shade=False, color='crimson')
        kdeline = ax.lines[0]
        mean = x.mean()
        xs = kdeline.get_xdata()
        ys = kdeline.get_ydata()
        height = np.interp(mean, xs, ys)
        ax.vlines(mean, 0, height, color='crimson', ls=':')
        ax.fill_between(xs, 0, ys, facecolor='crimson', alpha=0.2)
        plt.show()
