from analysis.csv_reader import CSV_Reader
from analysis.preprocessor import Preprocessor
from analysis.feature_selector_linear_regression import FeatureSelectorLinearRegression
from sklearn import linear_model
from analysis.model_builder import ModelBuilder
from analysis.statistics import Statistics

def _build_linear_regression_model():
    model_builder = ModelBuilder() 
    data_reader = CSV_Reader("../data/sample_amsterdam.csv")
    model_builder.setDataReader(data_reader)
    model_builder.addDataProcessor(Preprocessor())
    model_builder.setFeatureSelector(FeatureSelectorLinearRegression())
    model_builder.setModel(linear_model.LinearRegression())
    return model_builder.build()

def _build_statistics():
    data_reader = CSV_Reader("../data/sample_amsterdam.csv")
    df = data_reader.get_data()
    df = Preprocessor().process(df)
    return Statistics(df)
    

linear_regression_model = _build_linear_regression_model()
"""Linear regression model to predict the 'vraagprijs' from the features of a house."""

statistics = _build_statistics()
"""Summary statistics about funda housing market."""
