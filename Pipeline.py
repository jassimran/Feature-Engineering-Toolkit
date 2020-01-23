class Pipeline():
    '''Pipeline class '''
    
    def __init__(self, transformsList):
        '''
        Initialization Method
        :param transformsList: list of transformations that could be performed
        '''
        self.transformsList = transformsList
        super().__init__()

    def __call__(self, df, label_column):
        '''
        Perform data activity here
        :param df: dataframe object
        :param label_column: string, name of the column
        :return: transformed dataframe object
        '''
        for transform in self.transformsList:
            df = transform(df, label_column)
        return df




