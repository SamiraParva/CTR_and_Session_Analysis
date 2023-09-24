import pandas as pd
import os
from data_getter import DataGetter
from vissualizer import Vissulizer
from query_data import QueryData


def main():
    # Set parameters
    pd.options.display.max_colwidth  = 500
    pd.options.display.float_format = '{:.0f}'.format
    input_data_path=os.path.abspath("data/input/dataset")
    output_data_path=os.path.abspath("data/output/")
    data_getter = DataGetter(input_data_path)
    visulizer = Vissulizer()
    data_getter.create_datasets()

    query_data=QueryData(data_getter)
    brgroup_case_2 = query_data.brgroup_case_2
    brgroup_case_2.columns = brgroup_case_2.columns.str.replace(' ', '')
    brgroup_case_2 = brgroup_case_2.dropna()
    print(brgroup_case_2.shape)
    # stop 10 best and worst
    query_data.items_performance_analysis(brgroup_case_2, output_data_path, 10, 0.4)
    # the relationship between the average displayed position and the CTR 
    df = query_data.most_clicked_item_analysis(brgroup_case_2, output_data_path, 1000)
    #correlation value between CTR and avg_displayed_position for most 1000 clicked items
    corr = df['CTR'].corr(df['avg_displayed_position'])
    print(corr)
    # visulizer.frequency_distribution(df, 'CTR')
    # visulizer.frequency_distribution(df, 'avg_displayed_position')
    sorted_df = df.sort_values(by=['avg_displayed_position'], ascending=True).reset_index(drop=True)
    visulizer.plot(sorted_df, 'CTR', 'avg_displayed_position', 'CTR', 'Average Displayed Position'  )

if __name__ == "__main__":
    main()