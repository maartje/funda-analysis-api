"""Web API that exposes JSON endpoints for statistic analysis on the Amsterdam housing market."""

from bottle import route, run, request
from request_params_mapper import request_params_to_features
from models import linear_regression_model


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
    
    features = request_params_to_features(request.query.dict)
    vraagprijs = linear_regression_model.predict(features)
    return {'vraagprijs' : vraagprijs}


run(host='0.0.0.0', port=8080, debug=True)



