from .FeatureTransformer import FeatureTransformer
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class Normalize(FeatureTransformer):
    '''Min max normalize the individual columns'''
    
    def __init__(self, apply_columns = [], validation = True):
        '''
        Initialization Method
        :param apply_columns: which columns the transformation has to be applied
        :param validation: boolean, if validation has to be performed
        '''
        super().__init__()
        self.apply_columns = apply_columns
        self.validation = validation
        self.label_column = ''

    def __call__(self, df, label_column = ''):
        '''
        Perform data activity here
        :param df: dataframe object
        :param label_column: string, name of the column
        :return: transformed dataframe object
        '''
        if not self.apply_columns:
            self.apply_columns = df.columns

        self.label_column = label_column
        if not self.label_column:
            self.label_column = df.columns[-1]
        
        if self.validation:
            assert self.validate(df)

        df_copy = df.copy()
        label_values = df_copy[label_column]
        df_copy = df_copy.drop(label_column, axis=1)

        min_max_scaler = MinMaxScaler()
        df_copy[self.apply_columns] = min_max_scaler.fit_transform(df_copy[self.apply_columns])

        df_copy[label_column] = label_values
        return df_copy

    def validate(self, df):
        '''
        Validation if the transformation can be applied on the dataframe
        :param df: dataframe object
        :return: boolean, can or cannot be applied
        '''
        assert df[self.label_column].dtype in ['int', 'category'], "Label Column is not Categorical"

        numerical_columns = df.select_dtypes(include=['float']).dtypes
        for column in self.apply_columns:
            assert column in numerical_columns, column + " is not a categorical column"

        for column in self.apply_columns:
            assert not df[column].isna().sum() > 0, "The column has missing values, apply MissingValues transform first"
        return True