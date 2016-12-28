from analysis.funda_data_loader import FundaDataLoader
from analysis.datareaders.csv_reader import CSV_Reader
from analysis.feature_selector_linear_regression import FeatureSelectorLinearRegression
from analysis.preprocessors.filter_missing_values import FilterMissingValues
from sklearn import linear_model
from analysis.model_builder import ModelBuilder
from analysis.statistics import Statistics

def _build_linear_regression_model(paths_to_csv):
    variables = [
        'postcode_wijk',
        'vraagprijs',
        'woonoppervlakte'
    ]
    data_reader = CSV_Reader(paths_to_csv)
    fundaDataLoader = FundaDataLoader(data_reader)
    model_builder = ModelBuilder()
    model_builder.setSelectedVariables(variables)
    model_builder.setDataLoader(fundaDataLoader)
    model_builder.addDataProcessor(FilterMissingValues(variables))
    model_builder.setFeatureSelector(FeatureSelectorLinearRegression())
    model_builder.setModel(linear_model.LinearRegression())
    return model_builder.build()

def _build_statistics(paths_to_csv):
    data_reader = CSV_Reader(paths_to_csv)
    fundaDataLoader = FundaDataLoader(data_reader)
    return Statistics(fundaDataLoader)
    
def get_regression_model(gemeente):
    """ Return linear regression model to predict the 'vraagprijs' from the features of a house."""
    return _regression_models.get(gemeente)

def get_statistics(gemeente):
    """ Return summary statistics about funda housing market."""
    return _build_statistics(_get_csv_paths(gemeente))

def _get_csv_paths(gemeente = None):
    if gemeente:
        return ["../data/funda_sold_{}.csv".format(gemeente.lower())]
    return ["../data/funda_sold_{}.csv".format(gemeente) for gemeente in ['amsterdam', 'utrecht', 'rotterdam', 'denhaag']]

_regression_models = { gemeente: _build_linear_regression_model(_get_csv_paths(gemeente)) for gemeente in ['amsterdam', 'utrecht', 'rotterdam', 'denhaag']}
