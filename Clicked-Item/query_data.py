
from data_getter import DataGetter
import numpy as np
import pandas as pd

class QueryData(DataGetter):
    """
    This is a class for querying data based on proposed KPIs .

    Attributes:
        dg (object): object of DataGetter class.
    """
    def __init__(self, dg):
        """
        The constructor for QueryData class.

        Parameters:
          dg (object): object of DataGetter class.
        """
        self.brgroup_case_1 = dg.create_datasets()

    def JoinDfs(self,leftDf:pd.DataFrame,rightDf:pd.DataFrame,leftkey:str,rightkey:str,howjoin:str)-> pd.DataFrame:
        """
        A user-defined function to execute join operation on given dataframes.

        Parameters:
            leftDf (pd.dataFrame): a dataFrame that is indicating a dataset on the left side of the join operation.
            rightDf (pd.dataFrame): a dataFrame that is indicating a dataset on the right side of the join operation.
            leftkey (string): a name of a column as a join key that belongs to a dataset on the left side of the join operation.
            rightkey (string): a name of a column as a join key that belongs to a dataset on the right side of the join operation.
            howjoin (string): a name of a type of join operation.

        Returns:
            (pd.dataFrame): a dataFrame that is a result of a merge operation on two given dataFrames.
        """
        return pd.merge(leftDf,rightDf,how=howjoin,left_on=leftkey,right_on=rightkey)

    def unpivot_and_replace_11_with_median(self, df:pd.DataFrame, col: str):
        """
        A user-defined function to unpivot input df based on input col and replace unknown value of -11 of input col with median of same partition by item_id col

        Parameters:
            df (pd.dataFrame): a dataFrame
            col (string): a name of a column for unpivot

        Returns:
            (pd.dataFrame): a dataFrame that unpivoted and replaced missing values by col
        """
        brgroup_case_1 = df.assign(clicked_displayed_positions = df.clicked_displayed_positions.str.split(';')).explode(col)
        brgroup_case_1[col] = pd.to_numeric(brgroup_case_1[col])
        brgroup_case_1[col].replace(-11, np.nan, inplace=True)
        brgroup_case_1['median_for_11'] = brgroup_case_1.groupby(['item_id'], observed=True)[col].transform('median').round()
        brgroup_case_1[col] = brgroup_case_1[col].fillna(brgroup_case_1["median_for_11"])

        return brgroup_case_1

    def distribution_and_share_of_top25_pos(self, df:pd.DataFrame, output_data_path: str):
        """
        A user-defined function to unpivot input df based on input col and replace unknown value of -11 of input col with median of same partition by item_id col

        Parameters:
            df (pd.dataFrame): a dataFrame
            col (string): output path for csv output

        output:
            output12.csv a scv containing licked_displayed_positions,counts_click_top_25,share_prec column
        Returns:
            None
        """
        tbrgroup_case_12 = df[['item_id', 'impressions', 'clicked_displayed_positions']][df['clicked_displayed_positions'].between(0, 24)].groupby(['clicked_displayed_positions']).size().reset_index(name='counts_click_top_25')
        tbrgroup_case_12['share_prec'] = tbrgroup_case_12['counts_click_top_25'] / tbrgroup_case_12['counts_click_top_25'].sum()
        tbrgroup_case_12.to_csv(output_data_path+ '/output12.csv')

    def top_pos_half_of_the_click_outs_made(self, df:pd.DataFrame, output_data_path: str):
        """
        A user-defined function to calculate top position in which Half of the click-outs made

        Parameters:
            df (pd.dataFrame): a dataFrame
            col (string): output path for csv output

        output:
            output122.csv a scv containing licked_displayed_positions,counts_click_top_25,share_prec column
        Returns:
            None
        """
        tbrgroup_case_122 = df[['item_id', 'impressions', 'clicked_displayed_positions']][df['clicked_displayed_positions'] == 0].groupby(['item_id'])['clicked_displayed_positions'].count().reset_index(name='counts_click_0')
        #print(tbrgroup_case_122['counts_click_0'].describe(include='all'))
        tbrgroup_case_123 = df[['item_id', 'clicked_displayed_positions']][df['clicked_displayed_positions'].between(0, 24)].groupby(['clicked_displayed_positions']).size().reset_index(name='position_cliced')
        tbrgroup_case_123['Cumulative_position_cliced'] = tbrgroup_case_123['position_cliced'].cumsum()
        tbrgroup_case_123['Cumulative_position_cliced_scaled'] = tbrgroup_case_123['Cumulative_position_cliced'] / (tbrgroup_case_123['position_cliced'].sum()/2)
        minScale = tbrgroup_case_123[tbrgroup_case_123['Cumulative_position_cliced_scaled'] >= 1].min()
        outputDF = tbrgroup_case_123[tbrgroup_case_123['Cumulative_position_cliced_scaled'] <= minScale['Cumulative_position_cliced_scaled']]
        outputDF.to_csv(output_data_path+ '/output122.csv')

    def create_dataset_containing_avg_display_pos_and_clicked_one(self, df:pd.DataFrame):
        """
        A user-defined function to calculate dataset containing avg display position and clicked one

        Parameters:
            df (pd.dataFrame): a dataFrame

        output:

        Returns:
            (pd.dataFrame): a dataFrame that containing avg display position and clicked one
        """
        tbrgroup_case_13 = df[['item_id', 'avg_impressed_position', 'clicked_displayed_positions']].groupby('item_id')['clicked_displayed_positions'].mean().reset_index(name='avg_clicked_displayed_positions')
        tbrgroup_case_131= self.JoinDfs(howjoin='inner', leftDf=self.brgroup_case_1[['item_id', "avg_impressed_position"]], rightDf=tbrgroup_case_13,  leftkey='item_id', rightkey='item_id')

        return tbrgroup_case_131
