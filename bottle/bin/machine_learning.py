from csv_reader import CSV_Reader
from funda_data import columns, index_column
"""Processing pipeline that results in predictive models trained on Funda data set."""

from preprocessor import Preprocessor
from feature_selector_linear_regression import FeatureSelectorLinearRegression
from linear_regression import LinearRegression

class MachineLearning:
    """Models for predicting housing prices trained on funda data set."""
    
    def __init__(self):
        """Initialize models"""
        feature_selector_lr = FeatureSelectorLinearRegression() 
        self.linear_regression = LinearRegression(feature_selector_lr)
        
    def initialize(self):
        """Fit models on funda data."""
        
        # load data
        path_to_csv = "sample_amsterdam.csv"
        data_reader = CSV_Reader(path_to_csv, columns, index_column)
        df_housing_data = data_reader.get_data()
        print df_housing_data[0:1]

        # clean and transform
        preprocessor = Preprocessor()
        df_housing_data = preprocessor.preprocess(df_housing_data)

        # train the models
        self.linear_regression.fit(df_housing_data) 

