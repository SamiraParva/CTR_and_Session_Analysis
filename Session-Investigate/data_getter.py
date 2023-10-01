import tarfile
import os
from os import listdir
from os.path import isfile, join
import pandas as pd


class DataGetter:

    def __init__(self,input_data_path: str):
        self.input_data_path=input_data_path

    def unzip_data(self):
        '''DocString for this function'''
        with tarfile.open(self.input_zip_file, "r") as zip_ref:
            zip_ref.extractall("data/input/")
            zip_ref.close()


    def get_file(self,input_file : str)-> str:
        '''DocString for this function'''
        path = self.input_data_path
        for file in listdir(path):
            if join(path, file)==join(path,input_file):
                return file


    def data_into_df(self,input_file: str)-> pd.DataFrame:
        files = self.get_file(input_file)
        df = pd.read_csv(join(self.input_data_path,files))
        return df


    def create_datasets(self):
        brgroup_case_1 = self.data_into_df('data_analysis_ctr2.csv')
        return brgroup_case_1


