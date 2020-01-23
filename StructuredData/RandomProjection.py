from .FeatureTransformer import FeatureTransformer
import numpy as np
import pandas as pd
from sklearn import random_projection

class RandomProjection(FeatureTransformer):
    '''
    It reduces the dimensionality of data by trading a controlled amount 
    of accuracy for faster processing times.
    '''
    
    def __init__(self, validation = True, n_components = '2', proj_type = 'Gaussian'):
        '''
        Initialization Method
        :param validation: boolean, if validation has to be performed
        :param n_components: int, the output dimensions
        :param proj_type: 'Gaussian' or 'Sparse', for type of random projection
        '''
        super().__init__()
        self.validation = validation
        self.label_column = ''
        self.n_components = n_components
        self.proj_type = proj_type

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
        
        rp = None
        if self.proj_type == 'Gaussian':
            rp = random_projection.GaussianRandomProjection(self.n_components)
        elif self.proj_type == 'Sparse':
            rp = random_projection.SparseRandomProjection(self.n_components)
        
        rp.fit(df_copy)
        columns = [self.proj_type[:3]+'_%i' % i for i in range(self.n_components)]
        df_copy = pd.DataFrame(rp.transform(df_copy), columns=columns, index=df.index)

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
        assert self.n_components > 0, "The RP components must be more than 0"
        assert self.n_components < len(df.columns), "The RP components must be less than max columns"


        return True