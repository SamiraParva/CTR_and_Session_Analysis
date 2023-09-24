from heapq import merge
import inline as inline
import pandas as pd
import os
from data_getter import DataGetter
from query_data import QueryData
from visualizer import Visualizer


def main():
    pd.options.display.max_colwidth  = 500
    pd.options.display.float_format = '{:.0f}'.format
    input_data_path=os.path.abspath("data/input/dataset")
    output_data_path=os.path.abspath("data/output")
    data_getter = DataGetter(input_data_path)
    visulizer = Visualizer()
    data_getter.create_datasets()

    query_data=QueryData(data_getter)
    brgroup_case_1 = query_data.brgroup_case_1
    # calculate CTR and add it to main DF
    brgroup_case_1['CTR'] = brgroup_case_1['clicks'] / brgroup_case_1['impressions']
    overall_avg_ctr = brgroup_case_1['CTR'].mean()

    # the CTR of each item
    print(overall_avg_ctr, brgroup_case_1['CTR'].median())
    # plot frequency_distribution of CTR col
    visulizer.frequency_distribution(brgroup_case_1, 'CTR')


    unpivot_and_replace_11_with_median_df = query_data.unpivot_and_replace_11_with_median(brgroup_case_1, 'clicked_displayed_positions')


    #the relationship between the average displayed position and the clicked displayed position
    finalDF = query_data.create_dataset_containing_avg_display_pos_and_clicked_one(unpivot_and_replace_11_with_median_df)
    print(finalDF['avg_impressed_position'].corr(finalDF['avg_clicked_displayed_positions']))
    print(finalDF[['avg_impressed_position']].var())
    print(finalDF[['avg_clicked_displayed_positions']].var())
    visulizer.frequency_distribution(finalDF, 'avg_impressed_position' )
    visulizer.frequency_distribution(finalDF, 'avg_clicked_displayed_positions')


if __name__ == "__main__":
    main()