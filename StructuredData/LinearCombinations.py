from .FeatureTransformer import FeatureTransformer
import numpy as np

class LinearCombinations(FeatureTransformer):
    '''Lineraly combine features to get new features.'''
    
    def __init__(self, validation = True, imputation_type = None ):
        '''
        Initialization Method
        :param validation: boolean, if validation has to be performed
        '''
        super().__init__()
        self.validation = validation
        self.label_column = ''

    def __call__(self, df, label_column):
        '''
        Perform data activity here
        :param df: dataframe object
        :param label_column: string, name of the column
        :return: transformed dataframe object
        '''
        self.label_column = label_column
        if not self.label_column:
            self.label_column = df.columns[-1]
        
        if self.validation:
            assert self.validate(df)
        
        df_copy = df.copy()
        label_values = df_copy[label_column]
        df_copy = df_copy.drop(label_column, axis=1)
        if self.imputation_type == 'median':
            df_copy.fillna(df_copy.median(), inplace=True)
        elif self.imputation_type == 'mean':
            df_copy.fillna(df_copy.mean(), inplace=True)
        df_copy[label_column] = label_values
        return df_copy

    def validate(self, df):
        '''
        Validation if the transformation can be applied on the dataframe
        :param df: dataframe object
        :return: boolean, can or cannot be applied
        '''
        assert not df.empty

        return True