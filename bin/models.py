from analysis.csv_reader import CSV_Reader
from analysis.preprocessor import Preprocessor
from analysis.feature_selector_linear_regression import FeatureSelectorLinearRegression
from sklearn import linear_model
from analysis.model_builder import ModelBuilder

def build_linear_regression_model():
    model_builder = ModelBuilder() 
    data_reader = CSV_Reader("../data/sample_amsterdam.csv")
    model_builder.setDataReader(data_reader)
    model_builder.addDataProcessor(Preprocessor())
    model_builder.setFeatureSelector(FeatureSelectorLinearRegression())
    model_builder.setModel(linear_model.LinearRegression())
    return model_builder.build()

linear_regression_model = build_linear_regression_model()
