from .FeatureTransformer import FeatureTransformer
import numpy as np

class ChangeIndex(FeatureTransformer):
    '''Fill the missing values in your data.'''
    
    def __init__(self, validation = True):
        '''
        Initialization Method
        :param validation: boolean, if validation has to be performed
        '''
        super().__init__()
        self.validation = validation
        self.label_column = ''
        self.new_index = ''

    def __call__(self, df, label_column, new_index ):
        '''
        Perform data activity here
        :param df: dataframe object
        :param label_column: string, name of the column 
        :param new_index: string, name of the column on which new index has to be created.
        :return: transformed dataframe object
        '''
        self.label_column = label_column
        self.new_index = new_index
        if not self.label_column:
            self.label_column = df.columns[-1]
        
        if self.validation:
            assert self.validate(df)
        
        df_copy = df.copy()
        df_copy = df_copy.set_index(new_index)
        return df_copy

    def validate(self, df):
        '''
        Validation if the transformation can be applied on the dataframe
        :param df: dataframe object
        :return: boolean, can or cannot be applied
        '''
        assert not df.empty

        assert df[self.new_index].is_unique

        return True