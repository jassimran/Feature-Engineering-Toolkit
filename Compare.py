import numpy as np

class Compare():
    '''Compare class '''
    
    def __init__(self):
        '''Initialization Method'''
        super().__init__()

    def __call__(self, df, label_column, model, pipeline1, pipeline2, metric):
        '''
        Perform data activity here
        :param df: dataframe object
        :param label_column: string, name of the column
        :param model: an instance of sklearn() classifier model 
        :param pipeline1: an instance of Pipeline() class
        :param pipeline2: an instance of Pipeline() class
        :param metric: an instance of sklearn.metrics class
        :return: transformed dataframe object
        '''
        df_pipeline1 = pipeline1(df, label_column)
        df_pipeline2 = pipeline2(df, label_column)
        train_mask = np.random.rand(len(df)) < 0.8

        X_train, y_train, X_test, y_test = self.train_and_test_split(df_pipeline1, train_mask, label_column)
        trained_model_pipeline1, metric_value_pipeline1 = self.train_and_test_model(model, X_train, y_train, X_test, y_test, metric)

        X_train, y_train, X_test, y_test = self.train_and_test_split(df_pipeline2, train_mask, label_column)
        trained_model_pipeline2, metric_value_pipeline2 = self.train_and_test_model(model, X_train, y_train, X_test, y_test, metric)

        return metric_value_pipeline1, metric_value_pipeline2

    def train_and_test_split(self, df, train_mask, label_column):
        '''
        Split the data into train and test
        :param df: dataframe object
        :param train_mask: list of row indices chosen as training data
        :param label_column: string, name of the column
        :return: transformed dataframe object
        '''
        df_train = df[train_mask]
        df_test = df[~train_mask]
        y_train = df_train.loc[:,label_column]
        X_train = df_train.drop(label_column, axis=1).values
        y_test = df_test.loc[:,label_column]
        X_test = df_test.drop(label_column, axis=1).values
        return X_train, y_train, X_test, y_test

    def train_and_test_model(self, model, X_train, y_train, X_test, y_test, metric):
        '''
        Perform data activity here
        :param model: an instance of sklearn() classifier model 
        :param X_train: training data
        :param y_train: training labels
        :param X_test: testing data
        :param y_test: testing labels
        :param metric: an instance of sklearn.metrics class
        :return: transformed dataframe object
        '''
        trained_model = model.fit(X_train, y_train)
        y_pred = trained_model.predict(X_test)
        metric_value = metric(y_test, y_pred)
        return trained_model, metric_value

