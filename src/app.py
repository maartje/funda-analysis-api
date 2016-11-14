"""Web API that exposes JSON endpoints for statistic analysis on the Amsterdam housing market."""

from bottle import route, run, request
from request_params_mapper import RequestParamsMapper
from init import linear_regression_model, get_statistics
from response_formatter import dataframe_to_dict 

request_params_mapper = RequestParamsMapper()

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
    
    features = request_params_mapper.get_funda_variables(request.query.dict)
    vraagprijs = linear_regression_model.predict(features)
    return {'vraagprijs' : vraagprijs}
    
# @route('/mean')
# def mean():
#     dict = request.query.dict
#     select = request_params_mapper.get_select(dict)
#     groupby = request_params_mapper.get_groupby(dict)
#     orderby = request_params_mapper.get_orderby(dict)

#     df_means = get_statistics().mean(select, groupby, orderby)
    
#     return {'means' : df_means.to_dict('records')}

@route('/mean')
@route('/gemeente(<gemeente>)/mean')
def mean(gemeente = None):
    """ Return the mean for selected variables.

    method: GET
    url: /mean
    querystring parameters:
    - $select
    - $groupby
    - $orderby
    example url: https://funda-analysis-api-maartje.c9users.io/gemeente(amsterdam)/mean?$select=ppm2&$select=woonoppervlakte&$groupby=postcode_wijk&$orderby=postcode_wijk
    """
    
    dict = request.query.dict
    select = request_params_mapper.get_select(dict)
    groupby = request_params_mapper.get_groupby(dict)
    orderby = request_params_mapper.get_orderby(dict)

    df_means = get_statistics(gemeente).mean(select, groupby, orderby)
    
    return {'means' : df_means.to_dict('records')}

run(host='0.0.0.0', port=8080, debug=True)



