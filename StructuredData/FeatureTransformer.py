class FeatureTransformer():
    '''Wrapper Abstract Class for implementing different functionalities.'''

    def __init__(self):
        '''Initialization Method'''
        super().__init__()

    def __call__(self):
        '''Perform data activity here'''
        return None

    def validate(self):
        '''Validation if the transformation can be applied on the dataframe'''
        return None