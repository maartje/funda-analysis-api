"""Web API that exposes JSON endpoints for statistic analysis on the Amsterdam housing market."""

from bottle import route, run, request
from request_params_mapper import RequestParamsMapper

from analysis.ml.model_builder import ModelBuilder

from analysis.data_processing.preprocessor import Preprocessor
from analysis.data_processing.csv_reader import CSV_Reader
from data_config import path, columns, index_column

from analysis.ml.feature_selector_linear_regression import FeatureSelectorLinearRegression
from analysis.ml.linear_regression import LinearRegression

@route('/regression')
def regression():
    """ Predict the 'vraagprijs' of a house using linear regression.

    method: GET
    url: /regression
    querystring parameters:
    - postcode
    - buitenoppervlakte
    - ...
    example url: /regression?postcode=1016XE&woonoppervlakte=144&buitenoppervlakte=58
    """
    
    features = RequestParamsMapper().extract_features(request.query.dict)
    vraagprijs = linear_regression_model.predict(features)
    return {'vraagprijs' : vraagprijs}

def build_linear_regression_model():
    model_builder = ModelBuilder() 
    data_reader = CSV_Reader(path, columns, index_column)
    model_builder.setDataReader(data_reader)
    model_builder.addDataProcessor(Preprocessor())
    model_builder.setFeatureSelector(FeatureSelectorLinearRegression())
    model_builder.setModel(LinearRegression())
    model_builder.build()
    return model_builder.model

linear_regression_model = build_linear_regression_model()

run(host='0.0.0.0', port=8080, debug=True)



