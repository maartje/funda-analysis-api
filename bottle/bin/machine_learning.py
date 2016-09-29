from csv_reader import CSV_Reader
from preprocessor import Preprocessor
from feature_selector_linear_regression import FeatureSelectorLinearRegression
from linear_regression import LinearRegression

class MachineLearning:
    'Initializes models for machine learning'
    
    def __init__(self):
        feature_selector_lr = FeatureSelectorLinearRegression() 
        self.linear_regression = LinearRegression(feature_selector_lr)
        
    def initialize(self):
        
        # load data
        path_to_csv = "xxx.csv"
        data_reader = CSV_Reader(path_to_csv)
        df_housing_data = data_reader.get_data()

        # clean and transform
        preprocessor = Preprocessor()
        df_housing_data = preprocessor.preprocess(df_housing_data)

        # train the models
        self.linear_regression.fit(df_housing_data) 

