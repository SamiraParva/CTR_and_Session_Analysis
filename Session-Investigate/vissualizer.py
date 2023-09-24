
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

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

    def plot(self, df:pd.DataFrame, col1:str, col2:str, label1:str, label2:str):
        """
        A user-defined function to plot 2 input column of dataframe

        Parameters:
            df (pd.dataFrame): a dataFrame that is a source for calculating.
            col1 : column 1 name to plot
            col2 : column 2 name to plot
            label1 : label for column 1
            label2 : label for column 2
        Output:
            None
        Returns:
            None
        """
        plt.figure()
        x = df.index
        y1 = df[col1]
        y2 = df[col2]
        plt.plot(x,y1, label=label1)
        plt.plot(x,y2, label=label2)
        plt.xlabel('Index', fontsize=12)
        plt.ylabel('Magnitude', fontsize=12)
        plt.legend()
        plt.show()
