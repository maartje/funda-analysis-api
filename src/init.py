from analysis.funda_data_loader import FundaDataLoader
from analysis.datareaders.csv_reader import CSV_Reader
from analysis.feature_selector_linear_regression import FeatureSelectorLinearRegression
from analysis.preprocessors.filter_missing_values import FilterMissingValues
from sklearn import linear_model
from analysis.model_builder import ModelBuilder
from analysis.statistics import Statistics

def _build_linear_regression_model():
    variables = [
        'postcode_wijk',
        'vraagprijs',
        'woonoppervlakte'
    ]
    data_reader = CSV_Reader("../data/funda_sold_amsterdam.csv")
    fundaDataLoader = FundaDataLoader(data_reader)
    model_builder = ModelBuilder()
    model_builder.setSelectedVariables(variables)
    model_builder.setDataLoader(fundaDataLoader)
    model_builder.addDataProcessor(FilterMissingValues(variables))
    model_builder.setFeatureSelector(FeatureSelectorLinearRegression())
    model_builder.setModel(linear_model.LinearRegression())
    return model_builder.build()

def _build_statistics():
    data_reader = CSV_Reader("../data/funda_sold_amsterdam.csv")
    fundaDataLoader = FundaDataLoader(data_reader)
    return Statistics(fundaDataLoader)
    

linear_regression_model = _build_linear_regression_model()
"""Linear regression model to predict the 'vraagprijs' from the features of a house."""

statistics = _build_statistics()
"""Summary statistics about funda housing market."""
