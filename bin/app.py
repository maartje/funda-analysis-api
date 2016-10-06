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

@route('/summarystatistics')
def summarystatistics():
    select = request.query.dict.get('$select', None)
    groupby = request.query.dict.get('$groupby', None)
    df_stats = statistics.describe(select, groupby)
    return dataframe_to_dict(df_stats)
    
    # result = summarystatistics.calculate()
    # print result
    
    # return {
    #     '2015' : {
    #         'centrum' : { 'median' : 8000, 'mean' : 8200 },
    #         'oost' : { 'median' : 4200, 'mean' : 4100 }
    #     },
    #     '2014' : {
    #         'centrum' : { 'median' : 7900, 'mean' : 8020 },
    #         'oost' : { 'median' : 4100, 'mean' : 4010 }
    #     }
    # }

    # return { 'result' : [
    #     {
    #         'regio' : 'centrum',
    #         'median' : 4000,
    #         'mean' : 4200,
    #         'q1' : 2800,
    #         'q3' : 5200
    #     },
    #             {
    #         'regio' : 'oost',
    #         'median' : 2000,
    #         'mean' : 3000,
    #         'q1' : 1800,
    #         'q3' : 3200
    #     }]}


run(host='0.0.0.0', port=8080, debug=True)



