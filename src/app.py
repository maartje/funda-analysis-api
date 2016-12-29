"""Web API that exposes JSON endpoints for statistic analysis on the Amsterdam housing market."""

from bottle import route, run, request
from request_params_mapper import RequestParamsMapper
from init import get_regression_model, get_statistics

request_params_mapper = RequestParamsMapper()

@route('/<gemeente>/regression')
def regression(gemeente):
    """ Predict the 'vraagprijs' of a house using linear regression.

    method: GET
    url: /<gemeente>/regression
    querystring parameters:
    - postcode
    - woonoppervlakte
    - ... [optional]
    example url: /amsterdam/regression?postcode=1016XE&woonoppervlakte=64&buitenoppervlakte=5
    """
    
    features = request_params_mapper.get_funda_variables(request.query.dict)
    vraagprijs = get_regression_model(gemeente).predict(features)
    return {'vraagprijs' : vraagprijs}
    
@route('/<gemeente>/mean')
def mean(gemeente):
    """ Return the mean for selected variables.

    method: GET
    url: /<gemeente>/mean
    querystring parameters:
    - $select
    - $groupby [optional]
    - $orderby [optional]
    example url: /amsterdam/mean?$select=ppm2&$select=woonoppervlakte&$groupby=postcode_wijk&$orderby=postcode_wijk
    """
    
    dict = request.query.dict
    select = request_params_mapper.get_select(dict)
    groupby = request_params_mapper.get_groupby(dict)
    orderby = request_params_mapper.get_orderby(dict)

    df_means = get_statistics(gemeente).mean(select, groupby, orderby)
    
    return {'means' : df_means.to_dict('records')}

run(host='0.0.0.0', port=8080, debug=True)



