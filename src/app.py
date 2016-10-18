"""Web API that exposes JSON endpoints for statistic analysis on the Amsterdam housing market."""

from bottle import route, run, request
from request_params_mapper import request_params_to_features
from init import linear_regression_model, statistics
from response_formatter import dataframe_to_dict 



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

@route('/mean')
def mean():
    select = request.query.dict.get('$select', None)
    groupby = request.query.dict.get('$groupby', None)
    orderby = request.query.dict.get('$orderby', None)
    
    df_means = statistics.mean(select, groupby, orderby)
    
    return {'means' : df_means.to_dict('records')}

run(host='0.0.0.0', port=8080, debug=True)



