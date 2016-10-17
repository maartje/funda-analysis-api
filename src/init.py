from analysis.csv_reader import CSV_Reader
from analysis.preprocessors.row_filter import RowFilter
from analysis.preprocessors.stats_fields_processor import StatsFieldsProcessor
from analysis.feature_selector_linear_regression import FeatureSelectorLinearRegression
from sklearn import linear_model
from analysis.model_builder import ModelBuilder
from analysis.statistics import Statistics

def _build_linear_regression_model():
    columns = [
        'id',
        'postcode_wijk',
        'vraagprijs',
        'woonoppervlakte'
    ]
    index_column = 'id'
    dtype={'postcode_wijk': str}
    data_reader = CSV_Reader("../data/sample_amsterdam.csv", columns, index_column, dtype)
    model_builder = ModelBuilder() 
    model_builder.setDataReader(data_reader)
    required_fields = ['vraagprijs', 'woonoppervlakte', 'postcode_wijk']
    model_builder.addDataProcessor(RowFilter(required_fields))
    model_builder.setFeatureSelector(FeatureSelectorLinearRegression())
    model_builder.setModel(linear_model.LinearRegression())
    return model_builder.build()

def _build_statistics():
    columns = [
        'RowKey',
        'vraagprijs',
        'woonoppervlakte',
        'woningtype',
        'aangeboden_sinds',
        'postcode_wijk',
        'verkoopdatum'
    ]    
    index_column = 'RowKey'
    dtype={'postcode_wijk': str}
    data_reader = CSV_Reader("../data/funda_sold_amsterdam.csv", columns, index_column, dtype)
    df = data_reader.get_data()
    required_fields = [
        'vraagprijs',
        'woonoppervlakte',
        'woningtype',
        'aangeboden_sinds',
        'postcode_wijk',
        'verkoopdatum'
    ]
    rowfilter = RowFilter(required_fields)
    df = rowfilter.process(df)
    df = StatsFieldsProcessor().process(df)
    return Statistics(df)
    

linear_regression_model = _build_linear_regression_model()
"""Linear regression model to predict the 'vraagprijs' from the features of a house."""

statistics = _build_statistics()
"""Summary statistics about funda housing market."""
