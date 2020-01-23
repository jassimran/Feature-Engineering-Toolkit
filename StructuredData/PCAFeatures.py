from .FeatureTransformer import FeatureTransformer
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA

class PCAFeatures(FeatureTransformer):
    '''
    Linear dimensionality reduction using Singular Value Decomposition 
    of the data to project it to a lower dimensional space
    '''
    
    def __init__(self, validation = True, n_components = 2):
        '''
        Initialization Method
        :param validation: boolean, if validation has to be performed
        '''
        super().__init__()
        self.validation = validation
        self.label_column = ''
        self.n_components = n_components

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
        pca = PCA(self.n_components)
        pca.fit(df_copy)

        columns = ['pca_%i' % i for i in range(self.n_components)]
        df_copy = pd.DataFrame(pca.transform(df_copy), columns=columns, index=df.index)
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
        assert self.n_components > 0, "The PCA components must be more than 0"
        assert self.n_components < len(df.columns), "The PCA components must be less than max columns"


        return True