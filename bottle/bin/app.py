"""Web API that exposes JSON endpoints for statistic analysis on the Amsterdam housing market."""

from bottle import route, run, request
from linear_regression import LinearRegression
from machine_learning import MachineLearning

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
    vraagprijs = ml.linear_regression.predict(request.query.dict)
    return {'vraagprijs' : vraagprijs}


ml = MachineLearning()
ml.initialize()

run(host='0.0.0.0', port=8080, debug=True)



