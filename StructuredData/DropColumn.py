from .FeatureTransformer import FeatureTransformer
import numpy as np

class DropColumn(FeatureTransformer):
    '''Drop a column if its not needed'''
    
    def __init__(self, validation = True):
        '''
        Initialization Method
        :param validation: boolean, if validation has to be performed
        '''
        super().__init__()
        self.validation = validation
        self.label_column = ''
        self.columns_to_drop = []

    def __call__(self, df, label_column, columns_to_drop):
        '''
        Perform data activity here
        :param df: dataframe object
        :param label_column: string, name of the column
        :param columns_to_drop: list, list of names of the columns to be dropped
        :return: transformed dataframe object
        '''
        self.label_column = label_column
        if not self.label_column:
            self.label_column = df.columns[-1]
        
        if self.validation:
            assert self.validate(df)
        
        df_copy = df.copy()
        df_copy = df_copy.drop(columns_to_drop, axis=1)
        return df_copy

    def validate(self, df):
        '''
        Validation if the transformation can be applied on the dataframe
        :param df: dataframe object
        :return: boolean, can or cannot be applied
        '''
        assert not df.empty

        return True