from csv_reader import CSV_Reader
"""Models for predicting housing prices trained on Funda data set."""

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
        path_to_csv = "xxx.csv"
        data_reader = CSV_Reader(path_to_csv)
        df_housing_data = data_reader.get_data()

        # clean and transform
        preprocessor = Preprocessor()
        df_housing_data = preprocessor.preprocess(df_housing_data)

        # train the models
        self.linear_regression.fit(df_housing_data) 

