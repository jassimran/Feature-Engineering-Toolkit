from .FeatureTransformer import FeatureTransformer
import numpy as np
import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import Binarizer

class Discretization(FeatureTransformer):
    '''
    It's a way to partition continuous features into discrete values.
    '''
    
    def __init__(self, validation = True, n_bins = '2', disc_type = 'KBins'):
        '''
        Initialization Method
        :param validation: boolean, if validation has to be performed
        :param n_bins: int, the number of bins
        :param proj_type: 'KBins' or 'Binarizer', for type of Dicretization
        '''
        super().__init__()
        self.validation = validation
        self.label_column = ''
        self.n_bins = n_bins
        self.disc_type = disc_type

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
        
        disc = None
        if self.proj_type == 'KBins':
            disc = KBinsDiscretizer(self.n_bins, encode='ordinal', strategy='uniform')
        elif self.proj_type == 'Binarizer':
            disc = Binarizer()
        
        df_copy = disc.fit_transform(df_copy)
        df_copy[label_column] = label_values
        return df_copy

    def validate(self, df):
        '''
        Validation if the transformation can be applied on the dataframe
        :param df: dataframe object
        :return: boolean, can or cannot be applied
        '''
        assert not df.empty
        assert not df.isnull().sum().sum() > 0, "The data has missing values, apply MissingValues transform first"
        assert self.n_bins > 0, "The RP components must be more than 0"

        return True