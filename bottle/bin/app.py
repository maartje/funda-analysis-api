"""Web API that exposes JSON endpoints for statistic analysis on the Amsterdam housing market."""

from bottle import route, run, request
from machine_learning import MachineLearning
from request_params_mapper import RequestParamsMapper

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
    vraagprijs = ml.linear_regression.predict(features)
    return {'vraagprijs' : vraagprijs}


ml = MachineLearning()
ml.initialize()

run(host='0.0.0.0', port=8080, debug=True)



